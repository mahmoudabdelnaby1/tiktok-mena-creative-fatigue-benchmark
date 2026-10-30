"""
Unit tests for data integrity and schema validation in tiktok-mena-creative-fatigue-benchmark
"""
import unittest
import json
import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

class TestDatasetIntegrity(unittest.TestCase):
    def test_json_files_are_valid(self):
        json_files = list(REPO_ROOT.rglob("*.json"))
        # Exclude temporary or package files if any
        json_files = [f for f in json_files if not f.name.startswith(".")]
        for jf in json_files:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.assertIsNotNone(data, f"JSON in {jf.name} parsed to None")
                if isinstance(data, (dict, list)):
                    self.assertGreater(len(data), 0, f"JSON file {jf.name} is empty")

    def test_csv_files_are_valid(self):
        csv_files = list(REPO_ROOT.rglob("*.csv"))
        for cf in csv_files:
            with open(cf, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)
                self.assertGreaterEqual(len(rows), 2, f"CSV {cf.name} must have header and at least one data row")

if __name__ == "__main__":
    unittest.main()
