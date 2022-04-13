# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 02:00:19 2020

@author: erdal
"""


#print(tf.test.is_gpu_available())
#print(tf.test.gpu_device_name())

from tensorflow.python.client import device_lib

def get_available_devices():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos]



print(get_available_devices())