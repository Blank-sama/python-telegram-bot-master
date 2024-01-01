<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


image:: "https://te.legra.ph/file/70e5b4f5a754c1439d42f.jpg"

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
Table of contents
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

⋟ Introduction_

⋟ Telegram API support_

⋟ Installing_

⋟ Getting started_

  #. Learning by example_

  #. Logging_

  #. Documentation_

⋟ Getting help_

⋟ Contributing_

⋟ License_

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗜𝗡𝗧𝗥𝗢𝗗𝗨𝗖𝗧𝗜𝗢𝗡 
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

This library provides a pure Python interface for the
Telegram Bot API <https://core.telegram.org/bots/api>_.
It's compatible with Python versions 3.6.8+. PTB might also work on PyPy <http://pypy.org/>_, though there have been a lot of issues before. Hence, PyPy is not officially supported.

In addition to the pure API implementation, this library features a number of high-level classes to
make the development of bots easy and straightforward. These classes are contained in the
``telegram.ext`` submodule.

A pure API implementation *without* ``telegram.ext`` is available as the standalone package ``python-telegram-bot-raw``.  See here for details. <https://github.com/TeleGenic/TeleGenic/blob/master/README_RAW.rst>_

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗡𝗢𝗧𝗘 
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

Installing both ``TeleGenic`` and ``TeleGenic-raw`` in conjunction will result in undesired side-effects, so only install *one* of both.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗔𝗣𝗜 𝗦𝗨𝗣𝗣𝗢𝗥𝗧
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

All types and methods of the Telegram Bot API 5.6 are supported.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗜𝗡𝗚
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

You can install or upgrade TeleGenic with:

.. code:: shell

    $ pip install TeleGenic --upgrade

Or you can install from source with:

.. code:: shell

    $ git clone https://github.com/TeleGenic/TeleGenic--recursive
    $ cd python-telegram-bot
    $ python setup.py install
    
In case you have a previously cloned local repository already, you should initialize the added urllib3 submodule before installing with:

.. code:: shell

    $ git submodule update --init --recursive

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗢𝗣𝗧𝗜𝗢𝗡𝗔𝗟 𝗗𝗘𝗣𝗘𝗡𝗗𝗘𝗡𝗖𝗜𝗘𝗦
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

TeleGenic can be installed with optional dependencies:

* ``pip install TeleGenic[passport]`` installs the cryptography <https://cryptography.io>_ library. Use this, if you want to use Telegram Passport related functionality.
* ``pip install TeleGenic[ujson]`` installs the ujson <https://pypi.org/project/ujson/>_ library. It will then be used for JSON de- & encoding, which can bring speed up compared to the standard json <https://docs.python.org/3/library/json.html>_ library.
* ``pip install TeleGenic[socks]`` installs the PySocks <https://pypi.org/project/PySocks/>_ library. Use this, if you want to work behind a Socks5 server.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

Our Wiki contains a lot of resources to get you started with ``TeleGenic``:

⋟ 𝗜𝗡𝗧𝗥𝗢𝗗𝗨𝗖𝗧𝗜𝗢𝗡 𝗧𝗢 𝗧𝗛𝗘 𝗔𝗣𝗜 <https://github.com/TeleGenic/TeleGenic/wiki/Introduction-to-the-API>_
- Tutorial: Your first Bot <https://github.com/TeleGenic/TeleGenic/wiki/Extensions-%E2%80%93-Your-first-Bot>_

• 𝗢𝗧𝗛𝗘𝗥 𝗥𝗘𝗙𝗘𝗥𝗘𝗡𝗖𝗘𝗦 :- 

⋟ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗔𝗣𝗜 𝗗𝗢𝗖𝗨𝗠𝗘𝗡𝗧𝗔𝗧𝗜𝗢𝗡 <https://core.telegram.org/bots/api>_
⋟ 𝗧𝗘𝗟𝗘𝗚𝗘𝗡𝗜𝗖 𝗗𝗢𝗖𝗨𝗠𝗘𝗡𝗧𝗔𝗧𝗜𝗢𝗡 <https://TeleGenic.readthedocs.io/>_


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗟𝗘𝗔𝗥𝗡𝗜𝗡𝗚 𝗕𝗬 𝗘𝗫𝗔𝗠𝗣𝗟𝗘
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

We believe that the best way to learn this package is by example. Here
are some examples for you to review. Even if it is not your approach for learning, please take a
look at ``echobot.py``, it is the de facto base for most of the bots out there. Best of all,
the code for these examples are released to the public domain, so you can start by grabbing the
code and building on top of it.

• 𝗩𝗜𝗦𝗜𝗧 𝗧𝗛𝗜𝗦 𝗣𝗔𝗚𝗘 <https://github.com/TeleGenic/TeleGenic/blob/master/examples/README.md>_ to discover the official examples or look at the examples on the wiki <https://github.com/TeleGenic/TeleGenic/wiki/Examples>_ to see other bots the community has built.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗟𝗢𝗚𝗚𝗜𝗡𝗚
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

This library uses the ``logging`` module. To set up logging to standard output, put:
.. code:: python

    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

at the beginning of your script.

You can also use logs in your application by calling ``logging.getLogger()`` and setting the log level you want:

.. code:: python

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

If you want DEBUG logs instead:

.. code:: python

    logger.setLevel(logging.DEBUG)


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗗𝗢𝗖𝗨𝗠𝗘𝗡𝗧𝗔𝗧𝗜𝗢𝗡
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

``TeleGenic``'s documentation lives at readthedocs.io <https://TeleGenic.readthedocs.io/>_.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗛𝗘𝗟𝗣
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

• 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗚𝗘𝗧 𝗛𝗘𝗟𝗣 𝗜𝗡 𝗦𝗘𝗩𝗘𝗥𝗔𝗟 𝗪𝗔𝗬𝗦 :- 

1. We have a vibrant community of developers helping each other in our Telegram group <https://telegram.me/Devs_Union>_. Join us!

2. Report bugs, request new features or ask questions by creating an issue <https://github.com/TeleGenic/TeleGenic/issues/new/choose>_ or a discussion <https://github.com/TeleGenic/TeleGenic/discussions/new>_.

3. Our Wiki pages [Dev union](https://t.me/TheDevsUnion) offer a growing amount of resources.

4. You can even ask for help on Stack Overflow using the TeleGenic tag <https://stackoverflow.com/questions/tagged/TeleGenic>_.


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
⋟ 𝗟𝗜𝗖𝗘𝗡𝗦𝗘
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

You may copy, distribute and modify the software provided that modifications are described and licensed for free under LGPL-3 <https://www.gnu.org/licenses/lgpl-3.0.html>_. Derivatives works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don't have to be.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

𝗖𝗢𝗡𝗧𝗥𝗜𝗕𝗨𝗧𝗢𝗥𝗦 :- 

- [𝗔𝗔𝗥𝗨](https://t.me/Aaru_kun) 𝐗 <a href="https://github.com/Blank-sama" alt="Blank-sama"> <img src="https://img.shields.io/badge/Aaru-90302f?logo=github" /></a>
- [𝗟𝗘𝗩𝗜](https://t.me/LeviAckerman1709) 𝐗 <a href="https://github.com/Shauryanoobhai" alt="shauryanoobhai"> <img src="https://img.shields.io/badge/shaurya-90302f?logo=github" /></a>
- [𝗔𝗗𝗜𝗧𝗬𝗔](https://t.me/itzAditya_xD) 𝐗 <a href="https://github.com/ItzRexModZ" alt="ItzRexModZ"> <img src="https://img.shields.io/badge/Aditya-90302f?logo=github" /></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
