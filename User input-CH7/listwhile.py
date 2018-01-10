unconfirmed_users= ['alice','bob','sylva']
confirmed_user= []



while unconfirmed_users:
    current_user= unconfirmed_users.pop()
   
    print("Verifying user: " + current_user.title())
    confirmed_user.append(current_user)
    
print("The following users has been added: ")
for user in confirmed_user:
    print (user.title())