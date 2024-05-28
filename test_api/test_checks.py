from checks import (
    SkipCheck, Check, run_test, skip_test, format_err_msg,
    BOLD_GREEN, NORMAL_GREEN, BOLD_RED, NORMAL_RED, BOLD_YELLOW, NORMAL_YELLOW,
    DEFAULT
)
from unittest.mock import patch, call, Mock
import pytest


class TestSkipCheck:

    def test_skipCheck_is_initialised_with_a_function_and_title(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.func == add
        assert skip.title == "add"

    def test_when_called_with_returns_self(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.when_called_with(2) is skip

    def test_is_not_same_as_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num

        test_title = "add func"
        skip = SkipCheck(add, test_title)

        skip.is_not_same_as({"lucky_number": 13})

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_type_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num

        test_title = "add func"

        skip = SkipCheck(add, test_title)

        skip.is_type(str)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_should_print_skip_test_message(self, capsys):
        test_title = "returns 8"

        def add(num):
            return num + num

        skip = SkipCheck(add, test_title)
        skip.returns(4)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out


class TestCheck:

    def test_check_is_initialised_with_a_function_and_title(self):
        def add(num):
            return num + num

        check = Check(add, "add")

        assert check.func == add
        assert check.title == "add"

    def test_when_called_with_set_args_attr_single_arg(self):
        def add(num):
            return num + num

        check = Check(add, "add")

        check.when_called_with(1)

        assert check.args == (1,)

    def test_when_called_with_set_args_attr_multi_args(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        check.when_called_with(1, 2)

        assert check.args == (1, 2)

    def test_when_called_with_returns_self(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        returned = check.when_called_with(1, 2)

        assert returned is check

    def test_set_return_value_no_args(self):
        def say_hello():
            return "hello"

        check = Check(say_hello, "says hello title")

        check._set_return_value()

        assert check.return_value == "hello"

    def test_set_return_value_with_args(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        check.when_called_with(1, 2)

        check._set_return_value()

        assert check.return_value == 3

    @patch('checks.print')
    def test_set_return_value_prints_helpful_message_and_stack_trace_if_an_exception_is_raised(self, mock_print, capsys):
        def func_that_causes_exception():
            invalid_key = [1, 2, 3]
            test_dict = {}

            test_dict[invalid_key] = True

        test_title = "adds key to dict"
        check = Check(func_that_causes_exception, test_title)

        with pytest.raises(Exception, match="unhashable type: 'list'"):
            check.returns({})

        feedback_msg = (f"{BOLD_RED}func_that_causes_exception(){NORMAL_RED}, "
                        f"Test {test_title}: Test failed, see error "
                        f"message below{DEFAULT}\n")
        expected_calls = [call(feedback_msg)]

        assert mock_print.mock_calls == expected_calls

    def test_is_not_same_as_prints_helpful_message_when_return_value_IS_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns different list"

        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not_same_as(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, return value should be a new list"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_not_same_as_prints_helpful_message_when_return_value_IS_NOT_same_as_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return [el for el in some_list]

        test_title = "returns different list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not_same_as(test_list)

        captured = capsys.readouterr()
        log_message = f"Test {
            test_title}: Test passed, new Python object returned"

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_type_prints_pass_message_when_value_IS_correct_type(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_type(list)

        captured = capsys.readouterr()
        log_message = f"Test {
            test_title}: Test passed, correct data type returned"

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_type_prints_helpful_message_when_return_value_IS_NOT_same_as_correct_type(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_type(str)

        captured = capsys.readouterr()

        log_message = (
            f"Test {test_title}: Return value should "
            f"be of type {test_list.__class__.__name__}"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_should_print_test_passed_message(self, capsys):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: Test passed"

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_prints_message_when_return_value_is_not_same_as_expected(
        self, capsys
    ):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2 + 1

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: expected '8', but received '9'"

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_same_as_should_print_test_passed_message(self, capsys):
        def return_list(some_list):
            return some_list

        test_title = "same object returned"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_same_as(test_list)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: Test passed, same object returned"

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_same_as_should_print_test_failed_message(self, capsys):
        def return_list(some_list):
            return [el for el in some_list]

        test_title = "same object returned"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_same_as(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, "
            "return value should be the same object"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_mutates_input_should_print_test_passed_message(self, capsys):
        def add_one_to_list(some_list):
            some_list.append(1)

        test_title = "mutates input"
        check = Check(add_one_to_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).mutates_input("frogs")

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test passed, "
            "frogs successfully mutated"
        )

        assert f"{add_one_to_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_mutates_input_should_print_test_failed_message(self, capsys):
        def add_one_to_list(some_list):
            return some_list

        test_title = "mutates input"
        check = Check(add_one_to_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).mutates_input("bananas")

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, "
            "bananas has not been mutated"
        )

        assert f"{add_one_to_list.__name__}()" in captured.out
        assert log_message in captured.out


class TestRunTestDecorator:
    def test_wraps_function_correctly(self):
        def func_to_test():
            return 'hello'

        assert callable(run_test(func_to_test))

    def test_run_test_decorator_prints_success_message_if_tests_are_passing(self, capsys):
        @run_test
        def func_to_test():
            assert True

        func_to_test()

        captured = capsys.readouterr()

        expected_feedback = (f"{BOLD_GREEN}func_to_test()"
                             f"{NORMAL_GREEN}: Test passed ✅{DEFAULT}")

        assert expected_feedback in captured.out

    @patch('checks.print')
    def test_run_test_decorator_prints_failure_message_if_assert_fails(self, mock_print):
        def function_under_test():
            return True

        @run_test
        def testing_function():
            assert function_under_test() is False

        with pytest.raises(AssertionError) as e:
            testing_function()

        feedback_msg = (f"{BOLD_RED}testing_function(){NORMAL_RED}: "
                        f"Test failed ❌, see error message below:{DEFAULT}\n")
        expected_calls = [call(feedback_msg)]

        assert mock_print.mock_calls == expected_calls

    @patch('checks.print')
    def test_run_test_decorator_prints_failure_message_if_other_exception_raised(self, mock_print):
        function_under_test = Mock(side_effect=TypeError)

        @run_test
        def testing_function():
            assert function_under_test() is True

        with pytest.raises(TypeError) as e:
            testing_function()

        feedback_msg = (f"{BOLD_RED}testing_function(){NORMAL_RED}: "
                        f"Test failed ❌, see error message below:{DEFAULT}\n")
        expected_calls = [call(feedback_msg)]

        assert mock_print.mock_calls == expected_calls


class TestSkipTestDecorator:
    def test_wraps_function_correctly(self):
        def func_to_test():
            return 'hello'

        assert callable(skip_test(func_to_test))

    def test_skip_test_decorator_prints_skip_message(self, capsys):
        invocation_counter = 0

        def function_under_test():
            return True

        @skip_test
        def func_to_test():
            nonlocal invocation_counter
            invocation_counter += 1
            assert function_under_test() is True

        func_to_test()

        captured = capsys.readouterr()

        expected_feedback = (f"{BOLD_YELLOW}func_to_test()"
                             f"{NORMAL_YELLOW}: Test skipped 🔇{DEFAULT}")

        assert expected_feedback in captured.out
        assert invocation_counter == 0


class TestFormatErrorMessage:
    def test_format_error_message_returns_formatted_error_string(self):
        test_expected = 1
        test_received = 2

        expected_err_msg = (
            f"{NORMAL_RED}expected {test_expected}, instead received "
            f"{test_received}{DEFAULT}"
        )

        assert format_err_msg(test_expected, test_received) == expected_err_msg
