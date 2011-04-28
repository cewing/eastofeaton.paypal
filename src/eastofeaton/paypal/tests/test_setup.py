import unittest2 as unittest

from zope.component import queryUtility
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName

from eastofeaton.paypal.interfaces import IPaypalAPIUtility
from eastofeaton.paypal.interfaces import IPaypalConfiguration
from eastofeaton.paypal.testing import\
    EASTOFEATON_PAYPAL_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = EASTOFEATON_PAYPAL_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """ validate that our product GS profile has been run and installed
        """
        pid = 'eastofeaton.paypal'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        "Package appears not to be installed")

    def test_paypal_utility_available(self):
        utility = queryUtility(IPaypalAPIUtility, default=None)
        self.assertTrue(utility is not None)

    def test_paypal_configuration_available(self):
        registry = getUtility(IRegistry)
        config = registry.forInterface(IPaypalConfiguration)
        self.assertTrue(config is not None)
