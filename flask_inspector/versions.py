# coding: utf-8
import os
import subprocess


def get_git_changeset(repo_dir):
    '''
        Copy from django
    '''
    """Returns a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    try:
        git_log = subprocess.Popen('git log --pretty=oneline -1 HEAD',
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                shell=True, cwd=repo_dir, universal_newlines=True)
        return git_log.communicate()[0]
    except:
        return ''
