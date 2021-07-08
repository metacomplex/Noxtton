import unittest
from main.Main import get_repos

class TestStringMethods(unittest.TestCase):

    def test_len_repos(self):
        repos = get_repos("rammstein")
        self.assertEqual(len(repos), 50)

    def test_asc(self):
        repos = get_repos("rammstein", "asc")
        for i in range(len(repos) - 1):
            self.assertTrue(repos[i]["name"] <= repos[i + 1]["name"])

    def test_desc(self):
        repos = get_repos("rammstein", "desc")
        for i in range(len(repos) - 1):
            self.assertTrue(repos[i]["name"] >= repos[i + 1]["name"])

    def test_ignore(self):
        repos = get_repos("rammstein", "desc", "ram")
        self.assertEqual(len(repos), 4)


if __name__ == '__main__':
    unittest.main()