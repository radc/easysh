# tests/test_easysh.py

import unittest
from unittest.mock import patch
from easysh.main import generate_command

class TestEasySh(unittest.TestCase):

    @patch('easysh.main.openai.ChatCompletion.create')
    def test_generate_command(self, mock_create):
        mock_create.return_value = {
            'choices': [{
                'message': {
                    'content': 'cd abc'
                }
            }]
        }
        prompt = "open folder called abc"
        api_key = "fake-api-key"
        command = generate_command(prompt, api_key)
        self.assertEqual(command, 'cd abc')

    @patch('easysh.main.openai.ChatCompletion.create')
    def test_generate_command_auth_error(self, mock_create):
        from easysh.main import generate_command
        import openai

        mock_create.side_effect = openai.error.AuthenticationError("Invalid API key")

        prompt = "open folder called abc"
        api_key = "invalid-api-key"

        with self.assertRaises(SystemExit) as cm:
            generate_command(prompt, api_key)
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
