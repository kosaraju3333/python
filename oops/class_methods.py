class Instructor:

    followers = 0
    following = 0

    def __init__(self,ins_name,ins_address):
        self.name=ins_name
        self.address=ins_address

    def display(self,subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")
        return 200
    
    def update_followers(self,follower_name):
        self.followers += 1
    
    def update_following(self,following_name):
        self.following += 1


instructor_1=Instructor("Ram","Hyderabad")
print(instructor_1.name)
print(instructor_1.address)
instructor_1.display("python")
instructor_1.update_followers("Krish")
print(f"{instructor_1.name} followers count is {instructor_1.followers}")

instructor_2=Instructor("Krish","Bangalore")
print(instructor_2.name)
print(instructor_2.address)
instructor_2.display("Java")
instructor_2.update_following("Ram")
print(f"{instructor_2.name} following count is {instructor_2.following}")
