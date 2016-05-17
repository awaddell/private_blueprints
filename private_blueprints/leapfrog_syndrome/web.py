from __future__ import absolute_import, print_function
from troposphere import Join, FindInMap, Ref, autoscaling, GetAtt, Base64, If
from troposphere.autoscaling import Tag as ASTag
from private_blueprints.web.base import BaseWeb

__author__ = 'awaddell'

ELB_NAME = "%sLoadBalancer"
# CLUSTER_SG_NAME = "%sSG"
# ELB_SG_NAME = "%sElbSG"
ASG_INSTANCE_NAME = "web"


class MyWeb(BaseWeb):
    LOCAL_PARAMETERS = {
    }

    def create_conditions(self):
        super(BaseWeb, self).create_conditions()

    def create_security_groups(self):
        super(BaseWeb, self).create_security_groups()

    def create_load_balancer(self):
        super(BaseWeb, self).create_load_balancer()

    def create_autoscaling_group(self):
        super(BaseWeb, self).create_autoscaling_group()

    def get_launch_configuration_parameters(self):
        return {
            'ImageId': FindInMap('AmiMap',
                                 Ref("AWS::Region"),
                                 Ref('ImageName')),
            'InstanceType': Ref("InstanceType"),
            'KeyName': Ref("SshKeyName"),
            'UserData': self.generate_user_data(),
            'SecurityGroups': self.get_launch_configuration_security_groups(),
        }

    def get_autoscaling_group_parameters(self, launch_config_name, elb_name):
        return {
            'AvailabilityZones': Ref("AvailabilityZones"),
            'LaunchConfigurationName': Ref(launch_config_name),
            'MinSize': Ref("MinSize"),
            'MaxSize': Ref("MaxSize"),
            'VPCZoneIdentifier': Ref("PrivateSubnets"),
            'LoadBalancerNames': If("CreateELB", [Ref(elb_name), ], []),
            'Tags': [ASTag('Name', ASG_INSTANCE_NAME, True)],
        }

    def generate_user_data(self):
        stanza = Base64(Join(
            "",
            [
                "#cloud-config\n",
                "apt_update: true\n",
                "apt_upgrade: true\n",
                "ssh_authorized_keys:\n",
                "  - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQChIC/Hxpqhxl6XTRHTkHR8p0DgVelczDmqCXkR4khh4PY5xp9i7F/IDXPRXt+4sfKrhdNclDMQh7AE2wyGHsOIWoeD47aKd10t6p4Tt42+e3N1ATRzXNCXP8DGeQx0ZgJ6O6Tls6V/ArXXnrnIxpvSamnrCcfVDCKUyFkxcVb02zhKUXJ81fKXSBrw1WSnOXLVT/Y8PBb0OlOFX/lYTZ7Bb3m3AxiCTEozLsmteDtGNJh4gzCNQ9l3SV+lFJ5l87Jc8y6YdXpDovXTl11z/5s03KNdnecSckLwkUuiYzufLkQdVsA8AfiTo1RwRTHuGjeL+RBPDN8xIa1AR/uzeaDt ali@isp20.com\n",
                "write_files:\n",
                "-  encoding: b64\n",
                "   content: PD9waHAgcGhwaW5mbygpOyA/Pgo=\n",
                "   path: /var/www/html/phpinfo.php\n",
                "   permissions: '0644'\n",
                "   owner: root:root\n",
            ]
        ))
        return stanza
