"""This module contains an object that represents a TeleGenic ChatAction."""
from typing import ClassVar
from TeleGenic import constants
from TeleGenic.utils.deprecate import set_new_attribute_deprecated


class ChatAction:
    """Helper class to provide constants for different chat actions."""

    __slots__ = ('__dict__',)  # Adding __dict__ here since it doesn't subclass TGObject
    FIND_LOCATION: ClassVar[str] = constants.CHATACTION_FIND_LOCATION
    """:const:`TeleGenic.constants.CHATACTION_FIND_LOCATION`"""
    RECORD_AUDIO: ClassVar[str] = constants.CHATACTION_RECORD_AUDIO
    """:const:`TeleGenic.constants.CHATACTION_RECORD_AUDIO`

        .. deprecated:: 13.5
           Deprecated by TeleGenic. Use :attr:`RECORD_VOICE` instead.
    """
    RECORD_VOICE: ClassVar[str] = constants.CHATACTION_RECORD_VOICE
    """:const:`TeleGenic.constants.CHATACTION_RECORD_VOICE`

        .. versionadded:: 13.5
    """
    RECORD_VIDEO: ClassVar[str] = constants.CHATACTION_RECORD_VIDEO
    """:const:`TeleGenic.constants.CHATACTION_RECORD_VIDEO`"""
    RECORD_VIDEO_NOTE: ClassVar[str] = constants.CHATACTION_RECORD_VIDEO_NOTE
    """:const:`TeleGenic.constants.CHATACTION_RECORD_VIDEO_NOTE`"""
    TYPING: ClassVar[str] = constants.CHATACTION_TYPING
    """:const:`TeleGenic.constants.CHATACTION_TYPING`"""
    UPLOAD_AUDIO: ClassVar[str] = constants.CHATACTION_UPLOAD_AUDIO
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_AUDIO`

        .. deprecated:: 13.5
           Deprecated by TeleGenic. Use :attr:`UPLOAD_VOICE` instead.
    """
    UPLOAD_VOICE: ClassVar[str] = constants.CHATACTION_UPLOAD_VOICE
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_VOICE`

        .. versionadded:: 13.5
    """
    UPLOAD_DOCUMENT: ClassVar[str] = constants.CHATACTION_UPLOAD_DOCUMENT
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_DOCUMENT`"""
    CHOOSE_STICKER: ClassVar[str] = constants.CHATACTION_CHOOSE_STICKER
    """:const:`TeleGenic.constants.CHOOSE_STICKER`

        .. versionadded:: 13.8"""
    UPLOAD_PHOTO: ClassVar[str] = constants.CHATACTION_UPLOAD_PHOTO
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_PHOTO`"""
    UPLOAD_VIDEO: ClassVar[str] = constants.CHATACTION_UPLOAD_VIDEO
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_VIDEO`"""
    UPLOAD_VIDEO_NOTE: ClassVar[str] = constants.CHATACTION_UPLOAD_VIDEO_NOTE
    """:const:`TeleGenic.constants.CHATACTION_UPLOAD_VIDEO_NOTE`"""

    def __setattr__(self, key: str, value: object) -> None:
        set_new_attribute_deprecated(self, key, value)
