#xargs
def student(id):
    print(id)
student(101) 

def student(id,name):
    print(id,name)
student(101,"lewa")   

def student(*details):
    print(details)
student(101,"Lewa",3.23)    

def add(num1,num2):
    sum=num1+num2
    print(sum)
add(50,60)    
    