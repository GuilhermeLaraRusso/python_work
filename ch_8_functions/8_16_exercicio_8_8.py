# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def make_album(artist, album, tracks):
    """Return a dictionary with the artist, album"""
    full_album = {'artis':artist, 'album':album, 'tracks':tracks}
    return full_album

while True:
    print('\nInput the Artist and the Album')
    print('Enter "q" to quit')
    art = input('Name of the artist:')
    if art == 'q':
        break

    alb = input('Name of the album:')
    if alb == 'q':
        break
        
    trk = input('Number of tracks:')
    if trk == 'q':
        break

    album_completo = make_album(art, alb, trk)
    print(album_completo)




