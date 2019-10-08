from django.test import TestCase
from movies.models import Movies
# Create your tests here.

class MovieTestCase(TestCase):
    def setUp(self):
        Movies.object.create(name='Joker',img='#',rate=80)
        Movies.object.create(name="FightClub",img='#',rate=97)