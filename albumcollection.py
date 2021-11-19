"""..."""

from album import Album
from functools import cmp_to_key


class AlbumCollection:
    def __init__(self):
        self.albums = []

    def load_albums(self, album_path):
        with open(album_path) as f:
            lines = f.read().strip().split('\n')[1:]
        albums = [line.split(',') for line in lines]
        for i in range(len(albums)):
            album = albums[i]
            is_completed = album[0]
            title = album[1]
            artist = album[2]
            year = int(album[3])
            self.albums.append(Album(title, artist, year, is_completed))

    def sort_key(self, x, y):
        x_value = getattr(x, self.key)
        y_value = getattr(y, self.key)
        if x_value != y_value:
            return -1 if x_value < y_value else 1
        else:
            return x.year - y.year

    def sort(self, key=None):
        if key is None:
            self.albums.sort(key=lambda x: x.year)
        else:
            if len(self.albums) == 1:
                return
            keys = self.albums[0].__dict__.keys()
            if key not in keys:
                print(key, "is not a valid key")
                return
            self.key = key
            self.albums.sort(key=cmp_to_key(self.sort_key))

    def __str__(self):
        result = ""
        for i in range(len(self.albums)):
            result += str(self.albums[i]) + "\n"
        return result

    def add_album(self, album):
        self.albums.append(album)

    def save_albums(self):
        with open('albums_result.csv', 'w', encoding='utf8') as f:
            for i in range(len(self.albums)):
                album = self.albums[i]
                row = ['*' if album.is_completed else '', album.title, album.artist, str(album.year)]
                row.append('\n')
                row = ','.join(row)
                f.write(row)
