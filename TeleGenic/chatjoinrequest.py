"""This module contains an object that represents a TeleGenic ChatJoinRequest."""
import datetime
from typing import TYPE_CHECKING, Any, Optional

from TeleGenic import TeleGenicObject, User, Chat, ChatInviteLink
from TeleGenic.utils.helpers import from_timestamp, to_timestamp, DEFAULT_NONE
from TeleGenic.utils.types import JSONDict, ODVInput

if TYPE_CHECKING:
    from TeleGenic import Bot


class ChatJoinRequest(TeleGenicObject):
    """This object represents a join request sent to a chat.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`chat`, :attr:`from_user` and :attr:`date` are equal.

    Note:
        Since Bot API 5.5, bots are allowed to contact users who sent a join request to a chat
        where the bot is an administrator with the
        :attr:`~TeleGenic.ChatMemberAdministrator.can_invite_users` administrator right – even if
        the user never interacted with the bot before.

    .. versionadded:: 13.8

    Args:
        chat (:class:`TeleGenic.Chat`): Chat to which the request was sent.
        from_user (:class:`TeleGenic.User`): User that sent the join request.
        date (:class:`datetime.datetime`): Date the request was sent.
        bio (:obj:`str`, optional): Bio of the user.
        invite_link (:class:`TeleGenic.ChatInviteLink`, optional): Chat invite link that was used
            by the user to send the join request.
        bot (:class:`TeleGenic.Bot`, optional): The Bot to use for instance methods.

    Attributes:
        chat (:class:`TeleGenic.Chat`): Chat to which the request was sent.
        from_user (:class:`TeleGenic.User`): User that sent the join request.
        date (:class:`datetime.datetime`): Date the request was sent.
        bio (:obj:`str`): Optional. Bio of the user.
        invite_link (:class:`TeleGenic.ChatInviteLink`): Optional. Chat invite link that was used
            by the user to send the join request.

    """

    __slots__ = (
        'chat',
        'from_user',
        'date',
        'bio',
        'invite_link',
        'bot',
        '_id_attrs',
    )

    def __init__(
        self,
        chat: Chat,
        from_user: User,
        date: datetime.datetime,
        bio: str = None,
        invite_link: ChatInviteLink = None,
        bot: 'Bot' = None,
        **_kwargs: Any,
    ):
        # Required
        self.chat = chat
        self.from_user = from_user
        self.date = date

        # Optionals
        self.bio = bio
        self.invite_link = invite_link

        self.bot = bot
        self._id_attrs = (self.chat, self.from_user, self.date)

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['ChatJoinRequest']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['chat'] = Chat.de_json(data.get('chat'), bot)
        data['from_user'] = User.de_json(data.get('from'), bot)
        data['date'] = from_timestamp(data.get('date', None))
        data['invite_link'] = ChatInviteLink.de_json(data.get('invite_link'), bot)

        return cls(bot=bot, **data)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        data['date'] = to_timestamp(self.date)

        return data

    def approve(
        self,
        timeout: ODVInput[float] = DEFAULT_NONE,
        api_kwargs: JSONDict = None,
    ) -> bool:
        """Shortcut for::

            bot.approve_chat_join_request(chat_id=update.effective_chat.id,
            user_id=update.effective_user.id, *args, **kwargs)

        For the documentation of the arguments, please see
        :meth:`TeleGenic.Bot.approve_chat_join_request`.

        Returns:
            :obj:`bool`: On success, :obj:`True` is returned.

        """
        return self.bot.approve_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_user.id, timeout=timeout, api_kwargs=api_kwargs
        )

    def decline(
        self,
        timeout: ODVInput[float] = DEFAULT_NONE,
        api_kwargs: JSONDict = None,
    ) -> bool:
        """Shortcut for::

            bot.decline_chat_join_request(chat_id=update.effective_chat.id,
            user_id=update.effective_user.id, *args, **kwargs)

        For the documentation of the arguments, please see
        :meth:`TeleGenic.Bot.decline_chat_join_request`.

        Returns:
            :obj:`bool`: On success, :obj:`True` is returned.

        """
        return self.bot.decline_chat_join_request(
            chat_id=self.chat.id, user_id=self.from_user.id, timeout=timeout, api_kwargs=api_kwargs
        )
