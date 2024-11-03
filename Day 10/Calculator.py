def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multip(n1, n2):
    return n1 * n2

def divi(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": multip,
    "/": divi
    
}

answer = 0
done = True
n1 = float(input("What is the first number?: "))
while done:
    for symbol in operation:
        print(symbol)

    picked_operation = input("Pick an operation: ")

    n2 = float(input("What's the second number?: "))
        

    if picked_operation == "+" :
        answer = operation["+"](n1, n2)
        print(f"{n1} {picked_operation} {n2} = {answer}")
            
    elif picked_operation == "-":
        answer = operation["-"](n1, n2)
        print(f"{n1} {picked_operation} {n2} = {answer}")
            
    elif picked_operation == "*":
        answer = operation["*"](n1, n2)
        print(f"{n1} {picked_operation} {n2} = {answer}")
            
    elif picked_operation == "/":
        answer = operation["/"](n1, n2)
        print(f"{n1} {picked_operation} {n2} = {answer}")
        
    done = input(f"Are you done calculating with {answer}? type y or n: ").lower()
    
    
    if done == "n":
        n1 = answer
    else:
        break
    