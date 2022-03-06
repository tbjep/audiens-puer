import sounddevice as sd
import numpy as np

def sine_wave(frequency, idx, frames):
    return np.sin(2 * np.pi * frequency * np.arange(idx, idx + frames) / samplerate)

class SineGenerator:
    def __init__(self):
        self.i = 0

    def callback(self, outdata, frames, time, status):
        if status:
            print(status)

        outdata[:] = sine_wave(440, self.i, frames).reshape(-1, 1)
        self.i += frames

samplerate = 44100
duration = 3

def main():
    print(sine_wave(440, 0, 30))
    return
    print("Recording...")
    recording = sd.rec(int(samplerate * duration), samplerate, channels=1)
    sd.wait()

    print("Recording done. Playing back.")
    sd.play(recording, samplerate)
    sd.wait()

    print("Playing a (hopefully) smooth sine wave")
    sg = SineGenerator()
    with sd.OutputStream(samplerate, channels=1, callback=sg.callback):
        input("Press enter to quit.")

if __name__ == "__main__":
    main()
