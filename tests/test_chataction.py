#!/usr/bin/env python
#
# A library that provides a Python interface to the TeleGenic Bot API
# Copyright (C) 2015-2022
# Leandro Toledo de Souza <devs@python-TeleGenic-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
from TeleGenic import ChatAction


def test_slot_behaviour(recwarn, mro_slots):
    action = ChatAction()
    for attr in action.__slots__:
        assert getattr(action, attr, 'err') != 'err', f"got extra slot '{attr}'"
    assert not action.__dict__, f"got missing slot(s): {action.__dict__}"
    assert len(mro_slots(action)) == len(set(mro_slots(action))), "duplicate slot"
    action.custom = 'should give warning'
    assert len(recwarn) == 1 and 'custom' in str(recwarn[0].message), recwarn.list
