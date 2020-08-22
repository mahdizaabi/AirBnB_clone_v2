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

    filename = archive_path.split("/")[-1].split(".")[0]
    path = "/data/web_static/releases/{}/web_static/*".format(filename)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(filename))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(filename, filename))
        run("sudo rm /tmp/{}.tgz".format(filename))
        run("sudo mv {} /data/web_static/releases/{}/".format(path, filename))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(filename))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except:
        return False
    return True
