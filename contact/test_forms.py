from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = ContactForm(
            {'name': 'test', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertTrue(form.is_valid(), msg="Form not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = ContactForm(
            {'name': '', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(), msg="Name not provided, but form is valid")

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ContactForm(
            {'name': 'Test', 'email': '', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(), msg="Email not provided, but form is valid")

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ContactForm(
            {'name': 'Test', 'email': 'test@test.com', 'message': ''})
        self.assertFalse(
            form.is_valid(), msg="Message not provided, but form is valid")
