"""This module contains an object that represents a TeleGenic WebhookInfo."""

from typing import Any, List

from TeleGenic import TeleGenicObject


class WebhookInfo(TeleGenicObject):
    """This object represents a TeleGenic WebhookInfo.

    Contains information about the current status of a webhook.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`url`, :attr:`has_custom_certificate`,
    :attr:`pending_update_count`, :attr:`ip_address`, :attr:`last_error_date`,
    :attr:`last_error_message`, :attr:`max_connections` and :attr:`allowed_updates` are equal.

    Args:
        url (:obj:`str`): Webhook URL, may be empty if webhook is not set up.
        has_custom_certificate (:obj:`bool`): :obj:`True`, if a custom certificate was provided for
            webhook certificate checks.
        pending_update_count (:obj:`int`): Number of updates awaiting delivery.
        ip_address (:obj:`str`, optional): Currently used webhook IP address.
        last_error_date (:obj:`int`, optional): Unix time for the most recent error that happened
            when trying to deliver an update via webhook.
        last_error_message (:obj:`str`, optional): Error message in human-readable format for the
            most recent error that happened when trying to deliver an update via webhook.
        max_connections (:obj:`int`, optional): Maximum allowed number of simultaneous HTTPS
            connections to the webhook for update delivery.
        allowed_updates (List[:obj:`str`], optional): A list of update types the bot is subscribed
            to. Defaults to all update types, except :attr:`TeleGenic.Update.chat_member`.

    Attributes:
        url (:obj:`str`): Webhook URL.
        has_custom_certificate (:obj:`bool`): If a custom certificate was provided for webhook.
        pending_update_count (:obj:`int`): Number of updates awaiting delivery.
        ip_address (:obj:`str`): Optional. Currently used webhook IP address.
        last_error_date (:obj:`int`): Optional. Unix time for the most recent error that happened.
        last_error_message (:obj:`str`): Optional. Error message in human-readable format.
        max_connections (:obj:`int`): Optional. Maximum allowed number of simultaneous HTTPS
            connections.
        allowed_updates (List[:obj:`str`]): Optional. A list of update types the bot is subscribed
            to. Defaults to all update types, except :attr:`TeleGenic.Update.chat_member`.

    """

    __slots__ = (
        'allowed_updates',
        'url',
        'max_connections',
        'last_error_date',
        'ip_address',
        'last_error_message',
        'pending_update_count',
        'has_custom_certificate',
        '_id_attrs',
    )

    def __init__(
        self,
        url: str,
        has_custom_certificate: bool,
        pending_update_count: int,
        last_error_date: int = None,
        last_error_message: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        ip_address: str = None,
        **_kwargs: Any,
    ):
        # Required
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count

        # Optional
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates

        self._id_attrs = (
            self.url,
            self.has_custom_certificate,
            self.pending_update_count,
            self.ip_address,
            self.last_error_date,
            self.last_error_message,
            self.max_connections,
            self.allowed_updates,
        )
