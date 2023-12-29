import sys

instance_type = sys.argv[1]

if instance_type == "t2.small":
    print("This Instance type is used in dev environment")
elif instance_type == "t2.medium":
    print("This Instance type is used in stating/QA environment")
elif instance_type == "t2.large":
    print("This Instance type is used in Production environment")
else:
    print("You selected instance type is not allowed to use.")