from django.test import TestCase


# Create your tests here.
class MyTest(TestCase):

    def test_pass(self):
        self.assertEqual(1, 1)

    def test_fail(self):
        self.assertEqual(2, 1)