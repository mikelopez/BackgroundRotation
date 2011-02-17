#!/usr/bin/env python

# Tested on Ubuntu Desktop 10.10 Running Gnome

import os
import gconf
from random import randint
from datetime import datetime
import sys
# mike - 420 


#append the subdir cosmos :)
topdir = os.listdir('/usr/share/backgrounds/')
sub = os.listdir('/usr/share/backgrounds/cosmos')

newlist = []

for i in sub:
	topdir.append('cosmos/%s' % (i))

for i in topdir:
	if '.png' in i or '.jpg' in i or 'jpeg' in i:
		newlist.append(i)


try:
	envs = os.environ["DISPLAY"]
except KeyError:
	os.environ["DISPLAY"] = ':0.0'
	envs = os.environ["DISPLAY"]


random_weiner = newlist[randint(0, (len(newlist) - 1))]

# command line to do this
#cmd_exec = 'gconftool-2 --type string --set /desktop/gnome/background/picture_filename /usr/share/backgrounds/%s' % (
#	random_weiner
#)

client = gconf.client_get_default()
current_bg = client.get_string("/desktop/gnome/background/picture_filename")
client.set_string("/desktop/gnome/background/picture_filename", '/usr/share/backgrounds/%s' % (random_weiner))

"""
Uncomment this and customize if you want this to log everytime a wallpaper is changed

logg = open('/home/mikey/app_logs/change_background/commands.txt', 'a')
logg.write('DISPLAY=%s || UID=%s ||  %s :: /usr/share/backgrounds/%s\n' % (
	str(envs), str(os.getuid()), str(datetime.now()), random_weiner
))
logg.close()
"""

sys.exit()
