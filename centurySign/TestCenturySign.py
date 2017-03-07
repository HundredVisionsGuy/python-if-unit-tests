# TestCenturySign.py

# Import Statements
import unittest
import centurySign

class KnownValues(unittest.TestCase):

    def test_centurySignForFoodDrive(self):
        # Capture the results of the function
        result = centurySign.centurySign(11, 18)
        # Check for expected output
        self.assertEqual('Food Drive', result)

    def test_centurySignForJagFest(self):
        # Capture the results of the function
        result = centurySign.centurySign(8, 14)
        # Check for expected output
        self.assertEqual('JagFest', result)

    def test_centurySignForJagCrew(self):
        # Capture the results of the function
        result = centurySign.centurySign(8, 15)
        # Check for expected output
        self.assertEqual('Jag Crew', result)

    def test_centurySignForForecastingLastDay(self):
        # Capture the results of the function
        result = centurySign.centurySign(5, 14)
        # Check for expected output
        self.assertEqual('Forecasting', result)

    def test_centurySignForFoodDriveLastDay(self):
        # Capture the results of the function
        result = centurySign.centurySign(2, 14)
        # Check for expected output
        self.assertEqual('Food Drive', result)

    def test_centurySignForForecastingFirstDay(self):
        # Capture the results of the function
        result = centurySign.centurySign(2, 15)
        # Check for expected output
        self.assertEqual('Forecasting', result)

    def test_centurySignForMonthErrorHighValue(self):
        # Capture the results of the function
        result = centurySign.centurySign(13, 10)
        # Check for expected output
        self.assertEqual("Month Error", result)

    def test_centurySignForMonthErrorNegative(self):
        # Capture the results of the function
        result = centurySign.centurySign(-91, 15)
        # Check for expected output
        self.assertEqual('Month Error', result)

    def test_centurySignForDayErrorLowValue(self):
        # Capture the results of the function
        result = centurySign.centurySign(10, 0)
        # Check for expected output
        self.assertEqual('Day Error', result)

    def test_centurySignForDayErrorHighValue(self):
        # Capture the results of the function
        result = centurySign.centurySign(8, 42)
        # Check for expected output
        self.assertEqual('Day Error', result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
