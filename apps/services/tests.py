from django.test import TestCase
from .forms import ServicesContactForm
from .models import Service, Feature


class ServicesContactFormTest(TestCase):
         
    def setUp(self):
        self.service1 = Service.objects.create(name='Servicio 1')
        self.service2 = Service.objects.create(name='Servicio 2')

    def test_valid_form(self):
       
        data = {
            'first_name': 'John',
            'last_name': 'Rosero',
            'phone': '1234567890',
            'email': 'john@example.com',
            'services': self.service1.id, 
        }
        form = ServicesContactForm(data=data)

        
        if not form.is_valid():
            print(form.errors)
    
        self.assertTrue(form.is_valid())


    def test_valid_form_without_email(self):
        # creating data for the form
        data = {
            'first_name': 'Ivan',
            'last_name': 'Duque',
            'phone': '1234567890',
            'email': '',
            'services':  self.service2.id,
        }
        form = ServicesContactForm(data=data)

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())





    def test_invalid_form(self):
        # creating data for the form (without data)
        form = ServicesContactForm(data={})

        #Checks if the form is invalid
        self.assertFalse(form.is_valid())


class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Service test object to use in testing
        cls.service = Service.objects.create(name="Servicio de prueba")

    def test_str_representation(self):
        # Checks if the string representation of the Service model is correct
        self.assertEqual(str(self.service), "Servicio de prueba")

    def test_image_field(self):
        #Check if the Service image field is working correctly
        self.assertIsNotNone(self.service.image)


class FeatureModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a Service test object
        service = Service.objects.create(name="Servicio de Prueba")

        # Creates a Feature test object associated with the Service test object
        cls.feature = Feature.objects.create(
            name="Característica de Prueba",
            description="Descripción de la característica de prueba",
            service=service,
        )

    def test_str_representation(self):
        # Checks if the string representation of the Feature model is correct
        self.assertEqual(str(self.feature), "Característica de Prueba")
