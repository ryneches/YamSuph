#!/usr/bin/env python
from numpy import linspace
import subprocess
import sys

s = open( 'block.scad' ).read()

for d in linspace( 0, 10, int( sys.argv[1]) ) :
    base_name = 'block_' + str(d)
    scad_name = base_name + '.scad'
    stl_name  = base_name + '.stl'
    with open( scad_name, 'w' ) as f :
        f.write( 'd = ' + str(d) + ';\n' )
        f.write( s )
    args = ['openscad', '-o', stl_name, scad_name ]
    subprocess.call( args )
