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


def deploy():
    """ creates and deploys static to the web server """

    path = ""
    path = do_pack()
    is path == "":
        return False
    return(do_deploy(path))
