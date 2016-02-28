#!/bin/sh

set -e

# build site
hugo

# upload
rsync -avz --progress public/ dplarson@ieng6.ucsd.edu:~/public_html/
