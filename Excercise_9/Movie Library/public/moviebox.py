#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from functools import reduce
from movie import Movie

class MovieBox(Movie):

    def __init__(self, title, movies):
        super().__init__
        if not title:
            raise Warning("Invalid Title")
        if not movies:
            raise Warning("Invalid movies")
        self._movies = movies
        self._title = title


    def get_actors(self):
        actors = []
        for movie in self._movies:
            actors.append(movie.get_actors())
        #Flatten list of lists into a single list
        actors = reduce(list.__add__, actors) #list.__add__ is like [1] + [2] = [1,2]
        actors = list(set(actors))
        return sorted(actors)

    def get_duration(self):
        duration = 0
        for movie in self._movies:
            duration += movie.get_duration()
        return duration

    def get_movies(self):
        copy = []
        for el in self._movies:
            copy.append(el)
        return list(set(copy))

    def __repr__(self) -> str:
        repr = f'MovieBox(\"{self._title}\", {self.get_movies()})'
        repr = repr.replace("\'", "\"")
        return repr

print(repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)])))