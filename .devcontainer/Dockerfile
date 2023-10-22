# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory for Python in the container
WORKDIR /usr/src/app/python

# Copy the local requirements.txt file for Python into the container at /usr/src/app/python
COPY python/requirements.txt ./

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r python/requirements.txt

# Set the working directory for Rust in the container
WORKDIR /usr/src/app/rust

# Copy the entire project directory into the container at /usr/src/app/rust
COPY rust .

# Build the Rust code using Cargo
RUN cargo build

# Make port 80 available to the world outside this container (you can remove this line if not needed)
EXPOSE 80

# Define environment variable (if needed)
# ENV NAME World

# Create a shell script to run both Python and Rust
RUN echo -e '#!/bin/sh\npython script.py &\n./target/debug/main' > /usr/src/app/run.sh
RUN chmod +x /usr/src/app/run.sh

# Run the shell script when the container launches
CMD ["/usr/src/app/run.sh"]
