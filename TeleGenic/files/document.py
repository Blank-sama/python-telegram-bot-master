#!/usr/bin/env python
#
# A library that provides a Python interface to the TeleGenic Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-TeleGenic-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a TeleGenic Document."""

from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import PhotoSize, TeleGenicObject
from TeleGenic.utils.helpers import DEFAULT_NONE
from TeleGenic.utils.types import JSONDict, ODVInput

if TYPE_CHECKING:
    from TeleGenic import Bot, File


class Document(TeleGenicObject):
    """This object represents a general file
    (as opposed to photos, voice messages and audio files).

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`file_unique_id` is equal.

    Args:
        file_id (:obj:`str`): Identifier for this file, which can be used to download
            or reuse the file.
        file_unique_id (:obj:`str`): Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used to download or reuse the file.
        thumb (:class:`TeleGenic.PhotoSize`, optional): Document thumbnail as defined by sender.
        file_name (:obj:`str`, optional): Original filename as defined by sender.
        mime_type (:obj:`str`, optional): MIME type of the file as defined by sender.
        file_size (:obj:`int`, optional): File size.
        bot (:class:`TeleGenic.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        file_id (:obj:`str`): File identifier.
        file_unique_id (:obj:`str`): Unique identifier for this file, which
            is supposed to be the same over time and for different bots.
            Can't be used to download or reuse the file.
        thumb (:class:`TeleGenic.PhotoSize`): Optional. Document thumbnail.
        file_name (:obj:`str`): Original filename.
        mime_type (:obj:`str`): Optional. MIME type of the file.
        file_size (:obj:`int`): Optional. File size.
        bot (:class:`TeleGenic.Bot`): Optional. The Bot to use for instance methods.

    """

    __slots__ = (
        'bot',
        'file_id',
        'file_size',
        'file_name',
        'thumb',
        'mime_type',
        'file_unique_id',
        '_id_attrs',
    )

    _id_keys = ('file_id',)

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumb: PhotoSize = None,
        file_name: str = None,
        mime_type: str = None,
        file_size: int = None,
        bot: 'Bot' = None,
        **_kwargs: Any,
    ):
        # Required
        self.file_id = str(file_id)
        self.file_unique_id = str(file_unique_id)
        # Optionals
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.bot = bot

        self._id_attrs = (self.file_unique_id,)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['Document']:
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
