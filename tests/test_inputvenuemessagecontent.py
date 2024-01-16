import pytest

from telegram import InputVenueMessageContent, Location


@pytest.fixture(scope='class')
def input_venue_message_content():
    return InputVenueMessageContent(
        TestInputVenueMessageContent.latitude,
        TestInputVenueMessageContent.longitude,
        TestInputVenueMessageContent.title,
        TestInputVenueMessageContent.address,
        foursquare_id=TestInputVenueMessageContent.foursquare_id,
        foursquare_type=TestInputVenueMessageContent.foursquare_type,
        google_place_id=TestInputVenueMessageContent.google_place_id,
        google_place_type=TestInputVenueMessageContent.google_place_type,
    )


class TestInputVenueMessageContent:
    latitude = 1.0
    longitude = 2.0
    title = 'title'
    address = 'address'
    foursquare_id = 'foursquare id'
    foursquare_type = 'foursquare type'
    google_place_id = 'google place id'
    google_place_type = 'google place type'

    def test_slot_behaviour(self, input_venue_message_content, recwarn, mro_slots):
        inst = input_venue_message_content
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.title = 'should give warning', self.title
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_expected_values(self, input_venue_message_content):
        assert input_venue_message_content.longitude == self.longitude
        assert input_venue_message_content.latitude == self.latitude
        assert input_venue_message_content.title == self.title
        assert input_venue_message_content.address == self.address
        assert input_venue_message_content.foursquare_id == self.foursquare_id
        assert input_venue_message_content.foursquare_type == self.foursquare_type
        assert input_venue_message_content.google_place_id == self.google_place_id
        assert input_venue_message_content.google_place_type == self.google_place_type

    def test_to_dict(self, input_venue_message_content):
        input_venue_message_content_dict = input_venue_message_content.to_dict()

        assert isinstance(input_venue_message_content_dict, dict)
        assert input_venue_message_content_dict['latitude'] == input_venue_message_content.latitude
        assert (
            input_venue_message_content_dict['longitude'] == input_venue_message_content.longitude
        )
        assert input_venue_message_content_dict['title'] == input_venue_message_content.title
        assert input_venue_message_content_dict['address'] == input_venue_message_content.address
        assert (
            input_venue_message_content_dict['foursquare_id']
            == input_venue_message_content.foursquare_id
        )
        assert (
            input_venue_message_content_dict['foursquare_type']
            == input_venue_message_content.foursquare_type
        )
        assert (
            input_venue_message_content_dict['google_place_id']
            == input_venue_message_content.google_place_id
        )
        assert (
            input_venue_message_content_dict['google_place_type']
            == input_venue_message_content.google_place_type
        )

    def test_equality(self):
        a = InputVenueMessageContent(123, 456, 'title', 'address')
        b = InputVenueMessageContent(123, 456, 'title', '')
        c = InputVenueMessageContent(123, 456, 'title', 'address', foursquare_id=123)
        d = InputVenueMessageContent(456, 123, 'title', 'address', foursquare_id=123)
        e = Location(123, 456)

        assert a == b
        assert hash(a) == hash(b)

        assert a == c
        assert hash(a) == hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)
