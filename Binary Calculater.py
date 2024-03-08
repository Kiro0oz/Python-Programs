# Kirolos Adel 20230295
# Malak Amr 20230416
# Ahmed Tamer 20230012

# First complement function
# Tested on
# 11111 >>> 00000
# 1010101111000 >>> 0101010000111
def first_complement(num):
    result = ""
    for char in num:
        if char == "0":
            result += "1"
        else:
            result += "0"
    return result


# Second complement function
# tested on
# 1011110 >>> 0100010
# 1010111101 >>> 0101000011
def second_complement(num):
    res = ""
    flip = False
    for i in reversed(num):
        if flip:
            if i == "0":
                i = "1"
            else:
                i = "0"
        if i == "1":
            flip = True
        res = i + res
    return res


# Addition function
# Tested on
# 1111 + 1111 = 11110
# 1011101 + 11101 = 1111010
def addition(bin1, bin2):
    width = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(width)
    bin2 = bin2.zfill(width)
    result = ""
    carry = 0
    for i in range(width - 1, -1, -1):
        res = carry
        if bin1[i] == '1':
            res += 1
        else:
            res += 0
        if bin2[i] == '1':
            res += 1
        else:
            res += 0
        if res % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result
        # check for overflow
        if res < 2:
            carry = 0
        else:
            carry = 1
    if carry != 0:
        result = '1' + result
    return result

# Subtraction function
# tested on:
# 101 - 11 = 010
# 110000011 - 1111111 = 100000100
def subtraction(binary_num1, binary_num2):
    max_length = max(len(binary_num1), len(binary_num2))
    binary_num1 = binary_num1.zfill(max_length)
    binary_num2 = binary_num2.zfill(max_length)

    borrow = 0
    result: str = ''

    for i in range(max_length - 1, -1, -1):
        num1 = int(binary_num1[i])
        num2 = int(binary_num2[i])
        difference = num1 - num2 - borrow
        final_answer = str((difference + 2) % 2)
        if difference < 0:
            borrow = 1
        else:
            borrow = 0
        result = final_answer + result

    return result


# the function that checks if the user input is a valid binary number
def is_valid(number):
    binary_digits = '01'
    return all(bit in binary_digits for bit in number)


def menu1():
    print("\n**Binary Calculator**\n"
          "A) Insert new number\n"
          "B) Exit")


def menu2():
    print(
        "\n**please select the operation**\n"
        "A) Compute one's complement\n"
        "B) Compute two's complement\n"
        "C) Addition\n"
        "D) Subtraction")


# Main()

# the first while loop takes the input from the user to navigate him to the second menu
# or exit the program
# and checks if the input is a valid choice or not
# if not it returns him to menu1 to choose a right choice
while True:
    menu1()
    choice_menu1 = input('Please select an option: ').upper()
    if choice_menu1 == 'B':
        break
    if choice_menu1 != 'A':
        print("Error! Please insert a valid choice")
        continue

    # to check if the user inserted a value or not and whether this value is a valid binary or not
    # if not it returns the user to insert a valid number
    while True:
        main_number = input("Please insert the first number: ")
        if main_number == '':
            print("Error! please insert a number\n")
            continue
        if not is_valid(main_number):
            print("Error! Please insert a valid binary number\n")
            continue
        break
    # this while loop takes input from the user and shows him the result of the operation he wants
    # if he inserted a wrong choice it shows him menu2 again to choose the right choice
    # then returns him to menu1 to see whether he wants to do another operation or exit
    while True:
        menu2()
        choice_menu2 = input("\nPlease select an option: ").upper()

        if choice_menu2 == 'A':  # first complement choice
            answer = first_complement(main_number)
            print("\nThe result = {}".format(answer))

        elif choice_menu2 == 'B':  # second complement choice
            answer = second_complement(main_number)
            print("\nThe result = {}".format(answer))

    # if user chose addition or subtraction the program asks him to insert the second number
        elif choice_menu2 == 'C':  # Addition choice
            # this loop checks whether the user inserted a number or not
            # and whether it is a valid binary number or number
            # if not any of the previous it returns him to insert the second number again
            while True:
                second_number = input("Please insert the second number: ")
                if second_number == '':
                    print("Error! Please insert a number\n")
                    continue
                if not is_valid(second_number):
                    print("Error! Please insert a valid binary number\n")
                    continue
                break
            answer = addition(main_number, second_number)
            print("\nThe result = {}".format(answer))

        elif choice_menu2 == 'D':  # subtraction choice
            # this loop checks whether the user inserted a number or not
            # and whether it is a valid binary number or number
            # if not any of the previous it returns him to insert the second number again
            while True:
                second_number = input("Please insert the second number: ")
                if second_number == '':
                    print("Error! please insert a number\n")
                    continue
                if not is_valid(second_number):
                    print("Error! Please insert a valid binary number\n")
                    continue
                break
            answer = subtraction(main_number, second_number)
            print("\nThe result = {}".format(answer))

        else:
            print("Error! Please insert a valid choice\n")
            continue
        break
