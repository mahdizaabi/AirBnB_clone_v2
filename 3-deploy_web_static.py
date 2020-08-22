#!/usr/bin/python3
"""
script that distributes an archive to a server
"""

from fabric.api import put, run, env, local
from os.path import exists
from datetime import datetime
import os
env.hosts = ['35.185.121.162', '54.167.76.210']


def do_pack():
    """Archive the content of web_static folder"""
    if not os.path.exists('versions'):
        os.mkdir('versions')
    try:
        time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{}.tgz".format(time)
        tar = "tar -cvzf {} web_static/*".format(path)
        local("mkdir -p versions")
        local(tar)
        return path
    except Exception as e:
        return None

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
        run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
        run('sudo rm -rf /tmp/{}.tgz'.format(file_name))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf /data/web_static/releases/{}/ /data/web_static/current'.
            format(file_name))
        return True
    except:
        return False

def deploy():
    """ creates and deploys static to the web server """

    path = ""
    path = do_pack()
    if path == "":
        return False
    return(do_deploy(path))
