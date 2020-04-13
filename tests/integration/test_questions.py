import json
import unittest
from unittest import mock

from questions import create_app


def get_mock_data(filename):
    """Retrieves data from a file received as a parameter

    :param str filename: file with data
    :return: json data of the file
    """
    with open(filename) as mocked_data_file:
        return json.load(mocked_data_file)


class ViewsTests(unittest.TestCase):
    """Integration tests for the app"""

    @classmethod
    def setUpClass(cls):
        """Creates a patch for questions"""
        super(ViewsTests, cls).setUpClass()
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        cls.app = app
        cls.test_client = app.test_client()
        cls.questions_patch = mock.patch('questions.main.utils.get_questions')
        cls.mock_questions = get_mock_data('tests/mock_questions.json')

    def setUp(self):
        """Setup activates the patches with the mocked data"""
        super(ViewsTests, self).setUp()
        # Start patches
        self.movies = self.questions_patch.start()
        self.movies.return_value = self.mock_questions

    def tearDown(self):
        """Stops patches"""
        self.questions_patch.stop()

    def test_html_contains_list_of_questions(self):
        """Test questions are displayed in the page"""
        response = self.test_client.get('/questions/all', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Questions', response.data)

        question = self.mock_questions[0]
        self.assertIn(question['title'].encode(), response.data)
