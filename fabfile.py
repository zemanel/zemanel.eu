# -*- coding: utf-8 -*- #
from fabric.operations import local

from pelicanconf import OUTPUT_PATH
from pelicanconf import SITEDIR
from pelicanconf import THEME
from pelicanconf import _BOOTSTRAP_DIR

# LESS command-line config
LESSC = '%s/node_modules/less/bin/lessc' % SITEDIR
LESSC_ARGS = ' --verbose --include-path=%s/less/ ' % _BOOTSTRAP_DIR
LESSC_CMD = LESSC + LESSC_ARGS


def test():
    """
    Run quality tests.
    """
    # make Guido happy
    local('flake8 --ignore=F403 --exclude=vendor .')


def html():
    """
    Generate static content
    """
    local('pelican %s/content/ -s pelicanconf.py' % SITEDIR)
    pass


def compile_less(src, target):
    """
    Compile theme LESS file
    :param src: source LESS file relative to source theme folder
    :param target: source LESS file relative to output theme folder
    """
    cmd = '%s %s/%s %s/theme/%s'
    local(cmd % (LESSC_CMD, THEME, src, OUTPUT_PATH, target))


def assets():
    """
    Compile LESS files
    """
    compile_less('less/main.less', 'main.css')
    compile_less('less/main-responsive.less', 'main-responsive.css')


def clean():
    """
    Remove contents of output folder
    """
    local('rm -rf %s' % OUTPUT_PATH)

def update():
    """
    """
    html()
    assets()
