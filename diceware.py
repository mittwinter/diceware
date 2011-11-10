#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
import sys

try:
	with open( sys.argv[ 1 ], 'r' ) as f:
		wordsLines = f.readlines()
		words = dict( [ ( line.split()[ 0 ], line.split()[ 1 ] ) for line in wordsLines ] )
		password = ''.join( [ words[ ''.join( [ str( random.randint( 1, 6 ) ) for i in range( 5 ) ] ) ] for i in range( int( sys.argv[ 2 ] ) ) ] )
		print password
except IndexError:
	print sys.argv[ 0 ], '<wordList>', '<numWords>'
