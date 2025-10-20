from fib import fibonacci   # <-- update this import

class TestFibonacci(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fibonacci(1), [0])

    def test_seven(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_zero(self):
        self.assertEqual(fibonacci(0), [])
