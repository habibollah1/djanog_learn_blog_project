from django.test import TestCase
from django.shortcuts import reverse
from .models import KalaList
from django.contrib.auth.models import User


class TestKala(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.kala1 = KalaList.objects.create(
            title='title1',
            text='text1',
            status=KalaList.STATUS_CODE[0][0],
            author=cls.user,
        )
        cls.kala2 = KalaList.objects.create(
            title='title2',
            text='text2',
            status=KalaList.STATUS_CODE[1][0],
            author=cls.user,
        )

    def test_view_kala_list(self):
        response = self.client.get('/kala/')
        self.assertEqual(response.status_code, 200)

    def test_view_kala_list_by_name(self):
        response = self.client.get(reverse('kala_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_id_list(self):
        response = self.client.get(f'/kala/{self.kala1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_id_list_by_name(self):
        response = self.client.get(reverse('types_of_kala', args={self.kala1.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_kala_page(self):
        response = self.client.get(reverse('kala_list', ))
        self.assertContains(response, self.kala1.title)
        self.assertContains(response, self.kala1.text)

    def test_view_id_page(self):
        response = self.client.get(reverse('types_of_kala', args={self.kala1.id}))
        self.assertContains(response, self.kala1.title)

    def test_draft_kala_show_just_published(self):
        response = self.client.get(reverse('kala_list'))
        self.assertContains(response, self.kala1.title)
        self.assertNotContains(response, self.kala2.title)


