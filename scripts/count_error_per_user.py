import re

ip_pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
user_pattern = r'user\s(\S+)'
error_users_count = { }
error_ip_count = { }
with open('error.log', 'r') as file:
    for line in file:
        if "ERROR" in line:
            # print(line) 
            user_match=re.search(user_pattern,line)
            user = user_match.group(1)

            ip_match = re.search(ip_pattern, line)
            ip = ip_match.group()
            # print(user)
            # print(ip)
            if user in error_users_count:
                error_users_count[user] = error_users_count[user] + 1
            else:
                error_users_count[user] = 1
            
            if ip in error_ip_count:
                error_ip_count[ip] = error_ip_count[ip] + 1
            else:
                error_ip_count[ip] = 1

for user, count in error_users_count.items():
    print(user, count)

for  ip, count in error_ip_count.items():
    print(ip, count)