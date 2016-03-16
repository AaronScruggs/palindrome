import re
import logging

from datetime import datetime

logging.basicConfig(filename='info.log', level=logging.INFO)


def logging_info(string, result):
    """
    Logs the date, time, string, and result.
    """
    timedate = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    logging.info(timedate)
    logging.info(string)
    logging.info(result)


def clean_up(text):
    """
    :param text: String to be formatted.
    :return: A new string lowered and striped of punctuation.
    """
    match = re.sub(r"\W", "", text)
    lowered = match.lower()
    return lowered


def check_chars(front, back, word):
    """ Recursivley check to see if word is a palindrome """

    if front >= back:
        return True

    if word[front] != word[back]:
        return False
    else:
        return check_chars(front+1, back-1, word)


def palindrome(string):
    """
    Main function that checks if a string is a palindrome.
    :param string: A string of text.
    :return: True if string is a palindrome, else false.
    """

    working_string = clean_up(string)

    front = 0
    back = len(working_string) - 1

    result = check_chars(front, back, working_string)

    logging_info(string, result)
    return result


def alt_palindrome(string):
    """ Solution without recursion. """

    working = clean_up(string)

    front = 0
    back = len(working) - 1

    while front <= back:
        if working[front] != working[back]:
            return False
        front += 1
        back -= 1

    return True
