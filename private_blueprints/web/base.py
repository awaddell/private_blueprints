from __future__ import absolute_import, print_function

__author__ = 'awaddell'
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


from stacker_blueprints.asg import AutoscalingGroup


class BaseWeb(AutoscalingGroup):
    def create_conditions(self):
        logger.debug("No conditions to setup for %s", self.name)

    def create_security_groups(self):
        logger.debug("No security_groups to setup for %s", self.name)

    def create_load_balancer(self):
        logger.debug("No load_balancer to setup for %s", self.name)

    # def create_iam_profile(self):
    #     logger.debug("No iam_profile to setup for %s", self.name)

    def create_autoscaling_group(self):
        logger.debug("No autoscaling_group to setup for %s", self.name)

    def generate_user_data(self):
        logger.debug("No generate_user_data to setup for %s", self.name)

    def create_template(self):
        self.create_conditions()
        self.create_security_groups()
        self.create_load_balancer()
        # self.create_iam_profile()
        self.create_autoscaling_group()
