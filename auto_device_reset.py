import subprocess
import paramiko
import time

# IP address of the device to reset
device_ip = "x.x.x.x"

# SSH login credentials
ssh_username = "userman"
ssh_password = "password"

while True:
    # Ping the device until it responds

    ping_response = subprocess.run(["ping", "-c", "1", device_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        
    if ping_response.returncode != 0:
        
        print(f"Device at {device_ip} is not responding to pings. Retrying...")
    
    else:
            
        # Device is now responding to pings, so reset it with SSH
        print(f"Device at {device_ip} is responding to pings. Resetting with SSH...")

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(device_ip, username=ssh_username, password=ssh_password)

        try:
            stdin, stdout, stderr = ssh_client.exec_command("set-default")
            output = stdout.read().decode('utf-8').strip()
            error = stderr.read().decode('utf-8').strip()

        except paramiko.AuthenticationException:
            print("Authentication failed. Check your SSH credentials.")
            ssh_client.close()
            continue

        if error:
            print(f"Error resetting device: {error}")
        else:
            print("Device reset successfully.")

        ssh_client.close()
        
    # Wait for a few seconds before pinging the device again
    time.sleep(5)

