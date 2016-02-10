# CategorizeFiles
Move files from a directory (and subdirectories) into subdirectories of a target folder based on file modified year and month

Intention was to move photos in multiple folders into a central place categorized by yyyymm folders.  Program will use the source directory then traverse each subdirectory, then move the file to the target directory but within a subfolder named yyyymm where the date comes from the files modified date.

If the file already exists and has the same modiifed date, it is assumed to be a copy an the file will be moved to the destination and renamed to originalfile_cpy.originafileext

if the file already exists, but does not have the same modified date, file will be moved to the destination and renamed to originalfile_#.originalfileext where # is a number starting from 1 intended to make the filename unique.
