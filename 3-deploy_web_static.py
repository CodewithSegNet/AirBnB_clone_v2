#!/usr/bin/python3
"""
creates and distributes an archive to your web servers
fab -f 3-deploy_web_static.py deploy -i ssh-key -u ubuntu
"""

from datetime import datetime
import os.path
from fabric.api import put, run, env, local

env.hosts = ['35.243.128.200', '3.239.120.96']


def do_pack():
    """
    making an archive on web_static folder
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
