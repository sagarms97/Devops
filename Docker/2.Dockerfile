FROM ubuntu: latest
LABEL "Author"="sagar"
LABEL "Project"="Nano"
ENV DEBIAN_FRONTEND=noninteractive			                          # making noninteractive to stop the errors
RUN apt update                     		                          	# Every RUN instruction will create a layer
RUN apt install apache2 git -y     	                          		# best practice is to have less layer
CMD ["/usr/sbin/apache2 ctl","-D", "FOREGROUND"]    	

EXPOSE 80                		                                      # port mapping
WORKDIR /var/www/html
VOLUME /var/log/apache2            		                            # dont want to lose logs, in case the container deleted
ADD nano.tar.gz /var/www/html       		                        	# untar the content in html
















