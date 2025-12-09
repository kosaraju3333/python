class Father:
    def sleep(self):
        print("Sleeps from 10:00 PM to 5:00PM")
    def eat(self):
        print("eating")

class Son(Father):
    def sleep(self):
        print("Sleeps from 10:00 PM to 8:00PM")
        super().sleep()


ram=Son()
ram.sleep()