"""
    BOAVIZTAPI - DEMO

    # 🎯 Retrieving the impacts of digital elements This is a quick demo, to see full documentation [click here](http://api.boavizta.org)  ## ➡️Server router  ### Server routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |          | |   PE   |        X       |          | ## ➡️Cloud router  ### Cloud routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |     X    | |   ADP  |        X       |          | |   PE   |        X       |          | ## ➡️Component router  ### Component routers support the following impacts:  | Impact | 🔨 Manufacture | 🔌 Usage | |--------|----------------|----------| |   GWP  |        X       |          | |   ADP  |        X       |          | |   PE   |        X       |          |   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.configuration_server import ConfigurationServer
from openapi_client.model.model_server import ModelServer
from openapi_client.model.usage_server import UsageServer
globals()['ConfigurationServer'] = ConfigurationServer
globals()['ModelServer'] = ModelServer
globals()['UsageServer'] = UsageServer
from openapi_client.model.server_dto import ServerDTO


class TestServerDTO(unittest.TestCase):
    """ServerDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServerDTO(self):
        """Test ServerDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServerDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()