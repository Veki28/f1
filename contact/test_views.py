from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm

# Create your tests here.


class TestContactView(TestCase):

    def test_render_contact_page(self):
        """Verifies get request for contact containing a message"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Me', response.content)
        self.assertTrue(isinstance(
            response.context['contact_form'], ContactForm))

    def test_successful_contact_request_submission(self):
        """Test for a user requesting a contact"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('contact'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Your message has been recieved.", response.content)
