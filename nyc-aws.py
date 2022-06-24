#!/usr/bin/env python3
import os
import sys
import argparse
try:
    import json
except ImportError:
    import simplejson as json
class ExampleInventory(object):
    def __init__(self):
        self.inventory = {}
        self.read_cli_args()
        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()
        print (json.dumps(self.inventory))
    # Example inventory for testing.
    def example_inventory(self):
        return {
            'nyc_aws': {
                'hosts': ['node3', 'node4'],
                'vars': {
                    'ansible_ssh_private_key_file':
                        '~/.ssh/id_rsa',
                    'example_variable': 'value'
                }
}, '_meta': {
                'hostvars': {
                    'node3': {
                        "ansible_fqdn": "node3.ansi.example.com",
                        "ansible_hostname": "node3",
                        'security_group': 'web_9999'
}, 'node4': {
                        "ansible_fqdn": "node4.ansi.example.com",
                        "ansible_hostname": "node4",
                        'security_group': 'web_9898'
} }
} }
    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}
    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()
# Get the inventory.
ExampleInventory()
