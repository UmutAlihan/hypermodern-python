import click.testing
import pytest

from hypermodern_python import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner, mock_sleep):
    result = runner.invoke(console.main, ["--count=3"])
    assert result.exit_code == 0