#8-13. User Profile: Start with a copy of user_profile.py from page 153. 
# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.



def user_profile(first,last,**user_pro):
    user = {}
    user['first_name'] = first
    user['last_name'] = last

    for key,value in user_pro.items():
        user[key]= value
    return user

profile = user_profile("Ivan","Kapalala",passioni ='musica',city='Torino')
print(profile)
