import sys
import time
import os
import os.path


runOptions = []
os.system('cls')
os.system('color 4')
def getSpeed(path):
    
    try:
        file = open(path, "r+b")
        unstable = False
        nFrames = 0
        intervalCount = 0
        avg_interval = 0
        byte = file.read(3)
        if byte.decode() != "GIF":
            return(False, 0)
        
        while byte:
            if byte == b'\x21':
                byte = file.read(1)
                if byte == b'\xF9':
                    byte = file.read(1)
                    if byte == b'\x04':
                        file.seek(1, os.SEEK_CUR)
                        interval = int.from_bytes(file.read(1), "little")
                        nFrames += 1
                        intervalCount += interval
                        avg_interval = intervalCount / nFrames
                        if abs(interval - avg_interval) > 1 and not unstable:
                            unstable = True
                            print("This GIF file seems to have an unstable framerate...")
            byte = file.read(1)
    
        return(True, int(1/(0.01*avg_interval)))
    except Exception as e:
        return(False, 0)
    

def reSpeed(path, fps):   
    global runOptions
    fps = min(fps, 50)
    interval = int(100 / fps)
    intervalBytes = interval.to_bytes(1, "little")
        

    try:
        if os.path.isfile(path):
            print("Loading file: ", path, " ...")
            file = open(path, "r+b")
        else:
            print("The file was not found")
            return(False)
        
        byte = file.read(3)
        
        if byte.decode() != "GIF":
            print("Not a .gif")
            return(False)
        
        file.seek(0)
        fullFile = file.read()
        file.close()
        
        targetOut = os.path.splitext(path)[0] + "_reSpeed_" + str(fps) + ".gif"
        for runOption in runOptions:
            if runOption == "-r":
                targetOut = path
        
        
        outFile = open(targetOut, "wb")
        outFile.write(fullFile)
        outFile.close()
        
        file = open(targetOut, "r+b")
    except Exception as e:
        print("Not a .gif")
        return(False)
    
    try:
        print("ReSpeeding '", path, "' from a speed of ", getSpeed(path)[1], " FPS to ", fps, "FPS...")
        
        while byte:
            if byte == b'\x21':
                byte = file.read(1)
                if byte == b'\xF9':
                    byte = file.read(1)
                    if byte == b'\x04':
                        file.seek(1, os.SEEK_CUR)
                        file.write(intervalBytes)
            byte = file.read(1)
    except:
        print("This file is not a correct (/ correctly formatted) .GIF file")
        print("The file might be corrupt, or this file is not of the GIF type")
        file.close()
        return(False)
    
    
    file.close()
    
    for runOption in runOptions:
        if runOption == "-o":
            if sys.platform == "win32":
                os.startfile(targetOut)
    
    return(True)

def getUserInput():
    global runOptions
    fps = ""
    targetFile = ""
    if len(sys.argv) == 1:
        targetFile = input("Please specify the location of the .gif file")
    elif len(sys.argv) > 1:
        targetFile = sys.argv[1]
        runOptions = sys.argv[2:]

    if len(sys.argv) > 2:
        print("Running with additional arguments", runOptions)
        
    for runOption in runOptions:
        if runOption == "-g":
            print("Retrieving gif speed of...", targetFile)
            result = getSpeed(targetFile)
            if result[0]:
                print(result[1], " FPS")
            else:
                print("The file is not in the correct GIF format")
            return True
            
            
    while not isinstance(fps, int):
        try:
            fps = int(input("Please specify the new frame interval in frames per second: (GIF files only support up to 50 fps)"))
        except:
            print("Please enter a valid integer")
            
    for runOption in runOptions:
        if runOption == "-f":
            print("Converting all .gifs in folder...")
            if os.path.isdir(targetFile):
                targetFiles = os.listdir(targetFile)
                
                for f in targetFiles:
                    reSpeed(targetFile + "/" + f, fps)
                    
                return True
            else:
                print("Please specify a folder...")
                return True
                
                
    reSpeed(targetFile, fps)
    return True  



print("GIF ReSpeed")
print("Developed by LarsKDev")
print("Version 1.0.4 | 7 Mar 2022")
print("---------------------------")


getUserInput()
print("Exiting program...")
time.sleep(2)
os.system('color 7')
os.system('cls')

