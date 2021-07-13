from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import snacks
# Create your tests here.

class test_snacks_crud(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Sewar',
            email = 's.maqableh@yahoo.com',
            password = 'Sewar1997'
        )
        self.snack = snacks.objects.create(
            title = 'shawrma',
            purchaser = self.user,
            description  = 'Shawarma is prepared from thin cuts of seasoned marinated lamb, mutton, veal, beef, chicken, or turkey. The slices are stacked on a skewer about 60 cm (20 in) high. Lamb fat may be added to provide extra fat for juiciness and flavor. A motorized spit slowly turns the stack of meat in front of a heating element, continuously roasting the outer layer. Shavings are cut off the rotating stack for serving, customarily with a long, sharp knife.[1]',
        )


    def test_snack_list(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        expected=200
        self.assertEqual(actual_status_code, expected)

    def test_snack_view(self):
        expected = self.client.get(reverse('snack_view', args='1')).status_code
        actuall=200
        self.assertEqual(expected, actuall)

    def test_snack_update(self):
        expected = self.client.post(reverse('snack_update', args='1'), 
        {
            'title':'Potato chips' ,
            "description":"Delicious and crunchy",
        })
        self.assertContains(expected, 'Potato chips')
        self.assertContains(expected, 'Delicious and crunchy')
        
   
    def test_snack_create(self):
        expected = self.client.post(reverse("snack_creat"),
            {
                "title": "Orange juice",
                "purchaser": self.user,
                "description": "Healthy and rich in vitamins.",
            })

     
        self.assertEqual(expected.status_code, 200)
        self.assertContains(expected, 'Orange juice')
        self.assertContains(expected, 'Sewar'),
        self.assertContains(expected, 'Healthy and rich in vitamins.')


    def test_snack_delete(self):
        expected = self.client.get(reverse("snack_delete", args="1")).status_code
        actuall=200
        self.assertEqual(expected, actuall)