"""This module contains an object that represents a TeleGenic ChatPermission."""

from typing import Any

from TeleGenic import TeleGenicObject


class ChatPermissions(TeleGenicObject):
    """Describes actions that a non-administrator user is allowed to take in a chat.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`can_send_messages`, :attr:`can_send_media_messages`,
    :attr:`can_send_polls`, :attr:`can_send_other_messages`, :attr:`can_add_web_page_previews`,
    :attr:`can_change_info`, :attr:`can_invite_users` and :attr:`can_pin_messages` are equal.

    Note:
        Though not stated explicitly in the official docs, TeleGenic changes not only the
        permissions that are set, but also sets all the others to :obj:`False`. However, since not
        documented, this behaviour may change unbeknown to PTB.

    Args:
        can_send_messages (:obj:`bool`, optional): :obj:`True`, if the user is allowed to send text
            messages, contacts, locations and venues.
        can_send_media_messages (:obj:`bool`, optional): :obj:`True`, if the user is allowed to
            send audios, documents, photos, videos, video notes and voice notes, implies
            :attr:`can_send_messages`.
        can_send_polls (:obj:`bool`, optional): :obj:`True`, if the user is allowed to send polls,
            implies :attr:`can_send_messages`.
        can_send_other_messages (:obj:`bool`, optional): :obj:`True`, if the user is allowed to
            send animations, games, stickers and use inline bots, implies
            :attr:`can_send_media_messages`.
        can_add_web_page_previews (:obj:`bool`, optional): :obj:`True`, if the user is allowed to
            add web page previews to their messages, implies :attr:`can_send_media_messages`.
        can_change_info (:obj:`bool`, optional): :obj:`True`, if the user is allowed to change the
            chat title, photo and other settings. Ignored in public supergroups.
        can_invite_users (:obj:`bool`, optional): :obj:`True`, if the user is allowed to invite new
            users to the chat.
        can_pin_messages (:obj:`bool`, optional): :obj:`True`, if the user is allowed to pin
            messages. Ignored in public supergroups.

    Attributes:
        can_send_messages (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to send text
            messages, contacts, locations and venues.
        can_send_media_messages (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to
            send audios, documents, photos, videos, video notes and voice notes, implies
            :attr:`can_send_messages`.
        can_send_polls (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to send polls,
            implies :attr:`can_send_messages`.
        can_send_other_messages (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to
            send animations, games, stickers and use inline bots, implies
            :attr:`can_send_media_messages`.
        can_add_web_page_previews (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to
            add web page previews to their messages, implies :attr:`can_send_media_messages`.
        can_change_info (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to change the
            chat title, photo and other settings. Ignored in public supergroups.
        can_invite_users (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to invite
            new users to the chat.
        can_pin_messages (:obj:`bool`): Optional. :obj:`True`, if the user is allowed to pin
            messages. Ignored in public supergroups.

    """

    __slots__ = (
        'can_send_other_messages',
        'can_invite_users',
        'can_send_polls',
        '_id_attrs',
        'can_send_messages',
        'can_send_media_messages',
        'can_change_info',
        'can_pin_messages',
        'can_add_web_page_previews',
    )

    def __init__(
        self,
        can_send_messages: bool = None,
        can_send_media_messages: bool = None,
        can_send_polls: bool = None,
        can_send_other_messages: bool = None,
        can_add_web_page_previews: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_pin_messages: bool = None,
        **_kwargs: Any,
    ):
        # Required
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages

        self._id_attrs = (
            self.can_send_messages,
            self.can_send_media_messages,
            self.can_send_polls,
            self.can_send_other_messages,
            self.can_add_web_page_previews,
            self.can_change_info,
            self.can_invite_users,
            self.can_pin_messages,
        )
