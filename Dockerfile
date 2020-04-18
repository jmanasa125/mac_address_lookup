# Get image for python program
FROM ubuntu

# run commands while creating the container
RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install python-setuptools
RUN apt-get -y install python-pip
RUN pip install requests

# copy file from local to container
COPY mac_addr.py /tmp/mac_addr.py


# run the python script
ENTRYPOINT ["python", "/tmp/mac_addr.py"]






