import RPi.GPIO as GPIO
import time
import signal
import subprocess 
import os

bashCommand = "ffmpeg -y -f alsa -i hw:1 -t 10 ./audioFiles/file.wav"
ledCommand = "python recordLed.py"

#sudo killall not needed, as we send signal.SIGINT to the process
#pidCommand = "sudo killall ffmpeg"

#is_recording = False
#response_time = 1

'''
while True:
    state = GPIO.input(BUTTON)
    
    if not state and not is_recording:
        print("rec")
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        led = subprocess.Popen(ledCommand.split(), stdout=subprocess.PIPE)

        is_recording = True
    
    elif state and is_recording:
        print("off")
        #subprocess.Popen(pidCommand.split(), stdout=subprocess.PIPE)
    
        process.send_signal(signal.SIGINT) 
        led.send_signal(signal.SIGINT)

        is_recording = False
    
    time.sleep(response_time)
'''

def startRec(character):

    record = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    #led = subprocess.Popen(ledCommand.split(), stdout=subprocess.PIPE)
    
    