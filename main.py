from key_shift_register import ShiftIn
import vlc
from time import sleep
import os
from math import ceil

def which_key_pressed(keys):
    pressed_key = -1
    for key, value in enumerate(keys):
        if value == 0:
            pressed_key = key + 1
            break
    return pressed_key

def play_video(video_num):
    media_player = vlc.MediaPlayer()
 
    video_path = os.path.join('videos', str(video_num)+'.mp4')
    media = vlc.Media(video_path)
    
    media_player.set_media(media)   
    media_player.play()
    
    media_player.set_fullscreen(True)
    
    sleep(2)
    video_duration = media_player.get_media()
    
    sleep(ceil(video_duration/1000))
    media_player.release()
    

def main():
    key_shift = ShiftIn(ld_pin=19, data_pin=21, clk_pin=23)
    
    while True:
        keys = key_shift.read()
        pressed_key = which_key_pressed(keys)
        if pressed_key != -1:
            play_video(pressed_key)
        else:
            sleep(0.4)

if __name__=="__main__":
    main()
