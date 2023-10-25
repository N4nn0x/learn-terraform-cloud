import subprocess
import paramiko
from flask import Flask, request, jsonify

app = Flask(__name)

# Define the Docker container name
container_name = "nano"

# Define VM SSH credentials and IP address
vm_host = "your_vm_ip"
vm_username = "your_vm_username"
vm_password = "your_vm_password"

@app.route('/stop-container', methods=['POST'])
def stop_container():
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the VM
        ssh_client.connect(vm_host, username=vm_username, password=vm_password)

        # Build the Docker stop command
        docker_stop_command = f"sudo docker stop {container_name}"

        # Execute the Docker stop command on the VM
        stdin, stdout, stderr = ssh_client.exec_command(docker_stop_command)

        # Check the command's exit status
        if stdout.channel.recv_exit_status() == 0:
            return jsonify({"message": f"Container '{container_name}' stopped successfully."})
        else:
            return jsonify({"error": f"Error: {stderr.read().decode()}"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == '__main__':
    app.run()
