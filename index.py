import time
import simpleaudio as sa
import random



def play_fart_noise():
    # give path to file
    soundFile = sa.WaveObject.from_wave_file("reverbFart.wav")
    # play fart sound, 
    # wait for it to finish
    # before exiting
    soundFile.play().wait_done()

# while loop to 
# keep farting
gassy = True 
while gassy:
    play_fart_noise()
    # choose an amount
    # from 5-10 min
    extraMinutes = random.randint(300, 600)
    # wait 15 minutes
    # plus 5-10 extra
    time.sleep(900 + extraMinutes)