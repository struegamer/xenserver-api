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
    from exceptions import ConnectionException
    from exceptions import AuthenticationException
    from connection import Connection
    from properties import Properties
    from parser import Message
except ImportError, e:
    print('ImportError occured')
    print(e)
    sys.exit(1)


class Session(Properties):

    @staticmethod
    def logout(session=None, slave=False):
        """
        Type:
            Method
            
        Scope:
            Public
        
        Description:
            | When slave is False logout  from a Xen Server/Pool Master
            | When slave is True logout from a slave Xen Server
            
        Parameters:
            session: :py:class:`xen.api.session.Session`
            slave: bool
            
        Returns:
            bool
        """
        try:
            if slave is False:
                session._call('logout', session.session_id)
            else:
                session._call('local_logout', session.slave_session_id)
        except Exception, e:
            print(e)
            return False
        session.authenticated = False
        return True

    @classmethod
    def login(cls, connection, username, password, slave=False):
        """
        Type:
            Method
            
        Scope:
            Public
            
        Description:
            | Tries to login to a XenServer Hypervisor
            | When slave is False, it will connect to the master server
            | When slave is True, it needs a connection to the slave xenserver
            | and this slave needs to be set in ememergency mode
            
        Parameters:
            connection: :py:class:`xen.api.connection.Connection`
            username: str
            password: str
            slave: bool
            
        Returns: 
            :py:class:`xen.api.session.Session`
            
        Raises:
            ConnectionException: when connection is not initialized
        """
        if connection is None:
            raise ConnectionException('Your connection is not initialized!')
        session_obj = Session(connection)
        try:
            if slave is False:
                result = session_obj._call('login_with_password', username,
                                    password,
                                    __API_VERSION__)
                session_obj.session_id = result
                session_obj.authenticated = True
            else:
                result = session_obj._call('slave_local_login_with_password',
                                  username, password)
                session_obj.session_id = result
                session_obj.authenticated = True
            return session_obj
        except Exception, e:
            print(e)
            return None
        return None


    #
    # Private Methods
    #
    def _call(self, method, *args, **kwargs):
        result = self._conn.call('{0}.{1}'.format('session', method), *args,
                                 **kwargs)
        if result.status == MSG_STATUS_SUCCESS:
            return result.result
        if result.status == MSG_STATUS_FAILURE:
            raise Exception('{0}'.format(result.error_no))
        raise Exception('Not Authenticated')

    #
    # Public Properties
    #
    @property
    def authenticated(self):
        return self._authenticated

    @authenticated.setter
    def authenticated(self, value):
        self._authenticated = value

    @property
    def session_id(self):
        """
        Type:
            Property
            
        Description:
            Session Identifier
        
        Returns:
            str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    @property
    def uuid(self):
        """
        Type:
            Property
            
        Description:
            Unique identifier/object reference
        
        Returns:
            str or None
        """
        return self._call('get_uuid', self._session_id,
                                   self._session_id)

    @property
    def this_host(self):
        """
        Type:
            Property
        
        Description:
            Currently connected host
        
        Returns:
            Host Reference or None
        """
        return self._call('get_this_host', self._session_id, self._session_id)

    @property
    def this_user(self):
        """
        Type:
            Property
        
        Description:
            Currently connected user
        
        Returns:
            User Reference or None
        """
        return self._call('get_this_user', self._session_id, self._session_id)

    @property
    def last_active(self):
        """
        Type:
            Property
            
        Description:
            Timestamp for last time session was active
        
        Returns:
            datetime or None
            
        """
        return self._call('get_last_active', self._session_id, self._session_id)

    @property
    def pool(self):
        """
        Type:
            Property
        
        Description:
            | True if this session relates to a 
            | intrapool login, False otherwise
    
        Returns:
            bool or None
        """
        return self._call('get_pool', self._session_id, self._session_id)

    @property
    def other_config(self):
        """
        Type:
            Property
            
        Description:
            additional configuration
            
        Returns: 
            dict or None
        """
        return self._call('get_other_config', self._session_id, self._session_id)

    @other_config.setter
    def other_config(self, value={}):
        self._call('set_other_config', self._session_id, value)


    @property
    def is_local_superuser(self):
        """
        Type:
            Property
            
        Description:
            True if this session was created using local superuser credentials
        
        Returns: 
            bool or None
        
        """
        return self._call('get_is_local_superuser', self._session_id,
                          self._session_id)

    @property
    def subject(self):
        """
        Type:
            Property
            
        Description:
            | References the subject instance that
            | created the session. If a session in-
            | stance has is local superuser set, then
            | the value of this field is undefined.
            
        Returns:
            Referece to Subject or None
            
        """
        return self._call('get_subject', self._session_id, self._session_id)

    @property
    def validation_time(self):
        """
        Type:
            Property
        
        Description:
            time when session was last validated
            
        Returns:
            datetime or None
        """
        return self._call('get_validation_time', self._session_id,
                          self._session_id)

    @property
    def auth_user_sid(self):
        """
        Type:
            Property
            
        Description:
            | The subject identifier of the user
            | that was externally authenticated.
            | If a session instance has is local superuser set, then the value
            | of this field is undefined.
                    
        Returns:
            str or None
            
        """
        return self._call('get_auth_user_sid', self._session_id,
                          self._session_id)

    @property
    def auth_user_name(self):
        """
        Type:
            Property
            
        Description:
            | The subject name of the user that was externally authenticated. 
            | If a session instance has is local superuser set, then the value 
            | of this field is undefined.
            
        Returns:
            str or None
        """
        return self._call('get_auth_user_name', self._session_id,
                          self._session_id)

    @property
    def rbac_permissions(self):
        """
        Type:
            Property
        
        Description:
            list with all RBAC permissions for this session
        
        Returns:
            list of str or None
        """
        return self._call('get_rbac_permissions', self._session_id,
                          self._session_id)

    @property
    def tasks(self):
        """
        Type:
            Property
            
        Description:
            list of tasks created using the current session
        
        Returns:
            list of Task References or None
        """
        return self._call('get_tasks', self._session_id, self._session_id)

    @property
    def parent(self):
        """
        Type:
            Property
            
        Description:
            references the parent session that created this session
            
        Returns:
            Reference to a Session, or None
        """
        return self._call('get_parent', self._session_id, self._session_id)


    #
    # Public Methods
    #
    def change_password(self, old_password, new_password):
        """
        Type:
            Method
        
        Scope:
            Public
            
        Description:
            Change password for the actual user sesssion.
            
        Parameters:
            old_password: str
            new_password: str
        
        Returns:
            Void
        """
        self._call('change_password', old_password, new_password)
