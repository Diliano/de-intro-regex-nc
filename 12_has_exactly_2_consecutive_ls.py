from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def has_exactly_2_consecutive_ls(text):
    """
    This function should take a string as an argument

    You will need to check whether or not it contains *exactly* 2 consecutive
    occurrences of the letter "l" (lower case)

    This means that there *must* be exactly 2 "l"s in total and they *must* be
    consecutive

    You should return True if this is the case, and False otherwise
    """
    regex = re.compile(r"(?<!l)ll(?!l)")
    if regex.search(text):
        return True
    else:
        return False

@run_test
def test_returns_true_when_two_consecutive_ls_found():
    assert has_exactly_2_consecutive_ls("ll"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("ll"))
    assert has_exactly_2_consecutive_ls("hello"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("hello"))
    assert has_exactly_2_consecutive_ls("bells"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("bells"))
    assert has_exactly_2_consecutive_ls("bellows"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("bellows"))
    assert has_exactly_2_consecutive_ls("aaaallasdows"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("aaaallasdows"))
    assert has_exactly_2_consecutive_ls("llama"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("llama"))
    assert has_exactly_2_consecutive_ls("well"), \
        format_err_msg(True, has_exactly_2_consecutive_ls("well"))


@run_test
def test_returns_false_when_exactly_two_consecutive_ls_not_found():
    assert not has_exactly_2_consecutive_ls("mile"), \
        format_err_msg(False, has_exactly_2_consecutive_ls("mile"))
    assert not has_exactly_2_consecutive_ls("fly"), \
        format_err_msg(False, has_exactly_2_consecutive_ls("fly"))
    assert not has_exactly_2_consecutive_ls("wellll"), \
        format_err_msg(False, has_exactly_2_consecutive_ls("wellll"))
    assert not has_exactly_2_consecutive_ls("mitchelllloyd"), \
        format_err_msg(False, has_exactly_2_consecutive_ls("mitchelllloyd"))
    assert not has_exactly_2_consecutive_ls("l"), \
        format_err_msg(False, has_exactly_2_consecutive_ls("l"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_returns_true_when_two_consecutive_ls_found()
    test_returns_false_when_exactly_two_consecutive_ls_not_found()
