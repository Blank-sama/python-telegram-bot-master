"""This module contains the :class:`TeleGenic.ext.utils.promise.Promise` class for backwards
compatibility.
"""
import warnings

import TeleGenic.ext.utils.promise as promise
from TeleGenic.utils.deprecate import TeleGenicDeprecationWarning

warnings.warn(
    'TeleGenic.utils.promise is deprecated. Please use TeleGenic.ext.utils.promise instead.',
    TeleGenicDeprecationWarning,
)

Promise = promise.Promise
"""
:class:`TeleGenic.ext.utils.promise.Promise`

.. deprecated:: v13.2
   Use :class:`TeleGenic.ext.utils.promise.Promise` instead.
"""
