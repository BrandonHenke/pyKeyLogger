from pynput.keyboard import Key, Listener

def on_press(key):
	print('{0} pressed.'.format(key))

def on_release(key):
	print('{0} releaseed.'.format(key))
	if key == Key.esc:
		return False

with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()