# -*- coding: utf-8 -*-
###############################################################################
# python-xen-api - XenServer XMLRPC API Library
# Copyright (C) 2012 Stephan Adig <sh@sourcecode.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
###############################################################################

import sys

from connection import Connection
from session import Session

class XenServer(object):
    def __init__(self, url, username, password):
        self._connection = Connection(url)
        self._username = username
        self._password = password
        self._session = None
        self._slave_session = None

    #
    # Public Properties
    #
    @property
    def session(self):
        return self._session

    @property
    def slave_session(self):
        return self._slave_session
    #
    # Public Methods
    #

    def login(self):
        self._session = Session.login(self._connection,
                                                self._username, self._password)
        print self._session
        return True
    def login_slave(self):
        self._slave_session = Session.login(self._connection,
                                                      self._username,
                                                      self._password, True)
        return True
    def logout(self):
        if Session.logout(self._session, False):
            self._session = None
            return True
        return False

    def logout_slave(self):
        if Session.logout(self._slave_session, True):
            self._slave_session = None
            return True
        return False

