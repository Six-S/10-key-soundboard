
import os
import keyboard

# Record keystroke to queue
def record_keystroke(key):
    f = open("queue.txt", "w")
    f.write("," + key)
    return f.close()

if __name__ == "__main__":

    import keyboard  # using module keyboard
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break
