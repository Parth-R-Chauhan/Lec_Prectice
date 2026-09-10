

'''

1. String Formatting
2. String Indexing and slicing
3. f-string , format() , % formatting

'''

# Creating String

name = "Ram"
city = 'Rajkot'
work="student"


print(name)
print(city)
print(work)

# Multiline String

message = ''' Hello
Welcome to 
Lec practice sheet '''

print(message)

# String Indexing

text = "Computer"

print(text[0])
print(text[1])
print(text[2])
print(text[-1])
print(text[-2])

# String Slicing

print(text[0:3])
print(text[2:5])
print(text[:3])
print(text[3:])
print(text[:])
print(text[:-1])
print(text[::2])
print(text[::-1])

# String Concatinating

first_name = "Ram"
last_name = "Sharma"

full_name = first_name + " " +  last_name

print(full_name)

# String Formatting - f-string

item = "laptop"
price = 10.05

print(item)
print(price)

print(f"The price of {item} is {price}.")

# Decimal Places

print(f"The price of {item} is {price:.2f} dollars.")
print(f"The price of {item} is {price:.1f} dollars.")

# Expression inside f-string

a = 10
b = 20

print(f"Sum = {a + b}")

# format() Method

print("The price of {} is {}.".format(item , price))

# Positional Arguments

print("Hello , {0} {1}".format(first_name , last_name))
print("Hello , {1} {1}".format(first_name , last_name))
print("Hello , {1} {0}".format(first_name , last_name))


# Named Arguments

print("Hello , {first} {last}".format(first = first_name , last = last_name))
print("Hello , {last} {first}".format(first = first_name , last = last_name))