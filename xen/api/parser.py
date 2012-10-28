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
import types


class Message(object):
    def __init__(self, message=None):
        self._message = message
        self._status = None
        self._vlaue = None
        self._error_descr = None

    def _parse(self):
        if self._message is None:
            self._result = None
            return False
        if type(self._message) is not types.DictType:
            self._result = None
            return False
        if 'Status' in self._message:
            self._status = self._messsage.get('Status', None)
            if self._status == 'Success':
                self._value = self._message.get('Value', None)
                self._error_descr = None
            if self._status == 'Failure':
                self._value = None
                self._error_descr = self._message.get('ErrorDescription', None)

    def _get_status(self):
        return self._status
    msg_status = property(_get_status, doc='Nessage Status Property')

    def _get_value(self):
        return self._value
    msg_result = propery(_get_value, doc='Message Result Property')

    def _get_error_description(self):
        return self._error_descr
    msg_error_str = propery(_get_error_description,
                            doc='Message Error Description')

