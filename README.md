Django Eth Fields
===================

**Helpers for Python Django projects using ethereum**


Installation
------------

Using pip

.. code:: bash

    $ pip install django-eth-fields


Example
-----

.. code:: python

    from django_eth_fields.fields import EthereumAddressField, HexField, Uint256Field

    class MyModel(models.Model):
        address = EthereumAddressField()
        hex = HexField()
        unit_255 = Uint256Field()

