
from django.test import TestCase
from .models import User, Coords, PerevalAdded, PerevalImages, PerevalAreas, SprActivitiesTypes
from django.utils import timezone
import io

class UserTests(TestCase):
    def setUp(self):
        User.objects.create(email="test@example.com", name="Test User", phone="1234567890")

    def test_user_creation(self):
        user = User.objects.get(email="test@example.com")
        self.assertEqual(user.name, "Test User")

class CoordsTests(TestCase):
    def setUp(self):
        Coords.objects.create(latitude=55.7558, longitude=37.6176, height=200)

    def test_coords_creation(self):
        coords = Coords.objects.get(latitude=55.7558)
        self.assertEqual(coords.height, 200)
class PerevalAddedTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@example.com", name="Test User", phone="1234567890")
        self.coords = Coords.objects.create(latitude=55.7558, longitude=37.6176, height=200)
        PerevalAdded.objects.create(user=self.user, coord=self.coords, beautyTitle="Test Title", title="Test", other_titles="Other Titles", connect="Connection", add_time=timezone.now(), status='new')

    def test_pereval_added_creation(self):
        pereval = PerevalAdded.objects.get(title="Test")
        self.assertEqual(pereval.beautyTitle, "Test Title")

class SprActivitiesTypesTests(TestCase):
    def setUp(self):
        SprActivitiesTypes.objects.create(title="Hiking")

    def test_spr_activities_types_creation(self):
        activity_type = SprActivitiesTypes.objects.get(title="Hiking")
        self.assertEqual(activity_type.title, "Hiking")
class PerevalImagesTests(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@example.com", name="Test User", phone="1234567890")
        coords = Coords.objects.create(latitude=55.7558, longitude=37.6176, height=200)
        pereval_added = PerevalAdded.objects.create(user=user, coord=coords, beautyTitle="Test Title", title="Test", other_titles="Other Titles", connect="Connection", add_time=timezone.now(), status='new')

        PerevalImages.objects.create(pereval=pereval_added, img=b"Fake image data", date_added=timezone.now())

    def test_pereval_images_creation(self):
        image = PerevalImages.objects.get(pereval__title="Test")

        # Сравниваем двоичные данные
        self.assertEqual(bytes(image.img), b"Fake image data")
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
class BaseViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email="test@example.com", name="Test User", phone="1234567890")
        cls.coords = Coords.objects.create(latitude=55.7558, longitude=37.6176, height=200)
        cls.pereval_added = PerevalAdded.objects.create(
            user=cls.user,
            coord=cls.coords,
            beautyTitle="Test Title",
            title="Test",
            other_titles="Other Titles",
            connect="Connection",
            add_time=timezone.now(),
            status='new'
        )
        cls.pereval_image = PerevalImages.objects.create(
            pereval=cls.pereval_added,
            img=b"Fake image data",
            date_added=timezone.now()
        )
        cls.activity_type = SprActivitiesTypes.objects.create(title="Hiking")
class SubmitDataViewTest(BaseViewTest):
    def test_post_submit_data(self):
        url = reverse('submit-data')
        data = {
            'user': self.user.id,
            'coord': self.coords.id,
            'beautyTitle': 'New Title',
            'title': 'New Pereval',
            'other_titles': 'Other New Titles',
            'connect': 'New Connection Details',
            'add_time': timezone.now().isoformat(),
            'status': 'new'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_submit_data(self):
        url = reverse('submit-data-detail', args=[self.pereval_added.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_submit_data(self):
        url = reverse('submit-data-detail', args=[self.pereval_added.id])
        data = {'status': 'updated'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class UserViewTest(BaseViewTest):
    def test_post_user(self):
        url = reverse('user')
        data = {
            'email': "newuser@example.com",
            'name': "New User",
            'phone': "1234567890"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class CoordsViewTest(BaseViewTest):
    def test_post_coords(self):
        url = reverse('coords')
        data = {
            'latitude': 55.7558,
            'longitude': 37.6176,
            'height': 200
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_coords(self):
        url = reverse('coords-detail', args=[self.coords.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class PerevalImagesViewTest(BaseViewTest):
    def test_post_pereval_images(self):
        url = reverse('pereval-images')
        data = {
            'pereval': self.pereval_added.id,
            'img': b"New Image Data"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_pereval_images(self):
        url = reverse('pereval-images-detail', args=[self.pereval_image.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class SprActivitiesTypesViewTest(BaseViewTest):
    def test_post_activity_type(self):
        url = reverse('spr-activities-types')
        data = {'title': 'Climbing'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_activity_type(self):
        url = reverse('spr-activities-types-detail', args=[self.activity_type.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
