# Licensed under a 3-clause BSD style license - see LICENSE.rst
# LOCAL
from .. import exceptions
from .. import tree
from ....tests.helper import raises


@raises(exceptions.W07)
def test_check_astroyear_fail():
    config = {'pedantic': True}
    field = tree.Field(None, name='astroyear')
    tree.check_astroyear('X2100', field, config)


@raises(exceptions.W08)
def test_string_fail():
    config = {'pedantic': True}
    tree.check_string(42, 'foo', config)
