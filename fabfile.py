"""File read by fab polish"""

from fabpolish import sniff, polish, info, local
from fabpolish.contrib import (
    check_python_debug_info, find_merge_conflict_leftovers,
    python_code_analyzer
)


@sniff(severity='minor', timing='slow')
def find_pyflakes_violations():
    """Run pep8/pyflakes python coding standard check
    """
    info('Running coding standards check for python files...')
    return local(
        "git ls-files -z | "
        "grep -PZz '\.py$' | "  # noqa
        "xargs -0 pycodestyle"
    )
