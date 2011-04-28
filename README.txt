.. contents::


Introduction
============

This package provides a very thin utility wrapper around the `paypal-python`_
package. Installing this into a plone site will provide a utility with the
interface IPaypalAPIUtility. It will also provide some configuration settings
useful for getting started. The utility may be used in 'sandbox' mode or in
'production' based on the settings chosen. The default is to operate in
'sandbox' mode.

Users are encouraged to read carefully the documentation for the `Paypal
Website Payments Pro API`_

.. _paypal-python: http://pypi.python.org/pypi/paypal
-- _Paypal Website Payments Pro API: https://www.x.com/community/ppx/documentation#wpp


Work In Progress
================

This package is an early alpha. It is not yet suitable for production and is
in no way stable. If you have contributions, please be sure to write tests to
cover them.
