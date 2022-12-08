"""
Sample tests
"""
from django.test import SimpleTestCase
from app.calc import add, subtract

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self) -> None:
        """Test adding numbers together."""
        res: int = add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self) -> None:
        """Test Subtracting numbers together."""
        res: int = subtract(15, 10)
        self.assertEqual(res, 5)