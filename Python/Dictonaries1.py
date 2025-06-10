studentId={
       "23101182":"Masfi Rahman",
       "23101186":"Mahi Hasan",
       "23101189":"Robayet Ismum",
}
#print(studentId["23101182"])
#print(studentId["23101185"])#No value declare 
print(studentId.get("23101182"))
#print(studentId.get(23101185))#Not value declare
print(studentId.get("23101185","Not a valid key"))