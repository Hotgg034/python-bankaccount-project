import unittest
from bank import deposit, withdraw

class TestBank(unittest.TestCase):
    def test_deposit(self):
        self.assertEqual(deposit(100, 50), 150)
        self.assertEqual(deposit(0, 200), 200)

    def test_withdraw(self):
        self.assertEqual(withdraw(100, 40), 60)
        self.assertEqual(withdraw(50, 100), "Error: Insufficient funds")

if __name__ == "__main__":
    unittest.main()
