import sounddevice as sd

samplerate = 44100

duration = 3

print("Recording...")

recording = sd.rec(int(samplerate * duration), samplerate, channels=1)

sd.wait()

print("Recording done. Playing back.")

sd.play(recording, samplerate)

sd.wait()
