from __future__ import absolute_import, print_function
__author__ = 'awaddell'
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


from stacker_blueprints.bastion import Bastion


class BaseBastion(Bastion):
    def create_security_groups(self):
        logger.debug("No security_group to setup for %s", self.name)

    def create_autoscaling_group(self):
        logger.debug("No autoscaling_group to setup for %s", self.name)

    def generate_user_data(self):
        logger.debug("No generate_user_data to setup for %s", self.name)

    def create_template(self):
        self.create_security_groups()
        self.create_autoscaling_group()
