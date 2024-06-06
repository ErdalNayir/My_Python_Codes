import cv2
import socket
import struct
import pickle
import threading


class FrameReceiver(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.data = b""
        self.payload_size = struct.calcsize("L")
        self.running = True

    def run(self):
        while self.running:
            while len(self.data) < self.payload_size:
                packet = self.client_socket.recv(4096)
                if not packet:
                    self.running = False
                    break
                self.data += packet

            if not self.running:
                break

            packed_msg_size = self.data[:self.payload_size]
            self.data = self.data[self.payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]

            while len(self.data) < msg_size:
                self.data += self.client_socket.recv(4096)

            frame_data = self.data[:msg_size]
            self.data = self.data[msg_size:]

            frame = pickle.loads(frame_data)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break

        self.client_socket.close()
        cv2.destroyAllWindows()


class VideoClient:
    def __init__(self, server_ip, port=8080):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, port))

    def start(self):
        receiver = FrameReceiver(self.client_socket)
        receiver.start()


client = VideoClient('127.0.0.1')  # Sunucu IP'sini buraya girin
client.start()
