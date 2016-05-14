from __future__ import absolute_import, print_function
from private_blueprints.vpc.base import BaseVPC

__author__ = 'awaddell'
# -*- coding: utf-8 -*-

from troposphere import ec2, Ref, Output

import logging
logger = logging.getLogger(__name__)

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

    def create_vpc(self):
        super(BaseVPC, self).create_vpc()

    def create_default_security_group(self):
        super(BaseVPC, self).create_default_security_group()

    def create_dhcp_options(self):
        super(BaseVPC, self).create_dhcp_options()

    def create_network(self):
        super(BaseVPC, self).create_network()
