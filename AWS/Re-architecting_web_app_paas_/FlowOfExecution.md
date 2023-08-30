### Flow Of Execution
- Login to AWS Account
- Create key pair for Beanstalk instance 
- Create Security Group for Elastic cache, RDS & RabbitMQ
- Create -> RDS, Amazon Elastic Cache,  Amazon ActiveMQ
- Create Elastic Beanstalk Environment
- Update Security grp of Backend to allow traffic from Beanstalk SG
- Update Security grp of Backend to allow internal traffic from Beanstalk SG
- Launch EC2 instance for DB initializing.
- Login to the instance & initialize RDS DB
- Change health check on beanstalk to /login 
- Add 443 https listener to ELB
- Build artifact with backend information
- Deploy artifact to Beanstalk
- Create CDN with ssl certificate
- Update entry in Godaddy DNS zones
	- or we can do this Amazon route53 public DNS zone
- Test the URL.


#### Create Key Pair
Vprofile-bean-key

#### Create Security Group
- Backend services
	- name : vprofile-backend-sg
	- desc : security group for backend services
	- Rule : custom - port 22 - from MyIp   (its dummy rule)
		- all traffic - port all - from vprofile-backend-sg
		- (you can delete custom 22 rule)
	- Save

#### Now Create Backend Services
### RDS Services
- Subnet groups -> create DB subnet group
	- name : vprofile-rds -sub-grp
	- desc : vprofile-rds-sub-grp
	- avail zones : select all zones & all subnets
	- **create**
- Parameter groups  -> create parameter group
	- (RDS gives mysql, Oracle, PostgreSQL, MariaDB )
	- (Dont need ssh login , will login to EC2 Instance)
	- select DB : mysql 5.7
	- Group name : vprofile-rds-para-grp
	- desc : vprofile-rds-para-grp
	- **create**
- Data Base  -> Create 
	- standard create : mysql
	- version : mysql 5.7.22
	- free tier : template
	- settings : DB name -> vprofile-rds-mysql
	- Credentials : admin & password -> auto generate
	- Instance config : Burstable -> t2.micro  
	- storage : 20 gib
	- connectivity : default vpc
	- additional : select vprofile-rds -sub-grp  & select vpc  vprofile-backend-sg
	- additional config : db name -> accounts
		- select  : vprofile-rds-para-grp
		- backup -> 7days
		- monitoring -> disable
		- log exports -> select all (audit log , error log, general log)
		- [*] Enable delete protection 
	- **create DB**
	- copy & paste the credentials on notepad

   

### Elastic Cache Service
- Parameter -> Create
	- name : vprofile-memcache-para-grp
	- families : memcached 1.4
	- **create**
- subnet group -> create
	- name : vprofile-memcache-sub-grp
	- vpc : default vpc
	- subnet : select all subnets
	- **create**
- memcached cluster -> create cluster  ->  memcached cluster
	- standard create
	- AWS cloud
	- name : vprofile-Elastic-cache-service 
	- engine version : 1.4.5
	- select parameter group : vprofile-memcache-para-grp
		- node type : t2.micro
		- no of node : 1
	- select subnet group : select group
	- **next**
	- security group -> Manage  -> select vprofile-backend-sg
	- **choose**
	- Next
	- **create**
 

### Amazon-MQ service
- Rabbit -> single broker  -> next
	- name : vprofile-rmq
	- instance type : mq.t3.micro
	- rabbitmq access
		- user name : Rabbit,   password ->
	- additional
		- network : private access ( bean stalk EC2 instance it will privately accessing RMQ)
		- vpc : default
		- SG : select security group
		- tag : name -> vprofile-rmq01
		- Next
	- Create Broker

**One last thing left in backend that is DB Initializing.**
- we need to login RDS instance or mysql login create database & deploy our schema
-> Go-to RDS service and copy its endpoints & paste it to notepad


### Create EC2 instance (temporary)
- Launch instance
	- name : mysql-client
	- OS : ubuntu-server 22
		- */ The purpose is - we install mysql-client into ubuntu and login to RDS instance & initialize Database . After this we gonna delete this instance
	- type : t2.micro
	- key : Vprofile-bean-key
	- SG : mysql-client-sg
	- rule : ssh - port 22 - from myip
	- launch instance

 Git 
 ```bash
 ssh -i Download/vprofile-beanstalk-key ubuntu@ip
 sudo -i
 apt update -y
 apt install mysql-client -y
 # Now connect to RDS instance
 mysql -h <paste rds enpoints> -u admin -p<paste password>
 # not able to connect
 
 #ERROR 2003 (HY000): Can't connect to MySQL server on 'vprofile-rds-mysql.ceapieuvyupm.us-east-1.rds.amazonaws.com:3306' (110)
 
 # becz security group not letting us
 
```

EC2 -> SG -> vprofile-backend-sg 
inbound rule -> mysql/aurora - port 3306 - from mysql-client-sg
desc : allow to connect mysql client on port 3306
save

git 
```bash
 mysql -h <paste rds enpoints> -u admin -p<paste password>
 # connected
 show databases;
 use accounts;
 exit

git clone https://github.com/devopshydclud/vprofile-project.git
ls
cd vprofile-project
git branch -a
git checkout aws-refactor
ls
cd src/main/resource/
ls                           # he we have db_backup.sql file
# initialize database with this schema
# so initialize database wit this schema
mysql -h <paste rds enpoints> -u admin -p<paste password> accounts < db_backup.sql

# lets login
mysql -h <paste rds enpoints> -u admin -p<paste password> accounts
show databases;
exit



```




#### Now Frontend Services
### Elastic Beanstalk Service
- **Create I am role**
	- Aws standard
	- EC2 instance  ->  Next
	- policy -> 1- AWSElasticBeanstalkwebtier, 2>AdministratorAccess 3>AwsElasticSNS 4>EBSPlatFormEC2role 
	- role name : vprofile-bean-role
	- **Create**

- **Create01 Application**
	- name : vprofile-java-app
	- Environment name : vprofile-app-prod
	- domain : vprofile123 (it should be unique)
	
- **Service role**
	- select use an existing role : 
		- EC2 instance profile : vprofile-bean-role
		- key : vprofile-bean-key
	- select create & use new role
		- aws-elastic-role (default it will take )
	- VPC -> default
		- instance settings : check it activated
		- subnet : select all
	- - Tag : project -> vprofile
	- platform : tomcat
	- platform branch : tomcat 8.5 cornetto
	- Config more
- **presets** -> custom configure
	- instances -> EC2 sg ->vprofile-backend-sg
	- Root-volume : General purpose SSD & 8Gib
	- save
- **Capacity**  -> Edit  
	- Autoscaling -> load balancer
	- min instance - 2
	- max instances -8
	- instance type - t2.micro
	- save
- Rolling updates & deployments
	- deployment policy : rolling
	- Batch size : 80
	- save
- Security 
	- EC2 key pairs -> select key
	- I am instance pro 
	- create
	- save
- Tags
	- project -> vprofile
	- save
- **Create app**



- EC2 -> vprofile-backend-sg
	- add inbound rules :
	- custom 3306 vprofile-java-app
	- custom 11211 vprofile-java-app
	- custom 5671 vprofile-java-app
	- all traffic all vprofile-java-app
	- **save**

- Elastic Beanstalk
	- Environment -select name -> configuration
	- find load balancer and edit it
	- Add listener -> https 443 , and add SSL certificate
	- Process -> default -> action -> edit
	- health -> path - /login 
	- select stickiness
	- (it always connect same EC2 instance)
	- **save and apply**

### Build & deploy (from source code)

Git
```bash
cd /h/vprofile-project
git pull
git branch -a
git checkoutaws-refactor
cd src/main/resource
ls
vim application-properties
jdbc:mysql://<paste rds endpoints>:3306
user name=admin
password =paste password

memcache=<paste endpoints>

rqbbitmq=<paste endpoints>
port =5671
usr = rabbit
psw = paste password

:wq


cd ../../
ls                         # time to build
mvn install                # it will create an artifact 
ls
ls target/                 # here is the artifact
# we are going to upload this artifact to beanstalk environment




```

- **Elastic Beanstalk**
	- application version : upload
	- label : vprofile-v2.5
	- choose file : h/vprofile-project/target/vprofile-v2.war
	- upload
- [*] select version -> action -> deploy  
	- environment -> click name
	- vprofile-env -> Events
	- (check our endpoints ->we should see login page)
	- (we will make DNS entry)

**Godaddy**
DNS management -> add record
Cname : vprofile -> Paste EBS Endpoints
save

Browser 
https://vprofile.sagarsarawari.com



### Cloud Front Service
Its content delivery network
- create cloud 
	- origin : vprofile.sagarsarawi.com , match viewer
	- allowed http method -> all
	- setting -> all edges
	- Alternative domain name -> vprofile.sagarsarawari.com
	- choose certificate
	- security policy -> TLSV1
	- **Create distribution**
(it will take long time might be half an hour)

