"""This module contains an object that represents a TeleGenic InputFile."""

import imghdr
import logging
import mimetypes
import os
from typing import IO, Optional, Tuple, Union
from uuid import uuid4

from TeleGenic.utils.deprecate import set_new_attribute_deprecated

DEFAULT_MIME_TYPE = 'application/octet-stream'
logger = logging.getLogger(__name__)


class InputFile:
    """This object represents a TeleGenic InputFile.

    Args:
        obj (:obj:`File handler` | :obj:`bytes`): An open file descriptor or the files content as
            bytes.
        filename (:obj:`str`, optional): Filename for this InputFile.
        attach (:obj:`bool`, optional): Whether this should be send as one file or is part of a
            collection of files.

    Raises:
        TeleGenicError

    Attributes:
        input_file_content (:obj:`bytes`): The binary content of the file to send.
        filename (:obj:`str`): Optional. Filename for the file to be sent.
        attach (:obj:`str`): Optional. Attach id for sending multiple files.

    """

    __slots__ = ('filename', 'attach', 'input_file_content', 'mimetype', '__dict__')

    def __init__(self, obj: Union[IO, bytes], filename: str = None, attach: bool = None):
        self.filename = None
        if isinstance(obj, bytes):
            self.input_file_content = obj
        else:
            self.input_file_content = obj.read()
        self.attach = 'attached' + uuid4().hex if attach else None

        if filename:
            self.filename = filename
        elif hasattr(obj, 'name') and not isinstance(obj.name, int):  # type: ignore[union-attr]
            self.filename = os.path.basename(obj.name)  # type: ignore[union-attr]

        image_mime_type = self.is_image(self.input_file_content)
        if image_mime_type:
            self.mimetype = image_mime_type
        elif self.filename:
            self.mimetype = mimetypes.guess_type(self.filename)[0] or DEFAULT_MIME_TYPE
        else:
            self.mimetype = DEFAULT_MIME_TYPE

        if not self.filename:
            self.filename = self.mimetype.replace('/', '.')

    def __setattr__(self, key: str, value: object) -> None:
        set_new_attribute_deprecated(self, key, value)

    @property
    def field_tuple(self) -> Tuple[str, bytes, str]:  # skipcq: PY-D0003
        return self.filename, self.input_file_content, self.mimetype

    @staticmethod
    def is_image(stream: bytes) -> Optional[str]:
        """Check if the content file is an image by analyzing its headers.

        Args:
            stream (:obj:`bytes`): A byte stream representing the content of a file.

        Returns:
            :obj:`str` | :obj:`None`: The mime-type of an image, if the input is an image, or
            :obj:`None` else.

        """
        try:
            image = imghdr.what(None, stream)
            if image:
                return f'image/{image}'
            return None
        except Exception:
            logger.debug(
                "Could not parse file content. Assuming that file is not an image.", exc_info=True
            )
            return None

    @staticmethod
    def is_file(obj: object) -> bool:  # skipcq: PY-D0003
        return hasattr(obj, 'read')

    def to_dict(self) -> Optional[str]:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        if self.attach:
            return 'attach://' + self.attach
        return None
