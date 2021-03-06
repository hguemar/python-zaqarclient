# Copyright (c) 2014 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from zaqarclient.queues.v1 import core


class Flavor(object):

    def __init__(self, client, name,
                 pool, auto_create=True, **capabilities):
        self.client = client

        self.name = name
        self.pool = pool
        self.capabilities = capabilities

        if auto_create:
            self.ensure_exists()

    def ensure_exists(self):
        """Ensures pool exists

        This method is not race safe,
        the pool could've been deleted
        right after it was called.
        """
        req, trans = self.client._request_and_transport()

        data = {'pool': self.pool,
                'capabilities': self.capabilities}

        core.flavor_create(trans, req, self.name, data)

    def delete(self):
        req, trans = self.client._request_and_transport()
        core.flavor_delete(trans, req, self.name)
