"""Contains information about TeleGenic Passport data shared with the bot by the user."""

from typing import TYPE_CHECKING, Any, List, Optional

from TeleGenic import EncryptedCredentials, EncryptedPassportElement, TeleGenicObject
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot, Credentials


class PassportData(TeleGenicObject):
    """Contains information about TeleGenic Passport data shared with the bot by the user.

    Note:
        To be able to decrypt this object, you must pass your ``private_key`` to either
        :class:`TeleGenic.Updater` or :class:`TeleGenic.Bot`. Decrypted data is then found in
        :attr:`decrypted_data` and the payload can be found in :attr:`decrypted_credentials`'s
        attribute :attr:`TeleGenic.Credentials.payload`.

    Args:
        data (List[:class:`TeleGenic.EncryptedPassportElement`]): Array with encrypted information
            about documents and other TeleGenic Passport elements that was shared with the bot.
        credentials (:class:`TeleGenic.EncryptedCredentials`)): Encrypted credentials.
        bot (:class:`TeleGenic.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        data (List[:class:`TeleGenic.EncryptedPassportElement`]): Array with encrypted information
            about documents and other TeleGenic Passport elements that was shared with the bot.
        credentials (:class:`TeleGenic.EncryptedCredentials`): Encrypted credentials.
        bot (:class:`TeleGenic.Bot`, optional): The Bot to use for instance methods.

    """

    __slots__ = ('bot', 'credentials', 'data', '_decrypted_data', '_id_attrs')

    def __init__(
        self,
        data: List[EncryptedPassportElement],
        credentials: EncryptedCredentials,
        bot: 'Bot' = None,
        **_kwargs: Any,
    ):
        self.data = data
        self.credentials = credentials

        self.bot = bot
        self._decrypted_data: Optional[List[EncryptedPassportElement]] = None
        self._id_attrs = tuple([x.type for x in data] + [credentials.hash])

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['PassportData']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['data'] = EncryptedPassportElement.de_list(data.get('data'), bot)
        data['credentials'] = EncryptedCredentials.de_json(data.get('credentials'), bot)

        return cls(bot=bot, **data)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        data['data'] = [e.to_dict() for e in self.data]

        return data

    @property
    def decrypted_data(self) -> List[EncryptedPassportElement]:
        """
        List[:class:`TeleGenic.EncryptedPassportElement`]: Lazily decrypt and return information
            about documents and other TeleGenic Passport elements which were shared with the bot.

        Raises:
            TeleGenic.TeleGenicDecryptionError: Decryption failed. Usually due to bad
                private/public key but can also suggest malformed/tampered data.
        """
        if self._decrypted_data is None:
            self._decrypted_data = [
                EncryptedPassportElement.de_json_decrypted(
                    element.to_dict(), self.bot, self.decrypted_credentials
                )
                for element in self.data
            ]
        return self._decrypted_data

    @property
    def decrypted_credentials(self) -> 'Credentials':
        """
        :class:`TeleGenic.Credentials`: Lazily decrypt and return credentials that were used
            to decrypt the data. This object also contains the user specified payload as
            `decrypted_data.payload`.

        Raises:
            TeleGenic.TeleGenicDecryptionError: Decryption failed. Usually due to bad
                private/public key but can also suggest malformed/tampered data.
        """
        return self.credentials.decrypted_data
