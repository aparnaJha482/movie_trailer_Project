import webbrowser


class Movie:
    def __init__(self, movie_title, movie_storyline):
        self.title = movie_title
        self.storyline = movie_storyline

class Media(Movie):
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

toy_story =Movie("Toy story","story of a boy and his toys that comes to life",
                                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                    "https://www.youtube.com/watch?v=vwyZH85NQC4")





