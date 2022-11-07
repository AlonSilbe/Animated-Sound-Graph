import os
from math import radians
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt
import sounddevice
from scipy.io.wavfile import write
import matplotlib.animation as animation
import datetime as dt
import time

class ShowSound():
   def __init__(self): 
    self.fig=plt.figure(figsize=(25,10)) 
   
   def Start_Show(self):   
     def animate(i, xs, ys):
        fs=44100
        second=10
        print("recording>>>>")
        record_voice1=sounddevice.rec(int(second * fs),samplerate=fs,channels=1)
        sounddevice.wait()
        #save the recording as a wav file
        write("output1.wav",fs,record_voice1)
        data_dir1 = 'output1.wav'
        #load the wav file and its sampling rate
        output1, sr =librosa.load(data_dir1)
        record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
        sounddevice.wait()
        #save the recording as a wav file
        write("output2.wav",fs,record_voice)
        data_dir = 'output2.wav'
        #load the wav file and its sampling rate
        output2, sr =librosa.load(data_dir)
        Frame_size =2048
        HOP_SIZE=512
        # Short-time Fourier transform (STFT).
        # The STFT represents a signal in the time-frequency domain by computing discrete Fourier transforms (DFT) over short overlapping windows.
        # for more info: https://librosa.org/doc/latest/generated/librosa.stft.html#librosa.stft
        S_output2=librosa.stft(output2, n_fft=Frame_size,hop_length=HOP_SIZE )
        Y_output2 =np.abs(S_output2)**2
        S_output1=librosa.stft(output1, n_fft=Frame_size,hop_length=HOP_SIZE )
        Y_output1 =np.abs(S_output1)**2
        Y_log_output2 =librosa.power_to_db(Y_output2)
        Y_log_output1 =librosa.power_to_db(Y_output1)
        plt.subplot(121)
        librosa.display.specshow(Y_log_output2,sr=sr,cmap='afmhot',vmin=-10,vmax=70, fmax=4000)
        cb=plt.colorbar(format="%+2.f")
        cb.remove()
        plt.subplot(122)
        librosa.display.specshow(Y_log_output1,sr=sr,cmap='afmhot',vmin=-10,vmax=70, fmax=4000)
        cb2=plt.colorbar(format="%+2.f")
        cb2.remove()
     xs = []
     ys = []
     ani = animation.FuncAnimation(self.fig, animate, fargs=(xs, ys), interval=1000)
     plt.show()
def main():
   ShowRecording=ShowSound()
   ShowRecording.Start_Show()
if __name__=="__main__":
   main()