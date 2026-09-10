# Topic List

'''



1. String searching
2. String replacing
3. String counting
4. Split and Join
5.% formatting

'''

# % formatting

print("% Formatting")

name="ram"
city="Junagadh"
age = 20
salary=25000

print("My name is %s and my city is %s and my age is %d and my salary is %d." % (name , city ,  age, salary))
print("My name is %s and my city is %s " % (name , city ))
print("My name is %s and my age is %d and my salary is %.2f." % (name ,  age, salary))



# String Case Manipulation

text = "Python is a easy language"

print("Original Case :" , text)
print("Upper :" , text.upper())
print("lower :" , text.lower())
print("title:" , text.title())
print("Capitalize:" , text.capitalize())
print("Swapcase:" , text.swapcase())

# String Searching

text = "Python is a easy language."

print(text)

print("is Position:" , text.find("is"))

print("easy exists:" , "easy" in text)

print("easy index:" , text.index("easy"))

print(text.startswith("P"))
print(text.endswith("."))
print(text.endswith("language."))

# String Replacement

text = "Python is a easy language."

new_sentence = text.replace("language" , "to learn")



print(new_sentence)


# String Counting

name = "name is name or name no"

print(name.count("n"))


# String Split

animal='''Dog
Cat
Lion
Elephant
Cow
'''
animals = animal.split("\n")
print(animals)

for i in animals:
  print(i)