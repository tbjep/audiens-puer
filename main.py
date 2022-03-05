import sounddevice as sd
import numpy as np

samplerate = 44100
duration = 3

print("Recording...")

recording = sd.rec(int(samplerate * duration), samplerate, channels=1)

sd.wait()

print("Recording done. Playing back.")

sd.play(recording, samplerate)

sd.wait()

print("Playing a (hopefully) smooth sine wave")

class SineGenerator:
    def __init__(self):
        self.i = 0

    def callback(self, outdata, frames, time, status):
        if status:
            print(status)

        outdata[:] = np.sin(2 * np.pi * 440 * (self.i + np.arange(frames)) / samplerate).reshape(-1, 1)
        self.i += frames

sg = SineGenerator()
with sd.OutputStream(samplerate, channels=1, callback=sg.callback):
    input("Press enter to quit.")
