#8-8. User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.


def make_album(artist,album,number=''):
    entry={'name':artist.title(),'album_title':album.title()}
    if number:
        entry={'name':artist.title(),'album_title':album.title(),'Track_Number':number}
    return entry


while True:
    print('Please enter the required info or enter "q" to quit the session')
    user_artist=input('Whats your favourite artist? ')
    user_album=input('Whats his best album in you opinion? ')
    if user_artist == 'q':
        break
    elif user_album == 'q':
        break
    musician=make_album(user_artist,user_album)
    print(musician)
    