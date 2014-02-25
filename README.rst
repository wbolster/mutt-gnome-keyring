Mutt credentials in Gnome keyring
=================================

This is a helper script to make Mutt lookup passwords in Gnome keyring, instead
of having those unencrypted in ``~/.muttrc``. See the comments at the top of the
``mutt-gnome-keyring-password.py`` script for more information on how to use
this script.

To use this script, you will need to install the Python bindings for the
``gnome-keyring`` library. To install the relevant package on Debian and
Ubuntu::

    apt-get install python-gnomekeyring
