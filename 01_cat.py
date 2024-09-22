from test_api.checks import run_test, skip_test, format_err_msg
import re

# Change only the variable called `YOUR_REGEX_HERE`.
# Please do not adjust any code within the tests.


def cat():
    # Your pattern should **match** a string containing the characters cat
    YOUR_REGEX_HERE = 'cat'
    # replace 'x' with an appropriate regular expression pattern
    return re.compile(YOUR_REGEX_HERE)


@run_test
def test_cat_matches_correctly():
    cat_match_object = cat().match('cat')

    assert cat_match_object is not None, \
        format_err_msg('match object', cat_match_object)

    assert cat_match_object.group() == 'cat', \
        format_err_msg('cat', cat_match_object.group())

    assert cat_match_object.span() == (0, 3), \
        format_err_msg((0, 3), cat_match_object.span())


@run_test
def test_matches_cat_at_start_of_string_correctly():
    cat_match_object = cat().match('cat11234')

    assert cat_match_object is not None, \
        format_err_msg('match object', cat_match_object)

    assert cat_match_object.group() == 'cat',  \
        format_err_msg(cat, cat_match_object.group())

    assert cat_match_object.span() == (0, 3), \
        format_err_msg((0, 3), cat_match_object.span())


@run_test
def test_matches_cat_at_end_of_string_correctly():
    cat_match_object = cat().search("36237cat")

    assert cat_match_object is not None, \
        format_err_msg('match object', cat_match_object)

    assert cat_match_object.group() == 'cat',  \
        format_err_msg(cat, cat_match_object.group())

    assert cat_match_object.span() == (5, 8), \
        format_err_msg((5, 8), cat_match_object.span())


@run_test
def test_matches_cat_in_the_middle_of_string_correctly():
    cat_match_object = cat().search('asdcatfgh')

    assert cat_match_object is not None, \
        format_err_msg('match object', cat_match_object)

    assert cat_match_object.group() == 'cat', \
        format_err_msg(cat, cat_match_object.group())

    assert cat_match_object.span() == (3, 6), \
        format_err_msg((3, 6), cat_match_object.span())


@run_test
def test_ignores_capitalised_cats():
    cat_match_object = cat().search('Catalogue')

    assert not cat_match_object, \
        format_err_msg(None, cat_match_object)


@run_test
def test_ignores_incomplete_cats():
    assert not cat().search("ca123"), \
        format_err_msg(None, cat().search("ca123"))

    assert not cat().search("atasdads"), \
        format_err_msg(None, cat().search("atasdads"))

    assert not cat().search("caasdlkj"), \
        format_err_msg(None, cat().search("caasdlkj"))

    assert not cat().search("12123ca234"), \
        format_err_msg(None, cat().search("12123ca234"))


# DO NOT CHANGE CODE BELOW THIS LINE


if __name__ == '__main__':
    test_cat_matches_correctly()
    test_matches_cat_at_start_of_string_correctly()
    test_matches_cat_at_end_of_string_correctly()
    test_matches_cat_in_the_middle_of_string_correctly()
    test_ignores_capitalised_cats()
    test_ignores_incomplete_cats()
