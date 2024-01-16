"""This module contains an object that represents a TeleGenic Message Parse Modes."""
from typing import ClassVar

from TeleGenic import constants
from TeleGenic.utils.deprecate import set_new_attribute_deprecated


class ParseMode:
    """This object represents a TeleGenic Message Parse Modes."""

    __slots__ = ('__dict__',)

    MARKDOWN: ClassVar[str] = constants.PARSEMODE_MARKDOWN
    """:const:`TeleGenic.constants.PARSEMODE_MARKDOWN`\n

    Note:
        :attr:`MARKDOWN` is a legacy mode, retained by TeleGenic for backward compatibility.
        You should use :attr:`MARKDOWN_V2` instead.
    """
    MARKDOWN_V2: ClassVar[str] = constants.PARSEMODE_MARKDOWN_V2
    """:const:`TeleGenic.constants.PARSEMODE_MARKDOWN_V2`"""
    HTML: ClassVar[str] = constants.PARSEMODE_HTML
    """:const:`TeleGenic.constants.PARSEMODE_HTML`"""

    def __setattr__(self, key: str, value: object) -> None:
        set_new_attribute_deprecated(self, key, value)
