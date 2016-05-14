from __future__ import absolute_import, print_function
from private_blueprints.vpc.base import BaseVPC

__author__ = 'awaddell'
# -*- coding: utf-8 -*-

from troposphere import ec2, Ref, Output

import logging
logger = logging.getLogger(__name__)

# inherit via my base method
# from . import base

# or inherit directly
# from stacker_blueprints.vpc import VPC

VPC_NAME = "VPC"
VPC_ID = Ref(VPC_NAME)
DEFAULT_SG = "DefaultSG"
NAT_SG = "NATSG"


class MyVpc(BaseVPC):
    LOCAL_PARAMETERS = {
        "CidrBlock": {
            "type": str,
            "description": "Base CIDR block for subnets.",
            "default": "10.128.0.0/16"},
        "AZCount":  {
            "type": int,
            "default": 2,
        }
    }

    def create_conditions(self):
        super(BaseVPC, self).create_conditions()

    # Case 1: example override method using exact grandparent stanza
    def create_vpc(self):
        t = self.template
        t.add_resource(ec2.VPC(
            VPC_NAME,
            CidrBlock=Ref("CidrBlock"), EnableDnsSupport=True,
            EnableDnsHostnames=True))

        t.add_output(Output("VpcId", Value=VPC_ID))

    # Case 2: example override method using modified values
    def create_default_security_group(self):
        logger.debug("setting up Custom_security_group %s", self.name)
        t = self.template
        t.add_resource(ec2.SecurityGroup(
            DEFAULT_SG,
            VpcId=VPC_ID,
            GroupDescription='My Default Security Group'))
        t.add_output(
            Output('DefaultSG',
                   Value=Ref(DEFAULT_SG)))

    def create_dhcp_options(self):
        super(BaseVPC, self).create_dhcp_options()

    # Case 3: how can I make the grandparent method run using the grandparent method values?
    def create_network(self):
        super(BaseVPC, self).create_network()

        # otherwise, the grandparent method doesn't run at all

        # these instantiations serve no purpose here
        # def create_template(self):
        #     self.create_conditions()
        #     self.create_vpc()
        #     super.create_internal_zone()
        #     self.create_default_security_group()
        #     self.create_dhcp_options()
        #     self.create_network()
