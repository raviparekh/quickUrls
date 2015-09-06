from django.utils import unittest
import quickUrls.config as CONFIG
import os


class TestConfig(unittest.TestCase):

    def setUp(self):
        os.environ.update({"QUICKURL_ENV": "test"})

    def tearDown(self):
        os.environ.pop("QUICKURL_ENV", None)

    def test_active_config_should_be_correct_when_env_is_set(self):
        reload(CONFIG)
        self.assertEqual("TEST", CONFIG.APP_CONFIG.config_name)

    def test_active_config_default_to_dev(self):
        os.environ.pop("QUICKURL_ENV")
        reload(CONFIG)
        self.assertEqual("DEVELOPMENT", CONFIG.APP_CONFIG.config_name)



