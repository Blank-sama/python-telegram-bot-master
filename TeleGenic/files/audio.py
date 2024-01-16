"""This module contains an object that represents a TeleGenic Audio."""

from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import PhotoSize, TeleGenicObject
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import JSONDict, ODVInput

if TYPE_CHECKING:
    from TeleGenic import Bot, File


class Audio(TeleGenicObject):
    """This object represents an audio file to be treated as music by the Telegram clients.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`file_unique_id` is equal.

    Args:
        file_id (:obj:`str`): Identifier for this file, which can be used to download
            or reuse the file.
        file_unique_id (:obj:`str`): Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used to download or reuse the file.
        duration (:obj:`int`): Duration of the audio in seconds as defined by sender.
        performer (:obj:`str`, optional): Performer of the audio as defined by sender or by audio
            tags.
        title (:obj:`str`, optional): Title of the audio as defined by sender or by audio tags.
        file_name (:obj:`str`, optional): Original filename as defined by sender.
        mime_type (:obj:`str`, optional): MIME type of the file as defined by sender.
        file_size (:obj:`int`, optional): File size.
        thumb (:class:`telegram.PhotoSize`, optional): Thumbnail of the album cover to
            which the music file belongs.
        bot (:class:`telegram.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        file_id (:obj:`str`): Identifier for this file.
        file_unique_id (:obj:`str`): Unique identifier for this file, which
            is supposed to be the same over time and for different bots.
            Can't be used to download or reuse the file.
        duration (:obj:`int`): Duration of the audio in seconds.
        performer (:obj:`str`): Optional. Performer of the audio as defined by sender or by audio
            tags.
        title (:obj:`str`): Optional. Title of the audio as defined by sender or by audio tags.
        file_name (:obj:`str`): Optional. Original filename as defined by sender.
        mime_type (:obj:`str`): Optional. MIME type of the file as defined by sender.
        file_size (:obj:`int`): Optional. File size.
        thumb (:class:`telegram.PhotoSize`): Optional. Thumbnail of the album cover to
            which the music file belongs.
        bot (:class:`TeleGenic.Bot`): Optional. The Bot to use for instance methods.

    """

    __slots__ = (
        'file_id',
        'bot',
        'file_size',
        'file_name',
        'thumb',
        'title',
        'duration',
        'performer',
        'mime_type',
        'file_unique_id',
        '_id_attrs',
    )

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: str = None,
        title: str = None,
        mime_type: str = None,
        file_size: int = None,
        thumb: PhotoSize = None,
        bot: 'Bot' = None,
        file_name: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.file_id = str(file_id)
        self.file_unique_id = str(file_unique_id)
        self.duration = int(duration)
        # Optionals
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = thumb
        self.bot = bot

        self._id_attrs = (self.file_unique_id,)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['Audio']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['thumb'] = PhotoSize.de_json(data.get('thumb'), bot)

        return cls(bot=bot, **data)

    def get_file(
        self, timeout: ODVInput[float] = DEFAULT_NONE, api_kwargs: JSONDict = None
    ) -> 'File':
        """Convenience wrapper over :attr:`TeleGenic.Bot.get_file`

        For the documentation of the arguments, please see :meth:`TeleGenic.Bot.get_file`.

        Returns:
            :class:`TeleGenic.File`

        Raises:
            :class:`TeleGenic.error.TelegramError`

        """
        return self.bot.get_file(file_id=self.file_id, timeout=timeout, api_kwargs=api_kwargs)
