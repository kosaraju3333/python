import re
ip_pattern = r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
# ip_pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
user_pattern = r'user (\S+)'
port_pattern = r'port (\S+)'
with open('log-file.txt','r') as file:
    for line in file:
        if "Failed password" in line:
            # print(line)
            ip=re.search(ip_pattern, line)
            print(f"IP {ip.group()}")
            user=re.search(user_pattern, line)
            print(user.group())
            port=re.search(port_pattern, line)
            print(port.group())


