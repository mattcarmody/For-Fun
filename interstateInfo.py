#! python3
# interstateInfo.py - Offers information based on the Interstate naming system.

import sys


inter = input('Enter an Interstate Highway number!')

# Filter out other characters.
cut = " -_.,()[]{}iI"
for i in cut:
    inter = inter.replace(i,"")

# Warn about unexpected characters, not abhiprsu, and stop the program.
warn = "cdefgjklmnoqtvwxyzCDEFGJKLMNOQTVWXYZ"
warningMessage = ""
for i in warn:
    if i in inter:
        warningMessage = "\nYou've got unexpected letters in your input. Try again. Keep in mind, this program is for interstate numbers not state highways."
if warningMessage:
    print(warningMessage)
    sys.exit()

# Prefix of H-1 for Hawaii
if "H" in inter:
    print('Are you in Hawaii? Must be nice! Bring me a coconut or two.')
    print('The general rules don\'t really apply in your case, sorry!')
# Prefix of A and PR for Alaska and Puerto Rico, but they don't follow the rules.
elif "A" in inter or "a" in inter:
    print('The Last Frontier is a ways away.')
    print('The general rules don\'t really apply in your case, sorry!')
elif "PR" in inter or "pr" in inter or "Pr" in inter or "pR" in inter:
    print('?Tu estas en Puerto Rico?')
    print('The general rules don\'t really apply in your case, sorry!')
# Prefix of BUS for Business, but they don't follow the rules either.
elif "BUS" in inter or "bus" in inter or "Bus" in inter:
    print('I don\'t think a business route counts.')
    print('The general rules don\'t really apply in your case...')
else:
    print('You entered I-' + inter + '.\n')

    # Inter length of 0.
    if len(inter) == 0:
        print('I\'m missing the number, please try again.')

    # If one or two digits - Primary.
    elif len(inter) < 3:
        print('This is known as a primary interstate, because it is only one or two digits long.')
        
        # Odd - N/S
        if int(inter) % 2 == 1:
            print('It runs North to South, because it ends in an odd digit.')
        # Even - E/W
        elif int(inter) % 2 == 0:
            print('It runs East to West, because it ends in an even digit.')
        else:
            print('Error. Number not even or odd.')

        # Ending in 5 or 0 - main line
        if int(inter) % 5 == 0:
            print('It is considered a main line, because it ends in a 0 or 5. It may run all the way across the country!')

    # If three digits - Auxiliary. They're guidelines with exceptions.
    elif len(inter) == 3:
        print('This is an auxiliary route, because it is three digits long. It branches off the primary route that shares the final two digits, in this case I-' + inter[1:3] + '.')

        # Third digit odd - Spur.
        if int(inter[0]) % 2 == 1:
            print('This is also known as a spur route, only connecting to its primary route, I-' + inter[1:3] + ', in one location, evidenced by the odd first digit, ' + inter[0] + '.')

        # Third digit even - Circumferential/Radial of Primary. (They meet twice.)
        elif int(inter[0]) % 2 == 0:
            print('This is also known as a circumferential or radial route, connecting to the primary route, I-' + inter[1:3] + ', in two locations, evidenced by the even first digit, ' + inter[0] + '.')

        # East/West North/South of final digit doesn't necessarily apply.

    # Disclaimer, exceptions.
    print('\nThe Interstate Highway System names are structured and contain a lot of information about the road you\'re on! Unfortunately exceptions exist, casting doubt on the \'rules\'. These guidelines aren\'t 100% accurate, but they\'re widespread.')
    if len(inter) < 3 and len(inter) > 0:
        print('\nBonus tip! On primary routes, exit numbers usually increment with each mile, with 0 at either the West or South border of a state, depending on which way the Interstate runs.')
    
