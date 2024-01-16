"""This module facilitates the deprecation of functions."""

import warnings


# We use our own DeprecationWarning since they are muted by default and "UserWarning" makes it
# seem like it's the user that issued the warning
# We name it something else so that you don't get confused when you attempt to suppress it
class TeleGenicDeprecationWarning(Warning):
    """Custom warning class for deprecations in this library."""

    __slots__ = ()


# Function to warn users that setting custom attributes is deprecated (Use only in __setattr__!)
# Checks if a custom attribute is added by checking length of dictionary before & after
# assigning attribute. This is the fastest way to do it (I hope!).
def set_new_attribute_deprecated(self: object, key: str, value: object) -> None:
    """Warns the user if they set custom attributes on PTB objects."""
    org = len(self.__dict__)
    object.__setattr__(self, key, value)
    new = len(self.__dict__)
    if new > org:
        warnings.warn(
            f"Setting custom attributes such as {key!r} on objects such as "
            f"{self.__class__.__name__!r} of the PTB library is deprecated.",
            TeleGenicDeprecationWarning,
            stacklevel=3,
        )
