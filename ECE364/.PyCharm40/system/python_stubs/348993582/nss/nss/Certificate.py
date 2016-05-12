# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class Certificate(object):
    """
    Certificate(data=None, der_is_signed=True)
    
    :Parameters:
        data : SecItem or str or any buffer compatible object
            Data to initialize the certificate from, must be in DER format
        der_is_signed : bool
            True if certficate DER data is wrapped by signed DER data.
            If False then DER data is certifcate only.
    
    An object representing a Certificate
    """
    def check_valid_times(self, time=None, allow_override=False): # real signature unknown; restored from __doc__
        """
        check_valid_times(time=now, allow_override=False) --> validity
        
        :Parameters:
            time : number
                an optional point in time as number of microseconds
                since the NSPR epoch, midnight (00:00:00) 1 January
                1970 UTC, either as an integer or a float. If time 
                is not specified the current time is used.
            allow_override : bool
                If True then check to see if the invalidity has
                been overridden by the user, defaults to False.
        
        Checks whether a specified time is within a certificate's validity
        period.
        
        Returns one of:
        
        - secCertTimeValid
        - secCertTimeExpired
        - secCertTimeNotValidYet
        """
        pass

    def find_kea_type(self): # real signature unknown; restored from __doc__
        """
        find_kea_type() -> kea_type
        Returns key exchange type of the keys in an SSL server certificate.
        
        May be one of the following:
            - ssl_kea_null
            - ssl_kea_rsa
            - ssl_kea_dh
            - ssl_kea_fortezza (deprecated)
            - ssl_kea_ecdh
        """
        pass

    def format(self, level=0, indent='    '): # real signature unknown; restored from __doc__
        """
        format(level=0, indent='    ') -> string)
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
            indent : string
                string replicated once for each indent level then prepended to output line
        
        This is equivalent to:
        indented_format(obj.format_lines()) on an object providing a format_lines() method.
        """
        return ""

    def format_lines(self, level=0): # real signature unknown; restored from __doc__
        """
        format_lines(level=0) -> [(level, string),...]
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
        
        Formats the object into a sequence of lines with indent level
        information.  The return value is a list where each list item is a
        tuple.  The first item in the tuple is an integer
        representing the indentation level for that line. Any remaining items
        in the tuple are strings to be output on that line.
        
        The output of this function can be formatted into a single string by
        calling `indented_format()`, e.g.:
        
            print indented_format(obj.format_lines())
        
        The reason this function returns a tuple as opposed to an single
        indented string is to support other text formatting systems such as
        GUI's with indentation controls.  See `indented_format()` for a
        complete explanation.
        """
        pass

    def get_extension(self, oid): # real signature unknown; restored from __doc__
        """
        get_extension(oid) -> `CertificateExtension`
        
        Given an oid identifying the extension try to locate it in the
        certificate and return it as generic `CertificateExtension` object. If
        the extension is not present raise a KeyError.
        
        The generic `CertificateExtension` object is not terribly useful on
        it's own, howerver it's value property can be used to intialize
        instances of a class representing the extension.  Or it may be passed
        to functions that convert the value into some other usable format.
        Although one might believe this function should do these conversions
        for you automatically there are too many possible variations. Plus one
        might simple be interested to know if an extension is present or
        not. So why perform conversion work that might not be needed or might
        not be in the format needed? Therefore this function is just one
        simple element in a larger toolbox. Below are some suggestions on how
        to convert the generic `CertificateExtension` object (this list may
        not be complete).
        
            SEC_OID_PKCS12_KEY_USAGE
                `x509_key_usage()`
            SEC_OID_X509_SUBJECT_KEY_ID
                `SecItem.der_to_hex()`
            SEC_OID_X509_CRL_DIST_POINTS
                `CRLDistributionPts()`
            case SEC_OID_X509_AUTH_KEY_ID
                `AuthKeyID()`
            SEC_OID_X509_EXT_KEY_USAGE
                `x509_ext_key_usage()`
            SEC_OID_X509_BASIC_CONSTRAINTS
                `BasicConstraints()`
            SEC_OID_X509_SUBJECT_ALT_NAME
                `x509_alt_name()`
            SEC_OID_X509_ISSUER_ALT_NAME
                `x509_alt_name()`
        
        :Parameters:
             oid : may be one of integer, string, SecItem
                 The OID of the certification extension to retreive
                 May be one of:
        
                 * integer: A SEC OID enumeration constant (i.e. SEC_OID\_*)
                   for example SEC_OID_X509_BASIC_CONSTRAINTS.
                 * string: A string either the OID name, with or without the SEC_OID\_
                   prefix (e.g. "SEC_OID_X509_BASIC_CONSTRAINTS" or "X509_BASIC_CONSTRAINTS")
                   or as the dotted decimal representation, for example
                   'OID.2 5 29 19'. Case is not significant for either form.
                 * SecItem: A SecItem object encapsulating the OID in 
                   DER format.
        
        :returns:
            generic `CertificateExtension` object
        """
        pass

    def has_signer_in_ca_names(self, ca_names): # real signature unknown; restored from __doc__
        """
        has_signer_in_ca_names(ca_names) -> bool
        
        :Parameters:
            ca_names : (SecItem, ...)
                Sequence of CA distinguished names. Each item in the sequence must
                be a SecItem object containing a distinguished name.
        
        Returns True if any of the signers in the certificate chain for a
        specified certificate are in the list of CA names, False
        otherwise.
        """
        return False

    def make_ca_nickname(self): # real signature unknown; restored from __doc__
        """
        make_ca_nickname() -> string
        Returns a nickname for the certificate guaranteed to be unique
        within the the current NSS database.
        
        The nickname is composed thusly:
        
        A. Establish a name by trying in order:
        
           1. subject's common name (i.e. CN)
           2. subject's organizational unit name (i.e. OU)
        
        B. Establish a realm by trying in order:
        
           1. issuer's organization name (i.e. O)
           2. issuer's distinguished name (i.e. DN)
           3. set to "Unknown CA"
        
        C. If name exists the nickname will be "name - realm",
           else the nickname will be "realm"
        
        D. Then the nickname will be tested for existence in the database.
           If it does not exist it will be returned as the nickname.
           Else a loop is entered where the nickname will have " #%d" appended
           to it where %d is an integer beginning at 1. The generated nickname is
           tested for existence in the dabase until a unique name is found.
        """
        return ""

    def verify_hostname(self, hostname): # real signature unknown; restored from __doc__
        """
        verify_hostname(hostname) -> bool
        
        A restricted regular expression syntax is used to test if the common
        name specified in the subject DN of the certificate is a match,
        returning True if so, False otherwise.
        
        The regular expression systax is:
            \*
                matches anything
            \?
                matches one character
            \\ (backslash)
                escapes a special character
            \$
                 matches the end of the string
            [abc]
                matches one occurrence of a, b, or c. The only character
                that needs to be escaped in this is ], all others are not special.
            [a-z]
                matches any character between a and z
            [^az]
                matches any character except a or z
            \~
                followed by another shell expression removes any pattern matching
                the shell expression from the match list
            (foo|bar)
                matches either the substring foo or the substring bar.
                These can be shell expressions as well.
        """
        return False

    def verify_now(self, certdb, check_sig, required_usages, *user_data): # real signature unknown; restored from __doc__
        """
        verify_now(certdb, check_sig, required_usages, [user_data1, ...]) -> valid_usages
        
        :Parameters:
            certdb : CertDB object
                CertDB certificate database object
            check_sig : bool
                True if certificate signatures should be checked
            required_usages : integer
                A bitfield of all cert usages that are required for verification
                to succeed. If zero return all possible valid usages.
            user_dataN : object
                zero or more caller supplied parameters which will
                be passed to the password callback function
        
        Verify a certificate by checking if it's valid and that we
        trust the issuer.
        
        Possible usage bitfield values are:
            - certificateUsageCheckAllUsages
            - certificateUsageSSLClient
            - certificateUsageSSLServer
            - certificateUsageSSLServerWithStepUp
            - certificateUsageSSLCA
            - certificateUsageEmailSigner
            - certificateUsageEmailRecipient
            - certificateUsageObjectSigner
            - certificateUsageUserCertImport
            - certificateUsageVerifyCA
            - certificateUsageProtectedObjectSigner
            - certificateUsageStatusResponder
            - certificateUsageAnyCA
        
        Returns valid_usages, a bitfield of certificate usages.  If
        required_usages is non-zero, the returned bitmap is only for those
        required usages, otherwise it is for all possible usages.
        
        Hint: You can obtain a printable representation of the usage flags
        via `cert_usage_flags`.
        """
        pass

    def __init__(self, data=None, der_is_signed=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    der_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """raw certificate DER data as data buffer"""

    email_trust_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate email trust flags as array of strings, or None if trust is not defined"""

    extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate extensions as a tuple of CertificateExtension objects"""

    issuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate issuer as a `DN` object"""

    serial_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate serial number"""

    signature_algorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate signature algorithm"""

    signed_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate signature as SignedData object"""

    signing_trust_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate object signing trust flags as array of strings, or None if trust is not defined"""

    ssl_trust_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate SSL trust flags as array of strings, or None if trust is not defined"""

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate subject as a `DN` object"""

    subject_common_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate subject"""

    subject_public_key_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate public info as SubjectPublicKeyInfo object"""

    valid_not_after = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate not valid after this time (floating point value expressed as microseconds since the epoch, midnight January 1st 1970, UTC)"""

    valid_not_after_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate not valid after this time (string value expressed, UTC)"""

    valid_not_before = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate not valid before this time (floating point value expressed as microseconds since the epoch, midnight January 1st 1970 UTC)"""

    valid_not_before_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate not valid before this time (string value expressed, UTC)"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """certificate version"""



