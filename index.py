import time
import random
import winsound


# function to play
# any sfx
def play_sound(soundFile):
    winsound.PlaySound(soundFile, winsound.SND_FILENAME)
    time.sleep(5)

# while loop to 
# keep farting
gassy = True
while gassy:
    play_sound("reverbFart.wav")
    # play_fart_noise()
    # choose an amount
    # from 0-10 min
    extraMinutes = random.randint(0, 600)
    # wait 15 minutes
    # plus 0-10 extra
    time.sleep(900 + extraMinutes)