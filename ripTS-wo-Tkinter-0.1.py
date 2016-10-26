#ripTS originally created by Dickson Kwong

import urllib
import urllib2
import math
import platform
import subprocess
import time
import re
import sys
from urlparse import urlparse
from posixpath import basename, dirname


global userInputURL

def checkURL(x):
    response = urllib2.urlopen(x)
    html = response.read()
    linecountINT = html.count('\n') ## returns number of lines based on carriage return

    # Determine number of TS to download
    # 5 Start Headers and 1 End of File Header in m3u8 equals 6 lines / carriage returns that should not be counted
    # Then divide everything by 2 (because 2 carriage returns per numbered TS file)  to get the number of TS files to download
    linecountINT = (linecountINT - 6.00)
    linecountFLOAT = math.ceil(linecountINT / 2) #round up the return value because it can sometimes be .5
    global linecountRounded
    linecountRounded = 0
    linecountRounded = int(linecountFLOAT)
    print linecountRounded

def downloadTS():
    global userInputURL
    global linecountRounded

    # Download Section
    testfile = urllib.URLopener() #Used for downloading the files

    o = urlparse(userInputURL)
    Cutfilename = basename(o.path)
    Segments = Cutfilename.rpartition('.')
    fileNAME = Segments[0]
    fileEXT = ".ts"

    for x in range(0, linecountRounded, 1):
        reconstructURL = 'http://' + o.netloc + dirname(o.path) + '/' + fileNAME + str(x) + fileEXT + o.query
        print "Downloading: " + reconstructURL
        testfile.retrieve(reconstructURL, "video-" + str(x) + ".ts") #retrieve files

def combineTS():
    global linecountRounded
    # Combining Files to form one TS file without using a 3rd party program
    # Windows == copy /b *.ts CompleteVideo.ts
    # Nix == cat *.ts >> CompleteVideo.ts
    OSplatform = platform.system()
    if OSplatform == 'Windows':
        print 'Waiting 3 seconds to ensure all downloads have completed'
        time.sleep(3)
        print 'Merging TS files into one video file and deleting individual files'
        # DOS copy does not organize files name correctly so the videos will be out of sync if you dont manually sync them in order
        # Merge 0 - 9
        subprocess.call('copy /b video-0.ts + video-1.ts + video2.ts + video3.ts + video4.ts + video5.ts + video6.ts + video7.ts + video8.ts + video9.ts videoA.ts', shell=True)
        # Merge 10 - 99
        subprocess.call('copy /b video-10.ts + video-11.ts + video-12.ts + video-13.ts + video-14.ts + video-15.ts + video-16.ts + video-17.ts + video-18.ts + video-19.ts + video-20.ts + video-21.ts + video-22.ts + video-23.ts + video-24.ts + video-25.ts + video-26.ts + video-27.ts + video-28.ts + video-29.ts + video-30.ts + video-31.ts + video-32.ts + video-33.ts + video-34.ts + video-35.ts + video-36.ts + video-37.ts + video-38.ts + video-39.ts + video-40.ts + video-41.ts + video-42.ts + video-43.ts + video-44.ts + video-45.ts + video-46.ts + video-47.ts + video-48.ts + video-49.ts + video-50.ts + video-51.ts + video-52.ts + video-53.ts + video-54.ts + video-55.ts + video-56.ts + video-57.ts + video-58.ts + video-59.ts + video-60.ts + video-61.ts + video-62.ts + video-63.ts + video-64.ts + video-65.ts + video-66.ts + video-67.ts + video-68.ts + video-69.ts + video-70.ts + video-71.ts + video-72.ts + video-73.ts + video-74.ts + video-75.ts + video-76.ts + video-77.ts + video-78.ts + video-79.ts + video-80.ts + video-81.ts + video-82.ts + video-83.ts + video-84.ts + video-85.ts + video-86.ts + video-87.ts + video-88.ts + video-89.ts + video-90.ts + video-91.ts + video-92.ts + video-93.ts + video-94.ts + video-95.ts + video-96.ts + video-97.ts + video-98.ts + video-99.ts videoB.ts',shell=True)
        # Merge 100 - 199
        subprocess.call('copy /b video-100.ts + video-101.ts + video-102.ts + video-103.ts + video-104.ts + video-105.ts + video-106.ts + video-107.ts + video-108.ts + video-109.ts + video-110.ts + video-111.ts + video-112.ts + video-113.ts + video-114.ts + video-115.ts + video-116.ts + video-117.ts + video-118.ts + video-119.ts + video-120.ts + video-121.ts + video-122.ts + video-123.ts + video-124.ts + video-125.ts + video-126.ts + video-127.ts + video-128.ts + video-129.ts + video-130.ts + video-131.ts + video-132.ts + video-133.ts + video-134.ts + video-135.ts + video-136.ts + video-137.ts + video-138.ts + video-139.ts + video-140.ts + video-141.ts + video-142.ts + video-143.ts + video-144.ts + video-145.ts + video-146.ts + video-147.ts + video-148.ts + video-149.ts + video-150.ts + video-151.ts + video-152.ts + video-153.ts + video-154.ts + video-155.ts + video-156.ts + video-157.ts + video-158.ts + video-159.ts + video-160.ts + video-161.ts + video-162.ts + video-163.ts + video-164.ts + video-165.ts + video-166.ts + video-167.ts + video-168.ts + video-169.ts + video-170.ts + video-171.ts + video-172.ts + video-173.ts + video-174.ts + video-175.ts + video-176.ts + video-177.ts + video-178.ts + video-179.ts + video-180.ts + video-181.ts + video-182.ts + video-183.ts + video-184.ts + video-185.ts + video-186.ts + video-187.ts + video-188.ts + video-189.ts + video-190.ts + video-191.ts + video-192.ts + video-193.ts + video-194.ts + video-195.ts + video-196.ts + video-197.ts + video-198.ts + video-199.ts videoC.ts', shell=True)
        # Merge 0 - 199
        subprocess.call('copy /b videoA.ts + videoB.ts + videoC.ts CompleteVideo.ts', shell=True)
        print 'Deleting individual TS clips in 3 seconds'
        # Delete individual TS clips because they are all merged now
        time.sleep(3)
        subprocess.call('del video*.ts', shell=True)
        print 'CompleteVideo.ts Created Enjoy!'
    elif OSplatform == 'Linux':
        print 'Waiting 3 seconds to ensure all downloads have completed'
        time.sleep(3)
        print 'Merging TS files into one video file and deleting individual files'
        subprocess.call(['cat *.ts >> CompleteVideo.ts'], shell=True)  # <-- Change the command here
        print 'Deleting individual TS clips in 3 seconds'
        # Delete individual TS clips because they are all merged now
        time.sleep(3)
        subprocess.call(['rm video*.ts'], shell=True)
    else:
        print "FutureBuild"
        sys.exit()

def start():
    checkURL(userInputURL) #Check your URL and read from the m3u8 file you specified
    downloadTS() #download all the TS files
    combineTS() #combine all the TS files then delete the individual files downloaded

if __name__ == '__main__':
    userInputURL = raw_input("Enter the URL with the m3u8 file: ")

    m = re.search('.m3u8', userInputURL)
    if m is None:
        print "Bad URL please check your URL for m3u8"
    else:
        print "Starting Ripper TS!"
        start()  # Start download and combine TS Files