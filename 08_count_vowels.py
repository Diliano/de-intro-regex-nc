from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def count_vowels(text):
    """
    This function should take a string as an argument, and return a count
    representing the number of vowels it contains
    """
    regex = re.compile(r"[aeiouAEIOU]")
    return len(regex.findall(text))

@run_test
def test_count_vowels_counts_vowels_in_string():
    assert count_vowels("") == 0, \
        format_err_msg(0, count_vowels(""))
    assert count_vowels("bcd") == 0, \
        format_err_msg(0, count_vowels("bcd"))
    assert count_vowels("a") == 1, \
        format_err_msg(1, count_vowels("a"))
    assert count_vowels("abc") == 1, \
        format_err_msg(1, count_vowels("abc"))
    assert count_vowels("AEbiO") == 4, \
        format_err_msg(4, count_vowels("AEbiO"))
    assert count_vowels("aaeee!!!") == 5, \
        format_err_msg(5, count_vowels("aaeee!!!"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_count_vowels_counts_vowels_in_string()
