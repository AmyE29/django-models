from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Flavor

class FlavorModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.flavor = Flavor.objects.create(
            name='Chocolate Yum',
            description='Really Yummy',
            author=self.user,
        )

    def test_string_representation(self):
        flavor = Flavor(name='A flavor of Ice Cream')
        self.assertEqual(str(flavor), flavor.name)

    def test_flavor_content(self):
        self.assertEqual(f'{self.flavor.name}', 'Chocolate Yum')
        self.assertEqual(f'{self.flavor.description}', 'Really Yummy')
        self.assertEqual(f'{self.flavor.author}', 'testuser')

    def test_flavor_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Really Yummy')
        self.assertTemplateUsed(response, 'home.html')

    def test_flavor_detail_view(self):
        response = self.client.get('/icecream/1/')
        no_response = self.client.get('/icecream/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Chocolate Yum')
        self.assertTemplateUsed(response, 'flavors_details.html')
