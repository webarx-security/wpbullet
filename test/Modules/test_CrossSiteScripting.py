import unittest
from Modules.CrossSiteScripting import CrossSiteScripting


class TestCrossSiteScripting(unittest.TestCase):

    def setUp(self):
        pass

    '''
    Ignore
    '''
    # Test if ignores letter in front of function
    def test_ignore_letter_in_front(self):
        test_string = "aprint($_GET['cmd'])"
        matches = CrossSiteScripting.run(CrossSiteScripting, test_string, "file.php")
        self.assertFalse(matches)

    # Test if ignores (int) with brackets
    def test_ignore_int_value_with_brackets(self):
        test_string = "print( (int) $_GET['cmd'])"
        matches = CrossSiteScripting.run(CrossSiteScripting, test_string, "file.php")
        self.assertFalse(matches)

    # Test if ignores (int) without brackets
    def test_ignore_int_value_without_brackets(self):
        test_string = "print (int) $_GET['cmd']"
        matches = CrossSiteScripting.run(CrossSiteScripting, test_string, "file.php")

        self.assertFalse(matches)

    '''
    Match
    '''
    # Test if matches attribute
    def test_match_attribute(self):
        test_string = "print <input type='text' value='$_GET['cmd']'/>"
        matches = CrossSiteScripting.run(CrossSiteScripting, test_string, "file.php")

        self.assertTrue(matches)

    def tearDown(self):
        pass
