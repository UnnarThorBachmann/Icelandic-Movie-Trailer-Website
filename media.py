import webbrowser

""" This file was mostly written in class: Programmings Foundations for Python. However it was modified by Unnar Thor Bachmann to add further information for
    each movie.
"""
class Movie():
    """ Summary: A movie class which contains all the information displayed on the website.

    Attributes:
        title: A string which contains the name of the movie.
        storyline: The short storyline of the movie taken form IMDB.
        poster_image_url: An url to the image of the movie.
        trailer_youtube_url: An youtube url to the trailer of the movie.
        category: Category of the movie according to the IMDB categories.
        rating: User ratings taken from the IMDB website.
        director: The director of the movie.
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_category,movie_rating,movie_year,movie_director):
        """ The constructor of the class """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.category = movie_category
        self.rating = movie_rating
        self.year = movie_year
        self.director = movie_director
        
    def show_trailer(self):
        """ A function which runs the a youtubetrailer inside a broswer. """
        webbrowser.open(self.trailer_youtube_url)
        

