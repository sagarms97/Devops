#### Flow of execution
- Login to aws account
- create key pairs
- create security group
- Launch instance with user data (bash scripts)
- update ip to name mapping in route 53
- Build application from source code
- upload to s3 bucket 
- Download artifact to tomcat EC2 instance
- Setup ELB with https (amazon certificate manager)
- Map ELB endpoint to website name in godaddy DNS 
- verify
- Build auto scaling group for Tomcat instances


#### create key pair
vprofile-prod-key

#### create security group
1. Elastic load balancer
	1. name : vprofile-elb-sg
	2. rule: http - port 80 - from anywhere Ipv4 and Ipv6
	3. create sg
2. Tomcat
	1. name : vprofile-app-sg
	2. rule : custom - port 8080 - from vprofile-elb-sg
	3. and : ssh - port 22 - from  MyIp
	4. desc : allow traffic from ELB
	5. create sg
3. Backend services (Mysql, Memcached, RabbitMQ)
	1. name : vprofile-backend-sg
	2. rules : 
		1. ssh - port 22 -from MyIp
		2. mysql/aurora - port 3306 - from vprofile-app-sg - desc - allows tomcat to connect mysql
		3. custom - port 11211 - from vprofile-app-sg - desc - allows tomcat to connect memcached
		4. custom - port 5672 - from vprofile-app-sg - desc - allows tomcat to connect RabbitMq
		5. all traffic - all - from vprofile-backend-sg - desc - allow internal traffic to flow on all ports
	3. create sg

#### Launch instance with user data (bash scripts)

**local Git**
```bash
cd /h/
git clone http://github.com/devopshydclub/vprofile-project.git
cd vprofile-project/
git checkout aws-LiftAndShift   # new branch
cd userdata/
ls                              # here are the bashscripts

# use these scripts to run services

```


#####  EC2 instance for Mysql
1. 
	1. Name : vprofile-db01
	2. OS : centos7
	3. type : t2.micro
	4. key : vprofile-prod-key
	5. SG : vprofile-backend-sg
	6. Advance details : mysql.sh script

##### EC2 instance for memcached
1. 
	1. Name : vprofile-mc01
	2. OS : centos7
	3. type : t2.micro
	4. key : vprofile-prod-key
	5. SG : vprofile-backend-sg
	6. Advance details : memcache.sh script

##### EC2 instance for RabbitMQ
1. 
	1. Name : vprofile-mc01
	2. OS : centos7
	3. type : t2.micro
	4. key : vprofile-prod-key
	5. SG : vprofile-backend-sg
	6. Advance details : Rabbitmq.sh script

##### EC2 instance for Tomcat
1. 
	1. Name : vprofile-mc01
	2. OS : ubuntu20
	3. type : t2.micro
	4. key : vprofile-prod-key
	5. SG : vprofile-app-sg
	6. Advance details : tomcat_ubuntu.sh script


#### Route 53 service
It is designed to manage and route internet traffic efficiently.

- go to hosted zone
	domain name : sagarsarawari.com ( for this you have to buy domain)
	desc : Hosted zone for vprofile backend servers
	add simple records : add db01, mc01, rmq01 private ip address



**Local Git**
```bash
cd /h/vprofile-project
cd src/main/resources
ls
vim application.properties
# here change instance names like
db01 -> db01.sagarsarawari.com
mc01 -> mc01.sagarsarawari.com
rmq01 -> rmq01.sagarsarawari.com
:wq


cd
mvn install                    # it will create an artifact
ls                             # target folder will appear
cd target/
ls                             # we have aartifact here -> vprofile-v2.war
# we will store this local artifact to s3 bucket
# and tomcat server will download from s3 bucket
# upload artifact to s3 bucket from AWSCLI
# so we install AWSCLI



```

####  create I am user in aws
becz we are creating s3 bucket through AWSCLI commands and for that we need access key and secret key 

- Iam service
	- user : add user -> vprofile-s3-admin
	- programmatic access -> next
	- attach existing policies  -> search s3 full access -> next
	- create user
	- and download .csv file

**Local git**

```bash
cd
cat Downaloads/user.csv
# now configure aws
aws configure
access key -> paste access key
scret key  -> paste sceret key
region -> us-est-1
format -> Json

# now create s3 bucket
aws s3 mb s3://vprofile-artifact        # it will this bucket in s3 service
cd /h/vprofile-project
cd target/                          # now i'm going move this artifact to s3 bucket

aws s3 cp vprofile-v2.war s3://vprofile-artifact/vprofile-v2.war
aws s3 ls s3://vprofile-artifact
# inorder to download this artifact we have to create a role for tomcat instance




```

#### Create a role for tomcat
- iam service
	- create role -> use by EC2 -> next
	- s3FullAccess  -> next
	- role name : vprofile-artifact-role
	- save


**go-to vprofile-app01 instance**
	- action  -> security -> modify iam role -> select vprofile-artifact-role
	- save

**Now validate tomcat9 server**

```bash
ssh -i Download/vprofile-pro-key.pem ubuntu@ip
sudo -i
systemctl status tomcat9
cd /var/lib/tomcat9/webapps
ls                          # here will be aroot directory
# we will delete root directory
systemctl stop tomcat9
rm -rm ROOT                 # now we will download the artifact from s3 bucket
apt install awscli -y
cd
aws s3 ls s3://vprofile-artifact 
aws s3 cp s3://vprofile-artifactvprofile-v2.war /tmp/vprofile-v2.warls 
ls /tmp/
cp vprofile-v2.war /var/lib/tomcat9/webapps/ROOT.war
systemctl start tomcat9
cd /var/lib/tomcat9/webapps/ROOT
cd web-INF/classes
ls
cat application.properties


```

**If all the services are running and active state . then its time to create Load balancers**

#### Create Load Balancer

1. create target groups
	1. name : vprofile-app-TG
	2. port : 8080
	3. health check : /login
	4. advance : override 8080
	5. health threshold : 3
	6. available instance : select tomcat server - vprofile-app01
		1. include as pending below
	7. create target group
2. create load balancer
	1. name : vprofile-prod-elb
	2. avail zone : select all
	3. SG : vprofile-elb-sg
	4. listener : add https 443 vprofile-app-TG
	5. from acm : select certificate (sagarsarawari.com)
	6. create Load bal
view load balancer and copy DNS name

- **Go-to Godaddy**
	- dns
	- add records
		- cname -> vprofile -> paste DNS name
- **Check Browser**
	- http://vprofile.ssagarsarawari.com
	- user & password : admin_vp

#### Auto scaling group
create AMI for tomcat server (app01)
- vprofile-app01 instance -> action -> image -> create image
- name : vprofile-app-image

- **Auto scaling**
	- **launch configuration**
		- name : vprofile-app-LC
		- select ami :  vprofile-app-image
		- Instance type : t2.micro
		- iam role : vprofile-artifact-role
		- [*]  Enable EC2 instance
		- sg : vprofile-app-sg
		- key : vprofile-prod-key
		- create launch configuration
	- **auto scaling group**
		- name : vprofile-app-ASG
		- switch to launch configuration
		- select launch configuration
		- same VPC & select all subnets
		- [*]  enable load balancer
		- select TG
		- health check [./] elb
		- **next**
		- desired capacity : 1
		- max capacity : 4
		- min capacity : 1
		- [*] Target tracking
		- **next**
		- Add notification
		- **Create Auto scaling group**
**Terminate vprofile-app01**

**validate** : https://vprofileapp.sagarsarawari.com

**BOOOOM**










