def make_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        return {'Artist\'s name': artist_name, 
                'Album\'s title': album_title,
                'Number of songs': number_of_songs}
    else:
        return {'Artist\'s name': artist_name, 
                'Album\'s title': album_title}

print(make_album('Boobiebaabaa', 'Doodiedoodoo'))
print(make_album('abc', 'def', 13))
print(make_album('ghi', 'jkl'))
print(make_album('mno', 'pqr'))