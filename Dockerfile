# Use the official Spark base image
FROM apache/spark

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the Custom_folder to the container's working directory
COPY Custom_folder /app/Custom_folder

# Set the environment variables for Spark and Java
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

WORKDIR /app/Custom_folder

CMD ["sh", "-c", "spark-submit word_count.py 2>&1"]

CMD sleep 600