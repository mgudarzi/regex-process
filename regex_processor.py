import re
import os
import unittest


def read_file(filename):
    """Return a list of the lines in the file with the passed filename"""

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__)  # <-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path, "r", encoding="utf-8")

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines


def find_times(string_list):
    """Return a list of valid times in the list of strings"""
    out = []
    pattern = r"\b(?:[1-9]|1[0-2]):[0-5][0-9] ?[aApP][mM]\b"
    for element in string_list:
        out.extend(re.findall(pattern, element))
    return out


def find_urls(string_list):
    out = []
    """Return a list of valid URLs in the list of strings"""
    pattern = r"\b((?:http:\/\/|https:\/\/)www\.\S*(?:\.com|\.org)\S*)\b"
    for element in string_list:
        out.extend(re.findall(pattern, element))
    return out


def find_dates(string_list):
    """Return a list of valid dates in the list of strings"""
    out = []
    pattern = r"\b(?:(?:0?[1-9]|1[0-2])[\/\-\.](?:[0-2][0-9]|3[01])[\/\-\.](?:\d{2}|\d{4})|(?:[0-2][0-9]|3[01])\.(?:0?[1-9]|1[0-2])\.(?:\d{2}|\d{4}))\b"
    for element in string_list:
        out.extend(re.findall(pattern, element))
    return out


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.strings = read_file("alice_in_wonderland.txt")

    def test_find_times(self):
        times = find_times(self.strings)
        self.assertEqual(len(times), 6)
        self.assertEqual(
            times,
            ["11:11 pm", "12:00 pm", "12:25 am", "6:00 pm", "10:05 am", "4:32am"],
            "test of times returned",
        )
        str1 = ["12:20 pm and 4:20 am and 05:17"]
        self.assertEqual(find_times(str1), ["12:20 pm", "4:20 am"])
        str2 = str1 + ["4:00 am we are just getting started."]
        self.assertEqual(find_times(str2), ["12:20 pm", "4:20 am", "4:00 am"])

    def test_find_urls(self):
        urls = find_urls(self.strings)
        self.assertEqual(len(urls), 5)
        self.assertEqual(
            urls,
            [
                "https://www.goodreads.com/work/quotes/2933712-alice-in-wonderland",
                "https://www.youtube.com/watch?v=rPK67tnsfZc",
                "https://www.youtube.com/watch?v=msvOUUgv6m8",
                "https://www.pythex.com",
                "http://www.gutenberg.org/1/11",
            ],
            "test of URLs returned",
        )

        str1 = ["My URL https://www.fernando.org"]
        self.assertEqual(find_urls(str1), ["https://www.fernando.org"])

        str2 = str1 + ["Bad url https://www. fernando .com"]
        self.assertEqual(find_urls(str2), ["https://www.fernando.org"])

    def test_find_dates(self):
        dates = find_dates(self.strings)
        self.assertEqual(len(dates), 6)
        self.assertEqual(
            dates,
            [
                "06/08/2020",
                "06-08-2020",
                "06-05-2010",
                "04-05-1865",
                "26.11.1865",
                "26.11.1865",
            ],
            "test of dates returned",
        )

        str1 = ["End of the world 12/21/2012"]
        self.assertEqual(find_dates(str1), ["12/21/2012"])

        str2 = str1 + ["Sold out dates 04-12-2020, 12.12.2019, 123455"]
        self.assertEqual(find_dates(str2), ["12/21/2012", "04-12-2020", "12.12.2019"])


def main():
    # Use main to test your function.
    # Run unit tests, but feel free to run any additional functions you need
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
