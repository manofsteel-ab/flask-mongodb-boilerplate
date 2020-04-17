import pytest


def f():
    return "hello"
    # raise SystemExit(1)


def test_mytest():
    # with pytest.raises(SystemExit):
    assert f() == "hello"
