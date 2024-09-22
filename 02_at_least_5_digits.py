from test_api.checks import run_test, run_test, format_err_msg
import re

# Change only the variable called `YOUR_REGEX_HERE`.
# Please do not adjust any code within the tests.


def at_least_5_digits():
    # Your pattern should match a string or substring containing at least 5
    #  of the digits from 1 to 9 only
    YOUR_REGEX_HERE = r"[1-9]{5,}"
    # replace 'x' with an appropriate regular expression pattern
    return re.compile(YOUR_REGEX_HERE)


@run_test
def test_matches_5_digits_at_start_of_string():
    assert at_least_5_digits().match("12345"), \
        format_err_msg('match object', at_least_5_digits().match("12345"))

    assert at_least_5_digits().match("56783"), \
        format_err_msg('match object', at_least_5_digits().match("56783"))

    assert at_least_5_digits().match("98764").span() == (0, 5), \
        format_err_msg((0, 5), at_least_5_digits().match("98764").span())

    assert at_least_5_digits().match("13837").group() == '13837', \
        format_err_msg(13837, at_least_5_digits().match("13837").group())

    assert at_least_5_digits().match("45613837"), \
        format_err_msg(f"match object", at_least_5_digits().match("45613837"))


@run_test
def test_matches_5_digits_contained_within_string():
    assert len(at_least_5_digits().findall("45613sggs83767xy")) == 2, \
        format_err_msg(2, len(at_least_5_digits().findall("45613sggs83767xy")))

    assert at_least_5_digits().search("abc13837def").span() == (3, 8), \
        format_err_msg((3, 8), at_least_5_digits().search("abc13837def").span())  # noqa

    assert at_least_5_digits().search("00abcg77777"), \
        format_err_msg('match object', at_least_5_digits().search("00abcg77777"))  # noqa

    assert not at_least_5_digits().match("00abcg77777"), \
        format_err_msg(None, at_least_5_digits().match("00abcg77777"))

    assert at_least_5_digits().search("13837!f"), \
        format_err_msg('match object', at_least_5_digits().search("13837!f"))


@run_test
def test_should_not_match_string_with_fewer_than_5_digits():
    assert not at_least_5_digits().search("123"), \
        format_err_msg(None, at_least_5_digits().search("123"))

    assert not at_least_5_digits().search("12308"), \
        format_err_msg(None, at_least_5_digits().search("12308"))

    assert not at_least_5_digits().search("1234"), \
        format_err_msg(None, at_least_5_digits().search("1234"))

    assert not at_least_5_digits().search("addc6826asd"), \
        format_err_msg(None, at_least_5_digits().search("addc6826asd"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_matches_5_digits_at_start_of_string()
    test_matches_5_digits_contained_within_string()
    test_should_not_match_string_with_fewer_than_5_digits()
