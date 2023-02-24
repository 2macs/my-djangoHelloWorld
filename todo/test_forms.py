from django.test import TestCase
from .forms import Itemform


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = Itemform({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())  # Confirms the error is on the name field
        self.assertAlmostEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = Itemform({'name': 'This is a test'})
        self.assertTrue(form.is_valid())

    # Tests that only the nae fields and done fields are available

    def test_fields_are_explicit_in_form_metaclass(self):
        form = Itemform()
        self.assertAlmostEqual(form.Meta.fields, ['name', 'done'])



