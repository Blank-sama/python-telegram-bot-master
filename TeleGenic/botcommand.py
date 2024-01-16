"""This module contains an object that represents a TeleGenic Bot Command."""
from typing import Any

from TeleGenic import TeleGenicObject


class BotCommand(TeleGenicObject):
    """
    This object represents a bot command.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`command` and :attr:`description` are equal.

    Args:
        command (:obj:`str`): Text of the command, 1-32 characters. Can contain only lowercase
            English letters, digits and underscores.
        description (:obj:`str`): Description of the command, 1-256 characters.

    Attributes:
        command (:obj:`str`): Text of the command.
        description (:obj:`str`): Description of the command.

    """

    __slots__ = ('description', '_id_attrs', 'command')

    def __init__(self, command: str, description: str, **_kwargs: Any):
        self.command = command
        self.description = description

        self._id_attrs = (self.command, self.description)
