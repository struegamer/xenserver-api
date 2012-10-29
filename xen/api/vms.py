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
from properties import Properties

from constants import VM_TYPE_HOST
from constants import VM_TYPE_TEMPLATE


class VM(Properties):
    def __init__(self, connection=None, session=None):
        super(VM, self).__init__(connection)
        self._session = session

    #
    # Public Properties
    #
    @property
    def uuid(self):
        return self._call('get_uuid', self._session.session_id, self._vmref)

    @property
    def allowed_operations(self):
        pass

    @property
    def current_operations(self):
        pass

    @property
    def power_state(self):
        pass

    @property
    def name_label(self):
        pass

    @name_label.setter
    def name_label(self, value):
        pass

    @property
    def name_description(self):
        pass

    @name_description.setter
    def name_description(self, value):
        pass

    @property
    def user_version(self):
        pass

    @user_version.setter
    def user_version(self, value):
        pass

    @property
    def is_a_template(self):
        pass

    @is_a_template.setter
    def is_a_template(self, value):
        pass

    @property
    def suspend_VDI(self):
        pass

    @property
    def resident_on(self):
        pass

    @property
    def scheduled_to_be_resident_on(self):
        pass

    @property
    def affinity(self):
        pass

    @affinity.setter
    def affinitt(self, value):
        pass

    @property
    def memory_overhead(self):
        pass

    @property
    def memory_target(self):
        pass

    @property
    def memory_static_max(self):
        pass

    @property
    def memory_dynamic_max(self):
        pass

    @property
    def memory_dynamic_min(self):
        pass

    @property
    def memory_static_min(self):
        pass

    @property
    def VCPUs_params(self):
        pass

    @VCPUs_params.setter
    def VCPUs_params(self, value):
        pass

    @property
    def VCPUs_max(self):
        pass

    @property
    def VCPUs_at_startup(self):
        pass


    #
    # Private Methods
    #
    def _call(self, method, *args, **kwargs):
        result = self._conn.call('{0}.{1}'.format('VM', method), *args,
                                 **kwargs)
        if result.status == MSG_STATUS_SUCCESS:
            return result.result
        if result.status == MSG_STATUS_FAILURE:
            raise Exception('{0}'.format(result.error_no))
        raise Exception('Not Authenticated')

    @staticmethod
    def list(session=None, types=VM_TYPE_HOST | VM_TYPE_TEMPLATE,
             started=False):
        if session is None:
            raise SessionException('Session not Initialized')
        if session.authenticated:
            vmlist = session._call('get_all', session.session_id)
            for vm in vmlist:
                pass




