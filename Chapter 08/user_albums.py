def make_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        info = {'Artist\'s name': artist_name, 
                'Album\'s title': album_title,
                'Number of songs': number_of_songs}
    else:
        info = {'Artist\'s name': artist_name, 
                'Album\'s title': album_title}
    return info

while True:
    artist = input("Enter an artist: ")
    if artist == 'q':
        break
    album = input("Enter an album: ")
    if album == 'q':
        break
    songs = input("Enter a number of songs: ")
    if songs == 'q':
        break
    if songs:
        songs = int(songs)
    print(make_album(artist, album, songs))