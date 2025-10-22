from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest


from ansible_collections.ansible.certification.plugins.modules.sample_module import (
    make_hello_message,
)


@pytest.mark.parametrize(
    'input_str,expected',
    [
        ('Alice', 'Hello, Alice'),
        ('Bob', 'Hello, Bob'),
    ]
)
def test_make_hello_message(input_str, expected):
    # Testing the function is_uuid
    assert make_hello_message(input_str) == expected
