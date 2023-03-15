# Información del procesador: https://github.com/DeepLabCut/DeepLabCut-live/blob/master/dlclive/processor/README.md
# Ejemplo LED: https://github.com/DeepLabCut/DeepLabCut-live/blob/master/example_processors/MouseLickLED/lick_led.py
# Ejemplo sencillo: https://github.com/DeepLabCut/DeepLabCut-live/blob/master/dlclive/processor/processor.py

"""
DeepLabCut Toolbox (deeplabcut.org)
© A. & M. Mathis Labs
Licensed under GNU Lesser General Public License v3.0
"""


import serial
import struct
import time
import numpy as np

from dlclive import Processor


class MouseLickLED(Processor):
    def __init__(self, com, lik_thresh=0.5, baudrate=int(9600)):

        super().__init__()
        self.ser = serial.Serial(com, baudrate, timeout=0)
        self.lik_thresh = lik_thresh
        self.lick_frame_time = []
        self.out_time = []
        self.in_time = []

    def close_serial(self):

        self.ser.close()

    def switch_led(self):

        ### flush input buffer ###

        self.ser.reset_input_buffer()

        ### turn on IR LED ###

        self.out_time.append(time.time())
        self.ser.write(b"I")

        ### wait for receiver ###

        while True:
            led_byte = self.ser.read()
            if len(led_byte) > 0:
                break
        self.in_time.append(time.time())

    def process(self, pose, **kwargs):

        ### bodyparts
        # 0 Head
        # 1 Snout
        # 2 LeftEar
        # 3 RightEar
        # 4 Shoulder
        # 5 Spine1
        # 6 Spine2
        # 7 Spine3
        # 8 Spine4
        # 9 TailBase
        # 10 Tail1
        # 11 Tail2
        # 12 TailEnd
        # 13 LeftPaw1
        # 14 RightPaw1
        # 15 LeftPaw2
        # 16 RightPaw2
        # if kwargs["record"]: 
            # if pose[8, 5] > self.lik_thresh:
            #     self.lick_frame_time.append(kwargs["frame_time"])
            #     self.switch_led()
        self.switch_led()

        return pose

    def save(self, filename):

        ### save stim on and stim off times

        filename += ".npy"
        out_time = np.array(self.out_time)
        in_time = np.array(self.in_time)
        frame_time = np.array(self.lick_frame_time)
        try:
            np.savez(
                filename, out_time=out_time, in_time=in_time, frame_time=frame_time
            )
            save_code = True
        except Exception:
            save_code = False

        return save_code
    

'''
    Este código importa los módulos necesarios y define una clase MouseLickLED que hereda de la clase Processor del módulo dlclive. 
    La clase se inicializa con los siguientes argumentos: com, que especifica el puerto serial al que está conectado el dispositivo; 
    lik_thresh, que es el umbral de probabilidad para detectar un "lamido" de ratón; y baudrate, que es la velocidad de transmisión de datos a través del puerto serial.
    La clase tiene varios métodos. 
    El método close_serial se utiliza para cerrar el puerto serial. 
    El método switch_led es el que activa un LED infrarrojo y espera a que el receptor detecte su señal. 
    El método process toma como entrada una matriz pose que contiene información sobre la postura de un animal (en este caso, un ratón) y un diccionario
      kwargs que contiene información adicional. Si record es verdadero en kwargs y la probabilidad de que el animal haya lamido (pose[16,2]) es mayor que el umbral especificado 
      (self.lik_thresh), 
    entonces el método llama a self.switch_led() y registra el tiempo de fotograma en el que se activó el LED. 
    El método devuelve la matriz pose. El método save se utiliza para guardar los tiempos de activación del LED y los tiempos de fotograma en un archivo numpy con extensión .npy.
'''