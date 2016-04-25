import fresh_tomatoes
import media
import json
""" This code was entirely written by Unnar Thor Bachmann """

# Open the file with json data.
f = open('data2.json', "r")
lines = f.readlines()
f.close()
texti = ''
for line in lines:
    texti += line;

# Text file loaded into a python object.
data = json.loads(texti)

# An array containing each instance of the movie class.
movies = []
l = len(data.keys())

# Converting the the data object into a list of Movie objects.
for i in range(1,l + 1):
    t = str(i)
    movies.append(media.Movie(data[t]['title'],
                              data[t]['plot'],
                              data[t]['image'],
                              data[t]['trailer'],
                              data[t]['classes'],
                              data[t]['rating'],
                              data[t]['release'],
                              data[t]['director']))

# A function call which moves the data to the webpabe.
fresh_tomatoes.open_movies_page(movies)
