#!/usr/bin/python3
"""
script that distributes an archive to a server
"""

from fabric.api import put, run, env
import os.path
env.hosts = ['35.185.121.162', '54.167.76.210']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.isfile('archive_path'):
        return False
    try:
        fname = archive_path.split("/")[1]
        absname = fname.split(".")[:-4]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, absname))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fname, path, absname))
        run('rm /tmp/{}'.format(fname))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, absname))
        run('rm -rf {}{}/web_static'.format(path, absname))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, absname))
        return True
    except:
        return False
