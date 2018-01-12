#! /usr/bin/python3
# isbnCheck.py - A simple check to see if an ISBN number is potentially valid
# If one digit is missing, it provides the final digit
# ISBN 10 and ISBN 13 compatible

# Input ISBN, trim unnecessary characters, print ISBN
def launch():
    isbn = input("Welcome! Enter an ISBN.\nOr leave off the last digit"
                " and I'll guess it.\n")
    cut = " []{}(),.-_"
    for i in cut:
        isbn = isbn.replace(i,"")
    print("You entered {0}".format(isbn))
    return isbn

# Evaluates validity of a potential ISBN 10, uses two redundant methods
def check_isbn_10(isbn10):
    # Method 1 - count starts at 10
    total1 = 0
    count = 10
    for i in range(len(isbn10)):
        if isbn10[i] == "X":
            total1 += count*10
        else:
            total1 += count*int(isbn10[i])
        count -= 1
    
    # Method 2 - count starts at 1
    total2 = 0
    for i in range(1, len(isbn10)+1):
        if isbn10[i-1] == "X":
            total2 += i*10
        else:
            total2 += i*int(isbn10[i-1])
    
    # Evaluate results of method 1 & 2
    results10 = ""
    if (total1 % 11) == 0 and (total2 % 11) == 0:
        results10 = "10Y"
    elif (total1 % 11) == 0 or (total2 % 11) == 0:
        results10 = "10N"
    else:
        results10 = "10E"
    return results10

# Evaluates validity of a potential ISBN 13
def check_isbn_13(isbn13):
    evenTotal13 = 0
    oddTotal13 = 0
    # Sum even digits multiplied by 3
    evenList13 = isbn13[1::2]
    for i in range(len(evenList13)):
        evenTotal13 += int(evenList13[i])*3
    # Sum odd digits
    oddList13 = isbn13[::2]
    for i in range(len(oddList13)):
        oddTotal13 += int(oddList13[i])
    # Modulus 10 the complete total, 0 is valid
    results13 = ""
    if (evenTotal13 + oddTotal13) % 10 == 0:
        results13 = "13Y"
    else:
        results13 = "13N"
    return results13
    
# Calculates ISBN 10 check digit.
def complete_isbn_9(isbn9):
    total = 0
    for i in range(1, len(isbn9)+1):
        total += i*int(isbn9[i-1])
    for i in range(11):
        if (total + 10*i) % 11 == 0:
            check = i
            break
    if check == 10:
        check = "X"
    return str(isbn9) + str(check)

# Calculates ISBN 13 check digit.
def complete_isbn_12(isbn12):
    evenTotal12 = 0
    oddTotal12 = 0
    # Sum even digits multiplied by 3
    evenList12 = isbn12[1::2]
    for i in range(len(evenList12)):
        evenTotal12 += int(evenList12[i])*3
    # Sum odd digits
    oddList12 = isbn12[::2]
    for i in range(len(oddList12)):
        oddTotal12 += int(oddList12[i])
    # Find check value and print.
    check = 10 - (evenTotal12 + oddTotal12) % 10
    return str(isbn12) + str(check)
    
# Prints the results for all functions.
def printer(code):
    if code == "10Y": 
        print("This is a valid ISBN-10.")
    elif code == "10N":
        print("There's a problem with the ISBN-10 formulas, they don't match.")
    elif code == "10E":
        print("This ISBN-10 doesn't add up, it's no good. "
            "Double check your number.")
    elif code == "13Y":
        print("This is a valid ISBN-13.")
    elif code == "13N":
        print("That IBSN-13 doesn't seem quite right.")
    elif len(code) == 10:
        print("Check digit should be {0}, making the whole "
            "ISBN 10: {1}{2}".format(code[9], code[0:9], code[9]))
    elif len(code) == 13:
        print("Check digit should be {0}, making the whole "
            "ISBN 13: {1}{2}".format(code[12], code[0:12], code[12]))
    else:
        print("We've got an error somewhere!")

def main():
    ISBN = launch()
    if len(ISBN) == 9:
        result9 = complete_isbn_9(ISBN)
        if check_isbn_10(result9) == "10Y":
            printer(result9)
        else:
            print("Error in calculating or checking ISBN9/10 functions!")
    elif len(ISBN) == 10:
        printer(check_isbn_10(ISBN))
    elif len(ISBN) == 12:
        result12 = complete_isbn_12(ISBN)
        if check_isbn_13(result12) == "13Y":
            printer(result12)
        else:
            print("Error in calculating or checking ISBN12/13 functions!")
    elif len(ISBN) == 13:
        printer(check_isbn_13(ISBN))
    else:
        print("A dead giveaway is the number of digits. That number doesn't have "
            "10 or 13. It's not an ISBN.")

if __name__ == "__main__":
    main()
