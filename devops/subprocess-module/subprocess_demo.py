import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# result = subprocess.run(["ls", "-l"])
print(result.stdout)
print(result.stderr)

# ram = subprocess.run(["free", "-h"], capture_output=True, text=True)
# print(ram.stdout)

ram = subprocess.run(["vm_stat"], capture_output=True, text=True)
print(ram.stdout)
print(ram.returncode)

pods_status = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
if pods_status.returncode != 0:
    print("Kubectl get pods command get an error ")
    print(pods_status.stderr)
else:
    print("Kubectl get pods command works fine")
# print(pods_status.returncode)
# print(pods_status.stderr)

## Shell True
status = subprocess.run("kubectl get pods", shell=True, capture_output=True, text=True)
print(status.returncode)
print(status.stderr)

### Another Useful Function: subprocess.Popen()
# Use Popen() when you want:
#
# long-running command
# streaming output live
# background process

process = subprocess.Popen(
    ["ping", "-c", "10", "google.com"],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:
    print(line.strip())