from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary


class IPaypalAPIUtility(Interface):
    """ utility wrapper around the paypal NVP API

        API implmentation provided by paypal-python:
            http://pypi.python.org/pypi/paypal/
    """

    def address_verify(email, street, zip):
        """ AddressVerify """

    def do_authorization(transactionid, amt):
        """ DoAuthorization """

    def do_capture(authorizationid, amt, completetype="Complete", ** kwargs):
        """ DoCapture """

    def do_direct_payment(paymentaction="Sale", **kwargs):
        """ DoDirectPayment """

    def do_void(authorizationid, note=''):
        """ DoVoid """

    def get_express_checkout_details(token):
        """ GetExpressCheckoutDetails """

    def get_transaction_details(transactionid):
        """ GetTransactionDetails """

    def set_express_checkout(token='', **kwargs):
        """ SetExpressCheckout """

    def do_express_checkout_payment(token, **kwargs):
        """ DoExpressCheckoutPayment """

    def generate_express_checkout_rediret_url(token):
        """ create a redirect url for client with express checkout """

    def generate_cart_upload_redirect_url(**kwargs):
        """ generate a cart upload url for the client """


class IPaypalConfiguration(Interface):

    api_username = schema.TextLine(title=u'API Username')
    api_password = schema.TextLine(title=u'API Password')
    api_signature = schema.TextLine(title=u'API Signature')
    api_environment = schema.Choice(
        title=u'API Environment',
        vocabulary=SimpleVocabulary.fromValues(['sandbox', 'production']),
        default='sandbox')
