# ripts is a light weight python script that in combination with the Firefox plugin "HLS Stream" can acquire media for offline viewing.  

You should only use this software if you have explicit permission or ownership of the media that you are acquiring via this python script. 

I made this python script because I was tired of doing it manually to watch media offline on HLS stream format and the steps neccessary to manually download the material was annoying and I wanted an easier way to do it.

There are 2 python scripts
* ripTS with Tkinter 
* ripTS w/o Tkinter 

If you do not have Tkinter installed use the TSrip w/o obviously, for those that do not know what Tkinter is, it is a simple GUI for python that is installed on Windows platforms by default so you don't have to paste into a command prompt.

I have tested both versions on Windows 7 and Debian and they both work in my environments.

The code is ugly as sin (lack of error checking and need to do graceful error handling) but the code does work and I will be making improvements in the future but no solid ETA.

Thanks for trying out ripTS and I hope you find it useful. I will be sorting the name issue by the next release.

Dickson Kwong

Instructions for usage of ripTS

Use HLS Stream Detector in FireFox to detect streams that you wish to acquire for offline viewing
https://addons.mozilla.org/en-US/firefox/addon/hls-stream-detector/

Once you are on a page that uses HLS Stream the Firefox addon will prompt you with a link to the m3u8 file.

A m3u8 file lists all the parts of the video you want to acquire and you copy that m3u8 link and follow the instructions within the python script (litterally copy it into the input box) and it will auto download the files based off the m3u8 location / combine the multiple TS files into one and delete the individual TS files so you are just left with one TS file that you can encode later using FFmpeg https://www.ffmpeg.org/.
