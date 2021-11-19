"""..."""


class Album:
    def __init__(self, title='', artist='', year=0, is_completed=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed

    def mark_completed(self):
        print('Album:', self.title, ' is completed or not?:', self.is_completed)

    def mark_required(self):
        return self.title != '' and self.artist != '' and self.year != 0

    def __str__(self):
        return 'Album:' + 'title=' + self.title + ",artist=" + self.artist + ",year=" + str(
            self.year) + ',is_completed=' + str(
            self.is_completed)
