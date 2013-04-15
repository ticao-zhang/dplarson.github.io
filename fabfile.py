from fabric.api import local


def clean():
    local('rm -rf output')


def gen():
    clean()
    local('pelican content -s settings.py')
