#!/usr/bin/env python
#
# Use the IMAP password stored in Gnome Keyring in Mutt
#
# Wouter Bolsterlee <wbolster@gnome.org>, 2010
#
# This helper script writes out a Mutt config line with your IMAP server
# password stored in Gnome keyring (e.g. as saved by Evolution). The output is
# empty if the password was not available. In this case you will be prompted
# for your password by Mutt instead.
#
# Reference this script in your muttrc like this:
#
#   set folder = imaps://your.imap.server/
#   set imap_user = "yourusername"
#   source "~/bin/mutt-gnome-keyring-password.py yourusername your.imap.server imap"|
#
# Note the trailing | character in the last line!
#
# This script was inspired by a similar hack for offlineimap by Ross Burton:
# http://burtonini.com/blog/computers/offlineimap-2008-11-04-20-00
#

import sys
import gobject
import gnomekeyring


try:
    user, server, protocol = sys.argv[1:]
except ValueError as e:
    print 'Error parsing arguments: %s' % (e,)
    print 'Usage: %s USERNAME SERVERNAME PROTOCOL' % (sys.argv[0],)
    sys.exit(1)

gobject.set_application_name('Mutt')

try:
    q = dict(user=user, server=server, protocol=protocol)
    keys = gnomekeyring.find_network_password_sync(**q)
    password = keys[0]["password"].replace('"', r'\"')
    print 'set imap_pass = "%s"' % (password,)
except (gnomekeyring.NoMatchError, gnomekeyring.IOError), e:
    pass
