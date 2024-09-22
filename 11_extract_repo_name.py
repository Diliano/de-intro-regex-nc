from test_api.checks import run_test, skip_test, format_err_msg
import re

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def extract_repo_name(text):
    """
    This function should take a string representing a github url and return
    the name of the repo.

    Github urls are of the form https://github.com/northcoders/de-intro-regex
    where "northcoders" is the name of the account and "de-intro-regex" is the
    name of the repo
    """
    regex = re.compile(r"github.com/[^/]*/([^/]*)")
    if regex.search(text):
        return regex.search(text).group(1)


@run_test
def test_extract_repo_name_returns_repo_name():
    test_url_1 = "https://github.com/northcoders/intro-week"
    test_url_2 = "https://github.com/northcoders/remote-git-workshop"
    test_url_3 = "https://github.com/myAccount/notes"
    test_url_4 = "https://github.com/myAccount/notes/settings"
    assert extract_repo_name(test_url_1) == "intro-week", \
        format_err_msg("intro-week", extract_repo_name(test_url_1))
    assert extract_repo_name(test_url_2) == "remote-git-workshop", \
        format_err_msg("remote-git-workshop", extract_repo_name(test_url_2))
    assert extract_repo_name(test_url_3) == "notes", \
        format_err_msg("notes", extract_repo_name(test_url_3))
    assert extract_repo_name(test_url_4) == "notes", \
        format_err_msg("notes", extract_repo_name(test_url_4))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_extract_repo_name_returns_repo_name()
