"""
HW 3: Scripting - Reddit testing

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.

This assignment template was adapted from Peter Bui (c) 2020's Python scripting
assignment: https://gitlab.com/nd-cse-20289-sp20/cse-20289-sp20-assignments/
which is licensed under the MIT license agreement.
"""

import unittest

from reddit import build_parser, load_reddit_data, format_reddit_data

class RedditTestCases(unittest.TestCase):

    def test_build_parser(self):
        """tests the returned ArgumentParser from build_parser()"""
        parser = build_parser()

        # tests whether running the script with the help flag exits the script
        with self.assertRaises(SystemExit):
            parser.parse_args(['-h'])

        # test default values
        test_url = 'https://www.reddit.com/r/python/.json'
        args = parser.parse_args([test_url])
        self.assertEqual(args.url, test_url)
        self.assertEqual(args.n, 10)
        self.assertEqual(args.o, "score")
        self.assertEqual(args.t, 60)


    def test_load_reddit_data(self):
        # Tests the returned dict from load_reddit_data().
        parser = build_parser()
        # Parse command line arguments
        test_url = 'https://www.reddit.com/r/python/.json'
        args = parser.parse_args([test_url])

        # Load data from url and then print the data
        data = load_reddit_data(args.url)

        # scores are subject to change
        sample1 = {'score': 4, 'title': "Sunday Daily Thread: What's everyone working on this week?", 
        'url': 'https://www.reddit.com/r/Python/comments/115w23y/sunday_daily_thread_whats_everyone_working_on/'}
        sample2 = {'score': 1, 'title': 'Tuesday Daily Thread: Advanced questions', 
        'url': 'https://www.reddit.com/r/Python/comments/117ospx/tuesday_daily_thread_advanced_questions/'}
        self.assertEqual(len(data), 27)
        self.assertTrue(sample1 in data)
        self.assertTrue(sample2 in data)
        self.assertFalse({None: None} in data)



    def test_format_reddit_data(self):
        # Tests the sorted and formatted list from format_reddit_data().
        parser = build_parser()
        # Parse command line arguments
        test_url = 'chatgpt'
        args = parser.parse_args([test_url])

        # Load data from url and then print the data
        data = load_reddit_data(args.url)
        # format data
        formatted_data = format_reddit_data(data, 5)
        # scores are subject to change
        first = {'score': 1655, 'title': 'Google is history?', 'url': 'https://i.redd.it/2cm3dvrdnaja1.jpg'}
        last = {'score': 826, 'title': 'OpenAI: “We’ve trained a model called ChatGPT which interact', 'url': 'https://i.redd.it/6uxqxowmafja1.jpg'}

        self.assertEqual(first, formatted_data[0])
        self.assertEqual(last, formatted_data(len(formatted_data) - 1))



    def test_format_reddit_data(self):
        # Tests the sorted and formatted list from format_reddit_data().
        parser = build_parser()
        # Parse command line arguments
        test_url = 'chatgpt'
        args = parser.parse_args([test_url])

        # Load data from url and then print the data
        data = load_reddit_data(args.url)
        # format data
        formatted_data = format_reddit_data(data, 10, 'title', 14)
        # scores are subject to change
        first = {'score': 41, 'title': '"It\'s just a w', 'url': 'https://i.redd.it/ermallvh4eja1.jpg'}
        last = {'score': 36, 'title': "ChatGPT's Open", 'url': 'https://www.reddit.com/r/ChatGPT/comments/117ner5/chatgpts_open_alternative_we_need_your_help_open/'}
        self.assertEqual(first, formatted_data[0])
        self.assertEqual(last, formatted_data(len(formatted_data) - 1))


if __name__ == "__main__":
    """Run your unit tests by python3 test_reddit.py"""
    unittest.main()