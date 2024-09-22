from test_api.checks import run_test, skip_test, format_err_msg
import re

# Change only the variable called `YOUR_REGEX_HERE`.
# Please do not adjust any code within the tests.


def starts_with_exclamation_marks():
    # Your pattern should match one or more exclamation marks at the
    #  **beginning of a string**
    # You should look up regex anchors for this exercise
    YOUR_REGEX_HERE = r"^!{1,}"
    # replace 'x' with an appropriate regular expression pattern
    return re.compile(YOUR_REGEX_HERE)


@run_test
def test_matches_strings_that_start_with_exclamation_marks():
    assert starts_with_exclamation_marks().match("!!!sdlasjdlajsd"), \
        format_err_msg('match object', starts_with_exclamation_marks().match("!!!sdlasjdlajsd"))  # noqa

    assert starts_with_exclamation_marks().match("!!askjaa").span() == (0, 2), \
        format_err_msg((0, 2), starts_with_exclamation_marks().match("!!askjaa").span())  # noqa

    assert starts_with_exclamation_marks().match("!!!!!adjaksljd").group() == '!!!!!', \
        format_err_msg('!!!!!', starts_with_exclamation_marks().match("!!!!!adjaksljd").group())  # noqa

    assert len(starts_with_exclamation_marks().findall("!!!32749!!!anks")) == 1, \
        format_err_msg(1, len(starts_with_exclamation_marks().findall("!!!32749!!!anks")))  # noqa

    assert starts_with_exclamation_marks().match("!abc"), \
        format_err_msg('match object', starts_with_exclamation_marks().match("!abc"))  # noqa


@run_test
def test_does_not_match_string_that_do_not_start_with_exclamation_marks():
    assert not starts_with_exclamation_marks().match("adssdk!!!"), \
        format_err_msg(None, starts_with_exclamation_marks().match("adssdk!!!"))  # noqa

    assert not starts_with_exclamation_marks().match("asdk;alk!!!!"), \
        format_err_msg(None, starts_with_exclamation_marks().match("asdk;alk!!!!"))  # noqa

    assert not starts_with_exclamation_marks().match("errui!!!!gagahj"), \
        format_err_msg(None, starts_with_exclamation_marks().match("errui!!!!gagahj"))  # noqa

    assert not starts_with_exclamation_marks().match("cjljad!!!!gga!!sdd"), \
        format_err_msg(None, starts_with_exclamation_marks().match("cjljad!!!!gga!!sdd"))  # noqa


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_matches_strings_that_start_with_exclamation_marks()
    test_does_not_match_string_that_do_not_start_with_exclamation_marks()
