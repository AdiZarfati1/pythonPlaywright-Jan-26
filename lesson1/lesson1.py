import keyword
import math

a=1
print(a)

print(keyword.kwlist) # נקבל בהדפסה זו את כל המילים השמורות של פייתון

print(type(["a", "b", "c"])) #list
print(type(("a", "b", "c"))) #tuple
print(type({"a", "b", "c"})) #set
print(type({"a": "1", "b": "2"})) #dict

print(type(123123123123123)) #int
print(type(-123123123123123)) #int
print(type(122.6345345)) #float
print(type(-122.6345345)) #float
print(type("text")) #str
print(type("""text""")) #str

print("lalalala", math.pi) #example of functions

My_name = "Adi"
my_name = 123
print(id(my_name))
print(my_name)
print(id(My_name))
print(My_name)

# del my_name
# print(my_name)

print(type(2345e17))
print(2345e17) #complex = סוג של מספר

