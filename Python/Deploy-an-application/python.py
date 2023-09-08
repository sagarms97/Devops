#!/usr/bin/python
from fabric.api import *


    sudo("yum install mariadb-server -y")
    sudo("systemctl start mariadb")
    sudo("systemctl enable mariadb")

def web_setup(WEBURL, DIRNAME):
    print("####################################################")
    local("apt install zip unzip -y")

    print("####################################################")
    print "Installing dependencies"
    sudo("yum install https wget unzip -y")
    print("####################################################")
    print "start and enable the service"
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print "Downloading & pushing website to webserver"
    local(("wget -o website.zip %s") % WEBURL)
    local("wget -o website.zip")

    with lcd (DIRNAME):
	    local("zip -r tooplate.zip * ")
	    put("tooplate.zip", "/var/www/html/", use_sudo = True)
	with cd("/var/www/html/"):
		sudo("unzip tooplte.zip")
		sudo("systemctl restart httpd")
		print "website setup is done"


