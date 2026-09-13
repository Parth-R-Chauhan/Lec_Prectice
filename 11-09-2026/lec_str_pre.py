# String JOIN

words = ['Python' , 'java' , 'html']

result = ", ".join(words)
print(result)
result = " | ".join(words)
print(result)
result = " @ ".join(words)
print(result)

# String Strip

text = "     Hello world    ";

print("strip :" , len(text.strip()))
print("lstrip :" , len(text.lstrip()))
print("rstrip :" , len(text.rstrip()))

print("strip :" , text.strip())
print("lstrip :" , text.lstrip())
print("rstrip :" , text.rstrip())

print(f"the string {text} is remove space {text.strip()} length {len(text.strip())}")
print(f"the string {text} is remove left space {text.lstrip()} length {len(text.lstrip())}")
print(f"the string {text} is remove right space {text.rstrip()} length {len(text.rstrip())}")

print(len(text))

# Remove Non-Alphabetic Character


text = "python@1234"

clean_text = ""

for char in text:
  if char.isalpha():
    clean_text += char

print(text)
print(clean_text)

# String Cheking Method

text= "python@123"
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

text= "python"
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

text= " "
print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())
# Reverse String

text = 'Python'

reverse_text = "".join(reversed(text))

reverse_text1 = list(text)

reverse_text1.reverse()

print("".join(reverse_text1))

print(text[::-1])

print(reverse_text)

# Plindrome

text = input("\n Enter a string to check palindrome:")

reverse_text = text[::-1]

print(text)

print(reverse_text)

if text.lower() == reverse_text.lower():
  print("Plindrome")
else:
  print("Not Plingrome")

# Escape Characters

print("Hello\nWorld")
print("Hello\tworld")
print("she talk \"hello\"")
print('It\'s Python')
print("C:\\Python")