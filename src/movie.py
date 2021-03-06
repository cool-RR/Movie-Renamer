import imdb

class Movie(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def __str__(self):
        return '%s (%s)' % (self.name, self.year)
    
    @staticmethod
    def create_movie_from_query(query):
        db = imdb.IMDb()
        movie_obj = db.search_movie(query, results=1)[0]
        created_movie = Movie(name=movie_obj['title'], year=movie_obj['year'])
        return created_movie