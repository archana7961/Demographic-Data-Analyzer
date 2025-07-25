import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTests(unittest.TestCase):
    def test_demographics(self):
        result = calculate_demographic_data(print_data=False)
        self.assertAlmostEqual(result['average_age_men'], 39.4, places=1)
        self.assertAlmostEqual(result['percentage_bachelors'], 16.4, places=1)
        self.assertGreater(result['higher_education_rich'], 40.0)
        self.assertLess(result['min_work_hours'], 10)

if __name__ == "__main__":
    unittest.main()
