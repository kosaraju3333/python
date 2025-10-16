import re

line = "Jan 15 12:44:50 server sshd[1234]: Failed password for user nurix-dev from 192.172.5.10 port 443 and ip 10.5.4.5.6"

ip_pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
# user_pattern = r'user\s+\S+'
user_pattern = r'user\s+(\S+)'

port_pattern = r'port\s+(\d+)'

# ip_match = re.search(ip_pattern, line)
ip_match = re.findall(ip_pattern, line)
user_match = re.search(user_pattern, line)
port_pattern = re.search(port_pattern, line)

print(ip_match)
print(user_match.group(1))
print(port_pattern.group(1))




# print(match.group())

# import re

# line = "Failed password for user nurix-dev from 192.172.5.10 port 443"
# user_match = r"user (\S+)"


# match = re.search(user_match, line)
# print(match.group(1))

# if match:
#     print(match.group(1))  # nurix-dev