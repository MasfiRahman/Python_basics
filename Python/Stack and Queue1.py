books=[]
books.append("Learn C")#push
books.append("Lean C++")#push
books.append("Learn Java")#push
print(books)

books.pop()
#books.pop()
#print(books)
print("Now the top book is : ",books[-1])

books.pop()
print("Now the top book is : ",books[-1])

books.pop()
#print("Now the top book is : ",books[-1])#Error showing
if not books:
    print("No books left")