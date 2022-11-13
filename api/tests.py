from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from account.models import User


#command to run the tests. be in the cloud2fpga folder
#docker compose exec api python manage.py test

class UserTest(TestCase):
    def setUp(self):
        self.userlogin = get_user_model().objects.create_user(
            username='testuser',
            email='testemail',
            password='testpassword'
        )

        self.customuser = User.objects.create(
            birth_date = '1111-11-11',
            avatar = 'test.png'
        )

    def test_customuser(self):
        self.assertEqual(f'{self.customuser.birth_date}','1111-11-11')
        self.assertEqual(f'{self.customuser.avatar}','test.png')

# Create your tests here.
