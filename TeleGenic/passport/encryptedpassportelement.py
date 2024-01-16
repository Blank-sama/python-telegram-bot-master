"""This module contains an object that represents a TeleGenic EncryptedPassportElement."""
from base64 import b64decode
from typing import TYPE_CHECKING, Any, List, Optional

from TeleGenic import (
    IdDocumentData,
    PassportFile,
    PersonalDetails,
    ResidentialAddress,
    TeleGenicObject,
)
from TeleGenic.passport.credentials import decrypt_json
from TeleGenic.utils.types import JSONDict

if TYPE_CHECKING:
    from TeleGenic import Bot, Credentials


class EncryptedPassportElement(TeleGenicObject):
    """
    Contains information about documents or other TeleGenic Passport elements shared with the bot
    by the user. The data has been automatically decrypted by python-TeleGenic-bot.

    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their :attr:`type`, :attr:`data`, :attr:`phone_number`, :attr:`email`,
    :attr:`files`, :attr:`front_side`, :attr:`reverse_side` and :attr:`selfie` are equal.

    Note:
        This object is decrypted only when originating from
        :obj:`TeleGenic.PassportData.decrypted_data`.

    Args:
        type (:obj:`str`): Element type. One of "personal_details", "passport", "driver_license",
            "identity_card", "internal_passport", "address", "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration", "temporary_registration", "phone_number",
            "email".
        data (:class:`TeleGenic.PersonalDetails` | :class:`TeleGenic.IdDocument` | \
            :class:`TeleGenic.ResidentialAddress` | :obj:`str`, optional):
            Decrypted or encrypted data, available for "personal_details", "passport",
            "driver_license", "identity_card", "identity_passport" and "address" types.
        phone_number (:obj:`str`, optional): User's verified phone number, available only for
            "phone_number" type.
        email (:obj:`str`, optional): User's verified email address, available only for "email"
            type.
        files (List[:class:`TeleGenic.PassportFile`], optional): Array of encrypted/decrypted files
            with documents provided by the user, available for "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration" and "temporary_registration" types.
        front_side (:class:`TeleGenic.PassportFile`, optional): Encrypted/decrypted file with the
            front side of the document, provided by the user. Available for "passport",
            "driver_license", "identity_card" and "internal_passport".
        reverse_side (:class:`TeleGenic.PassportFile`, optional): Encrypted/decrypted file with the
            reverse side of the document, provided by the user. Available for "driver_license" and
            "identity_card".
        selfie (:class:`TeleGenic.PassportFile`, optional): Encrypted/decrypted file with the
            selfie of the user holding a document, provided by the user; available for "passport",
            "driver_license", "identity_card" and "internal_passport".
        translation (List[:class:`TeleGenic.PassportFile`], optional): Array of encrypted/decrypted
            files with translated versions of documents provided by the user. Available if
            requested for "passport", "driver_license", "identity_card", "internal_passport",
            "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and
            "temporary_registration" types.
        hash (:obj:`str`): Base64-encoded element hash for using in
            :class:`TeleGenic.PassportElementErrorUnspecified`.
        bot (:class:`TeleGenic.Bot`, optional): The Bot to use for instance methods.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    Attributes:
        type (:obj:`str`): Element type. One of "personal_details", "passport", "driver_license",
            "identity_card", "internal_passport", "address", "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration", "temporary_registration", "phone_number",
            "email".
        data (:class:`TeleGenic.PersonalDetails` | :class:`TeleGenic.IdDocument` | \
            :class:`TeleGenic.ResidentialAddress` | :obj:`str`):
            Optional. Decrypted or encrypted data, available for "personal_details", "passport",
            "driver_license", "identity_card", "identity_passport" and "address" types.
        phone_number (:obj:`str`): Optional. User's verified phone number, available only for
            "phone_number" type.
        email (:obj:`str`): Optional. User's verified email address, available only for "email"
            type.
        files (List[:class:`TeleGenic.PassportFile`]): Optional. Array of encrypted/decrypted files
            with documents provided by the user, available for "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration" and "temporary_registration" types.
        front_side (:class:`TeleGenic.PassportFile`): Optional. Encrypted/decrypted file with the
            front side of the document, provided by the user. Available for "passport",
            "driver_license", "identity_card" and "internal_passport".
        reverse_side (:class:`TeleGenic.PassportFile`): Optional. Encrypted/decrypted file with the
            reverse side of the document, provided by the user. Available for "driver_license" and
            "identity_card".
        selfie (:class:`TeleGenic.PassportFile`): Optional. Encrypted/decrypted file with the
            selfie of the user holding a document, provided by the user; available for "passport",
            "driver_license", "identity_card" and "internal_passport".
        translation (List[:class:`TeleGenic.PassportFile`]): Optional. Array of encrypted/decrypted
            files with translated versions of documents provided by the user. Available if
            requested for "passport", "driver_license", "identity_card", "internal_passport",
            "utility_bill", "bank_statement", "rental_agreement", "passport_registration" and
            "temporary_registration" types.
        hash (:obj:`str`): Base64-encoded element hash for using in
            :class:`TeleGenic.PassportElementErrorUnspecified`.
        bot (:class:`TeleGenic.Bot`): Optional. The Bot to use for instance methods.

    """

    __slots__ = (
        'selfie',
        'files',
        'type',
        'translation',
        'email',
        'hash',
        'phone_number',
        'bot',
        'reverse_side',
        'front_side',
        'data',
        '_id_attrs',
    )

    def __init__(
        self,
        type: str,  # pylint: disable=W0622
        data: PersonalDetails = None,
        phone_number: str = None,
        email: str = None,
        files: List[PassportFile] = None,
        front_side: PassportFile = None,
        reverse_side: PassportFile = None,
        selfie: PassportFile = None,
        translation: List[PassportFile] = None,
        hash: str = None,  # pylint: disable=W0622
        bot: 'Bot' = None,
        credentials: 'Credentials' = None,  # pylint: disable=W0613
        **_kwargs: Any,
    ):
        # Required
        self.type = type
        # Optionals
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash

        self._id_attrs = (
            self.type,
            self.data,
            self.phone_number,
            self.email,
            self.files,
            self.front_side,
            self.reverse_side,
            self.selfie,
        )

        self.bot = bot

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['EncryptedPassportElement']:
        """See :meth:`TeleGenic.TeleGenicObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        data['files'] = PassportFile.de_list(data.get('files'), bot) or None
        data['front_side'] = PassportFile.de_json(data.get('front_side'), bot)
        data['reverse_side'] = PassportFile.de_json(data.get('reverse_side'), bot)
        data['selfie'] = PassportFile.de_json(data.get('selfie'), bot)
        data['translation'] = PassportFile.de_list(data.get('translation'), bot) or None

        return cls(bot=bot, **data)

    @classmethod
    def de_json_decrypted(
        cls, data: Optional[JSONDict], bot: 'Bot', credentials: 'Credentials'
    ) -> Optional['EncryptedPassportElement']:
        """Variant of :meth:`TeleGenic.TeleGenicObject.de_json` that also takes into account
        passport credentials.

        Args:
            data (Dict[:obj:`str`, ...]): The JSON data.
            bot (:class:`TeleGenic.Bot`): The bot associated with this object.
            credentials (:class:`TeleGenic.FileCredentials`): The credentials

        Returns:
            :class:`TeleGenic.EncryptedPassportElement`:

        """
        if not data:
            return None

        if data['type'] not in ('phone_number', 'email'):
            secure_data = getattr(credentials.secure_data, data['type'])

            if secure_data.data is not None:
                # If not already decrypted
                if not isinstance(data['data'], dict):
                    data['data'] = decrypt_json(
                        b64decode(secure_data.data.secret),
                        b64decode(secure_data.data.hash),
                        b64decode(data['data']),
                    )
                if data['type'] == 'personal_details':
                    data['data'] = PersonalDetails.de_json(data['data'], bot=bot)
                elif data['type'] in (
                    'passport',
                    'internal_passport',
                    'driver_license',
                    'identity_card',
                ):
                    data['data'] = IdDocumentData.de_json(data['data'], bot=bot)
                elif data['type'] == 'address':
                    data['data'] = ResidentialAddress.de_json(data['data'], bot=bot)

            data['files'] = (
                PassportFile.de_list_decrypted(data.get('files'), bot, secure_data.files) or None
            )
            data['front_side'] = PassportFile.de_json_decrypted(
                data.get('front_side'), bot, secure_data.front_side
            )
            data['reverse_side'] = PassportFile.de_json_decrypted(
                data.get('reverse_side'), bot, secure_data.reverse_side
            )
            data['selfie'] = PassportFile.de_json_decrypted(
                data.get('selfie'), bot, secure_data.selfie
            )
            data['translation'] = (
                PassportFile.de_list_decrypted(
                    data.get('translation'), bot, secure_data.translation
                )
                or None
            )

        return cls(bot=bot, **data)

    def to_dict(self) -> JSONDict:
        """See :meth:`TeleGenic.TeleGenicObject.to_dict`."""
        data = super().to_dict()

        if self.files:
            data['files'] = [p.to_dict() for p in self.files]
        if self.translation:
            data['translation'] = [p.to_dict() for p in self.translation]

        return data
