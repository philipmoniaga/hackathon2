FROM python:2.7

MAINTAINER MAINTAINER Philip Moniaga
# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=./
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/opt
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/opt/intercom


RUN pip install -U "setuptools==3.4.1"
RUN pip install -U "pip==1.5.4"
RUN pip install -U "Mercurial==2.9.1"
RUN pip install -U "virtualenv==1.11.4"
RUN pip install -U "pytest==4.6.3"

# Create application subdirectories
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ
RUN mkdir /var/logs
VOLUME ["$DOCKYARD_SRVPROJ/src"]
ENV        SHELL=/bin/bash
CMD        ["python"]
