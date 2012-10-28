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

from exceptions import SessionException
from session import Session

from constants import VM_TYPE_HOST
from constants import VM_TYPE_TEMPLATE


class VM(object):
    def __init__(self, session=None):
        self._session = session

    def list(self, types=VM_TYPE_HOST | VM_TYPE_TEMPLATE):
        if self._session is None:
            raise SessionException('Session not Initialized')
        result = self._session.connection.proxy.VM.get_all(self.
                                                           _session.session_id)




