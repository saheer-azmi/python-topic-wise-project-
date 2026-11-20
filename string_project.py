print("==customer cleaning system==")
customers=[
"saheer azmi  ",
 "Rahul kumar   ",
 "aman kumar  "]

print(customers[0].strip().title())
print(customers[1].strip().title())
print(customers[2].strip().title())


print("===employe management & data validator")
employe_name=" saheer azmi "
employe_id= "emp206"
email="SAHEER@GMAIL.COM"
department="python development"

print(employe_name.strip())
print(employe_id.upper())
print(email.lower())
print(department.title())
print(department.split())
print(email.endswith("GMAIL.COM"))
print(email.partition("@"))
print(email.find("GMAIL"))
print(employe_name.isalpha())
print(employe_id.isalnum())
print(email.lower())
print(len(employe_name))
print(employe_id.isalnum())
print(email.isupper())
print(department.count("o"))



print("/Text Analyzer/")
text="python is a powerful programming language.python is easy to learn.i am learning python for development. "
email="SAHEER.AZMI@GMAIL.COM"
website="https://www.python.org"
old_word="python"
new_word="java"


print(len(text))
print(text.count("i"))
print(text.count("is"))
print(text.count("python"))
print(old_word.replace("python","java"))
print(text.replace(old_word,new_word))
print(text.upper())
print(text.lower())
print(text.title())
print(email.lower())
print(email.upper())
print(website.startswith("https"))
print(email.partition("@"))
