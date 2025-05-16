import re

## 'r' it defines a raw string literal.
## "Don't interpret backslashes (\) as escape characters. Just pass them as-is."
## Without 'r', Python might misinterpret things:
ip_pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
user_pattern = r'user (\S+)'
port_pattern = r'port (\S+)'
try:
    with open('log-file.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            if 'Failed' in line:
                username = re.search(user_pattern, line)
                ### Find the IP address from the line by default it will give list so we converted to string using {''.join}
                ipaddress = ' '.join(re.findall(ip_pattern, line))
                port = re.search(port_pattern, line)
                print(f"Username = {username.group(1)}, IP = {ipaddress}, Port = {port.group(1)}")
except OSError as e:
    print(f"{e}")


### This Will read one line ata time
# with open('log-file.txt','r') as file:
#     line = file.readline()
#     # print(line)
#     while line:
#         print(line,end='')
#         line = file.readline()


