# Kirolos Adel 20230295
# Malak Amr 20230416
# Ahmed Tamer 20230012

# Function converts Decimal to Binary
# tested on
# 7 >>> 111
# 246 >>> 11110110
def dec_to_bin(number):
    bases = "01"
    result = ""
    while number > 0:
        result = bases[number % 2] + result
        number //= 2
    return result


# Function converts Decimal to octal
# Tested on
# 155 >>> 233
# 6579 >>> 14663
def dec_to_octal(number):
    bases = "01234567"
    result = ""
    while number > 0:
        result = bases[number % 8] + result
        number //= 8
    return result


# Function converts Decimal to Hexadecimal
# Tested on
# 180 >>> B4
# 54607 >>> D54F
def dec_to_hex(number):
    bases = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = bases[number % 16] + result
        number //= 16
    return result


# Function converts Binary to Decimal
# Tested on
# 1001010 >>> 74
# 01100111 >>> 103
def bin_to_dec(number):
    n = int(number)
    i = 0
    result = 0
    while n > 0:
        last_digit = n % 10
        result += last_digit * (2 ** i)
        n //= 10
        i += 1
    return result


# Function converts octal to Decimal
# Tested on
# 674 >>> 444
# 267 >>> 183
def oct_to_dec(number):
    n = int(number)
    i = 0
    result = 0
    while n > 0:
        last_digit = n % 10
        result += last_digit * (8 ** i)
        n //= 10
        i += 1
    return result


# Function converts Hexadecimal to Decimal
# Tested on
# 2A >>> 42
# 4E9B >>> 20123
def hex_to_dec(hex_num):
    hexa = "0123456789ABCDEF"
    result = 0
    for digit in hex_num:
        result = result * 16 + hexa.index(digit)
    return result


# Function checks whether the user inserted a number or not
# and whether the number is valid for the four bases or not (e.g. (gfh) is not a valid number)
def is_a_number(user_number):
    bases = "0123456789ABCDEF"
    if not user_number:
        return False
    for char in user_number:
        if char not in bases:
            return False
    return True


# Function check the number of user is valid or not
# and check whether the user chose the right base to convert from
def is_valid(user_num, base):
    bases = "0123456789ABCDEF"
    bases = bases[:base]
    for character in user_num:
        if character not in bases:
            return False
    return True


Menu = """
A) Decimal
B) Binary
C) Octal
D) Hexadecimal
=> """


# Functions assigns the value of the base the user chose
# and checks whether the user chose a valid base (choice) or not
def main_bases(msg):
    while True:
        base = input(msg + Menu).upper()
        if base == "A":
            base = 10
        elif base == "B":
            base = 2
        elif base == "C":
            base = 8
        elif base == "D":
            base = 16
        else:
            print("Error! Please select a valid choice")
            continue
        break
    return base


Menu_1 = """
** Numbering System Converter **
A) Insert a new number
B) Exit program
=> """

# Main menu of the problem

# this first while true value takes the input from the user to navigate him to the second menu
# or exit the program
# and checks if the input is a valid choice or not
# if not it returns him to menu1 to choose a right choice
while True:
    menu1_ch = input(Menu_1).upper()
    if menu1_ch == "B":
        break
    if menu1_ch != "A":
        print("Error! Please select a valid choice")
        continue

    # This second while loop checks whether the user inserted a number or not
    # if not it returns him to insert a valid number
    while True:
        main_number = input("\nPlease insert a number: ").upper()
        if not is_a_number(main_number):
            print("Error! Please insert a valid number")
            continue
        break

    # The third while loop takes the base the user want to convert from
    # and checks if it is a valid base for the number he inserted
    # and checks if the user chose a valid base (choice)
    # if not any of the previous it returns him to choose a right/valid choice
    while True:
        first_base = main_bases("\n** Please select the base you want to convert the number from **")
        if not is_valid(str(main_number), first_base):
            print("Error in base number:", first_base, "Please insert the right base for the number you inserted")
            continue
        break
    second_base = main_bases("\n** Please select the base you want to convert the number to **")

    # Convert all values to decimal number
    if first_base == 10:
        main_number = int(main_number)
    elif first_base == 2:
        main_number = bin_to_dec(main_number)
    elif first_base == 8:
        main_number = oct_to_dec(main_number)
    elif first_base == 16:
        main_number = hex_to_dec(main_number)

    # Convert from Decimal to any system
    if second_base == 2:
        main_number = dec_to_bin(main_number)
    elif second_base == 8:
        main_number = dec_to_octal(main_number)
    elif second_base == 16:
        main_number = dec_to_hex(main_number)

    # the end of the program
    print("The Result Is:", main_number)

# converting from octal to binary tested on:
# 567 >>> 101110111
# 471 >>> 100111001

# converting from octal to hexadecimal tested on:
# 673 >>> 1BB
# 5076 >>> A3E

# converting from binary to octal tested on:
# 11001010 >>> 312
# 111011110 >>> 736

# converting from binary to hexadecimal tested on:
# 1001001110 >>> 24E
# 110111111001 >>> DF9

# Converting from hexadecimal to binary tested on:
# AEB >>> 101011101011
# DFC >>> 110111111100

# converting from hexadecimal to octal tested on:
# C77 >>> 6167
# 2B0 >>> 1260
