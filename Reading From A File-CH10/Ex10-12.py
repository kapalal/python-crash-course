#10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. 
# If the number is already stored, report the favorite number to the user. 
# If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.


import json

def get_stored_num():
    """Get stored number"""
    filename = 'usernum.json'
    try:
        with open(filename) as f_obj:
            favnum= json.load(f_obj) 
    except FileNotFoundError:
        return None
    else:
        return favnum
        
def tell_favnum():
    """Tell favorite number"""
    favnum = get_stored_num()
    if favnum:
        print("Your favourite number is: " + favnum)
    else:
        filename = 'usernum.json'
        usernum = input("Whats your fav number?: ")
        with open(filename,'w') as obj:
            json.dump(usernum,obj)
            print("Your fav num has been saved!")

tell_favnum()   