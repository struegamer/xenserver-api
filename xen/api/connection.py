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
import xmlrpclib

from exceptions import ConnectionException

class Connection(object):
    """Connection Object
    
    Subclass this, to provide special SSL Transport etc.
    """
    def __init__(self, xenserver_url=''):
        """Constructor
        
        :param xenserver_url: URL to a XenServer
        :type xenserver_url: str
        
        """
        self._xenserver_url = xenserver_url
        self._proxy = None

    def _create_proxy(self):
        if (self._xenserver_url is not None and self._xenserver_url != ''):
            try:
                self._proxy = xmlrpclib.ServerProxy(self._xenserver_url,
                                                    allow_none=True)
            except Exception, e:
                print('File: {0}'.format(__file__))
                print(e)
                raise ConnectionException('Connection Error')

    def _connect(self):
        if self._proxy is None:
            self._create_proxy()

    def _get_proxy(self):
        if self._proxy is None:
            self._connect()
        return self._proxy
    proxy = property(_get_proxy, doc='XenServer Connection')

