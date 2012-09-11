#!/usr/bin/env python
# <test_server_configs.py>
# Created: September 11, 2012
# Version: 0.0.1
# By:  (bwghughes@gmail.com)

import os
from lxml import objectify


class TestUCCoreConfig(object):
    def setup(self):
        """ This loads the XML file into an object so we can test it """
        file_under_test = os.path.join(os.curdir, 'application-core',
                                       'app.core.config.xml')
        with open(file_under_test) as f:
            config = f.read()
        self.config = objectify.fromstring(config)

    def teardown(self):
        pass

    def test_node_has_all_required_information(self):
        required_nodes = ['id', 'name', 'member-of', 'director-port']
        for required in required_nodes:
            assert getattr(self.config.cluster.node, required) is not None

    def test_application_has_all_required_information(self):
        required_nodes = ['root', 'logs', 'static-dir']
        for required in required_nodes:
            assert getattr(self.config.cluster.application, required) \
                is not None
