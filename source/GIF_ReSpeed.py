import sys
import time
import os
import os.path


delay = ""
targetFile = ""

print("GIF ReSpeed")
print("Developed by LarsKDev")
print("Version 1.0.1 | 18 Feb 2022")
print("---------------------------")


if len(sys.argv) == 1:
    targetFile = input("Target File:")
elif len(sys.argv) == 2:
    targetFile = sys.argv[1]

print("Loading file: ", targetFile, " ...")


if os.path.exists(targetFile):
    file = open(targetFile, "r+b")
else:
    print("File not found. Exiting...")
    time.sleep(2)
    exit()

print("Loaded file.")
byte = file.read(3)
if byte.decode() != "GIF":
    print("This file is not a correct (/ correctly formatted) .GIF file")
    print("The file might be corrupt, or this file is not of the GIF type")
    print("Exiting...")
    time.sleep(2)
    exit()


while not isinstance(delay, int):
    try:
        delayFPS = int(input("Please specify the new frame interval in frames per second: "))
        
        if delayFPS > 50:
            print("FPS can at most be 50") 
            delay = ""
        elif delayFPS < 1:
            print("FPS must at least be 1")
            delay = ""
        else:
            delay = int(100/delayFPS)
    except:
        print("Please enter a valid integer (< 256) ")
        
    
delayBytes = delay.to_bytes(1, 'little')

print("Starting conversion. This should not take too long...")

while byte:

    if byte == b'\x21':
        byte = file.read(1)
        if byte == b'\xF9':
            byte = file.read(1)
            if byte == b'\x04':
                file.seek(1, os.SEEK_CUR)
                file.write(delayBytes)
    byte = file.read(1)

print("Succesfully converted the file. Finishing up.")
file.close()

print("Done!")
os.startfile(targetFile)
time.sleep(3) 
