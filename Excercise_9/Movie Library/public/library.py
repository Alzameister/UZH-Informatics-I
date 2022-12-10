#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox

class Library:
    def __init__(self) -> None:
        self._movies = []

    def add_movie(self, movie):
        self._movies.append(movie)
        self._movies = list(set(self._movies))

    def get_movies(self):
        return self._movies

    def get_total_duration(self):
        duration = 0
        for movie in self._movies:
            duration += movie.get_duration()
        return duration
