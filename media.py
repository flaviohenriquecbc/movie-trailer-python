import webbrowser

"""
This class represents an object named Movie. This object will be
used to store a movie with its attributes.
"""
class Movie():

    """
        The attributes to create an instance of movie are:
            title:
                The name of the movie
            poster_image_url:
                a full address of an image that represents the movie
                (e.g.: http://br.web.img3.acsta.net/medias/nmedia/18/93/64/37/20269376.jpg )
            trailer_youtube_url:
                a link from youtube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    """
        This function calls a method from fresh_tomatoes.py and shows
        the trailer of the selected movie
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
