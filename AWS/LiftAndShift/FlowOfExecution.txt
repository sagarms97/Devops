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


