import unittest2 as unittest

from zope.component import queryUtility
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from paypal.settings import PayPalConfig
from paypal.interface import PayPalInterface

from eastofeaton.paypal.interfaces import IPaypalAPIUtility
from eastofeaton.paypal.interfaces import IPaypalConfiguration
from eastofeaton.paypal.testing import\
    EASTOFEATON_PAYPAL_INTEGRATION_TESTING

_marker = object()

CONFIG = {'API_USERNAME': u'foo', 'API_PASSWORD': u'1234',
          'API_SIGNATURE': u'aBc123-czy', 'API_ENVIRONMENT': u'sandbox'}


class TestPaypalUtility(unittest.TestCase):

    layer = EASTOFEATON_PAYPAL_INTEGRATION_TESTING

    def setUp(self):
        # explicitly start each test with a clean slate
        self.clear_configuration()
        self.utility = queryUtility(IPaypalAPIUtility, default=_marker)

    def setup_configuration(self):
        registry = getUtility(IRegistry)
        config = registry.forInterface(IPaypalConfiguration)
        config.api_username = CONFIG['API_USERNAME']
        config.api_password = CONFIG['API_PASSWORD']
        config.api_signature = CONFIG['API_SIGNATURE']
        config.api_environment = CONFIG['API_ENVIRONMENT']

    def clear_configuration(self):
        registry = getUtility(IRegistry)
        config = registry.forInterface(IPaypalConfiguration)
        config.api_username = u''
        config.api_password = u''
        config.api_signature = u''
        config.api_environment = u'sandbox'

    def test_utility_call_without_configuration(self):
        """ verify that calling utility w/o config settings is an error
        """
        self.assertRaises(ValueError, self.utility)

    def test_call_utility_with_configuration(self):
        self.setup_configuration()
        try:
            api = self.utility()
            self.assertTrue(api is not None,
                            'unexpected return value for api: %s' % api)
        except ValueError, e:
            self.fail('calling util raised error: %s' % str(e))

    def test_calling_utility_returns_api(self):
        self.setup_configuration()
        api = self.utility()
        self.assertTrue(isinstance(api, PayPalInterface),
                        'api object of wrong type: %s' % api.__class__)

    def test_get_config_without_configuration(self):
        config = self.utility._get_config()
        self.assertTrue(config is None, "config should be None: %s" % config)

    def test_get_config_with_configuration(self):
        self.setup_configuration()
        config = self.utility._get_config()
        self.assertTrue(isinstance(config, PayPalConfig),
                        'config object of wrong type: %s' % config.__class__)
        for key, val in CONFIG.items():
            self.assertEquals(getattr(config, key, None), val,
                              'expected %s for %s, but got %s' %
                              (val, key, getattr(config, key, None)))
