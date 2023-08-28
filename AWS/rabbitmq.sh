#!/bin/bash
yum update
yum install epel-release -y
yum install wget -y
cd /tmp 
yum install rabbitmq-server -y
yum install firewalld -y
systemctl enable rabbitmq-server
systemctl start firewalld
systemctl enable firewalld
systemctl status firewalld
firewall-cmd --add-port=5672/tcp
firewall-cmd --runtime-to-permanent
systemctl start rabbitmq-server
systemctl enable rabbitmq-server
systemctl status rabbitmq-server
yum install vim -y
sudo vim /etc/rabbitmq/rabbitmq.config
[{rabbit, [{loopback_users, []}]}].
:wq
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
sudo systemctl restart rabbitmq-server
