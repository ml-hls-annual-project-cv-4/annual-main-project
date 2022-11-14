FROM yandex/clickhouse-server

LABEL maintainer="Maksim Kovalenko"

# Copy all files from current directory
COPY . /home

# RUN instructions
# Some utils
RUN apt-get update \
&& apt-get install nano -y \
&& apt-get install net-tools 
# copy config file
RUN cp /home/default-user.xml /etc/clickhouse-server/users.d \
&& cp /home/additional_users.xml /etc/clickhouse-server/users.d \
&& cp /home/timezone_config.xml /etc/clickhouse-server/config.d \
&& cp /home/default_database.xml /etc/clickhouse-server/config.d

