# RHCE-Expanse-Test
My Solutions for the RHCE Expanse Practice Test 


RHCE8 Practice Test EXPANSE
This exam covers objectives from EX294 and EX407
Use rd.break’s rhce8 test environment to complete this test. You will also need the chi-aws.py and nyc- aws.py scripts which are included in the Appendix. Add an extra 4GB hard drive to node1. Ansible should already be installed.
Task 1: Set up Ansible
1. Create a user named holden with a password of 'earth' on the control node. Create an ssh keypair for this user.
2. Create a directory /home/holden/plays where all of your files for this exam will be created.
3. Create a configuration file that:
• Runs ansible commands as the user holden
• Points at the inventory directory /home/holden/plays/inventory
• Allows you to update at most 5 servers at a time
• Set the roles directory to /home/holden/plays/roles as well as any other required directories
• Runs ansible as a non-root user by default
4. Use the 2 dynamic inventory files that are included (chi_aws.py and nyc_aws.py) to create an inventory that meets the following requirements:
• Your inventory is made up of 4 groups: ◦ dev
◦ chi_aws (member of web group) ◦ nyc_aws (member of web group) ◦ web
• node1.ansi.example.com is a member of dev
• Other nodes will be assigned to their groups via the python scripts
◦ node2.ansi.example.com is a member of the chi_aws and web groups ◦ node3.ansi.example.com is a member of the nyc_aws and web groups ◦ node4.ansi.example.com is a member of the nyc_aws and web groups
Task 2: Adhoc Commands
1. Write a script called holden.sh that:
• Creates the user holden on all hosts with a password of earth. He should have a secondary group of wheel.
• Sets up passwordless login to each node for holden.
• Sets up the proper sudo privileges that allow holden to elevate privileges without using a
password.
• Deletes all repo files currently located in /etc/yum.repos.d/ on nodes 1-4.
Task 3: Secrets
1. Create an encrypted vault file (using thering as the password) named ~/plays/vars/secret.yml that will set the following variables:
• crew_pass = 'roci'
• muscle_pass = 'duhhh'
2. Save the password to secret.yml file in a file named ~/plays/secret_key. 3. Make your playbooks use the secret.yml file without interaction.
Task 4: Set up Repositories
 
1. Create a playbook called repo.yml that will:
• Create a single repo file named exam.repo that will include the following repositories:
◦ A repository named base with a description of "Exam BaseOS Repo" that points at the repository located at http://repo.ansi.example.com/BaseOS.
◦ A repository named apps with a description of "Exam AppStream Repo" that points at the repository located at http://repo.ansi.example.com/AppStream.
• Both repositories should be enabled and gpg checking should be disabled
Task 5: Set timezone
1. Write a playbook named time.yml that will:
• Set the timezone on the chi_aws servers to American Central time.
• Set the timezone on the nyc_aws servers to American Eastern time.
• On the web nodes:
◦ Creates a file named /var/log/logins.log owned by root,with a group of root and permissions of 0766. The file should contain the line:
---- User Logins for HOSTNAME ----
where HOSTNAME is replaced with the fully qualified domain name of the node.
◦ Add the following line to /etc/skel/.bashrc: date >> /var/log/logins.log
Task 6: Packages and Services
1. Write a playbook named packages.yml that will:
• Install git, php, httpd, mod_ssl, mariadb, and mariadb-server on the dev group.
• Install php, httpd, and mod_ssl on the web group.
• Updates all packages on all nodes
• Verify that the firewall is running and start up apache for the web group and allow secure and
non-secure HTTP traffic.
• Verify the firewall is running on the dev group and start apache and mariadb-server. Allow tcp
traffic on ports 80, 443, and 3306.
• All services and firewall rules should survive a reboot.
Task 7: Set up Users
1. Create a file named ~/plays/vars/crew.yml with the following information in it:
2. Write a playbook called users.yml that uses the crew.yml file that you just made to create the users for the nodes.
• Passwords will be pulled from the secret.yml file from earlier everyone except the muscle users will be using the crew_pass variable for their passwords.
• All users should be created on the dev group.
• The muscle users should be created on the nyc_aws group.
• The brains users should be created on the web group.
      crew
 name
groups
shell
expires
naomi
wheel, brains
/bin/bash
Insert a value for never
amos
muscle
/sbin/nologin
Insert value for 60 days from now
alex
brains
/bin/sh
Insert value for 60 days from now
bobbie
muscle
/bin/bash
Insert value for 60 days from now
         
Task 8: Facts
1. Create a playbook that will contains 2 plays . Thei first play will place custom facts file on the web group. The file should:
• Be named custom.fact
• Contain a section called customer
• Nodes in the nyc_aws group should have these facts:
◦ company – Big Apple Hosting
◦ contact – miller@bigapplehosting.com
• Nodes in the chi_aws group should have these facts:
◦ company – Windy City Hosting
◦ contact – chrisjen@windycityhosting.com
2. Create a second play that will build a dynamic index.html page to be placed in /var/www/html/index.html. The page should contain:
<H2>Welcome to HOSTNAME at Windy City Hosting!</H2>
<p>This webserver has ### MB of RAM to serve up your requests on IP ADDRESS. If you have questions, please email chrisjen@windycityhosting.com</p>
• Everything in red should be dynamically generated for each host.
• This play should run on the web group.
Task 9: Creating a Role
1. Create a directory for your roles: ~/plays/roles
2. In the roles directory, create a role named vsftpd-web. The role should do the following:
• Install vsftpd, start and enable the service, and create appropriate firewall rules.
• Creates a file /etc/vsftpd/banned_emails that includes: joe@mama.com, joe@daddy.com, and
joe@sistertoo.com
• Includes these default variables:
◦ ftp_banner – Eff Tee Pee ◦ ftp_anon_enable – YES ◦ deny_emails - YES
• Changes the following settings in /etc/vsftpd/vsftpd.conf:
◦ Changes the anonymous_enable line to include the variable ftp_anon_enable.
◦ Enables a banner and changes the banner line to use the ftp_banner variable in place of the
word "blah"
◦ Sets deny_email_enable to the value in the variable deny_emails.
• Restarts vsftpd any time a change is made to the config file.
3. Create a playbook named vsftpd.yml that installs your new role on node2.
Task 10: Using RHEL System Roles
1. Install the the timesync RHEL system role on node1. 2. Use the following ntp servers with iburst enabled:
• time-a-g.nist.gov
• time-a-wwv.nist.gov • time-e-b.nist.gov
Task 11: Storage
1. Write a playbook that only runs on all servers called storage.yml that meets the following requirements:
 
• On nodes that do NOT have a /dev/sdc, it will mount /dev/sdb on /NODE-backup where NODE is the hostname of the node.
• On nodes that DO have a /dev/sdc, it will mount /dev/sdc on /NODE-backup where NODE is the hostname of the node
• On the node that has the extra hard drive, create a logical volume called tycho_station in the volume group belters.
• The vg should reside on the 4GB storage device.
• Mount an ext3 filesystem on the new logical volume in the directory /logical.
Task 12: Blocks
1. Write a playbook named rescue.yml that will:
• Create a backup of the /etc/httpd/conf/httpd.conf file named httpd.conf.backup on the
control node.
• Copy a new config file over to the node and restart the httpd server. Simulate a bad config file
by uploading a file that contains only the line "I am a bad config file".
• If the server fails to restart (and it should), then the play should recover by re-uploading the
backup file and restarting the httpd server. 2. Run this play on the web group.
Task 13: Security
1. Create a playbook called security.yml that will:
• Apply the rhel-system-role.selinux to the web group.
• Use the hostvars to determine which security_group each node is in:
◦ web_9999 should have selinux_state set to enforcing ◦ web_9898 should have selinux_state set to permissive
Task 14: Using Variables
1. Write a playbook called maria.yml that will run on the all nodes that will:
• Check the mariadb log on node1for the last time it was restarted using this (admittedly super ugly) bash one-liner: grep ready /var/log/mariadb/mariadb.log | tail -n1 | awk '{print $2,"on",$1}'
• Register the output of the above command and then on the web group, add a line to the bottom of /var/www/html/index.html that says "The database was last restarted at BLANK" (where BLANK is the output.
• If the command from above does not return a value, then the line should read "The database is NOT RUNNING!"
Task 15: Archiving
1. Write a playbook called configs.yml that will run on all hosts. It should:
• Create a bzip2 archive of the /etc/ directory named HOSTNAME_etc_backup.tar.bz2 where HOSTNAME is the name of the node.
• Each backup file should be copied to the /logical/backups directory on node1
Task 16: Scheduled Tasks
1. Write a playbook named scheduled.yml that will run on all hosts. It should:

• Create a task that will run every Friday at 5:00pm that uses the wall command to output the message "Time to go home!" to all logged in terminals.
• It should run from the root user and have a name of "Dismiss the staff".
Task 17: Ansible Galaxy Roles
1. Install the ansible galaxy role geerlingguy.nfs in the roles directory. 2. Write a playbook called nfs.yml that will:
• Apply the geerlingguy.nfs role to node1 using this for your nfs export: /logical/backups *(ro,sync,no_root_squash)
• Create a mount in the /configs directory on all nyc-aws hosts that points at the newly created nfs share.
• Ensure that the nfs share in /configs is mounted at boot.
