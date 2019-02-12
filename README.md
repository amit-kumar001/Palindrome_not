# Palindrome_not
## Key features of this code  
<ol>
  <li> This code is intended to find the palindrome of string. If number is palindrome, it will exit otherwise it will check the condition again for the new input string.</li> 
  <li> This code is created using yield function.</li>
  <li> Program contains user defined function where the execution takes place.</li>
  <li> <strong>generator object *NAME* at 0x7f8c8370a410</strong> returned from the yield function is iterated to display the result of yield.</li> </ol>  
  Have a look at the below screenshot  
  
  ![untitled-1](https://user-images.githubusercontent.com/47202519/52624922-e10abd80-2ed5-11e9-9c6e-aaccf03d0813.jpg)
  
  


## User Defined Function  

```
def input_entries():
    n = input("Enter the value you want palindrome: ")
    n = n.casefold()
    a=pal(n)
    print(a)
    value_real = n
    value_return = a
    value_to_return = ""

    for i in value_return:
        value_to_return = value_to_return + i

    if value_real == value_to_return:
        print("Number is palindrome")
        exit()

    else:
        print("Number is not palindrome", end=".")
        print("Please try with the new number", )
        input_entries()

    return value_real,value_return
   ```
   
   
   
## How to run this file  
```
 python palindrome_or_not.py
 python3 palindrome_or_not.py
 
```
