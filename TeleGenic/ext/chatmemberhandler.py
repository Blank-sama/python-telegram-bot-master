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
"""This module contains the ChatMemberHandler classes."""
from typing import ClassVar, TypeVar, Union, Callable

from TeleGenic import Update
from TeleGenic.utils.helpers import DefaultValue, DEFAULT_FALSE
from .handler import Handler
from .utils.types import CCT

RT = TypeVar('RT')


class ChatMemberHandler(Handler[Update, CCT]):
    """Handler class to handle TeleGenic updates that contain a chat member update.

    .. versionadded:: 13.4

    Note:
        :attr:`pass_user_data` and :attr:`pass_chat_data` determine whether a ``dict`` you
        can use to keep any data in will be sent to the :attr:`callback` function. Related to
        either the user or the chat that the update was sent in. For each update from the same user
        or in the same chat, it will be the same ``dict``.

        Note that this is DEPRECATED, and you should use context based callbacks. See
        https://git.io/fxJuV for more info.

    Warning:
        When setting ``run_async`` to :obj:`True`, you cannot rely on adding custom
        attributes to :class:`TeleGenic.ext.CallbackContext`. See its docs for more info.

    Args:
        callback (:obj:`callable`): The callback function for this handler. Will be called when
            :attr:`check_update` has determined that an update should be processed by this handler.
            Callback signature for context based API:

            ``def callback(update: Update, context: CallbackContext)``

            The return value of the callback is usually ignored except for the special case of
            :class:`TeleGenic.ext.ConversationHandler`.
        chat_member_types (:obj:`int`, optional): Pass one of :attr:`MY_CHAT_MEMBER`,
            :attr:`CHAT_MEMBER` or :attr:`ANY_CHAT_MEMBER` to specify if this handler should handle
            only updates with :attr:`TeleGenic.Update.my_chat_member`,
            :attr:`TeleGenic.Update.chat_member` or both. Defaults to :attr:`MY_CHAT_MEMBER`.
        pass_update_queue (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``update_queue`` will be passed to the callback function. It will be the ``Queue``
            instance used by the :class:`TeleGenic.ext.Updater` and :class:`TeleGenic.ext.Dispatcher`
            that contains new updates which can be used to insert updates. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        pass_job_queue (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``job_queue`` will be passed to the callback function. It will be a
            :class:`TeleGenic.ext.JobQueue` instance created by the :class:`TeleGenic.ext.Updater`
            which can be used to schedule new jobs. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        pass_user_data (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``user_data`` will be passed to the callback function. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        pass_chat_data (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``chat_data`` will be passed to the callback function. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        run_async (:obj:`bool`): Determines whether the callback will run asynchronously.
            Defaults to :obj:`False`.

    Attributes:
        callback (:obj:`callable`): The callback function for this handler.
        chat_member_types (:obj:`int`, optional): Specifies if this handler should handle
            only updates with :attr:`TeleGenic.Update.my_chat_member`,
            :attr:`TeleGenic.Update.chat_member` or both.
        pass_update_queue (:obj:`bool`): Determines whether ``update_queue`` will be
            passed to the callback function.
        pass_job_queue (:obj:`bool`): Determines whether ``job_queue`` will be passed to
            the callback function.
        pass_user_data (:obj:`bool`): Determines whether ``user_data`` will be passed to
            the callback function.
        pass_chat_data (:obj:`bool`): Determines whether ``chat_data`` will be passed to
            the callback function.
        run_async (:obj:`bool`): Determines whether the callback will run asynchronously.

    """

    __slots__ = ('chat_member_types',)
    MY_CHAT_MEMBER: ClassVar[int] = -1
    """:obj:`int`: Used as a constant to handle only :attr:`TeleGenic.Update.my_chat_member`."""
    CHAT_MEMBER: ClassVar[int] = 0
    """:obj:`int`: Used as a constant to handle only :attr:`TeleGenic.Update.chat_member`."""
    ANY_CHAT_MEMBER: ClassVar[int] = 1
    """:obj:`int`: Used as a constant to handle bot :attr:`TeleGenic.Update.my_chat_member`
    and :attr:`TeleGenic.Update.chat_member`."""

    def __init__(
        self,
        callback: Callable[[Update, CCT], RT],
        chat_member_types: int = MY_CHAT_MEMBER,
        pass_update_queue: bool = False,
        pass_job_queue: bool = False,
        pass_user_data: bool = False,
        pass_chat_data: bool = False,
        block: Union[bool, DefaultValue] = DEFAULT_FALSE,
    ):
        super().__init__(
            callback,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            pass_user_data=pass_user_data,
            pass_chat_data=pass_chat_data,
            block=block,
        )

        self.chat_member_types = chat_member_types

    def check_update(self, update: object) -> bool:
        """Determines whether an update should be passed to this handlers :attr:`callback`.

        Args:
            update (:class:`TeleGenic.Update` | :obj:`object`): Incoming update.

        Returns:
            :obj:`bool`

        """
        if isinstance(update, Update):
            if not (update.my_chat_member or update.chat_member):
                return False
            if self.chat_member_types == self.ANY_CHAT_MEMBER:
                return True
            if self.chat_member_types == self.CHAT_MEMBER:
                return bool(update.chat_member)
            return bool(update.my_chat_member)
        return False
