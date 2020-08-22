#!/usr/bin/python3
"""
script that distributes an archive to a server
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.185.121.162', '54.167.76.210']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        path = ""
        fname = archive_path.split("/")[1]
        absname = fname.split(".")[:-4]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, absname))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(fname, path, absname))
        run('sudo rm /tmp/{}'.format(fname))
        run("sudo mv {} /data/web_static/releases/{}/".format(path1, filename))
        run('sudo rm -rf {}{}/web_static'.format(path, absname))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, absname))
        return True
    except:
        return False
