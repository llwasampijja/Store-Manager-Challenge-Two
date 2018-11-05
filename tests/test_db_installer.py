import psycopg2
import unittest
from app.db_installer import create_tables

class TestDbInstaller(unittest.TestCase):
    def test_create_tables(self):
        self.assertEqual(create_tables(), "success")
