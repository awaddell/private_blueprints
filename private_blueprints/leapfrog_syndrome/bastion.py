from __future__ import absolute_import, print_function
from troposphere import Base64, Join
from private_blueprints.bastion.base import BaseBastion
__author__ = 'awaddell'


class MyBastion(BaseBastion):
    def create_security_groups(self):
        super(BaseBastion, self).create_security_groups()

    def create_autoscaling_group(self):
        super(BaseBastion, self).create_autoscaling_group()

    def generate_user_data(self):
        stanza = Base64(Join(
            "",
            [
                "#cloud-config\n",
                "apt_update: true\n",
                "apt_upgrade: true\n",
                "ssh_authorized_keys:\n",
                "  - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQChIC/Hxpqhxl6XTRHTkHR8p0DgVelczDmqCXkR4khh4PY5xp9i7F/IDXPRXt+4sfKrhdNclDMQh7AE2wyGHsOIWoeD47aKd10t6p4Tt42+e3N1ATRzXNCXP8DGeQx0ZgJ6O6Tls6V/ArXXnrnIxpvSamnrCcfVDCKUyFkxcVb02zhKUXJ81fKXSBrw1WSnOXLVT/Y8PBb0OlOFX/lYTZ7Bb3m3AxiCTEozLsmteDtGNJh4gzCNQ9l3SV+lFJ5l87Jc8y6YdXpDovXTl11z/5s03KNdnecSckLwkUuiYzufLkQdVsA8AfiTo1RwRTHuGjeL+RBPDN8xIa1AR/uzeaDt ali@isp20.com\n",
                "packages:\n",
                # "  - python-pip\n",
                "  - fail2ban\n",
                # "  - awscli\n",
                "  - mysql-client\n",
                "  - s3cmd\n",
            ]
        ))
        return stanza

