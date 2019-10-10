from django.test import TestCase,Client
from movies.models import Movies,ScrappingLoader
from datetime import datetime,date
# Create your tests here.

class MovieTestCase(TestCase):
    def setUp(self):
        Movies.objects.create(name='Joker',img='#',rate=80,years="2019-10-09",description="C'est le joker qui est un méchant fou")
        Movies.objects.create(name="FightClub",img='#',rate=97,years="1999-03-18",description="Brandon se tappe sur la gueule")
    
    # Vérification de chaque donnée et du str
    def test_affichageMovies(self):
        #INIT MOVIES
        joker = Movies.objects.get(name="Joker")
        fightclub = Movies.objects.get(name="FightClub")
        #TEST WITH JOKER
        self.assertEqual(str(joker),"Joker 2019-10-09")
        self.assertEqual(joker.name,"Joker")
        self.assertEqual(joker.years,date(2019,10,9))
        self.assertEqual(joker.rate,80)
        self.assertEqual(joker.description,"C'est le joker qui est un méchant fou")
        self.assertEqual(joker.img,"#")
        #TEST WITH FIGHTCLUB
        self.assertEqual(str(fightclub),"FightClub 1999-03-18")
        self.assertEqual(fightclub.name,"FightClub")
        self.assertEqual(fightclub.years,date(1999,3,18))
        self.assertEqual(fightclub.rate,97)
        self.assertEqual(fightclub.description,"Brandon se tappe sur la gueule")
        self.assertEqual(fightclub.img,"#")
    
    def test_remove_Movies(self):
        joker = Movies.objects.get(name="Joker")
        fightclub = Movies.objects.get(name="FightClub")
        self.assertEqual(joker.delete(),(1,{'movies.Movie_has_Actor': 0, 'movies.Movies': 1}))
    
class RouteTestCase(TestCase):

    def test_url_index_STATUS200(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code,200)

    def test_url_formAddMovies_STATUS200(self):
        c = Client()
        response = c.get("/add/")
        self.assertEqual(response.status_code,200)

class ScrapingTestCase(TestCase):
    pass
