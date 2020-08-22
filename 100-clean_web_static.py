#!/usr/bin/python3
"""
script that distributes an archive to a server
"""
import os
import glob
from fabric.api import put, run, env, local
from os.path import exists
env.hosts = ['35.185.121.162']

def do_clean(number=0):
    """ keep the archvie clean """
    number = int(number)
    run("sudo mkdir -p /data/web_static/releases/tempx")
    path = "/data/web_static/releases"
    list_of_files = glob.glob(path)
    sorted_files = sorted(list_of_files, key=os.path.getmtime)
    for i in range(len(sorted_files)):
        run("sudo touch cp {} /data/web_static/releases/tempx".format(sorted_files[i]))
    run("sudo rm -rf /data/web_static/releases/*.tgz")
    run("cp -a /data/web_static/releases/tempx/. /data/web_static/releases")
    run("sudo rm -rf /data/web_static/releases/tempx")   
