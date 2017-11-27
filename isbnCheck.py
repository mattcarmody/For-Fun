#! python3
# isbnCheck.py - A simple check to see if an ISBN number is potentially valid.


ISBN = input('Enter an ISBN number.')

# Remove unnecessary characters here.
cut = " []{}(),.-_"
for i in cut:
    ISBN = ISBN.replace(i,"")
print('You entered ' + ISBN)

# ISBN 10
if len(ISBN) == 10:
    # First Method - count starts at 10
    total1 = 0
    count = 10
    for i in range(len(ISBN)):
        if ISBN[i] == 'X':
            total1 += count*10
        else:
            total1 += count*int(ISBN[i])
        count -= 1
    # Second Method - count starts at 1
    total2 = 0
    for i in range(1, len(ISBN)+1):
        if ISBN[i-1] == 'X':
            total2 += i*10
        else:
            total2 += i*int(ISBN[i-1])
    # Does it work?
    if (total1 % 11) == 0 and (total2 % 11) == 0:
        print('This is a valid ISBN-10.')
    elif (total1 % 11) == 0 or (total2 % 11) == 0:
        print('There\'s a problem with the ISBN-10 formulas, they don\'t match.')
    else:
        print('This ISBN-10 doesn\'t add up, it\'s no good. Double check your number.')

# ISBN 13
elif len(ISBN) == 13:
    totalE = 0
    totalO = 0
    # Sum even digits multiplied by 3
    even = ISBN[1::2]
    for i in range(len(even)):
        totalE += int(even[i])*3
    # Sum odd digits
    odd = ISBN[::2]
    for i in range(len(odd)):
        totalO += int(odd[i])
    # Modulus 10 the complete total, 0 is valid
    if (totalE + totalO) % 10 == 0:
        print('This is a valid ISBN-13.')
    else:
        print('That IBSN-13 doesn\'t seem quite right.')
    
# Entered 9 digits - Give user the ISBN 10 check digit.
elif len(ISBN) == 9:
    total = 0
    for i in range(1, len(ISBN)+1):
        total += i*int(ISBN[i-1])
    # check = (11 - total % 11) * 10 
    for i in range(10):
        if (total + 10*i) % 11 == 0:
            check = i
            break
    print('Check digit should be ' + str(check) + ", making the whole ISBN 10: " + ISBN + str(check))

# Entered 12 digits - Give user the ISBN 13 check digit.
elif len(ISBN) == 12:
    totalE = 0
    totalO = 0
    # Sum even digits multiplied by 3
    even = ISBN[1::2]
    for i in range(len(even)):
        totalE += int(even[i])*3
    # Sum odd digits
    odd = ISBN[::2]
    for i in range(len(odd)):
        totalO += int(odd[i])
    # Find check value and print.
    check = 10 - (totalE + totalO) % 10
    print('Check digit should be ' + str(check) + ", making the whole ISBN 13: " + ISBN + str(check))
    
# Other
else:
    print('A dead giveaway is the number of digits. That number doesn\'t have 10 or 13. It\'s not an ISBN.')


