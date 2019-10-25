#!/usr/bin/env python
"""
Kremepuff, Copyright (C) 2019, Ace Monster Toys 

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.  

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import atexit
import os
import sys

import escpos.escpos
import escpos.printer

p = escpos.printer.Serial('/dev/ttyUSB0')

from authbox.api import BaseDispatcher, GPIO
from authbox.config import Config
#from msauth.software.authbox.api import BaseDispatcher, GPIO
#from msauth.software.authbox.config import Config


class Dispatcher(BaseDispatcher):
  def __init__(self, config):
    super(Dispatcher, self).__init__(config)

    self.load_config_object('badge_reader', on_scan=self.badge_scan)

  def badge_scan(self, badge_id):
    p.qr("mailto:officers@acemonstertoys.org?subject=New%20Fob%20Activation&body=2A{:08X}".format(int(badge_id[1:-1], 2)))
    footer = 'Your fob ID is:\n'
    fob = '2A{:08X}'.format(int(badge_id[1:-1], 2))
    msg1 = """1) Set up your member account and pay your dues on the website
2) Send in your paperwork via Docusign
3) Send an email to\nofficers@acemonstertoys.org\nwith the subject line:\n"""
    email="New Fob Activation\n"
    msg2 = """Put the fob id below in the body of the email.  For your convenience, try using the QR code above.\n"""
    
    header = "THIS FOB IS NOT ACTIVE\nIT WILL OPEN NOTHING\n"
    p.set(text_type='BU', align='CENTER')
    p.text(header)
    p.set(text_type='NORMAL')
    p.text(msg1)
    p.set(text_type='B', align='CENTER')
    p.text(email)
    p.set(text_type='NORMAL')
    p.text(msg2)
    p.text(footer)
    p.set(text_type='B', align='CENTER')
    p.text(fob)
    p.set(text_type='NORMAL')
    p.cut()


def main(args):
  atexit.register(GPIO.cleanup)

  if not args:
    root = '~'
  else:
    root = args[0]

  config = Config(os.path.join('kremepuff.ini'))
  Dispatcher(config).run_loop()

if __name__ == '__main__':
  main(sys.argv[1:])
