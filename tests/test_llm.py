import unittest
from sas2py.llm import replace_names
import json

class TestLLM(unittest.TestCase):

    def test_replace_names(self):
        code = "select Model, KmH_City, KmH_Highway from sashelp.cars"
        names = json.dumps({"KmH_City": "kmh_city", "sashelp.cars": "dealership.cars"})
        expected_code = "select Model, kmh_city, KmH_Highway from dealership.cars"
        self.assertEqual(replace_names(code, names), expected_code)

    def test_replace_names_multiple(self):
        code = "select Model, KmH_City from sashelp.cars where KmH_City > 20"
        names = json.dumps({"KmH_City": "kmh_city", "sashelp.cars": "dealership.cars"})
        expected_code = "select Model, kmh_city from dealership.cars where kmh_city > 20"
        self.assertEqual(replace_names(code, names), expected_code)
