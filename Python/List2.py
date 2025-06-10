subjects=["C","C++","Java","Python","Go"]
subjects2=[789,367,6530,820,216,216,216]

print(len(subjects))#length finding

subjects.append("JavaScript")#add/append new variable
print(subjects)

subjects.insert(2,"Django")#insert new variable on th position
print(subjects)

subjects.remove("JavaScript")#remove of declare variable
print(subjects)

subjects.sort()#sort of lists elements
print(subjects)
subjects2.sort()#sort of lists elements
print(subjects2)

subjects.reverse()#reverse of every elements
print(subjects)

subjects.pop()#pop of last element of the list
print(subjects)

subjects.clear()#clear of the lists elements
print(subjects)

subjects3 = subjects.copy()
print(subjects3)

pos = subjects2.index(216)#postion elements
print(subjects2)

cou = subjects2.count(216)#counts specific element
print(subjects2)