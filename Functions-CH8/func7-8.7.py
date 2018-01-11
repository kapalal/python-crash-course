#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album. 
# If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of tracks on an album.


def make_album(artist,album,number=''):
    entry={'name':artist.title(),'album_title':album.title()}
    if number:
        entry={'name':artist.title(),'album_title':album.title(),'Track_Number':number}
    return entry



musician1= make_album('jay-z','the blueprint')
musician2= make_album('kanye west','last registration')
musician3= make_album('prince','purple rain')
musician4= make_album('micheal jackson','thriller','3')
print(musician1)
print(musician2)
print(musician3)   
print(musician4)