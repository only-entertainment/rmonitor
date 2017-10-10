from unittest import TestCase


class TestTestCase(TestCase):

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)
