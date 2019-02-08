def pal(my):
    l = len(my)# check length
    for m in range(l -1,-1,-1): #
        yield my[m]

def input_entries():
    n = input("Enter the value you want to check palindrome or not: ")
    n = n.casefold() #similar to lower() string method
    a=pal(n)
    value_real = n
    value_return = a
    value_to_return = ""

    for i in value_return:
        value_to_return = value_to_return + i

    if value_real == value_to_return:
        print("Number is palindrome",end=". ")
        print("Thanks for visiting us")


    else:
        print("Number is not palindrome", end=".")
        print("Please try with the new number", )
        input_entries()

    return value_real,value_return

call_function = input_entries()
value_real =call_function[0]
value_return =call_function[1]








