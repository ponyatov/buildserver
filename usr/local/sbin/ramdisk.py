#!/usr/bin/env python
import os, re, sys, time
print sys.argv

RD = [
	'/home/ponyatov/.mozilla',
	'/home/ponyatov/cross/host'
]

SYMCMD = sys.argv[0].split('.')[-1]; print 'SYMCMD', SYMCMD
try:
	CMDCMD = sys.argv[1]
except:
	CMDCMD = ''
print 'CMDCMD',CMDCMD

if 'sync' in [SYMCMD,CMDCMD] :
	for i in RD:
		C = 'rsync -a --delete %s/ %s-rd' % (i, i)
		print C,
		print os.system(C)


