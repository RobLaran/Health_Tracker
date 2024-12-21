import unittest
from unittest.mock import MagicMock
from datetime import date
from features import LogBodyMeasurement

class TestLogBodyMeasurement(unittest.TestCase):
    def setUp(self):
        """
        Set up a mock database and an instance of LogBodyMeasurement for testing.
        """
        self.mock_database = MagicMock()
        self.log_body_measurement = LogBodyMeasurement(self.mock_database)
        self.userid = 1

    def test_log_new_entry(self):
        """
        Test logging a new body measurement entry.
        """
        date_str = date.today().isoformat()
        weight = 70
        height = 175

        self.log_body_measurement.log(self.userid, date_str, weight, height)

        # Assert that weight and height are updated in the database
        self.mock_database.updateWeight.assert_called_once_with(weight, self.userid, date_str)
        self.mock_database.updateHeight.assert_called_once_with(height, self.userid, date_str)

    def test_log_empty_date(self):
        """
        Test logging a body measurement entry with an empty date (uses today's date).
        """
        weight = 70
        height = 175

        self.log_body_measurement.log(self.userid, "", weight, height)

        # Assert that weight and height are updated with today's date
        self.mock_database.updateWeight.assert_called_once_with(weight, self.userid, self.log_body_measurement.date)
        self.mock_database.updateHeight.assert_called_once_with(height, self.userid, self.log_body_measurement.date)

    def test_view_logs(self):
        """
        Test viewing logs with mock data.
        """
        mock_logs = {
            "2024-12-01": {"weight": 70, "height": 175},
            "2024-12-02": {"weight": 72, "height": 176},
        }
        self.mock_database.getUserLogs.return_value = mock_logs

        self.log_body_measurement.viewLogs(self.userid)

        # Ensure the method fetches logs from the database
        self.mock_database.getUserLogs.assert_called_once_with(self.userid)

    def test_calculate_bmi_underweight(self):
        """
        Test calculating BMI for underweight.
        """
        weight = 50
        height = 175
        bmi, status = self.log_body_measurement.calculateBMI(weight, height)

        self.assertEqual(bmi, round(50 / (1.75 * 1.75), 2))
        self.assertEqual(status, "Underweight")

    def test_calculate_bmi_normal(self):
        """
        Test calculating BMI for normal weight.
        """
        weight = 68
        height = 175
        bmi, status = self.log_body_measurement.calculateBMI(weight, height)

        self.assertEqual(bmi, round(68 / (1.75 * 1.75), 2))
        self.assertEqual(status, "Normal")

    def test_calculate_bmi_overweight(self):
        """
        Test calculating BMI for overweight.
        """
        weight = 85
        height = 175
        bmi, status = self.log_body_measurement.calculateBMI(weight, height)

        self.assertEqual(bmi, round(85 / (1.75 * 1.75), 2))
        self.assertEqual(status, "Overweight")

    def test_calculate_bmi_obese(self):
        """
        Test calculating BMI for obese.
        """
        weight = 110
        height = 175
        bmi, status = self.log_body_measurement.calculateBMI(weight, height)

        self.assertEqual(bmi, round(110 / (1.75 * 1.75), 2))
        self.assertEqual(status, "Overweight")

    def test_calculate_avg_weight(self):
        """
        Test calculating average weight.
        """
        mock_data = [
            ["2024-12-01", 70, 175],
            ["2024-12-02", 72, 176],
        ]

        avg_weight = self.log_body_measurement.calculateAVGWeight(mock_data)

        self.assertEqual(avg_weight, round((70 + 72) / 2, 2))

    def test_calculate_avg_height(self):
        """
        Test calculating average height.
        """
        mock_data = [
            ["2024-12-01", 70, 175],
            ["2024-12-02", 72, 176],
        ]

        avg_height = self.log_body_measurement.calculateAVGHeight(mock_data)

        self.assertEqual(avg_height, round((175 + 176) / 2, 2))


if __name__ == "__main__":
    unittest.main()
