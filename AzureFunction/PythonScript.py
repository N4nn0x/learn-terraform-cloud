import subprocess
import paramiko
from flask import Flask, request, jsonify

app = Flask(__name)

# Define the Docker container name
container_name = "nano"

# Define VM SSH credentials and IP address
vm_host = "20.70.52.229"
vm_username = adminuser
vm_password = "-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
"

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
