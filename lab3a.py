#!/usr/bin/env python3

text = "Good Morning Terry"

def print_out_text():
    print(text)

def return_text_value():
    return text

# ——————————————

# step 2: define the expected integer
number = 15   # ← use the exact number from the test file

# step 3: implement the number functions
def print_out_number():
    print(number)

def return_number_value():
    return number

if __name__ == "__main__":
    print_out_text()
    print_out_number()

