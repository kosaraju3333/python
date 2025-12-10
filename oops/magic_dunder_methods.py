class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"{self.book_name} by {self.name}"

    def __call__(self, *args, **kwargs):
        print("Hi")

    def __del__(self):
        print("Author object has been deleted.")

a=Author("Ramki","Python basics to advance",309)
print(len(a.name))

### called __string__
print(a)

### called class object as a function
a()

# ### Delete a class object
# del a
# print(a)

print(str.__add__("ram","123"))

print(str.__str__(a.name))