# Copyright (c) 2013 Red Hat, Inc.
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

import mock

from marconiclient.queues.v1 import core
from marconiclient.tests import base
from marconiclient.tests.transport import dummy
import marconiclient.transport.errors as errors
from marconiclient.transport import request
from marconiclient.transport import response


class TestV1Core(base.TestBase):

    def setUp(self):
        super(TestV1Core, self).setUp()
        self.transport = dummy.DummyTransport(self.conf)

    def test_queue_create(self):
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:
            send_method.return_value = None

            req = request.Request()
            core.queue_create(self.transport, req, 'test')
            self.assertIn('queue_name', req.params)

    def test_queue_delete(self):
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:
            send_method.return_value = None

            req = request.Request()
            core.queue_delete(self.transport, req, 'test')
            self.assertIn('queue_name', req.params)

    def test_queue_exists(self):
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:
            send_method.return_value = None

            req = request.Request()
            ret = core.queue_exists(self.transport, req, 'test')
            self.assertIn('queue_name', req.params)
            self.assertTrue(ret)

    def test_queue_exists_not_found(self):
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:

            send_method.side_effect = errors.ResourceNotFound

            req = request.Request()
            ret = core.queue_exists(self.transport, req, 'test')
            self.assertIn('queue_name', req.params)
            self.assertFalse(ret)

    def test_get_queue_metadata(self):
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:
            resp = response.Response(None, '{}')
            send_method.return_value = resp

            req = request.Request()
            core.queue_get_metadata(self.transport, req, 'test')

    def test_set_queue_metadata(self):
        update_data = {'some': 'data'}
        with mock.patch.object(self.transport, 'send',
                               autospec=True) as send_method:
            send_method.return_value = None

            req = request.Request()
            core.queue_exists(self.transport, req, update_data, 'test')
            self.assertIn('queue_name', req.params)

        self.assertIn('queue_name', req.params)