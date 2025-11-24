import re

order_id_pattern = r'ID\s+\d+'
user_pattern = r'User (\S+)'
ip_pattern = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'

with open('log_file.log','r') as f:
    for line in f:
        # print(line)
        if "Payment delayed" in line:
            payment_delayed_match = re.search(order_id_pattern,line)
            with open('script_log.txt','a') as file:
                print(f"############ Payment delayed info ##############",file=file)
                print(payment_delayed_match.group(),file=file)

            print(f"############ Payment delayed info ##############")
            print(payment_delayed_match.group())

        if "logged in" in line:
            user_match = re.search(user_pattern, line)
            ip_match = re.search(ip_pattern, line)
            with open('script_log.txt','a') as file:
                print(f"############ Logged in info ##############", file=file)
                print(f"Username = {user_match.group(1)}, logged in from IP = {ip_match.group()}", file=file)


            print(f"############ Logged in info ##############")
            print(f"Username = {user_match.group(1)}, logged in from IP = {ip_match.group()}")

        if "ERROR" in line:
            error_match = re.search(r'ERROR (\S+)', line)
            with open('script_log.txt','a') as file:
                print(f"############ ERROR info ##############", file=file)
                print(f"{error_match.group(1)}", file=file)

            print(f"############ ERROR info ##############")
            print(f"{error_match.group(1)}")


