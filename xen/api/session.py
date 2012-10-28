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

try:
    from constants import __API_VERSION__
    from constants import MSG_STATUS_SUCCESS
    from constants import MSG_STATUS_FAILURE
    from exceptions import AuthenticationException
    from connection import Connection
    from connection import ConnectionException
    from parser import Message
except ImportError, e:
    print('ImportError occured')
    print(e)
    sys.exit(1)


class Session(object):
    def __init__(self, connection=None, username=None, password=None):
        self._conn = connection
        self._user = username
        self._password = password
        self._authenticated = False
        self._session_id = None

    def _get_auth(self):
        return self._authenticated
    authenticated = property(_get_auth, doc='Authentication Status Property')

    def _get_session_id(self):
        return self._session_id
    session_id = property(_get_session_id, doc='Session ID Property')

    def _get_connection(self):
        return self._conn
    connection = property(_get_connection, doc='Connection Property')

    @property
    def uuid(self):
        """UUID property
        
        :rtype: str or None
        """
        if self._authenticated:
            result = self._conn.proxy.session.get_uuid(self._session_id,
                                                       self._session_id)
            m = Message(result)
            if m.status == MSG_STATUS_SUCCESS:
                return m.result
        return None

    @property
    def this_host(self):
        """this_host property
        
        :rtype: Host Reference or None
        """
        if self._authenticated:
            result = self._conn.proxy.session.get_this_host(self._session_id,
                                                            self._session_id)
            m = Message(result)
            if m.status == MSG_STATUS_SUCCESS:
                return m.result
        return None

    @property
    def this_user(self):
        """this_user property
        
        :rtype: User Reference or None
        """
        if self._authenticated:
            result = self._conn.proxy.session.get_this_user(self._session_id,
                                                            self._session_id)
            m = Message(result)
            if m.status == MSG_STATUS_SUCCESS:
                return m.result
        return None

    def login(self):
        if self._conn is None:
            raise ConnectionException('Your connection is not initialized!')
        result = self._conn.proxy.session.login_with_password(self._user,
                                                              self._password,
                                                                __API_VERSION__)
        m = Message(result)
        if m.status == MSG_STATUS_SUCCESS:
            self._session_id = m._get_value()
            self._authenticated = True

        if m.status == MSG_STATUS_FAILURE:
            self._authenticated = False
            raise AuthenticationException(m._error_descr)

    def logout(self):
        if self._authenticated:
            self._conn.proxy.session.logout(self._session_id)
            self._authenticated = False


