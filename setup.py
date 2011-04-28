from setuptools import setup, find_packages

version = '1.0a1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='eastofeaton.paypal',
      version=version,
      description="A zca utility providing the paypal API for plone",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='paypal plone zope utility',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['eastofeaton'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'paypal',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
