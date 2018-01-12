#! /usr/bin/python3
# interstateInfo.py - Offers information based on the Interstate naming system.

import sys

inter = input("Enter an Interstate Highway number!")
inter = inter.lower()

# Filter out unneeded characters. "I-65" becomes "65"
cut = " -_.,()[]{}i"
for i in cut:
    inter = inter.replace(i,"")

# Warn about unexpected characters, not abhiprsu, and stop the program.
# A - Alaska, BUS - Business, H - Hawai'i, I - Interstate, PR - Puerto Rico
warn = "cdefgjklmnoqtvwxyz"
warningMessage = ""
for i in warn:
    if i in inter:
        warningMessage = "\nYou've got unexpected letters in your input. "
        "Try again. Keep in mind, this program is for interstate numbers not "
        "state  highways."
if warningMessage:
    print(warningMessage)
    sys.exit()

# Rules don't apply to Hawai'i, Alaska, Puerto Rico or Business
if "h" in inter:
    print("Are you in Hawaii? Must be nice! Bring me a coconut or two.\n"
    "The general rules don't really apply in your case, sorry!")
elif "a" in inter:
    print("The Last Frontier is a ways away.\n"
    "The general rules don't really apply in your case, sorry!")
elif "pr" in inter:
    print("?Tu estas en Puerto Rico?\n"
    "The general rules don't really apply in your case, sorry!")
elif "bus" in inter:
    print("I don't think a business route counts.\n"
    "The general rules don't really apply in your case...")
else:
    print("You entered I-{0}.\n".format(inter))

    # No number.
    if len(inter) == 0:
        print("I'm missing the number, please try again.")

    # If one or two digits - Primary Interstate.
    elif len(inter) < 3:
        print("This is known as a primary interstate, "
        "because it is only one or two digits long.")
        
        # Odd - N/S
        if int(inter) % 2 == 1:
            print("It runs North to South, because it ends in an odd digit.")
        # Even - E/W
        elif int(inter) % 2 == 0:
            print("It runs East to West, because it ends in an even digit.")
        else:
            print("Error. Number not even or odd.")

        # Ending in 5 or 0 -  Main Line
        if int(inter) % 5 == 0:
            print("It is considered a main line, because it ends in a 0 or 5. "
            "It may run all the way across the country!")

    # If three digits - Auxiliary.
    elif len(inter) == 3:
        print("This is an auxiliary route, because it is three digits long. "
        "It branches off the primary route that shares the final two digits, "
        "in this case I-{0}.\n".format(inter[1:3]))

        # Third digit odd - Spur.
        if int(inter[0]) % 2 == 1:
            print("This is also known as a spur route, only connecting to "
            "its primary route, I-{0}, in one location, evidenced by the odd "
            "first digit, {1}.".format(inter[1:3], inter[0]))
        # Third digit even - Circumferential/Radial of Primary.
        elif int(inter[0]) % 2 == 0:
            print("This is also known as a circumferential or radial route, "
            "connecting to the primary route, I-{0}, in two locations, "
            "evidenced by the even first digit, {1}.".format(inter[1:3], 
            inter[0]))

    # Disclaimer, exceptions.
    print("\nThe Interstate Highway System names are structured and contain "
    "a lot of information about the road you're on! Unfortunately "
    "exceptions exist, casting doubt on the 'rules'. "
    "These guidelines aren't 100% accurate, but they're widespread.")
    # Primary bonus - increment miles from S/W state boundary
    if len(inter) < 3 and len(inter) > 0:
        print("\nBonus tip! On primary routes, exit numbers usually increment "
        "with each mile, with 0 at either the West or South border of a state, "
        "depending on which way the Interstate runs.")
