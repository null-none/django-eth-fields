from django.core.exceptions import ValidationError

from web3 import Web3


def validate_checksumed_address(address):
    try:
        if not Web3.isChecksumAddress(address):
            raise ValidationError(
                "%(address)s has an invalid checksum",
                params={"address": address},
            )
    except:
        raise ValidationError(
            "%(address)s is not a valid ethereum address",
            params={"address": address},
        )


def validate_address(address):
    try:
        if not Web3.isAddress(address):
            raise ValidationError(
                "%(address)s has an invalid address",
                params={"address": address},
            )
    except:
        raise ValidationError(
            "%(address)s is not a valid address",
            params={"address": address},
        )
