# TestcaughtSpeeding.py

# Import Statements
import unittest
import caughtSpeeding

class KnownValues(unittest.TestCase):

    def test_caughtSpeedingFor60NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(60, False)
        # Check for expected output
        self.assertEqual(0, result)

    def test_caughtSpeedingFor61NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(61, False)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor65NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(65, False)
        # Check for expected output
        self.assertEqual(500)

    def test_caughtSpeedingFor65Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(65, True)
        # Check for expected output
        self.assertEqual(0, result)


    def test_caughtSpeedingFor80NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(80, False)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor81NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(81, False)
        # Check for expected output
        self.assertEqual(1000, result)

    def test_caughtSpeedingFor85NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(85, False)
        # Check for expected output
        self.assertEqual(1000)

    def test_caughtSpeedingFor85NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(85, True)
        # Check for expected output
        self.assertEqual(500, result)

    def test_caughtSpeedingFor91NoBirthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(91, False)
        # Check for expected output
        self.assertEqual(1000)

    def test_caughtSpeedingFor55Birthday(self):
        # Capture the results of the function
        result = caughtSpeeding.caughtSpeeding(55, True)
        # Check for expected output
        self.assertEqual(0, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
