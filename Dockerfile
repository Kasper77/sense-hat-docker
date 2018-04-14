FROM raspbian/jessie

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD app /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# install required packages
RUN apt-get update && apt-get install -y sense-hat

# Make port 80 available to the world outside this container
#EXPOSE 80

# Run app.py when the container launches
CMD ["python", "microservice.py"]

