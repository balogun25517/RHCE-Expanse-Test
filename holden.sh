#!/bin/bash 

ansible all -b -m user -a "name=holden password=earth groups=wheel append=yes"
ansible all -b -m file -b -a "path=/home/holden/.ssh state=directory"
ansible all -b -m copy -b -a "src=/home/holden/.ssh/id_rsa.pub dest=/home/holden/.ssh/authorized_keys"
ansible all -b -m lineinfile -a "path=/etc/sudoers state=present line='holden ALL=(ALL) NOPASSWD:ALL'"
#ansible all -b -m file -a "path=/etc/yum.repos.d/* state=absent"
ansible all -b -m command -a "rm -rf /etc/yum.repos.d/*"
ansible all -b -m command -a "yum clean all"
