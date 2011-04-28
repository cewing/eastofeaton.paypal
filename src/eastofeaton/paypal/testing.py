from zope.configuration import xmlconfig
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile


class EastofeatonPaypal(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import eastofeaton.paypal
        xmlconfig.file('configure.zcml',
                       eastofeaton.paypal,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eastofeaton.paypal:default')

EASTOFEATON_PAYPAL_FIXTURE = EastofeatonPaypal()
EASTOFEATON_PAYPAL_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(EASTOFEATON_PAYPAL_FIXTURE, ),
                       name="EastofeatonPaypal:Integration")
EASTOFEATON_PAYPAL_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(EASTOFEATON_PAYPAL_FIXTURE, ),
                      name="EastofeatonPaypal:Functional")