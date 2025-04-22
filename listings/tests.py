from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class HomePageTests(TestCase):
    def test_home_page(self):
        ''''
        tests if home page can be accessed
        '''
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listings/index.html")