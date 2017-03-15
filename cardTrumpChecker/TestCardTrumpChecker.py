# TestcaughtSpeeding.py

# Import Statements
import unittest
import cardTrumpChecker

class KnownValues(unittest.TestCase):

    def test_cardTrumpCheckerForLowNumHighColor(self):
        # Capture the results of the function
        result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'yellow'), ('card2', 7, 'green') )
        # Check for expected output
        self.assertEqual("card2", result)

    def test_cardTrumpCheckerForSameNumHighColor(self):
        # Capture the results of the function
        result = cardTrumpChecker.cardTrumpChecker(('card1', 5, 'red'), ('card2', 5, 'yellow') )
        # Check for expected output
        self.assertEqual("card1", result)

    def test_cardTrumpCheckerForSameNumLowColor(self):
        # Capture the results of the function
        result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'green'), ('card2', 10, 'yellow') )
        # Check for expected output
        self.assertEqual("card2")

    def test_cardTrumpCheckerForHighNumLowColor(self):
        # Capture the results of the function
        result = cardTrumpChecker.cardTrumpChecker(('card1', 2, 'green'), ('card2', 1, 'red'))
        # Check for expected output
        self.assertEqual("card1", result)


    def test_cardTrumpCheckerForSameCardSameNum(self):
        # Capture the results of the function
        result = cardTrumpChecker.cardTrumpChecker(('card1', 10, 'red'), ('card2', 10, 'red'))
        # Check for expected output
        self.assertEqual("card1", result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
