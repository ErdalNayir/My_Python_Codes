import cv2
import socket
import struct
import pickle
import threading
import queue


class ClientHandler(threading.Thread):
    def __init__(self, conn, addr, frame_queue):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.frame_queue = frame_queue

    def run(self):
        print(f"Bağlantı kabul edildi: {self.addr}")
        while True:
            frame = self.frame_queue.get()
            data = pickle.dumps(frame)
            message_size = struct.pack("L", len(data))

            try:
                self.conn.sendall(message_size + data)
            except:
                break

        self.conn.close()


class VideoServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print("Sunucu başlatıldı, bekleniyor...")
        self.frame_queue = queue.Queue()
        self.capture_thread = threading.Thread(target=self.capture_frames)
        self.capture_thread.start()

    def capture_frames(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if not self.frame_queue.full():
                self.frame_queue.put(frame)

        cap.release()

    def start(self):
        while True:
            conn, addr = self.server_socket.accept()
            client_handler = ClientHandler(conn, addr, self.frame_queue)
            client_handler.start()
