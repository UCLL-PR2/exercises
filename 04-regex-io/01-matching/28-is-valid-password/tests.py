import pytest
import student
import solution


@pytest.mark.parametrize("string", [
    *[f'{a}{b}{c}{d}'
      for a in ['A', 'FQPIQFK', 'fjkla']
      for b in ['g', 'pfoajaz', '9512']
      for c in ['+', '-', '*', '/', '.', '@', 'F']
      for d in ['1', '4312948', 'FQZJFP'] ],
    'ABCabc123@+/',
    'ABCabcA123A@+A/',
    'ABCabc11123@+/',
])
def test_function(string):
    function_name = 'is_valid_password'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")


    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(solution_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
