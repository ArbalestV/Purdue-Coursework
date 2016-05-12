# encoding: utf-8
# module gpgme._gpgme
# from /usr/lib64/python2.6/site-packages/gpgme/_gpgme.so
# by generator 1.136
# no doc
# no imports

# functions

def make_constants(*args, **kwargs): # real signature unknown
    pass

# classes

class Context(object):
    # no doc
    def card_edit(self, *args, **kwargs): # real signature unknown
        pass

    def decrypt(self, *args, **kwargs): # real signature unknown
        pass

    def decrypt_verify(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def edit(self, *args, **kwargs): # real signature unknown
        pass

    def encrypt(self, *args, **kwargs): # real signature unknown
        pass

    def encrypt_sign(self, *args, **kwargs): # real signature unknown
        pass

    def export(self, *args, **kwargs): # real signature unknown
        pass

    def genkey(self, *args, **kwargs): # real signature unknown
        pass

    def get_key(self, *args, **kwargs): # real signature unknown
        pass

    def import_(self, *args, **kwargs): # real signature unknown
        pass

    def keylist(self, *args, **kwargs): # real signature unknown
        pass

    def set_engine_info(self, *args, **kwargs): # real signature unknown
        pass

    def set_locale(self, *args, **kwargs): # real signature unknown
        pass

    def sign(self, *args, **kwargs): # real signature unknown
        pass

    def verify(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    armor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    include_certs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keylist_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    passphrase_cb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress_cb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    textmode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GenkeyResult(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    fpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    primary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GpgmeError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ImportResult(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    considered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imported_rsa = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_revocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_signatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_sub_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_user_ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    not_imported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    no_user_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret_imported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret_unchanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipped_new_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unchanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Key(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    can_authenticate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_certify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_encrypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chain_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    issuer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    issuer_serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keylist_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner_trust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revoked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subkeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class KeyIter(object):
    # no doc
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class KeySig(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exportable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pubkey_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revoked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sig_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NewSignature(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    fpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pubkey_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sig_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Signature(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    exp_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    validity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    validity_reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrong_key_usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Subkey(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    can_authenticate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_certify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_encrypt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_sign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pubkey_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revoked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UserId(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revoked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    validity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



