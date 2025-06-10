#xxargs->dictonary
def student(**details):
    print(details)
student(id=182,name="masfi")

def student(**details):
    print(details["name"])
student(id=182,name="masfi")   