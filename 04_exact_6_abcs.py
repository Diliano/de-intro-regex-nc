from test_api.checks import run_test, skip_test, format_err_msg
import re

# Change only the variable called `YOUR_REGEX_HERE`.
# Please do not adjust any code within the tests.


def exact_6_abcs():
    # Your pattern should match a string consisting of exactly 6 characters. 
    # These characters may only consist of 'a', 'b' or 'c' in any order.
    # You should look up regex anchors for this exercise.
    
    YOUR_REGEX_HERE = r"^[abc]{6}$"
    # replace 'x' with an appropriate regular expression pattern
    return re.compile(YOUR_REGEX_HERE)


@run_test
def test_matches_exact_6_abcs():
    assert exact_6_abcs().search("abcabc"), \
        format_err_msg('match object', exact_6_abcs().search("abcabc"))

    assert exact_6_abcs().match("cbabac"), \
        format_err_msg('match object', exact_6_abcs().search("cbabac"))


@run_test
def test_does_not_match_unless_string_contains_exact_6_abcs():
    assert not exact_6_abcs().search("jdjdhgcacacamzmxm"), \
        format_err_msg(None, exact_6_abcs().search("jdjdhgcacacamzmxm"))

    assert not exact_6_abcs().search("bbbccakkksyyt"), \
        format_err_msg(None, exact_6_abcs().search("bbbccakkksyyt"))

    assert not exact_6_abcs().search("xyzxyz"), \
        format_err_msg(None, exact_6_abcs().search("xyzxyz"))

    assert not exact_6_abcs().search("pqrsqp"), \
        format_err_msg(None, exact_6_abcs().search("pqrsqp"))

    assert not exact_6_abcs().search("pprrss"), \
        format_err_msg(None, exact_6_abcs().search("pprrss"))

    assert not exact_6_abcs().search("vsxprh"), \
        format_err_msg(None, exact_6_abcs().search("vsxprh"))

    assert not exact_6_abcs().search("abcabca"), \
        format_err_msg(None, exact_6_abcs().search("abcabca"))

    assert not exact_6_abcs().search("abca"), \
        format_err_msg(None, exact_6_abcs().search("abca"))

    assert not exact_6_abcs().search("jdjdhgcacacabmzmxm"), \
        format_err_msg(None, exact_6_abcs().search("jdjdhgcacacabmzmxm"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_matches_exact_6_abcs()
    test_does_not_match_unless_string_contains_exact_6_abcs()
