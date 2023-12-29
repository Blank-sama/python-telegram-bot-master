<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


![telegenic](https://te.legra.ph/file/70e5b4f5a754c1439d42f.jpg)

=================
Table of contents
=================

- Introduction_

- Telegram API support_

- Installing_

- Getting started_

  #. Learning by example_

  #. Logging_

  #. Documentation_

- Getting help_

- Contributing_

- License_

============
Introduction
============

This library provides a pure Python interface for the
Telegram Bot API <https://core.telegram.org/bots/api>_.
It's compatible with Python versions 3.6.8+. PTB might also work on PyPy <http://pypy.org/>_, though there have been a lot of issues before. Hence, PyPy is not officially supported.

In addition to the pure API implementation, this library features a number of high-level classes to
make the development of bots easy and straightforward. These classes are contained in the
``telegram.ext`` submodule.

A pure API implementation *without* ``telegram.ext`` is available as the standalone package ``python-telegram-bot-raw``.  See here for details. <https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README_RAW.rst>_

----
Note
----

Installing both ``python-telegram-bot`` and ``python-telegram-bot-raw`` in conjunction will result in undesired side-effects, so only install *one* of both.

====================
Telegram API support
====================

All types and methods of the Telegram Bot API 5.6 are supported.

==========
Installing
==========

You can install or upgrade python-telegram-bot with:

.. code:: shell

    $ pip install python-telegram-bot --upgrade

Or you can install from source with:

.. code:: shell

    $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
    $ cd python-telegram-bot
    $ python setup.py install
    
In case you have a previously cloned local repository already, you should initialize the added urllib3 submodule before installing with:

.. code:: shell

    $ git submodule update --init --recursive

---------------------
Optional Dependencies
---------------------

PTB can be installed with optional dependencies:

* ``pip install python-telegram-bot[passport]`` installs the cryptography <https://cryptography.io>_ library. Use this, if you want to use Telegram Passport related functionality.
* ``pip install python-telegram-bot[ujson]`` installs the ujson <https://pypi.org/project/ujson/>_ library. It will then be used for JSON de- & encoding, which can bring speed up compared to the standard json <https://docs.python.org/3/library/json.html>_ library.
* ``pip install python-telegram-bot[socks]`` installs the PySocks <https://pypi.org/project/PySocks/>_ library. Use this, if you want to work behind a Socks5 server.

===============
Getting started
===============

Our Wiki contains a lot of resources to get you started with ``python-telegram-bot``:

- Introduction to the API <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API>_
- Tutorial: Your first Bot <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot>_

Other references:

- Telegram API documentation <https://core.telegram.org/bots/api>_
- python-telegram-bot documentation <https://python-telegram-bot.readthedocs.io/>_

-------------------
Learning by example
-------------------

We believe that the best way to learn this package is by example. Here
are some examples for you to review. Even if it is not your approach for learning, please take a
look at ``echobot.py``, it is the de facto base for most of the bots out there. Best of all,
the code for these examples are released to the public domain, so you can start by grabbing the
code and building on top of it.

Visit this page <https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/README.md>_ to discover the official examples or look at the examples on the wiki <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Examples>_ to see other bots the community has built.

-------
Logging
-------

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


=============
Documentation
=============

``python-telegram-bot``'s documentation lives at readthedocs.io <https://python-telegram-bot.readthedocs.io/>_.

============
Getting help
============

You can get help in several ways:

1. We have a vibrant community of developers helping each other in our Telegram group <https://telegram.me/pythontelegrambotgroup>_. Join us!

2. Report bugs, request new features or ask questions by creating an issue <https://github.com/python-telegram-bot/python-telegram-bot/issues/new/choose>_ or a discussion <https://github.com/python-telegram-bot/python-telegram-bot/discussions/new>_.

3. Our Wiki pages <https://github.com/python-telegram-bot/python-telegram-bot/wiki/>_ offer a growing amount of resources.

4. You can even ask for help on Stack Overflow using the python-telegram-bot tag <https://stackoverflow.com/questions/tagged/python-telegram-bot>_.


𝗖𝗢𝗡𝗧𝗥𝗜𝗕𝗨𝗧𝗢𝗥𝗦 :- 

- [𝗔𝗔𝗥𝗨](https://t.me/Aaru_kun) 𝐗 <a href="https://github.com/Blank-sama" alt="Blank-sama"> <img src="https://img.shields.io/badge/Aaru-90302f?logo=github" /></a>
- [𝗟𝗘𝗩𝗜](https://t.me/LeviAckerman1709) 𝐗 <a href="https://github.com/Shauryanoobhai" alt="shauryanoobhai"> <img src="https://img.shields.io/badge/shaurya-90302f?logo=github" /></a>
- [𝗔𝗗𝗜𝗧𝗬𝗔](https://t.me/itzAditya_xD) 𝐗 <a href="https://github.com/ItzRexModZ" alt="ItzRexModZ"> <img src="https://img.shields.io/badge/Aditya-90302f?logo=github" /></a>