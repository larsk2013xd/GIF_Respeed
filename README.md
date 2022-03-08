# GIF ReSpeed
This is a tool that can be used to speed up / slow down .GIF files. This file is meant for GIF89a files (but 87a files will work most of the time as well)

There's not much more to it. I decided to create one because the only other way I found was uploading my gifs to some weird site and having to wait half an hour before I had to download my 60MB gif file again.

# How to use
Simply drag / drop a .gif file onto the program. Indicate the desired framerate and within a matter of seconds your GIF will go FAF or SAF!

For advanced use open CMD and enter `python GIF_ReSpeed.py [fileLocation] [args]` if `[fileLocation]` is not indicated the program will ask the user for a file location. Optional arguments can be passed in the `[args]` argument. Possible arguments are:
- `-r` : This will overwrite the original file. This introduces the danger of corruption so it is not adviced to use this.
- `-o` : This will open the converted file after conversion (Windows only)
- `-f` : This will iterate through an entire folder. All .gif files in this folder will be converted to the desired framerate

# Changelog

`1.0.4`
- Added `-g` argument. This will retrieve the framerate of the given .gif file without changing the speed


`1.0.3`
- Added `-f` argument. This will convert all files in the given `[fileLocation]` folder. In this case the user should indicate a folder location and not a file location
- Fixed `-r`.

`1.0.2`
- Added arguments. See the "How to use" for explanation.
- Gif_ReSpeed will now make a copy of the file and adjust its framerate to prevent accidental corruption. (The original file can still be overwritten using the `-r` argument)

# Requirements
This program uses no extra packages besides the default `os`, `path` and `time` packages. Neat isn't it :)
