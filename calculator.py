# Membuat class Calculator
class Calculator:

    # Method untuk penjumlahan
    def tambah(self, a, b):
        return a + b

    # Method untuk pengurangan
    def kurang(self, a, b):
        return a - b

    # Method untuk perkalian
    def kali(self, a, b):
        return a * b

    # Method untuk pembagian
    def bagi(self, a, b):
        # Cek jika pembagi = 0
        if b == 0:
            # Menghasilkan error
            raise ValueError("Tidak bisa dibagi nol")
        
        return a / b

    
# Import library unittest
import unittest

# Import class Calculator dari file calculator.py
from calculator import Calculator

# Membuat class testing
class TestCalculator(unittest.TestCase):

    # Method ini dijalankan sebelum setiap test
    def setUp(self):
        self.calc = Calculator()

    # Test penjumlahan
    def test_tambah(self):
        self.assertEqual(self.calc.tambah(2, 3), 5)

    # Test pengurangan
    def test_kurang(self):
        self.assertEqual(self.calc.kurang(5, 3), 2)

    # Test perkalian
    def test_kali(self):
        self.assertEqual(self.calc.kali(2, 4), 8)

    # Test pembagian
    def test_bagi(self):
        self.assertEqual(self.calc.bagi(10, 2), 5)

    # Test pembagian dengan nol (error)
    def test_bagi_nol(self):
        with self.assertRaises(ValueError):
            self.calc.bagi(10, 0)

# Menjalankan unit test
if __name__ == "__main__":
    unittest.main()