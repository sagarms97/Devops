#### AWS services
- Front-End
	- Bean Stalk (VM for Tomcat (app server))
	- Bean Stalk (Nginx & ELB Replacement)
	- Bean Stalk (automation for VM scaling)
	- S3 / EFS (Storage for the artifact)
- Back-End
	- RDS Instance  (Database)(Regular backup scaling easily)
	- Elastic Cache  (Replacement for memcached instance)
	- Active-MQ      (Replacement for RabbitMQ instance)
	- Route 53         (For DNS)
	- Cloud Front     (Content Delivery Network)

#### Objectives
- Flexibility
- No upfront cost
- IAAS
- PAAS & SAAS


#### Comparisons of LiftAndShit & Re-architecting projects 

**New Project                                                              Previous project**
- Bean stalk                                                              Tomcat   EC2 / vm
- ELB in Bean stalk                                                       Nginx lb / ELB
- Autoscaling                                                             Autoscaling
- EFS / S3                                                                EFS / S3
- RDS                                                                     Mysql EC2/ vm
- Elastic Cache                                                           memcached EC2 / vm
- Active MQ                                                               RabbitMq EC2 / vm
- Route53                                                                 Godaddy
