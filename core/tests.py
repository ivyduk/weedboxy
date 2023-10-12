from django.test import TestCase
from django.urls import reverse
from apps.users.forms import SubscribeForm
from django.contrib.messages import get_messages


class SubscribeFormTest(TestCase):

    def test_subscribe_form_valid(self):
        # Create a test data dictionary for the form
        form_data = {
            'email': 'correo@example.com',
            'is_subscribed': True
        }

        # Simulates a POST request to the form
        response = self.client.post(reverse('index'), form_data, follow=True)

        # Verify that it redirects to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that a success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), '¡Tus datos han sido enviados satisfactoriamente, pronto nuestro equipo se pondrá en contacto contigo!')

    def test_subscribe_form_invalid(self):
        # Create a test data dictionary for the form with a duplicate mail
        form_data = {
            'email': 'correo@example.com',
            'is_subscribed': True
        }

        form = SubscribeForm(data=form_data)
     
        # Simulates a POST request to the form
        response = self.client.post(reverse('index'), form_data, follow=True)

        # Verify that it redirects to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that an error message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        print(str(messages[0]))
        self.assertEqual(str(messages[0]), 'El correo electrónico ya está registrado.')
        

       
     
    def test_subscribe_form_empty(self):
        # Create a test data dictionary for the empty form
        form_data = {}

        # Simulates a POST request to the form
        response = self.client.post(reverse('index'), form_data, follow=True)

        # Verify that it redirects to the home page
        self.assertEqual(response.status_code, 200)

        # Verify that form errors are displayed
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('email', 'required'))
      
