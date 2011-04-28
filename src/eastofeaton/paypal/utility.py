from zope.interface import implements
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from paypal.interface import PayPalInterface
from paypal.settings import PayPalConfig

from eastofeaton.paypal.interfaces import IPaypalAPIUtility
from eastofeaton.paypal.interfaces import IPaypalConfiguration


class PaypalAPIUtility(object):
    """ the utility returns an interface object when called 
    """
    implements(IPaypalAPIUtility)

    def __call__(self):
        config = self._get_config()
        if config is None:
            raise ValueError("paypal configuration settings not available")

        return PayPalInterface(config=config)

    def _get_config(self):
        registry = getUtility(IRegistry)
        config = registry.forInterface(IPaypalConfiguration)
        if config.api_username and config.api_password and \
            config.api_signature and config.api_environment:
            kw = {'API_USERNAME': config.api_username,
                  'API_PASSWORD': config.api_password,
                  'API_SIGNATURE': config.api_signature,
                  'API_ENVIRONMENT': config.api_environment}
            return PayPalConfig(**kw)
        else:
            return None
