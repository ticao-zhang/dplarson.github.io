from fabric.api import local
import urllib

CONTENT = 'content'
CONFIG_FILE = 'settings.py'
BUILD_PATH = 'output'

FTP_USER = 'dplarson'
FTP_HOST = 'ieng6.ucsd.edu:/home/linux/ieng6/oce/60/dplarson/public_html/'


def clean():
    local('rm -rf output')


def update_cv():
    """Get current version of my CV."""
    pdf_remote = "https://github.com/dplarson/CV/raw/master/David_Larson.pdf"
    pdf_local = "output/David_Larson.pdf"
    try:
        urllib.urlretrieve(pdf_remote, pdf_local)
    except:
        print "Error: unable to download newest version of CV."


def build():
    """Generate website."""
    clean()
    local('pelican content -s settings.py')
    update_cv()


def serve():
    """Server website locally."""
    build()
    local('cd output && python -m SimpleHTTPServer')


def deploy(user=FTP_USER, host=FTP_HOST):
    """Push website to server."""
    build()
    local('rsync -rav output/ {0}@{1}'.format(user, host))
