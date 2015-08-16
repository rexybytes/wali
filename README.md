README for Wali

This simple script will change the desktop wallpaper between intervals specified
by the user. The interval is specified on the command line.
Run this script like this:
	python wallpaper.py 'directory' 'interval in s'
	
Example
 	python wallpaper.py ~/wallpapers 300

Wali will look in the ~/wallpapers directory, collect all the available files
and change your desktop wallpaper once in every 5 minutes.
