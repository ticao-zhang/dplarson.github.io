"""
Fabric file for common hyde tasks.

author: David Larson
email: dplarson@ucsd.edu
"""

from fabric.api import local
from fabric.contrib.project import rsync_project

def clean():
    local('rm -rf deploy')

def gen():
	clean()
	local('hyde gen')

def gen_prod():
    clean()
    local('hyde gen -c prod.yaml')

def serve():
	gen()
	local('hyde serve')

def push():
    gen_prod()
    local('rsync -rav deploy/ dplarson@ieng6.ucsd.edu:/home/linux/ieng6/oce/60/dplarson/public_html/')
