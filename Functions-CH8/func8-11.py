#8-11. Unchanged Magicians: Start with your work from Exercise 8-10. 
# Call the function make_great() with a copy of the list of magicians’ names. 
# Because the original list will be unchanged, return the new list and store it in a separate list. 
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

magname=['forrest','shazam','david']
modname=[]

def make_great(name,newname):
    for mag in range(len(name)):
        name[mag] = "The great " + name[mag] 
        newname.append(name[mag]) 

def show_magicians(name,newname):
    for nam in name:
        print nam.title()
    for newnam in newname:
        print newnam.title()



make_great(magname[:],modname)

show_magicians(magname,modname)
    