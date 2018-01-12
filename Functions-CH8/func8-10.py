#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. 
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. 
# Call show_magicians() to see that the list has actually been modified.

magname=['forrest','shazam','david']
modname=['amy','sabrina']

def show_magician(name):
    for mag in range(len(name)):
        name[mag] = "The great " + name[mag] 
    print name


show_magician(modname)
    