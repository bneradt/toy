#!/usr/bin/env python3

import argparse
import sys

DIVISOR = 20201227

def parse_args():
    parser = argparse.ArgumentParser(
            description='Derive the encryption key from the given public keys.')

    parser.add_argument(
            '-c', '--card_subject_number',
            type=int,
            default=7,
            help="The card's subject number.")

    parser.add_argument(
            '-d', '--door_subject_number',
            type=int,
            default=7,
            help="The door's subject number.")

    parser.add_argument(
            'card_public_key',
            type=int,
            help="The card's public, cryptographic key.")
    parser.add_argument(
            'door_public_key',
            type=int,
            help="The door's public, cryptographic key.")

    return parser.parse_args()

def derive_loop_size(subject_number, public_key):
    """
    Given the subject_number and public_key, derive the loop size.

    Arguments:
        subject_number (int): The cryptographic subject number.
        public_key (int): The public key.

    Returns (int): The number of iterations performed on the subject number to
    get the public_key.
    """
    loop_size = 0
    transformed_value = 1
    while transformed_value != public_key:
        transformed_value *= subject_number
        transformed_value %= DIVISOR
        loop_size += 1
    return loop_size

def derive_encryption_key(loop_size, public_key):
    """
    Given the loop_size of one device, derive the common encryption key via the
    public key of the other.

    Arguments:
        loop_size (int): The cryptographic loop size of either the card or the
        door.

        public_key (int): The public key of the alternate device from that of
        the loop_size.

    Returns (int): the private encryption key.
    """
    encryption_key = 1
    for i in range(loop_size):
        encryption_key *= public_key
        encryption_key %= DIVISOR
    return encryption_key


def main():
    args = parse_args()

    card_loop_size = derive_loop_size(
            args.card_subject_number,
            args.card_public_key)
    door_loop_size = derive_loop_size(
            args.door_subject_number,
            args.door_public_key)

    encryption_key = derive_encryption_key(
            card_loop_size,
            args.door_public_key)

    # The encryption key is symetric and therefore should be the same computed
    # using either sets of loops sizes or public keys.
    encyrption_key_check = derive_encryption_key(
            door_loop_size,
            args.card_public_key)

    if encryption_key != encyrption_key_check:
        print(f"Internal computation error: mismatched encryption keys:")
        print(f"  {encryption_key}")
        print(f"  {encryption_key_check}")
        return 1

    print(encryption_key)


if __name__ == '__main__':
    sys.exit(main())
