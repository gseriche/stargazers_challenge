import unittest
from main import get_repo_stars

class TestGitHubStars(unittest.TestCase):

    def test_get_repo_stars(self):
        # Test with a single, popular repository
        repo_list = ['microsoft/vscode']
        result = get_repo_stars(repo_list)
        
        # Check if the result is a dictionary
        self.assertIsInstance(result, dict)
        
        # Check if the dictionary has the expected key
        self.assertIn('vscode', result)
        
        # Check if the star count is a positive integer
        self.assertIsInstance(result['vscode'], int)
        self.assertGreater(result['vscode'], 0)

if __name__ == '__main__':
    unittest.main()