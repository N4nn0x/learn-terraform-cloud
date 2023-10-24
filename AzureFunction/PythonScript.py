import subprocess

# Define the Docker container name
container_name = "nano"

# Build the Docker stop command
docker_stop_command = ["sudo", "docker", "stop", container_name]

try:
    # Run the Docker stop command
    subprocess.run(docker_stop_command, check=True)
    print(f"Container '{container_name}' stopped successfully.")
except subprocess.CalledProcessError as e:
    # Handle any errors, such as if the container doesn't exist
    print(f"Error: {e}")
