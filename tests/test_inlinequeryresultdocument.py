import pytest

from telegram import (
    InlineKeyboardButton,
    InputTextMessageContent,
    InlineQueryResultDocument,
    InlineKeyboardMarkup,
    InlineQueryResultVoice,
    MessageEntity,
)


@pytest.fixture(scope='class')
def inline_query_result_document():
    return InlineQueryResultDocument(
        TestInlineQueryResultDocument.id_,
        TestInlineQueryResultDocument.document_url,
        TestInlineQueryResultDocument.title,
        TestInlineQueryResultDocument.mime_type,
        caption=TestInlineQueryResultDocument.caption,
        parse_mode=TestInlineQueryResultDocument.parse_mode,
        caption_entities=TestInlineQueryResultDocument.caption_entities,
        description=TestInlineQueryResultDocument.description,
        thumb_url=TestInlineQueryResultDocument.thumb_url,
        thumb_width=TestInlineQueryResultDocument.thumb_width,
        thumb_height=TestInlineQueryResultDocument.thumb_height,
        input_message_content=TestInlineQueryResultDocument.input_message_content,
        reply_markup=TestInlineQueryResultDocument.reply_markup,
    )


class TestInlineQueryResultDocument:
    id_ = 'id'
    type_ = 'document'
    document_url = 'document url'
    title = 'title'
    caption = 'caption'
    parse_mode = 'Markdown'
    caption_entities = [MessageEntity(MessageEntity.ITALIC, 0, 7)]
    mime_type = 'mime type'
    description = 'description'
    thumb_url = 'thumb url'
    thumb_width = 10
    thumb_height = 15
    input_message_content = InputTextMessageContent('input_message_content')
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('reply_markup')]])

    def test_slot_behaviour(self, inline_query_result_document, recwarn, mro_slots):
        inst = inline_query_result_document
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.id = 'should give warning', self.id_
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_expected_values(self, inline_query_result_document):
        assert inline_query_result_document.id == self.id_
        assert inline_query_result_document.type == self.type_
        assert inline_query_result_document.document_url == self.document_url
        assert inline_query_result_document.title == self.title
        assert inline_query_result_document.caption == self.caption
        assert inline_query_result_document.parse_mode == self.parse_mode
        assert inline_query_result_document.caption_entities == self.caption_entities
        assert inline_query_result_document.mime_type == self.mime_type
        assert inline_query_result_document.description == self.description
        assert inline_query_result_document.thumb_url == self.thumb_url
        assert inline_query_result_document.thumb_width == self.thumb_width
        assert inline_query_result_document.thumb_height == self.thumb_height
        assert (
            inline_query_result_document.input_message_content.to_dict()
            == self.input_message_content.to_dict()
        )
        assert inline_query_result_document.reply_markup.to_dict() == self.reply_markup.to_dict()

    def test_to_dict(self, inline_query_result_document):
        inline_query_result_document_dict = inline_query_result_document.to_dict()

        assert isinstance(inline_query_result_document_dict, dict)
        assert inline_query_result_document_dict['id'] == inline_query_result_document.id
        assert inline_query_result_document_dict['type'] == inline_query_result_document.type
        assert (
            inline_query_result_document_dict['document_url']
            == inline_query_result_document.document_url
        )
        assert inline_query_result_document_dict['title'] == inline_query_result_document.title
        assert inline_query_result_document_dict['caption'] == inline_query_result_document.caption
        assert (
            inline_query_result_document_dict['parse_mode']
            == inline_query_result_document.parse_mode
        )
        assert inline_query_result_document_dict['caption_entities'] == [
            ce.to_dict() for ce in inline_query_result_document.caption_entities
        ]
        assert (
            inline_query_result_document_dict['mime_type']
            == inline_query_result_document.mime_type
        )
        assert (
            inline_query_result_document_dict['description']
            == inline_query_result_document.description
        )
        assert (
            inline_query_result_document_dict['thumb_url']
            == inline_query_result_document.thumb_url
        )
        assert (
            inline_query_result_document_dict['thumb_width']
            == inline_query_result_document.thumb_width
        )
        assert (
            inline_query_result_document_dict['thumb_height']
            == inline_query_result_document.thumb_height
        )
        assert (
            inline_query_result_document_dict['input_message_content']
            == inline_query_result_document.input_message_content.to_dict()
        )
        assert (
            inline_query_result_document_dict['reply_markup']
            == inline_query_result_document.reply_markup.to_dict()
        )

    def test_equality(self):
        a = InlineQueryResultDocument(self.id_, self.document_url, self.title, self.mime_type)
        b = InlineQueryResultDocument(self.id_, self.document_url, self.title, self.mime_type)
        c = InlineQueryResultDocument(self.id_, '', self.title, self.mime_type)
        d = InlineQueryResultDocument('', self.document_url, self.title, self.mime_type)
        e = InlineQueryResultVoice(self.id_, '', '')

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a == c
        assert hash(a) == hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
