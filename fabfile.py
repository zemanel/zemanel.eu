# -*- coding: utf-8 -*- #
from fabric.operations import local

from pelicanconf import OUTPUT_PATH
from pelicanconf import SITEDIR


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
    local('pelican --debug %s/content/ -s pelicanconf.py' % SITEDIR)


def clean():
    """
    Remove contents of output folder
    """
    local('rm -rf %s' % OUTPUT_PATH)


def update():
    """
    """
    html()


def serve():
    """
    """
    local('honcho start')
