#!/usr/bin/python3
"""
script that distributes an archive to a server
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.185.121.162', '54.167.76.210']


def do_deploy(archive_path):
    """Distribute an Archive to servers"""
    if not os.path.exists(archive_path):
        return false
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, '/tmp/')
        run('sudo mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.
            format(file_name, file_name))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.
            format(file_name, file_name))
        run('sudo rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))
        run('sudo rm -rf /tmp/{}.tgz'.format(file_name))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current'.format(file_name))
        return True
    except:
        return False
