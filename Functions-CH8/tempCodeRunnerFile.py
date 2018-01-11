def make_album(artist,album,number=''):
    entry={'name':artist.title(),'album_title':album.title()}
    if number:
        entry={'name':artist.title(),'album_title':album.title(),'Track_Number':number}
    return entry


while True:
    print('Please enter the required info or enter "q" to quit the session')
    user_artist=input('Whats your favourite album? ')
    user_album=input('Whats his best album in you opinion? ')
    if user_album == 'q' or user_artist == 'q':
        break
    musician=make_album(user_artist,user_album)
    print(musician)
    