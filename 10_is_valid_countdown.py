from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def is_valid_countdown(text):
    """
    This function should take a string as an argument

    The function must return a boolean depending on if the string is a valid
    collection of letters for the TV show countdown.

    In countdown a valid collection contains at least 4 consonants and 3
    vowels and has exactly 9 letters
    """
    vowel_regex = re.compile(r"[aeiou]")
    consonant_regex = re.compile(r"[b-df-hj-np-tv-z]")
    return len(vowel_regex.findall(text)) >= 3 and len(consonant_regex.findall(text)) >= 4 and len(text) == 9

@run_test
def test_is_valid_countdown_returns_true_for_a_valid_countdown():
    # >=4 consonants, >=3 vowels, exactly 9 letters
    assert is_valid_countdown("aaabbbccc"), \
        format_err_msg(True, is_valid_countdown("aaabbbccc"))
    assert is_valid_countdown("eeeedddff"), \
        format_err_msg(True, is_valid_countdown("eeeedddff"))
    assert is_valid_countdown("aeiouwxyz"), \
        format_err_msg(True, is_valid_countdown("aeiouwxyz"))
    assert is_valid_countdown('abejikosu'), \
        format_err_msg(True, is_valid_countdown("abejikosu"))


@run_test
def test_is_valid_countdown_returns_false_for_an_invalid_countdown():
    assert not is_valid_countdown("aeiouaxyz"), \
        format_err_msg(False, is_valid_countdown("aeiouaxyz"))
    assert not is_valid_countdown("aabbbcccd"), \
        format_err_msg(False, is_valid_countdown("aabbbcccd"))
    assert not is_valid_countdown("aeiouvwxyz"), \
        format_err_msg(False, is_valid_countdown("aeiouvwxyz"))
    assert not is_valid_countdown('aaaaaaaaa'), \
        format_err_msg(False, is_valid_countdown("aaaaaaaaa"))
    assert not is_valid_countdown('bbbbbbbbb'), \
        format_err_msg(False, is_valid_countdown("bbbbbbbbb"))
    assert not is_valid_countdown('aaaabbbb'), \
        format_err_msg(False, is_valid_countdown("aaaabbbb"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_is_valid_countdown_returns_true_for_a_valid_countdown()
    test_is_valid_countdown_returns_false_for_an_invalid_countdown()
