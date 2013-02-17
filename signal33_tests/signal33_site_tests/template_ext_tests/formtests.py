from signal33_site.template_ext import form
import unittest

class FormTest(unittest.TestCase):

    def test_begin_form_valid(self):
        ret = form.begin_form('test', "test")
        self.assertEqual(ret, '<form id="test" name="test" action="test" method="post">')

    def test_end_form(self):
        self.assertEqual(form.end_form(), "</form>")

    def test_input(self):
        self.assertEqual(form.form_input('test'), '<input type="text" id="test" name="test" />')

