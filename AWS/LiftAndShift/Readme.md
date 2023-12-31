### About project
- Muti-tier web application stack (vprofile)(using vagrant)
- Host & run on aws cloud for production
- we are going to use lift and shift  strategy

### Scenarios
- Applications services running on Physical / virtual machines
	- Exs:- oracle, Nodejs, linux, php, nginx, java, apache2, etc..
- we have all these work load in our datacentre 
	- so many servers running variety of services on local data-centre
- teams -> 
	- virtualization team
	- Data-centre operation team
	- Monitoring Team (24/7)
	- system admin team etc..


### Problem's
- It has complexity
- It is more complex for scale up /down 
- UpFront CapEx & Regular OpEX 
- Manual process
- Difficult to automate (virtual Layer)
- Time consuming

### Solutions
- solution to all these problem is to have **cloud computing setup** 
- instead of running our workload in our **data-centre**  , we run it on **cloud computing** **platform** 
- where we dont pay for **upfront** cost
- consuming infrastructure as a service (just like electricity) 
- we get **flexibility**
- Its **elastic** in nature.
	- we can scale out / in & really control in our cost
- Managing infrastructure is easier
- we can **automation** each & every step & process to avoid **human errors** & save **our time**.


### AWS Services
- EC2 Instances (Elastic compute cloud)
	- Vm for Tomcat, RabbitMQ, Memcached, mysql..
- ELB (Elastic Load Balancer)
	- Replacement for Nginx load Bal
- Autoscaling
	- Automation for VM scaling out / in our EC2 instances
	- which will automatically control our resources & cost
- S3 / EFS
	- EFS for shared storage
	- S3 for store / retrieve data
- Route 53
	- private DNS service

### Objectives
- Flexible Infrastructure
- No Upfront cost
- Modernize effectively
- IAAC (Infrastructure)

### Architecture of aws services for the project
- EC2 Instance
- ELB
- Auto scaling
- EFS /S3 
- Amazon certificate manager
- Route 53
