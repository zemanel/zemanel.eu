# -*- coding: utf-8 -*- #
from fabric.operations import local

from pelicanconf import OUTPUT_PATH
from pelicanconf import SITEDIR


def install():
    """
    Install local dependencies
    """
    local('npm install .')
    local('pip install -r requirements.txt')


def check():
    """
    Run quality tests.
    """
    # make Guido happy
    local('flake8 --ignore=F403 --exclude=vendor .')


def html():
    """
    Generate static content
    """
    local('pelican -D %s/content/ -s pelicanconf.py' % SITEDIR)


def clean():
    """
    Remove contents of output folder
    """
    local('rm -rf %s' % OUTPUT_PATH)


def update():
    """
    Update (or create) static content
    """
    clean()
    html()


def serve():
    """
    Start http-serving content
    """
    local('honcho start')


def publish():
    """
    Publish content
    """
    html()
    local('ghp-import _output')
    local('git push origin gh-pages')


def generate_pygments_style(theme='colorful', cssclass='highlight'):
    """
    Generates a CSS
    """
    local('pygmentize -f html -S %s -a .%s' % (theme, cssclass))
