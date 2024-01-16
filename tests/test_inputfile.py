import logging
import os
import subprocess
import sys
from io import BytesIO

from TeleGenic import InputFile


class TestInputFile:
    png = os.path.join('tests', 'data', 'game.png')

    def test_slot_behaviour(self, recwarn, mro_slots):
        inst = InputFile(BytesIO(b'blah'), filename='tg.jpg')
        for attr in inst.__slots__:
            assert getattr(inst, attr, 'err') != 'err', f"got extra slot '{attr}'"
        assert not inst.__dict__, f"got missing slot(s): {inst.__dict__}"
        assert len(mro_slots(inst)) == len(set(mro_slots(inst))), "duplicate slot"
        inst.custom, inst.filename = 'should give warning', inst.filename
        assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list

    def test_subprocess_pipe(self):
        if sys.platform == 'win32':
            cmd = ['type', self.png]
        else:
            cmd = ['cat', self.png]

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=(sys.platform == 'win32'))
        in_file = InputFile(proc.stdout)

        assert in_file.input_file_content == open(self.png, 'rb').read()
        assert in_file.mimetype == 'image/png'
        assert in_file.filename == 'image.png'

        try:
            proc.kill()
        except ProcessLookupError:
            # This exception may be thrown if the process has finished before we had the chance
            # to kill it.
            pass

    def test_mimetypes(self, caplog):
        # Only test a few to make sure logic works okay
        assert InputFile(open('tests/data/TeleGenic.jpg', 'rb')).mimetype == 'image/jpeg'
        assert InputFile(open('tests/data/TeleGenic.webp', 'rb')).mimetype == 'image/webp'
        assert InputFile(open('tests/data/TeleGenic.mp3', 'rb')).mimetype == 'audio/mpeg'

        # Test guess from file
        assert InputFile(BytesIO(b'blah'), filename='tg.jpg').mimetype == 'image/jpeg'
        assert InputFile(BytesIO(b'blah'), filename='tg.mp3').mimetype == 'audio/mpeg'

        # Test fallback
        assert (
            InputFile(BytesIO(b'blah'), filename='tg.notaproperext').mimetype
            == 'application/octet-stream'
        )
        assert InputFile(BytesIO(b'blah')).mimetype == 'application/octet-stream'

        # Test string file
        with caplog.at_level(logging.DEBUG):
            assert InputFile(open('tests/data/text_file.txt')).mimetype == 'text/plain'

            assert len(caplog.records) == 1
            assert caplog.records[0].getMessage().startswith('Could not parse file content')

    def test_filenames(self):
        assert InputFile(open('tests/data/TeleGenic.jpg', 'rb')).filename == 'TeleGenic.jpg'
        assert InputFile(open('tests/data/TeleGenic.jpg', 'rb'), filename='blah').filename == 'blah'
        assert (
            InputFile(open('tests/data/TeleGenic.jpg', 'rb'), filename='blah.jpg').filename
            == 'blah.jpg'
        )
        assert InputFile(open('tests/data/TeleGenic', 'rb')).filename == 'TeleGenic'
        assert InputFile(open('tests/data/TeleGenic', 'rb'), filename='blah').filename == 'blah'
        assert (
            InputFile(open('tests/data/TeleGenic', 'rb'), filename='blah.jpg').filename
            == 'blah.jpg'
        )

        class MockedFileobject:
            # A open(?, 'rb') without a .name
            def __init__(self, f):
                self.f = open(f, 'rb')

            def read(self):
                return self.f.read()

        assert InputFile(MockedFileobject('tests/data/TeleGenic.jpg')).filename == 'image.jpeg'
        assert (
            InputFile(MockedFileobject('tests/data/TeleGenic.jpg'), filename='blah').filename
            == 'blah'
        )
        assert (
            InputFile(MockedFileobject('tests/data/TeleGenic.jpg'), filename='blah.jpg').filename
            == 'blah.jpg'
        )
        assert (
            InputFile(MockedFileobject('tests/data/TeleGenic')).filename
            == 'application.octet-stream'
        )
        assert (
            InputFile(MockedFileobject('tests/data/TeleGenic'), filename='blah').filename == 'blah'
        )
        assert (
            InputFile(MockedFileobject('tests/data/TeleGenic'), filename='blah.jpg').filename
            == 'blah.jpg'
        )

    def test_send_bytes(self, bot, chat_id):
        # We test this here and not at the respective test modules because it's not worth
        # duplicating the test for the different methods
        with open('tests/data/text_file.txt', 'rb') as file:
            message = bot.send_document(chat_id, file.read())

        out = BytesIO()
        assert message.document.get_file().download(out=out)
        out.seek(0)
        assert out.read().decode('utf-8') == 'PTB Rocks!'
