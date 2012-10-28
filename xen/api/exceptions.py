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


class ConnectionException(Exception):
    """Connection Excpetion
    
    Will be thrown when a Connection object is normally not 
    initialized or None
    """
    pass


class SessionException(Exception):
    pass


class AuthenticationException(Exception):
    def __init__(self, error_arr):
        self._error = error_arr
        self.error_no = self._error[0]
        self.error_msg = self._error[2]
        self.error_user = self._error[1]

    def __str__(self):
        return 'Error: {0} => {1} ({2})'.format(self._error[0], self._error[2],
                                              self._error[1])
