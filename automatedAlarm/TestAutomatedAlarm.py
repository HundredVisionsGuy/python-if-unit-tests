# TestCenturySign.py

# Import Statements
import unittest
import automatedAlarm

class KnownValues(unittest.TestCase):

    def test_automatedAlarmForWednesdayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Wednesday", True)
        # Check for expected output
        self.assertEqual('8:30', result)

    def test_automatedAlarmForMondayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Monday", True)
        # Check for expected output
        self.assertEqual('9:30', result)

    def test_automatedAlarmForMondaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Monday", False)
        # Check for expected output
        self.assertEqual('7:00', result)

    def test_automatedAlarmForWednesdaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Wednesday", False)
        # Check for expected output
        self.assertEqual('7:30', result)

    def test_automatedAlarmForSaturdayOff(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Saturday", True)
        # Check for expected output
        self.assertEqual('9:00', result)

    def test_automatedAlarmForSaturdaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Saturday", False)
        # Check for expected output
        self.assertEqual('9:00', result)

    def test_automatedAlarmForFridaySchool(self):
        # Capture the results of the function
        result = automatedAlarm.automatedAlarm("Saturday", False)
        # Check for expected output
        self.assertEqual('7:00', result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
