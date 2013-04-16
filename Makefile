PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/_output
CONFFILE=$(BASEDIR)/pelicanconf.py

# LESS compilation
BOOTSTRAPDIR=$(BASEDIR)/vendor/bootstrap/less
THEMEDIR=$(BASEDIR)/theme/zen


help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '

html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

less:
	lessc --include-path=$(BOOTSTRAPDIR) $(THEMEDIR)/less/main.less $(OUTPUTDIR)/theme/main.css
	lessc --include-path=$(BOOTSTRAPDIR) $(THEMEDIR)/less/main-responsive.less $(OUTPUTDIR)/theme/main-responsive.css
	@echo 'Done'


$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

devserver:
	$(BASEDIR)/develop_server.sh restart

.PHONY: html help clean regenerate serve devserver
