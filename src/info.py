##
# @internal
# @file info.py
# @authors Yossi Bokor Bleile
# @version 0.1
# @date April 2023
# @copyright BSD
#


def license():
    """! obtain license information and print it
    """
    with open("LICENSE", 'r') as license:
    	print(license.read())
     
def intro():
    """! print brief introduction about the program
    """
    print("Topological Amorphous Material Analysis Copyright (C) Yossi Bokor Bleile, Aalborg University\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it under certain conditions.\nTo see the liencese conditions, run `AMA.py -l'.\nFor help run `AMA.py -h`.")