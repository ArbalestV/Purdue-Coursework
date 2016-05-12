# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class PK11Slot(object):
    """ An object representing a PKCS #11 Slot """
    def authenticate(self, load_certs=False, *user_data): # real signature unknown; restored from __doc__
        """
        authenticate(load_certs=False, [user_data1, ...]) -> 
        
        :Parameters:
            load_certs : bool
                If True load certificates after authenticating.
        
        Checks to see if token needs to be logged in.  If so it invokes the
        password callback (set via `nss.set_password_callback()`) passing the
        optional user_data parameters to the password callback.
        """
        pass

    def generate_key_pair(self, mechanism, key_params, token, sensitive, *user_data): # real signature unknown; restored from __doc__
        """
        generate_key_pair(mechanism, key_params, token, sensitive, [user_data1, ...]) -> public_key, private_key
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
            key_params : SecItem object or None
                SecItem key parameters. None is also valid.
            token : bool
                If true the key is a token object otherwise it's a session object.
            sensitive : bool
                If a key is sensitive, certain attributes of the key cannot be
                revealed in plaintext outside the token. It is also more
                expensive to move between tokens.
            user_dataN : object ...
                zero or more caller supplied parameters which will
                be passed to the password callback function
        
        Generate a public and private key pair.
        
        Example::
        
            # Generate a DSA key pair
            key_params = nss.KEYPQGParams()
            mechanism = nss.CKM_DSA_KEY_PAIR_GEN
            slot = nss.get_best_slot(mechanism)
            pub_key, priv_key = slot.generate_key_pair(mechanism, key_params, False, False)
        
            # Generate a DSA key pair
            key_params = nss.RSAGenParams()
            mechanism = nss.CKM_RSA_PKCS_KEY_PAIR_GEN
            slot = nss.get_best_slot(mechanism)
            pub_key, priv_key = slot.generate_key_pair(mechanism, key_params, False, False)
        """
        pass

    def get_best_key_length(self, mechanism): # real signature unknown; restored from __doc__
        """
        get_best_key_length(mechanism) -> length
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
        
        Return the best key length for this slot and mechanism.
        A zero result means that token knows how long the key should be,
        the result is typically used with key_gen(), token_key_gen(), or
        token_key_gen_with_flags()
        """
        pass

    def get_best_wrap_mechanism(self): # real signature unknown; restored from __doc__
        """
        get_best_wrap_mechanism() -> mechanism
        
        Find the best key wrap mechanism for this slot.
        """
        pass

    def get_disabled_reason(self): # real signature unknown; restored from __doc__
        """
        get_disabled_reason() -> integer
        
        Returns a diabled reason enumerated constant (i.e. PK11_DIS_*).
        
        May be one of:
        
            * PK11_DIS_NONE
            * PK11_DIS_USER_SELECTED
            * PK11_DIS_COULD_NOT_INIT_TOKEN
            * PK11_DIS_TOKEN_VERIFY_FAILED
            * PK11_DIS_TOKEN_NOT_PRESENT
        """
        return 0

    def has_protected_authentication_path(self): # real signature unknown; restored from __doc__
        """
        has_protected_authentication_path() -> bool
        
        Returns True if token has a "protected authentication path", whereby
        a user can log into the token without passing a PIN through the
        library, False otherwise.  An example might be a token with an
        integrated key pad.
        """
        return False

    def has_root_certs(self): # real signature unknown; restored from __doc__
        """
        has_root_certs() -> bool
        
        Returns True if the slot contains the root certificate , False otherwise.
        """
        return False

    def is_disabled(self): # real signature unknown; restored from __doc__
        """
        is_disabled() -> bool
        
        Returns True if the slot is disabled, False otherwise.
        """
        return False

    def is_friendly(self): # real signature unknown; restored from __doc__
        """
        is_friendly() -> bool
        
        Returns True if the slot allows certificates to be read
        without logging in to the token, False otherwise.
        """
        return False

    def is_hw(self): # real signature unknown; restored from __doc__
        """
        is_hw() -> bool
        
        Returns True if the slot is implemented in hardware, False otherwise.
        """
        return False

    def is_internal(self): # real signature unknown; restored from __doc__
        """
        is_internal() -> bool
        
        Returns True if the the slot is internal, False otherwise.
        """
        return False

    def is_logged_in(self, *user_data): # real signature unknown; restored from __doc__
        """
        is_logged_in([user_data1, ...]) -> bool
        
        :Parameters:
            user_data1 : object ...
                zero or more caller supplied parameters which will
                be passed to the password callback function
        
        Return True if token is logged in, False otherwise.
        """
        return False

    def is_present(self): # real signature unknown; restored from __doc__
        """
        is_present() -> bool
        
        Returns True if the slot's token present, False otherwise.
        """
        return False

    def is_read_only(self): # real signature unknown; restored from __doc__
        """
        is_read_only() -> bool
        
        Returns True if the the slot is read-only, False otherwise.
        """
        return False

    def is_removable(self): # real signature unknown; restored from __doc__
        """
        is_removable() -> bool
        
        Returns True if the token is removable, False otherwise.
        """
        return False

    def key_gen(self, mechanism, sec_param, key_size, *user_data): # real signature unknown; restored from __doc__
        """
        key_gen(mechanism, sec_param, key_size, [user_data1, ...]) -> PK11SymKey object
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
            sec_param : SecItem object or None
                SecItem key parameters. None is also valid.
            key_size : int
                key length (use get_best_key_length())
            user_dataN : object ...
                zero or more caller supplied parameters which will
                be passed to the password callback function
        
        Generate a symmetric key.
        """
        return PK11SymKey

    def logout(self): # real signature unknown; restored from __doc__
        """
        logout()l
        
        Logs a user out of a session destroying any objects
        allocated on their behalf.
        """
        pass

    def need_login(self): # real signature unknown; restored from __doc__
        """
        need_login() -> bool
        
        Returns True if there are some cryptographic functions that a
        user must be logged in to perform, False otherwise.
        """
        return False

    def need_user_init(self): # real signature unknown; restored from __doc__
        """
        need_user_init() -> bool
        
        Returns True if the slot needs to be logged into by
        the user by providing their pin, False otherwise.
        """
        return False

    def user_disable(self): # real signature unknown; restored from __doc__
        """
        user_disable() 
        
        Prevents the slot from being used, and sets disable reason to
        PK11_DIS_USER_SELECTED.
        
        Mechanisms that were on continue to stay on. Therefore, when the slot
        is enabled again via `PK11Slot.user_enable()`, it will remember what
        mechanisms needs to be turned on.
        """
        pass

    def user_enable(self): # real signature unknown; restored from __doc__
        """
        user_enable() 
        
        Allow all mechanisms that are ON before `PK11Slot.user_disable()` was
        called to be available again. Sets disable reason to PK11_DIS_NONE.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    slot_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """slot name"""

    token_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """token name"""



