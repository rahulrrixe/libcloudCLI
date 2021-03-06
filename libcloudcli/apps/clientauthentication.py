#
"""Manage access to the clients, including authentication"""

import logging
import sys

LOG = logging.getLogger(__name__)

# important
# For libcloud caching is not necessary
class ClientCache(object):
    """ Descripter class for caching created client"""
    def __init__(self, factory):
        self.factory = factory
        self._handle = None

    def __get__(self, instance, owner):
        # Tell the ClientManager to login to keystone
        if self._handle is None:
            self._handle = self.factory(instance)
        return self._handle

# Write code for the authentication for each provider using the libcloud identity api
