import os
import hashlib

#Create an object that maps keys to sounds
sound_map = {
    "1": "bruh.mp3",
    "2": "prettygood.mp3",
    "3": "hello.mp3",
    "4": "lyin.mp3",
    "5": "okay.mp3",
    "6": "whatdoyoumean.mp3"
}

# Returns the checksum of our file
def get_checksum():
    return hashlib.md5(open('queue.txt','rb').read()).hexdigest()

#Clears out the queue
def clear_queue():
    f = open('queue.txt', 'r+')
    f.truncate(0)
    return True

# load file of comma seperated values to be turned into our queue
def load_queue():
    with open('queue.txt', 'r') as f:
        data = f.read().split(',')

        if data[0] == '':
            return None
        
        return data

# Load the queue from load_queue, 
#then play sounds from queue one by one
def load_sounds_from_queue():
    queue = load_queue()

    if queue == None:
        return False

    for value in queue:
        play_sound(sound_map[value])

#Play our sound
def play_sound(sound):
    os.system("mpg123 sounds/{0}".format(sound))
    return True

# Entrypoint
if __name__ == "__main__":
    
    # Get initial checksum
    checksum = get_checksum()
    
    # Loop forever comparing our checksum
    # and triggering our workflow if the file changes
    while True:
        if checksum != get_checksum():
            load_sounds_from_queue()
            # reset the checksum
            checksum = get_checksum()
            clear_queue()

        
