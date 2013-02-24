"""
Fabric file for common hyde tasks.

author: David Larson
email: dplarson@ucsd.edu
"""

from fabric.api import local
import urllib


def clean():
    """Clean."""
    local('rm -rf deploy')


def update_cv():
    """Get current version of my CV."""
    pdf_remote = "https://github.com/dplarson/CV/raw/master/David_Larson.pdf"
    pdf_local = "deploy/media/David_Larson.pdf"
    try:
        urllib.urlretrieve(pdf_remote, pdf_local)
    except:
        print "Error: unable to download newest version of CV."


def gen():
    """Generate website."""
    clean()
    local('hyde gen')
    update_cv()


def gen_prod():
    """Generate production version of website."""
    clean()
    local('hyde gen -c prod.yaml')
    update_cv()


def serve():
    """Start local webserver."""
    gen()
    local('hyde serve')
    update_cv()


def push():
    """Upload website to UCSD server."""
    gen_prod()
    local('rsync -rav deploy/ dplarson@ieng6.ucsd.edu:/home/linux/ieng6/oce/60/dplarson/public_html/')
