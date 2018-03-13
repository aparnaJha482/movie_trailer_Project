import webbrowser


class Movie:
    def __init__(self, movie_title, movie_storyline):
        print "Movie constructor called"
        self.title = movie_title
        self.storyline = movie_storyline

class Media(Movie):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        print "Media constructor called"
        Movie.__init__(self, movie_title, movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

toy_story =Media("Toy story","story of a boy and his toys that comes to life",
                                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                    "https://www.youtube.com/watch?v=vwyZH85NQC4")






