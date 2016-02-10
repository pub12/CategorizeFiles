#!/usr/bin/python

import sys
import os
import os.path, time
import datetime
from shutil import copyfile, move

print "hello world"

readDir = 'N:/NetBakData/user@USER-HP/Disk C/Data/01 - Docs/DC/0 - Photos'
targetDir = 'N:/NetBakData/user@USER-HP/Disk C/Data/01 - Docs/DCCat/'

created = dict()

def uniqueFileMove( filename, file_extension,  targetDirSubFolder, sep, uniqueSuffix):
    if os.path.exists( targetDirSubFolder + filename + sep + str(uniqueSuffix) +  file_extension ):
        return sep + str( uniqueFileMove(filename, file_extension, targetDirSubFolder, sep, uniqueSuffix +1) )
    else:
        return sep + str( uniqueSuffix )


from os.path import join, getsize
for root, dirs, files in os.walk(readDir):
    print root, "##", len(files)
    cnt = 0
    for file in files:
        cnt +=1
        srcFile = root + '/' + file
        modifiedMonthSrc = time.strftime( "%Y%m", time.gmtime( os.path.getmtime(srcFile)))
        targetDirSubFolder = targetDir + modifiedMonthSrc + "/"
        targetFile = targetDirSubFolder + file
        if  not modifiedMonthSrc in created.keys() :
            created[ modifiedMonthSrc] = 1
            if not os.path.exists( targetDirSubFolder ):
                os.makedirs( targetDirSubFolder  )

        if not os.path.exists( targetFile ):
            print cnt,"/", len(files), " moving file", file, " to ", targetFile
            move(srcFile, targetFile )
        else: #file exists
            if time.gmtime( os.path.getmtime(srcFile)) == time.gmtime( os.path.getmtime(targetFile)):
                srcFilenameFile,srcFilenameExt = os.path.splitext(file)
                #same modified time - assume same file, skip
                print cnt,"/", len(files), " target file same - skipping for file", file
                uniqueFile = srcFilenameFile + uniqueFileMove(srcFilenameFile, srcFilenameExt, targetDirSubFolder, "_cpy_", 1) +  srcFilenameExt
                move(srcFile, targetDirSubFolder + uniqueFile   )
            else: #different modified time
                srcFilenameFile,srcFilenameExt = os.path.splitext(file)
                uniqueFile = srcFilenameFile + uniqueFileMove(srcFilenameFile, srcFilenameExt, targetDirSubFolder, "_", 1) +   srcFilenameExt
                print cnt,"/", len(files), " collision - renaming file to:", uniqueFile
                move(srcFile, targetDirSubFolder + uniqueFile   )


