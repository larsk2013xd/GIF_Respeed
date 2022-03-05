import sys
import time
import os
import os.path

def reSpeed(path, fps):   
    
    fps = min(fps, 50)
    interval = int(100 / fps)
    intervalBytes = interval.to_bytes(1, "little")
    
    print("Loading file: ", path, " ...")
    
    if os.path.exists(targetFile):
        file = open(targetFile, "r+b")
    else:
        print("The file was not found")
        return(False)
        
    fullFile = file.read()
    file.close()
    
    targetOut = os.path.splitext(targetFile)[0] + "_reSpeed_" + str(fps) + ".gif"
    outFile = open(targetOut, "wb")
    outFile.write(fullFile)
    outFile.close()
    
    for runOption in runOptions:
        if runOption == "-r":
            targetOut = targetFile
    
    file = open(targetOut, "r+b")
        
    byte = file.read(3)
    
    if byte.decode() != "GIF":
        print("This file is not a correct (/ correctly formatted) .GIF file")
        print("The file might be corrupt, or this file is not of the GIF type")
        return(False)
     
    print("ReSpeeding '", path, "' to a speed of", fps, "FPS...")
    
    while byte:
        if byte == b'\x21':
            byte = file.read(1)
            if byte == b'\xF9':
                byte = file.read(1)
                if byte == b'\x04':
                    file.seek(1, os.SEEK_CUR)
                    file.write(intervalBytes)
        byte = file.read(1)
    
    
    file.close()
    
    for runOption in runOptions:
        if runOption == "-o":
            if sys.platform == "win32":
                os.startfile(targetOut)
    
    return(True)
    

fps = ""
targetFile = ""
runOptions = []

print("GIF ReSpeed")
print("Developed by LarsKDev")
print("Version 1.0.2 | 5 Mar 2022")
print("---------------------------")

if len(sys.argv) == 1:
    targetFile = input("Please specify the location of the .gif file")
elif len(sys.argv) > 1:
    targetFile = sys.argv[1]
    runOptions = sys.argv[2:]

if len(sys.argv) > 2:
    print("Running with additional arguments", runOptions)
    

while not isinstance(fps, int):
    try:
        fps = int(input("Please specify the new frame interval in frames per second: (GIF files only support up to 50 fps)"))
    except:
        print("Please enter a valid integer")
        

reSpeed(targetFile, fps)
time.sleep(2)

