# Description
My personal research website. Currently hosted at http://ieng6.ucsd.edu/~dplarson/

## Requirements
- ``hugo``

## Instructions
To view the website locally (for testing):

1. start a webserver: ``hugo server``
2. view the site: ``localhost:1313/``

To deploy the website:

1. rebuild the website: ``hugo``
2. upload the website: ``rsync -avz --progress public/ dplarson@ieng6.ucsd.edu:~/public_html/``

## Inspiration
The organization and formatting is inspired by Jon Barron's excellent research website ([link](http://www.cs.berkeley.edu/~barron/)), as well as derivative of his design (e.g. [Stefan Harmeling's site](http://people.kyb.tuebingen.mpg.de/harmeling/)).

## License
MIT
