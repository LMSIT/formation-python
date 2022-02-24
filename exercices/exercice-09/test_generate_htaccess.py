import unittest

from generate_htaccess import render_template

class TestHtaccess(unittest.TestCase):

    def test_parse_csv(self):
        self.fail("NotImplemented")

    def test_render_template(self):
        ip_rules = [("Allow", "1.1.1.1")]
        result = render_template(ip_rules)

        attempt_result = """Order Allow,Deny
Allow from 1.1.1.1
Deny from all"""

        self.assertEqual(result, attempt_result)

    def test_write_file(self):
        self.fail("NotImplemented")

    def test_options(self):
        self.fail("NotImplemented")

if __name__ == '__main__':
    unittest.main()