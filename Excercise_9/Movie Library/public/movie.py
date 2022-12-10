#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        if not title:
            raise Warning("Invalid title")
        elif not actors:
            raise Warning("Invalid actors")
        self._title = title
        self._actors = actors
        self._duration = duration

    def get_title(self):
        return self._title

    def get_actors(self):
        copy = []
        for el in self._actors:
            copy.append(el)
        return sorted(copy)

    def get_duration(self):
        return self._duration

    def __repr__(self) -> str:
        repr = f'Movie(\"{self._title}\", {self._actors}, {self._duration})'
        repr = repr.replace("\'", "\"")
        return repr

    def __hash__(self) -> int:
        return hash((self._title, tuple(self._actors), self._duration))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Movie):
            return self._title == other.get_title() and self._duration == other.get_duration() and self._actors == other.get_actors()

    # also implement the required special functions
