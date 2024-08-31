The script imports the keyboard module from the pynput library.

The on_press function is called whenever a key is pressed. It tries to print the alphanumeric key that was pressed and appends it to a file named "keylog.txt". If a non-alphanumeric key (like Shift, Ctrl, etc.) is pressed, it prints and appends the key's name to the file.

The on_release function is called when a key is released. It prints which key was released. If the Esc key is released, it returns False, which stops the keylogger.

The script creates a Listener object from the keyboard module, passing the on_press and on_release functions as callbacks.

The listener.join() method is called, which starts the listener and keeps it running until stopped (by pressing Esc)




    For Advanced Key Logger

from pynput import keyboard     
import threading               
import smtplib                  

def grab_keys(key):
    # This function is called whenever a key is pressed
    # It stores the pressed keys in the 'log' variable
    # It handles special keys like space, backspace, caps lock, etc.
    # It prints the current value of 'log' to the console

def send_email():   
    # This function sends the contents of the 'log' variable via email
    # It uses the smtplib module to connect to a Gmail SMTP server
    # The sender's email address and password are hardcoded (insecure)
    # The recipient's email address is also hardcoded
    # If sending is successful, it returns "successful", else "failed"

def keys_logged():
    # This function is called periodically (every 300 seconds)
    # It calls send_email() to send the current contents of 'log'
    # It resets 'log' to an empty string
    # It sets up a timer to call itself again after the time interval

# This sets up a keyboard listener using pynput
# Whenever a key is pressed, the grab_keys function is called
# The listener runs until stopped manually

# The keys_logged function is called to start the logging process
