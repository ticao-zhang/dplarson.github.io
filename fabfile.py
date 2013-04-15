from fabric.api import local
import urllib


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


def gen():
    clean()
    local('pelican content -s settings.py')
    update_cv()


def push():
    gen()
    local('rsync -rav output/ dplarson@ieng6.ucsd.edu:/home/linux/ieng6/oce/60/dplarson/public_html/')
