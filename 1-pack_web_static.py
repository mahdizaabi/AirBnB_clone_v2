#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
from fabric.api import local

import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static"""

    path = ""
    if not os.path.exists('versions'):
        os.mkdir('versions')
    try:
        path = os.getcwd() + "/versions"
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        fname = "web_static_{}".format(date)
        local("tar -cvzf {}.tgz web_static".format(fname))
        local("mv {}.tgz {}".format(fname, path))
        return (path)
    except Exception as e:
        return None
