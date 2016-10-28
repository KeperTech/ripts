# ripTS is a light weight python script that in combination with the Firefox plugin "HLS Stream" can acquire TS format media for offline viewing.

Lots of HLS stream ripper varients on GitHub but ripTS works on Windows & Nix, will download all the HLS streams based on the m3u8 file, and will combine them into one file (name of your choice) and delete the individual TS files so your left with one clean video file. 


* ripTS w/o Tkinter 
Does Not need any additional libraries then what is provided in default python install both Win / Nix*

Windows / Dos

![ScreenShot](https://raw.github.com/KeperTech/ripts/master/RipTS-wo-Tk-Screenshot.png)

Debian / Nix*

![ScreenShot](https://raw.github.com/KeperTech/ripts/master/RipTS-wo-TK-Nix-Screenshot.png)

* ripTS MP with Tikinter
Needs Tkinter and Multiprocessing Support
(Windows default python installs have Tkinter and Multiprocessing support so if your running windows run this one)

![ScreenShot](https://raw.github.com/KeperTech/ripts/master/RipTS-Screenshot.png)

I have tested both versions on Windows 7 and Debian 8 and they both work in my environments.

The code is ugly as sin (lack of error checking and need to do graceful error handling, using globals etc) but the code does work and I will be making improvements in the future.

# Instructions for usage of ripTS

Use HLS Stream Detector in FireFox to detect streams that you wish to acquire for offline viewing
https://addons.mozilla.org/en-US/firefox/addon/hls-stream-detector/

Once you are on a page that uses HLS Stream the Firefox addon will prompt you with a link to the m3u8 file.

A m3u8 file lists all the parts of the video you want to acquire and you copy that m3u8 link and follow the instructions within the python script (litterally copy it into the input box) and it will auto download the files based off the m3u8 location / combine the multiple TS files into one and delete the individual TS files so you are just left with one TS file that you can encode later using FFmpeg https://www.ffmpeg.org/.

If your using the Tkinter version a popup box will ask you to insert the URL with the m3u8 so you do not need to utilize CLI

# Future Versions
* Crypto / SSL features --Script will download from SSL just don't have some of the fancy features of crypto that other scripts have
* Multiprocessing Version --available in MP versions
* Auto Encode using FFMpeg

I made this python script because I was tired of doing it manually to watch media offline on HLS stream format and the steps neccessary to manually download the material was annoying and I wanted an easier way to do it.

You should only use this software if you have explicit permission or ownership of the media that you are acquiring via this python script. 
