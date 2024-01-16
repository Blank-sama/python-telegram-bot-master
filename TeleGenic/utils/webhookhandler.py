"""This module contains the :class:`TeleGenic.ext.utils.webhookhandler.WebhookHandler` class for
backwards compatibility.
"""
import warnings

import TeleGenic.ext.utils.webhookhandler as webhook_handler
from TeleGenic.utils.deprecate import TeleGenicDeprecationWarning

warnings.warn(
    'TeleGenic.utils.webhookhandler is deprecated. Please use TeleGenic.ext.utils.webhookhandler '
    'instead.',
    TeleGenicDeprecationWarning,
)

WebhookHandler = webhook_handler.WebhookHandler
WebhookServer = webhook_handler.WebhookServer
WebhookAppClass = webhook_handler.WebhookAppClass
