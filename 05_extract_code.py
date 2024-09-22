from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def extract_code(text):
    """
    This function should take a string as an argument

    Somewhere in the middle of the string, there will be a series of
    consecutive digits composing a number

    You should extract that number from the string and return it as
    an integer
    """
    regex = re.compile(r"[0-9]+")
    return int(regex.search(text).group())


@run_test
def test_extract_code_finds_number_in_single_word_string():
    assert extract_code("abcd67yuio") == 67, \
        format_err_msg(67, extract_code("abcd67yuio"))
    assert extract_code("abcd103yuio") == 103, \
        format_err_msg(67, extract_code("abcd103yuio"))
    assert extract_code("abcd4567yuio") == 4567, \
        format_err_msg(67, extract_code("abcd4567yuio"))
    assert extract_code("abcd1000289yuio") == 1000289, \
        format_err_msg(67, extract_code("abcd1000289yuio"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_extract_code_finds_number_in_single_word_string()
