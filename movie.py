# importing webbrowser module to open url from internet
import webbrowser
# importing fresh_tomatoes_module that stores movie trailer file
import fresh_tomatoes


# creating parent class Movie
class Movie:
    """This class consits of variables and way to its subclasses """
    def __init__(self, movie_title, movie_storyline):
        print "Movie constructor called"
        # initialising variables
        self.title = movie_title
        self.storyline = movie_storyline


# creating subclass Media
class Media(Movie):
    """This is a subclass and contains movie information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        print "Media constructor called"
        # inheriting functions from class movie
        Movie.__init__(self, movie_title, movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # defining function show_trailer and using function open to access url
    def show_trailer(self):
        """this class redirects to url provided"""
        webbrowser.open(self.trailer_youtube_url)


# creating movie objects
toy_story = Media("Toy story", "story of a boy and his toys that comes to life",
                  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = Media("avatar", " a marine on an alien planet",
               "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=d1_JBMrrYw8")
krish = Media("krish", "story of a boy with supernatural powers",
              "https://upload.wikimedia.org/wikipedia/en/9/95/Krrish_poster.jpg",
              "https://www.youtube.com/watch?v=y0wzwujpkFg")
wolf_of_wall_street = Media("wolf of wall street", "story of a man rising hig and making money ",
                            "https://upload.wikimedia.org/wikipedia/en/d/d8/"
                            "The_Wolf_of_Wall_Street_%282013%29.png",
                            "https://www.youtube.com/watch?v=iszwuX1AK6A")
life_of_pie = Media("life of pie", "story of relation between man and animal",
                    "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                    "https://www.youtube.com/watch?v=j9Hjrs6WQ8M")
harry_potter = Media("harry potter", "story of a supernatural kid and his powers",
                     "https://upload.wikimedia.org/wikipedia/en/a/a9/Harry_Potter_and_the_Deathly_Hallows.jpg",
                     "https://www.youtube.com/watch?v=9hXH0Ackz6w")

# creating array list of movies
movies = [toy_story, avatar, krish, wolf_of_wall_street, life_of_pie, harry_potter]
# calling functionality of fresh_tomatoes to open file
fresh_tomatoes.open_movies_page(movies)
