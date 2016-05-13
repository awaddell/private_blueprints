from __future__ import absolute_import, print_function
__author__ = 'awaddell'
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


from stacker_blueprints.vpc import VPC


class BaseVPC(VPC):
    def create_conditions(self):
        logger.debug("No conditions to setup for %s", self.name)

    def create_vpc(self):
        logger.debug("No vpc to setup for %s", self.name)

    def create_internal_zone(self):
        logger.debug("No internal_zone to setup for %s", self.name)

    def create_default_security_group(self):
        logger.debug("No default_security_group to setup for %s", self.name)

    def create_dhcp_options(self):
        logger.debug("No dhcp_options to setup for %s", self.name)

    def create_network(self):
        logger.debug("No network to setup for %s", self.name)

    def create_template(self):
        self.create_conditions()
        self.create_vpc()
        self.create_internal_zone()
        self.create_default_security_group()
        self.create_dhcp_options()
        self.create_network()
