from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import requests
from adventure.views import home_page

class HomePageTest(TestCase):
#gitbash is broken today sorry. These work I've tested them before.
#I've read the book. 



    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('Merlin\'s Adventure', html)
        self.assertIn('WELCOME TO MERLIN\'S ADVENTURE', html)
        self.assertIn('What is your name weary traveler?', html)
        self.assertTrue(html.strip().endswith('</html>'))
        

        self.assertTemplateUsed(response, 'home.html')

    #def test_bad_maths(self):
        #self.assertEqual(1 + 1, 3)
    

    
