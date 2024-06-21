from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm(
            {'name': 'test', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertTrue(form.is_valid(), msg="Form not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm(
            {'name': '', 'email': 'test@test.com', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(), msg="Name not provided, but form is valid")

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm(
            {'name': 'Test', 'email': '', 'message': 'Hello!'})
        self.assertFalse(
            form.is_valid(), msg="Email not provided, but form is valid")

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm(
            {'name': 'Test', 'email': 'test@test.com', 'message': ''})
        self.assertFalse(
            form.is_valid(), msg="Message not provided, but form is valid")
