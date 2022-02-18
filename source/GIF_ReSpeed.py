import sys
import time
import os
import os.path

print("GIF ReSpeed")
print("Developed by LarsKDev")
print("Version 1.0 | 18 Feb 2022")
print("---------------------------")

targetFile = ""

if len(sys.argv) == 1:
    # No file has been fed ask user for file
    print("Please specify the path of your .gif:")
    targetFile = input("Target:")
elif len(sys.argv) == 2:
    targetFile = sys.argv[1]



if os.path.exists(targetFile):
    file = open(targetFile, "r+b")
else:
    print("File not found. Exiting...")
    time.sleep(2)
    exit()

print("A delay of 0.01 seconds might not cause wanted results in some viewers. Consider setting the interval to at least 0.02")
delay = ""
while not isinstance(delay, int):
    try:
        delay = int(input("Please specify the frame interval in hundredths of seconds..."))
        if delay > 255:
            print("Please enter a value of less than 256") 
            delay = ""
        elif delay <= 0:
            print("Please enter a strictly positive number")
            delay = ""
    except:
        print("Please enter a valid integer (< 256) ")
        
    
delayBytes = delay.to_bytes(1, 'little')


byte = file.read(3)

offsetCount = 0

print("Starting conversion")
if byte.decode() == "GIF":

    while byte:
        
        if byte == b'\x21':
            byte = file.read(1)
            if byte == b'\xF9':
                byte = file.read(1)
                if byte == b'\x04':
                    file.seek(1, os.SEEK_CUR)
                    file.write(delayBytes)
                    
                    
                
            
        byte = file.read(1)

else:
    print("Unsupported file...")
    time.sleep(3)
    exit()

print("Finishing up...")
file.close()

print("File converted... Closing program")
os.startfile(targetFile)
time.sleep(3) 
