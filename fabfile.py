#!/usr/bin/env python
# <fabfile.py>
# Created: September 11, 2012
# Version: 0.0.1
# By:  (bwghughes@gmail.com)
import os
import time
import sys
from datetime import datetime


from fabric.api import env, cd, local, settings
from fabric.colors import red, green
from fabric.contrib.console import confirm
from fabric.utils import fastprint


#############################################
#
# Environment Definition
#
#############################################

def dev():
    env.user = 'deploy'
    env.hosts = ['192.168.1.101']
    env.name = 'dev'
    env.root = "/opt/apps/application-core/"

#############################################
#
# Tasks
#
#############################################


def clean():
    if confirm(red("This will remove all packaged deployables.")):
        with settings(warn_only=True):
            local('rm *.tar.gz')


def pack_uc_core():
    date = datetime.strftime(datetime.now(), '%Y%m%d-%H%M')
    archive_file = 'application-core-{0}.tar.gz'.format(date)
    print green('Creating deployable archive {0}...'.format(archive_file))
    local('tar -cvzf {0} application-core'.format(archive_file)
          .format(archive_file))
    return archive_file


def unpack_uc_core():
    pass


def run_config_tests():
    print green('Testing configuration...')
    with cd(os.path.join(os.curdir, 'application-core')):
        local('nosetests')


def fake_activity(message):
    print green(message)
    for x in xrange(10):
        fastprint('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print green('OK')


def deploy_to_server(archive_file):
    fake_activity('Copying {0} to server...'.format(archive_file))
    fake_activity('Unpacking {0} to /opt/app/application-core/...'
                  .format(archive_file))


def restart_server():
    print green('Restarting app server...')
    for x in xrange(10):
        fastprint('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print green('OK')


def deploy():
    clean()
    run_config_tests()
    archive_file = pack_uc_core()
    deploy_to_server(archive_file)
    restart_server()
