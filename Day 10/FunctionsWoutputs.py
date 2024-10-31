# def format_name(f_name, l_name):
#     a =print(f"The first name is {f_name}")
#     b =print(f"The last name is {l_name}")
    
#     return f"{a} {b}"
    
    
# formated = format_name(f_name= input("What is your first name?: ").title(), l_name=input("What is your last name?: ").title())

# print(formated)

def func1(text):
    return text + text

def func2(text):
    return text.title()

output = func2(func1("Hello"))

print(output)