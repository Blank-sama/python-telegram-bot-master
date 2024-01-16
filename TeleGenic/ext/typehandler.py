"""This module contains the TypeHandler class."""

from typing import Callable, Type, TypeVar, Union
from TeleGenic.utils.helpers import DefaultValue, DEFAULT_FALSE

from .handler import Handler
from .utils.types import CCT

RT = TypeVar('RT')
UT = TypeVar('UT')


class TypeHandler(Handler[UT, CCT]):
    """Handler class to handle updates of custom types.

    Warning:
        When setting ``run_async`` to :obj:`True`, you cannot rely on adding custom
        attributes to :class:`telegram.ext.CallbackContext`. See its docs for more info.

    Args:
        type (:obj:`type`): The ``type`` of updates this handler should process, as
            determined by ``isinstance``
        callback (:obj:`callable`): The callback function for this handler. Will be called when
            :attr:`check_update` has determined that an update should be processed by this handler.
            Callback signature for context based API:

            ``def callback(update: Update, context: CallbackContext)``

            The return value of the callback is usually ignored except for the special case of
            :class:`telegram.ext.ConversationHandler`.
        strict (:obj:`bool`, optional): Use ``type`` instead of ``isinstance``.
            Default is :obj:`False`
        pass_update_queue (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``update_queue`` will be passed to the callback function. It will be the ``Queue``
            instance used by the :class:`telegram.ext.Updater` and :class:`telegram.ext.Dispatcher`
            that contains new updates which can be used to insert updates. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        pass_job_queue (:obj:`bool`, optional): If set to :obj:`True`, a keyword argument called
            ``job_queue`` will be passed to the callback function. It will be a
            :class:`telegram.ext.JobQueue` instance created by the :class:`telegram.ext.Updater`
            which can be used to schedule new jobs. Default is :obj:`False`.
            DEPRECATED: Please switch to context based callbacks.
        run_async (:obj:`bool`): Determines whether the callback will run asynchronously.
            Defaults to :obj:`False`.

    Attributes:
        type (:obj:`type`): The ``type`` of updates this handler should process.
        callback (:obj:`callable`): The callback function for this handler.
        strict (:obj:`bool`): Use ``type`` instead of ``isinstance``. Default is :obj:`False`.
        pass_update_queue (:obj:`bool`): Determines whether ``update_queue`` will be
            passed to the callback function.
        pass_job_queue (:obj:`bool`): Determines whether ``job_queue`` will be passed to
            the callback function.
        run_async (:obj:`bool`): Determines whether the callback will run asynchronously.

    """

    __slots__ = ('type', 'strict')

    def __init__(
        self,
        type: Type[UT],  # pylint: disable=W0622
        callback: Callable[[UT, CCT], RT],
        strict: bool = False,
        pass_update_queue: bool = False,
        pass_job_queue: bool = False,
        block: Union[bool, DefaultValue] = DEFAULT_FALSE,
    ):
        super().__init__(
            callback,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            block=block,
        )
        self.type = type  # pylint: disable=E0237
        self.strict = strict  # pylint: disable=E0237

    def check_update(self, update: object) -> bool:
        """Determines whether an update should be passed to this handlers :attr:`callback`.

        Args:
            update (:obj:`object`): Incoming update.

        Returns:
            :obj:`bool`

        """
        if not self.strict:
            return isinstance(update, self.type)
        return type(update) is self.type  # pylint: disable=C0123
