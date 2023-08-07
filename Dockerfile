# Use the official Spark base image
FROM apache/spark

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the Custom_folder to the container's working directory
COPY Custom_folder /app/Custom_folder

# Set the environment variables for Spark and Java
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Start your Spark application (replace word_count_app.py with your actual app name)
CMD ["spark-submit", "--master", "local[*]", "/app/Custom_folder/word_count_app.py"]