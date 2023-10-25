import subprocess
from flask import Flask, request, jsonify

app = Flask(__name)

# Define the Docker container name
container_name = "nano"

# Build the Docker stop command
docker_stop_command = ["sudo", "docker", "stop", container_name]

@app.route('/stop-container', methods=['POST'])
def stop_container():
    try:
        # Run the Docker stop command
        subprocess.run(docker_stop_command, check=True)
        return jsonify({"message": f"Container '{container_name}' stopped successfully."})
    except subprocess.CalledProcessError as e:
        # Handle any errors, such as if the container doesn't exist
        return jsonify({"error": f"Error: {e}"}), 500

if __name__ == '__main__':
    app.run()


"""
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
"""
