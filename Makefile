# Makefile for my Pelican-powered website
#

INPUTDIR = content
BUILDDIR = output
CONFFILE = settings.py

help:
	@echo 'Makefile for my Pelican-powered website 			'
	@echo ' 												'
	@echo 'Usage: 											'
	@echo ' 	make html 		(re)generate the website 	'
	@echo ' 	make clean 		remove the generated files 	'
	@echo ' 												'

clean:
	rm -rf $(BUILDDIR)

html: clean
	pelican $(INPUTDIR) -s $(CONFFILE) -o $(BUILDDIR)
	@echo "Build finished. The HTML pages are in $(BUILDDIR)"

# quiet
.SILENT: clean html

# what do to do when no target given
.DEFAULT: help

.PHONY: clean html
