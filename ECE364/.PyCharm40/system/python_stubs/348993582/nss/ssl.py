# encoding: utf-8
# module nss.ssl
# from /usr/lib64/python2.6/site-packages/nss/ssl.so
# by generator 1.136
""" This module implements the SSL functionality in NSS """

# imports
import nss.io as __nss_io


# Variables with simple values

SSL_ALLOWED = 1

SSL_BYPASS_PKCS11 = 16

SSL_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA = 17

SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA = 19

SSL_DHE_DSS_WITH_DES_CBC_SHA = 18

SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA = 20

SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA = 22

SSL_DHE_RSA_WITH_DES_CBC_SHA = 21

SSL_DH_ANON_EXPORT_WITH_DES40_CBC_SHA = 25

SSL_DH_ANON_EXPORT_WITH_RC4_40_MD5 = 23

SSL_DH_ANON_WITH_3DES_EDE_CBC_SHA = 27

SSL_DH_ANON_WITH_DES_CBC_SHA = 26

SSL_DH_ANON_WITH_RC4_128_MD5 = 24

SSL_DH_DSS_EXPORT_WITH_DES40_CBC_SHA = 11

SSL_DH_DSS_WITH_3DES_EDE_CBC_SHA = 13

SSL_DH_DSS_WITH_DES_CBC_SHA = 12

SSL_DH_RSA_EXPORT_WITH_DES40_CBC_SHA = 14

SSL_DH_RSA_WITH_3DES_EDE_CBC_SHA = 16

SSL_DH_RSA_WITH_DES_CBC_SHA = 15

SSL_ENABLE_FDX = 11
SSL_ENABLE_SSL2 = 7
SSL_ENABLE_SSL3 = 8
SSL_ENABLE_TLS = 13

SSL_EN_DES_192_EDE3_CBC_WITH_MD5 = 65287

SSL_EN_DES_64_CBC_WITH_MD5 = 65286

SSL_EN_IDEA_128_CBC_WITH_MD5 = 65285

SSL_EN_RC2_128_CBC_EXPORT40_WITH_MD5 = 65284

SSL_EN_RC2_128_CBC_WITH_MD5 = 65283

SSL_EN_RC4_128_EXPORT40_WITH_MD5 = 65282

SSL_EN_RC4_128_WITH_MD5 = 65281

SSL_HANDSHAKE_AS_CLIENT = 5
SSL_HANDSHAKE_AS_SERVER = 6

SSL_NOT_ALLOWED = 0

SSL_NO_CACHE = 9
SSL_NO_LOCKS = 17

SSL_NO_STEP_DOWN = 15

SSL_NULL_WITH_NULL_NULL = 0

SSL_REQUEST_CERTIFICATE = 3

SSL_REQUIRE_ALWAYS = 1
SSL_REQUIRE_CERTIFICATE = 10

SSL_REQUIRE_FIRST_HANDSHAKE = 2

SSL_REQUIRE_NEVER = 0

SSL_REQUIRE_NO_ERROR = 3

SSL_RESTRICTED = 2

SSL_ROLLBACK_DETECTION = 14

SSL_RSA_EXPORT_WITH_DES40_CBC_SHA = 8

SSL_RSA_EXPORT_WITH_RC2_CBC_40_MD5 = 6

SSL_RSA_EXPORT_WITH_RC4_40_MD5 = 3

SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA = 65279

SSL_RSA_FIPS_WITH_DES_CBC_SHA = 65278

SSL_RSA_WITH_3DES_EDE_CBC_SHA = 10

SSL_RSA_WITH_DES_CBC_SHA = 9

SSL_RSA_WITH_IDEA_CBC_SHA = 7

SSL_RSA_WITH_NULL_MD5 = 1
SSL_RSA_WITH_NULL_SHA = 2

SSL_RSA_WITH_RC4_128_MD5 = 4
SSL_RSA_WITH_RC4_128_SHA = 5

SSL_SECURITY = 1

SSL_SECURITY_STATUS_NOOPT = -1
SSL_SECURITY_STATUS_OFF = 0

SSL_SECURITY_STATUS_ON_HIGH = 1
SSL_SECURITY_STATUS_ON_LOW = 2

SSL_SOCKS = 2

SSL_V2_COMPATIBLE_HELLO = 12

TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA = 99

TLS_DHE_DSS_EXPORT1024_WITH_RC4_56_SHA = 101

TLS_DHE_DSS_WITH_AES_128_CBC_SHA = 50

TLS_DHE_DSS_WITH_AES_256_CBC_SHA = 56

TLS_DHE_DSS_WITH_RC4_128_SHA = 102

TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 51

TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 57

TLS_DH_ANON_WITH_AES_128_CBC_SHA = 52

TLS_DH_ANON_WITH_AES_256_CBC_SHA = 58

TLS_DH_DSS_WITH_AES_128_CBC_SHA = 48

TLS_DH_DSS_WITH_AES_256_CBC_SHA = 54

TLS_DH_RSA_WITH_AES_128_CBC_SHA = 49

TLS_DH_RSA_WITH_AES_256_CBC_SHA = 55

TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA = 49160

TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 49161

TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 49162

TLS_ECDHE_ECDSA_WITH_NULL_SHA = 49158

TLS_ECDHE_ECDSA_WITH_RC4_128_SHA = 49159

TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA = 49170

TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 49171

TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 49172

TLS_ECDHE_RSA_WITH_NULL_SHA = 49168

TLS_ECDHE_RSA_WITH_RC4_128_SHA = 49169

TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA = 49175

TLS_ECDH_anon_WITH_AES_128_CBC_SHA = 49176

TLS_ECDH_anon_WITH_AES_256_CBC_SHA = 49177

TLS_ECDH_anon_WITH_NULL_SHA = 49173

TLS_ECDH_anon_WITH_RC4_128_SHA = 49174

TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA = 49155

TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA = 49156

TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA = 49157

TLS_ECDH_ECDSA_WITH_NULL_SHA = 49153

TLS_ECDH_ECDSA_WITH_RC4_128_SHA = 49154

TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA = 49165

TLS_ECDH_RSA_WITH_AES_128_CBC_SHA = 49166

TLS_ECDH_RSA_WITH_AES_256_CBC_SHA = 49167

TLS_ECDH_RSA_WITH_NULL_SHA = 49163

TLS_ECDH_RSA_WITH_RC4_128_SHA = 49164

TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA = 98

TLS_RSA_EXPORT1024_WITH_RC4_56_SHA = 100

TLS_RSA_WITH_AES_128_CBC_SHA = 47

TLS_RSA_WITH_AES_256_CBC_SHA = 53

# functions

def clear_session_cache(): # real signature unknown; restored from __doc__
    """
    clear_session_cache()
    
    You must call ssl.clear_session_cache() after you use one of the SSL
    Export Policy Functions to change cipher suite policy settings or use
    ssl.set_default_cipher_pref() to enable or disable any cipher
    suite. Otherwise, the old settings remain in the session cache and
    will be used instead of the new settings. This function clears only
    the client cache. The client cache is not configurable. It is located
    in RAM (not on disk).
    """
    pass

def config_mp_server_sid_cache(max_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None): # real signature unknown; restored from __doc__
    """
    config_mp_server_sid_cache(max_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None)
    
    :Parameters:
        max_cache_entries : integer
            The maximum number of entries in the cache. If ZERO the server
            default value is used (10,000).
        
        ssl2_timeout : integer
            The lifetime in seconds of an SSL2 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (100 seconds).
        
        ssl3_timeout : integer
            The lifetime in seconds of an SSL3 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (24 hours).
        
        directory : string
            A string specifying the pathname of the directory that will
            contain the session cache. If None the server default value is
            used (/tmp (Unix) or \temp (NT)).
    
    This function sets up a Server Session ID (SID) cache that is safe for
    access by multiple processes on the same system.
    
    Like `ssl.config_server_session_id_cache()`, with one important
    difference.  If the application will run multiple processes (as
    opposed to, or in addition to multiple threads), then it must call
    this function, instead of calling
    `ssl.config_server_session_id_cache()`.  This has nothing to do with
    the number of processors, only processes.
    """
    pass

def config_server_session_id_cache(max_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None): # real signature unknown; restored from __doc__
    """
    config_server_session_id_cache(max_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None)
    
    :Parameters:
        max_cache_entries : integer
            The maximum number of entries in the cache. If ZERO the server
            default value is used (10,000).
        
        ssl2_timeout : integer
            The lifetime in seconds of an SSL2 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (100 seconds).
        
        ssl3_timeout : integer
            The lifetime in seconds of an SSL3 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (24 hours).
        
        directory : string
            A string specifying the pathname of the directory that will
            contain the session cache. If None the server default value is
            used (/tmp (Unix) or \temp (NT)).
    
    If you are writing an application which will use SSL sockets to
    handshake as a server, you must call config_server_session_id_cache()
    to configure the session caches for server sessions.
    
    If your server application uses multiple processes (instead of or in
    addition to multiple threads), use `ssl.config_mp_server_sid_cache()`
    instead.  You must use one of these functions to create a server
    cache.
    
    This function creates two caches: the server session ID cache (also
    called the server session cache, or server cache), and the client-auth
    certificate cache (also called the client cert cache, or client auth
    cache). Both caches are used only for sessions where the program will
    handshakes as a server. The client-auth certificate cache is used to
    remember the certificates previously presented by clients for client
    certificate authentication.
    
    A zero value or a value that is out of range for any of the parameters
    causes the server default value to be used in the server cache. Note,
    this function only affects the server cache, not the client cache.
    """
    pass

def config_server_session_id_cache_with_opt(max_cache_entries=0, max_cert_cache_entries=0, max_server_name_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None, enable_mp_cache=False): # real signature unknown; restored from __doc__
    """
    config_server_session_id_cache_with_opt(max_cache_entries=0, max_cert_cache_entries=0, max_server_name_cache_entries=0, ssl2_timeout=0, ssl3_timeout=0, directory=None, enable_mp_cache=False)
    
    :Parameters:
        max_cache_entries : integer
            The maximum number of entries in the cache. If ZERO the server
            default value is used (10,000).
        
        max_cert_cache_entries : integer
            The maximum number of entries in the cert cache. If ZERO the server
            default value is used (10,000).
        
        max_server_name_cache_entries : integer
            The maximum number of entries in the server name cache. If ZERO the server
            default value is used (10,000).
        
        ssl2_timeout : integer
            The lifetime in seconds of an SSL2 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (100 seconds).
        
        ssl3_timeout : integer
            The lifetime in seconds of an SSL3 session. The minimum timeout
            value is 5 seconds and the maximum is 24 hours. Values outside
            this range are replaced by the server default value (24 hours).
        
        directory : string
            A string specifying the pathname of the directory that will
            contain the session cache. If None the server default value is
            used (/tmp (Unix) or \temp (NT)).
        
        enable_mp_cache : bool
            If True enable the multi-process cache.
    
    Configure a secure server's session-id cache. Depends on value of
    enable_mp_cache, configures multi-proc or single proc cache.
    
    A zero value or a value that is out of range for any of the parameters
    causes the server default value to be used in the server cache. Note,
    this function only affects the server cache, not the client cache.
    """
    pass

def get_cipher_policy(cipher): # real signature unknown; restored from __doc__
    """
    get_cipher_policy(cipher) -> policy
    
    :Parameters:
        cipher : integer
            The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
    
    Returns the cipher policy.
    """
    pass

def get_default_cipher_pref(cipher): # real signature unknown; restored from __doc__
    """
    get_default_cipher_pref(cipher) -> enabled
    
    :Parameters:
        cipher : integer
            The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
    
    Returns the application default preference for the specified SSL2,
    SSL3, or TLS cipher.
    """
    pass

def get_max_server_cache_locks(): # real signature unknown; restored from __doc__
    """
    get_max_server_cache_locks() -> int
    
    Get the configured maximum number of mutexes used for the server's
    store of SSL sessions.  This value is used by the server session ID
    cache initialization functions.
    """
    return 0

def get_ssl_default_option(value): # real signature unknown; restored from __doc__
    """
    get_ssl_default_option(value)
    
    Gets the default value of a specified SSL option for all
    subsequently opened sockets as long as the current application program
    is running. Refer to the documentation for SSLSocket.set_ssl_option()
    for an explanation of the possible values.
    """
    pass

def nssinit(cert_dir): # real signature unknown; restored from __doc__
    """
    nssinit(cert_dir)
    WARNING: nssinit() has been moved to the nss module, use nss.nss_init() instead of ssl.nssinit()
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
    
    Sets up configuration files and performs other tasks required to run
    Network Security Services.
    """
    pass

def nss_init(cert_dir): # real signature unknown; restored from __doc__
    """
    nss_init(cert_dir)
    WARNING: nss_init() has been moved to the nss module, use nss.nss_init() instead of ssl.nss_init()
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
    
    Sets up configuration files and performs other tasks required to run
    Network Security Services.
    """
    pass

def nss_shutdown(): # real signature unknown; restored from __doc__
    """
    nss_shutdown()
    WARNING: nss_shutdown() has been moved to the nss module, use nss.nss_shutdown() instead of ssl.nss_shutdown()
    
    Closes the key and certificate databases that were opened by nss_init().
    
    Note that if any reference to an NSS object is leaked (for example, if an SSL
    client application doesn't call clear_session_cache() first) then nss_shutdown fails
    with the error code SEC_ERROR_BUSY.
    """
    pass

def set_cipher_policy(*args, **kwargs): # real signature unknown
    """
    set_cipher_pref(cipher, enabled)
    
    :Parameters:
        cipher : integer
            The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
        enabled : bool
            Boolean value
    
    Tells the SSL library that the specified cipher suite is allowed by
    the application's export license, or is not allowed by the
    application's export license, or is allowed to be used only with a
    Step-Up certificate. It overrides the factory default policy for that
    cipher suite. The default policy for all cipher suites is
    SSL_NOT_ALLOWED, meaning that the application's export license does
    not approve the use of this cipher suite. A U.S.domestic version of a
    product typically sets all cipher suites to SSL_ALLOWED. This setting
    is used to separate export and domestic versions of a product, and is
    not intended to express user cipher preferences.
    """
    pass

def set_default_cipher_pref(*args, **kwargs): # real signature unknown
    """
    set_cipher_pref(cipher, enabled)
    
    :Parameters:
        cipher : integer
            The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
        enabled : bool
            Boolean value
    
    Sets the application default preference for the specified SSL2, SSL3,
    or TLS cipher. A cipher suite is used only if the policy allows it and
    the preference for it is set to True.
    
    This function must be called once for each cipher you want to enable
    or disable by default.
    
    Note, which cipher suites are permitted or disallowed are modified by
    previous calls to one or more of the SSL Export Policy Functions.
    """
    pass

def set_domestic_policy(): # real signature unknown; restored from __doc__
    """
    set_domestic_policy()
    
    Configures cipher suites to conform with current U.S. export
    regulations related to domestic software products with encryption
    features.
    """
    pass

def set_export_policy(): # real signature unknown; restored from __doc__
    """
    set_export_policy()
    
    Configures the SSL cipher suites to conform with current U.S. export
    regulations related to international software products with encryption
    features.
    """
    pass

def set_france_policy(): # real signature unknown; restored from __doc__
    """
    set_france_policy()
    Configures the SSL cipher suites to conform with French import
    regulations related to software products with encryption features.
    """
    pass

def set_max_server_cache_locks(max_locks): # real signature unknown; restored from __doc__
    """
    set_max_server_cache_locks(max_locks)
    
    :Parameters:
        max_locks : int
            Maximum number of locks
    
    Set the configured maximum number of mutexes used for the server's
    store of SSL sessions.  This value is used by the server session ID
    cache initialization functions.  Note that on some platforms, these
    mutexes are actually implemented with POSIX semaphores, or with
    unnamed pipes.  The default value varies by platform.  An attempt to
    set a too-low maximum will return an error and the configured value
    will not be changed.
    """
    pass

def set_ssl_default_option(option, value): # real signature unknown; restored from __doc__
    """
    set_ssl_default_option(option, value)
    
    Changes the default value of a specified SSL option for all
    subsequently opened sockets as long as the current application program
    is running. Refer to the documentation for SSLSocket.set_ssl_option()
    for an explanation of the possible values.
    """
    pass

def shutdown_server_session_id_cache(): # real signature unknown; restored from __doc__
    """ shutdown_server_session_id_cache() """
    pass

# classes

class SSLSocket(__nss_io.Socket):
    """
    SSLSocket(family=PR_AF_INET, type=PR_DESC_SOCKET_TCP)
    
    
    :Parameters:
        family : integer
            one of:
                - PR_AF_INET
                - PR_AF_INET6
                - PR_AF_LOCAL
        type : integer
            one of:
                - PR_DESC_SOCKET_TCP
                - PR_DESC_SOCKET_UDP
    
    Create a new NSPR SSL socket:
    """
    def accept(self, timeout=None): # real signature unknown; restored from __doc__
        """
        accept(timeout=PR_INTERVAL_NO_TIMEOUT) -> (Socket, NetworkAddress)
        
        :Parameters:
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        The socket is a rendezvous socket that has been bound to an address
        with Socket.bind() and is listening for connections after a call to
        Socket.listen(). Socket.accept() accepts the first connection from the
        queue of pending connections and creates a new socket for the newly
        accepted connection. The rendezvous socket can still be used to accept
        more connections.
        
        Socket.accept() blocks the calling thread until either a new
        connection is successfully accepted or an error occurs. If the timeout
        parameter is not PR_INTERVAL_NO_TIMEOUT and no pending connection can
        be accepted before the time limit, Socket.accept() raises a
        nss.error.NSPRError exception with the error code PR_IO_TIMEOUT_ERROR.
        
        Socket.accept() returns a tuple containing a new Socket object and
        Networkaddress object for the peer.
        """
        pass

    def config_secure_server(self, cert, key, kea): # real signature unknown; restored from __doc__
        """
        config_secure_server(cert, key, kea)
        
        :Parameters:
            cert : Certificate object
                Server's certificate as a Certificate object
            key : PrivateKey object
                Server's private key as a PrivateKey object
            kea : integer
                Key exchange type (e.g. ssl_kea_rsa, ssl_kea_dh, etc.)
        
        Configures a listen socket with the information needed to handshake as
        an SSL server. SSLSocket.config_secure_server() requires the
        certificate for the server and the server's private key.
        """
        pass

    def data_pending(self): # real signature unknown; restored from __doc__
        """
        data_pending()
        
        Returns the number of bytes waiting in internal SSL buffers to be read
        by the local application from the SSL socket.
        
        If SSL_SECURITY has not been enabled with a call to
        SSLSocket.set_ssl_default_option() or SSLSocket.set_ssl_option(), the
        function returns zero.
        """
        pass

    def force_handshake(self): # real signature unknown; restored from __doc__
        """
        force_handshake()
        
        Drives a handshake for a specified SSLSocket to completion on a
        socket that has already been prepared to do a handshake or is in the
        middle of doing a handshake.
        
        When you are forcing the initial handshake on a blocking socket, this
        function returns when the handshake is complete. For subsequent
        handshakes, the function can return either because the handshake is
        complete, or because application data has been received on the
        connection that must be processed (that is, the application must read
        it) before the handshake can continue. You can use
        SSLSocket.force_handshake() when a handshake is desired but neither
        end has anything to say immediately. This occurs, for example, when an
        HTTPS server has received a request and determines that before it can
        answer the request, it needs to request an authentication certificate
        from the client. At the HTTP protocol level, nothing more is being
        said (that is, no HTTP request or response is being sent), so the
        server uses SSLSocket.force_handshake() to make the handshake
        occur. SSLSocket.force_handshake() does not prepare a socket to do a
        handshake by itself. The following functions prepare a socket to do a
        handshake:
        
            * SSLSocket.connect()
            * SSLSocket.accept()
            * SSLSocket.rehandshake()
              (after the first handshake is finished)
            * SSLSocket.reset_handshake
              (for sockets that were connected or accepted prior to being imported)
        
        A call to SSLSocket.force_handshake() will almost always be preceded
        by one of those functions. In versions prior to NSS 1.2, you cannot
        force a subsequent handshake. If you use this function after the
        initial handshake, it returns immediately without forcing a handshake.
        """
        pass

    def force_handshake_timeout(self, timeout): # real signature unknown; restored from __doc__
        """
        force_handshake_timeout(timeout)
        
        :Parameters:
            timeout : integer
                timeout value expressed as a NSPR interval
        
        See the documentation for SSLSocket.force_handshake(). This function
        adds a timeout interval.
        """
        pass

    def get_certificate(self): # real signature unknown; restored from __doc__
        """
        get_certificate() -> Certficate
        
        Returns the certificate associated with the socket or
        None if not previously set.
        """
        pass

    def get_cipher_pref(self, cipher): # real signature unknown; restored from __doc__
        """
        get_cipher_pref(cipher) -> enabled
        
        :Parameters:
            cipher : integer
                The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
        
        Returns the preference for the specified SSL2, SSL3, or TLS cipher on
        the socket.
        """
        pass

    def get_hostname(self): # real signature unknown; restored from __doc__
        """
        get_hostname()
        
        SSLSocket.get_hostname() is used by certificate authentication callback
        function to obtain the domain name of the desired SSL server for the
        purpose of comparing it with the domain name in the certificate
        presented by the server actually contacted.
        """
        pass

    def get_peer_certificate(self): # real signature unknown; restored from __doc__
        """
        get_peer_certificate() -> Certficate
        
        SSLSocket.get__peer_certificate() is used by certificate
        authentication and bad-certificate callback functions to obtain the
        certificate under scrutiny. If the client calls
        SSLSocket.get_peer_certificate(), it always returns the server's
        certificate. If the server calls SSLSocket.get_peer_certificate(), it
        may return None if client authentication is not enabled or if the
        client had no certificate when asked.
        """
        pass

    def get_pkcs11_pin_arg(self): # real signature unknown; restored from __doc__
        """
        get_pkcs11_pin_arg()
        
        Returns a tuple of arguments or None if not previously set with
        SSLSocket.set_pkcs11_pin_arg()
        """
        pass

    def get_security_status(self): # real signature unknown; restored from __doc__
        """
        get_security_status() -> on, cipher, key_size, secret_key_size, issuer, subject
        
        Gets information about the security parameters of the current connection.
        Returns the tuple (on, cipher, key_size, secret_key_size, issuer, subject)
        
        The interpretation of each value is:
            on
                An integer, will be one of these values:
                    - SSL_SECURITY_STATUS_OFF
                    - SSL_SECURITY_STATUS_ON_HIGH
                    - SSL_SECURITY_STATUS_ON_LOW
            cipher
                A string specifying the name of the cipher.
                    - For SSL v2, the string is one of the following:
                        - RC4
                        - RC4-Export
                        - RC2-CBC
                        - RC2-CBC-Export
                        - DES-CBC,
                        - DES-EDE3-CBC
                    - For SSL v3, the string is one of the following:
                        - RC4
                        - RC4-40
                        - RC2-CBC
                        - RC2-CBC-40
                        - DES-CBC
                        - 3DES-EDE-CBC
                        - DES-CBC-40
            keySize
                An integer, the session key size used, in bits.
            secret_key_size
                An integer. indicates the size, in bits, of the secret portion of
                the session key used (also known as the 'effective key size'). The
                secret key size is never greater than the session key size.
            issuer
                A string specifying the DN of the issuer of the certificate at
                the other end of the connection, in RFC1485 format. If no
                certificate is supplied, the string is 'no certificate'
            subject
                A string specifying the distinguished name of the certificate at
                the other end of the connection, in RFC1485 format. If no
                certificate is supplied, the string is 'no certificate'
        """
        pass

    def get_session_id(self): # real signature unknown; restored from __doc__
        """
        get_session_id() -> id
        
        Returns the SSL session ID as a SecItem.
        """
        pass

    def get_ssl_option(self, value): # real signature unknown; restored from __doc__
        """
        get_ssl_option(value) -> value
        
        :Parameters:
            value : integer
                a constant value identifying which option to query
        
        Retrieves the value of a specified SSL option. Refer to the
        documentation for SSLSocket.set_ssl_option() for an explanation of the
        possible values.
        """
        pass

    def import_tcp_socket(self, osfd): # real signature unknown; restored from __doc__
        """
        import_tcp_socket(osfd) -> Socket
        :Parameters:
            osfd : integer
                file descriptor of the SOCK_STREAM socket to import
        
        Returns a Socket object that uses the specified socket file descriptor for
        communication.
        """
        pass

    def invalidate_session(self): # real signature unknown; restored from __doc__
        """
        invalidate_session()
        
        After you call SSLSSocket.invalidate_session(), the existing
        connection using the session can continue, but no new connections can
        resume this SSL session.
        """
        pass

    def rehandshake(self, flush_cache): # real signature unknown; restored from __doc__
        """
        rehandshake(flush_cache)
        
        :Parameters:
            flush_cache : bool
                 - If flush_cache is True, the SSL3 cache entry will be flushed
                   first, ensuring that a full SSL handshake from scratch will
                   occur.
                 - If flush_cache is False, and an SSL connection is established, it
                   will do the much faster session restart handshake. This will
                   regenerate the symmetric session keys without doing another
                   private key operation.
                 
        
        Causes SSL to begin a new SSL 3.0 handshake on a connection that has
        already completed one handshake.
        
        If flush_cache is True, the SSLSocket.rehandshake() function
        invalidates the current SSL session associated with the specified
        SSLSocket from the session cache and starts another full SSL 3.0
        handshake. It is for use with SSL 3.0 only. You can call this function
        to redo the handshake if you have changed one of the socket's
        configuration parameters (for example, if you are going to request
        client authentication). Setting flush_cache to False can be useful,
        for example, if you are using export ciphers and want to keep changing
        the symmetric keys to foil potential
        attackers. SSLSocket.rehandshake() only initiates the new handshake by
        sending the first message of that handshake. To drive the new
        handshake to completion, you must either call
        SSLSocket.force_handshake() or do another I/O operation (read or
        write) on the socket. A call to SSLSocket.rehandshake() is typically
        followed by a call to SSLSocket.force_handshake().
        """
        pass

    def rehandshake_timeout(self, flush_cache, timeout): # real signature unknown; restored from __doc__
        """
        rehandshake_timeout(flush_cache, timeout)
        
        :Parameters:
            flush_cache : bool
                cache flush flag
            timeout : integer
                timeout value expressed as a NSPR interval
        
        See the documentation for SSLSocket.rehandshake(). This function
        adds a timeout interval.
        """
        pass

    def reset_handshake(self, as_server): # real signature unknown; restored from __doc__
        """
        reset_handshake(as_server)
        
        :Parameters:
            as_server : bool
                - True means the socket will attempt
                  to handshake as a server the next time it tries, and
                - False means the socket will attempt to handshake as
                  a client the next time it tries.
        
        Calling SSLSocket.reset_handshake() causes the SSL handshake protocol
        to start from the beginning on the next I/O operation. That is, the
        handshake starts with no cipher suite already in use, just as it does
        on the first handshake on a new socket. When an application imports a
        socket into SSL after the TCP connection on that socket has already
        been established, it must call SSLSocket.reset_handshake() to
        determine whether SSL should behave like an SSL client or an SSL
        server. Note that this step would not be necessary if the socket
        weren't already connected. For an SSL socket that is configured before
        it is connected, SSL figures this out when the application calls
        SSLSocket.connect() or SSLSocket.accept(). If the socket is already
        connected before SSL gets involved, you must provide this extra hint.
        """
        pass

    def set_auth_certificate_callback(self, callback, *user_data): # real signature unknown; restored from __doc__
        """
        set_auth_certificate_callback(callback, [user_data1, ...])
        
        :Parameters:
            callback : function pointer
                callback to invoke
            user_dataN:
                zero or more caller supplied parameters which will be passed to the callback
        
        The callback has the following signature::
            
            callback(socket, check_sig, is_server, [user_data1, ...]) -> bool
        
        socket
            the SSLSocket object
        check_sig
            boolean, True means signatures are to be checked and the
            certificate chain is to be validated. False means they are not
            to be checked. (The value is normally True.)
        is_server
            boolean, True means the callback function should evaluate the
            certificate as a server does, treating the remote end as a
            client. False means the callback function should evaluate the
            certificate as a client does, treating the remote end as a server.
        user_dataN
             zero or more caller supplied optional parameters
        
        The callback function should return True if authentication is
        successful, False otherwise. If authentication is not successful the
        callback should indicate the reason for the failure (if possible) by
        calling nss.set_error() with the appropriate error code.
        
        The callback function obtains the certificate to be authenticated by
        calling ssl.get_peer_certificate(). If is_server is false, the
        callback should also check that the domain name in the remote server's
        certificate matches the desired domain name specified in a previous
        call to ssl.set_hostname(). To obtain that domain name, the callback calls
        ssl.get_hostname(). 
        
        The callback may need to call one or more PK11 functions to obtain the
        services of a PKCS 11 module. Some of the PK11 functions require a
        PIN argument (see ssl.set_pkcs11_pin_arg() for details). To obtain the
        value that was set with ssl.set_pkcs11_pin_arg(), the callback calls
        ssl.get_pkcs11_pin_arg().
        
        If the callback returns False, the SSL connection is terminated
        immediately unless the application has supplied a bad-certificate
        callback function by having previously called
        ssl.set_bad_cert_callback(). A bad-certificate callback function gives
        the application the opportunity to choose to accept the certificate as
        authentic and authorized even though it failed the check performed by
        the certificate authentication callback function.
        
        Example::
            
            def auth_certificate_callback(sock, check_sig, is_server, certdb):
                cert_is_valid = False
        
                cert = sock.get_peer_certificate()
                pin_args = sock.get_pkcs11_pin_arg()
                if pin_args is None:
                    pin_args = ()
        
                # Define how the cert is being used based upon the is_server flag.  This may
                # seem backwards, but isn't. If we're a server we're trying to validate a
                # client cert. If we're a client we're trying to validate a server cert.
                if is_server:
                    intended_usage = nss.certificateUsageSSLClient
                else:
                    intended_usage = nss.certificateUsageSSLServer
        
                try:
                    # If the cert fails validation it will raise an exception, the errno attribute
                    # will be set to the error code matching the reason why the validation failed
                    # and the strerror attribute will contain a string describing the reason.
                    approved_usage = cert.verify_now(certdb, check_sig, intended_usage, *pin_args)
                except Exception, e:
                    cert_is_valid = False
                    return cert_is_valid
        
                # Is the intended usage a proper subset of the approved usage
                if approved_usage & intended_usage:
                    cert_is_valid = True
                else:
                    cert_is_valid = False
        
                # If this is a server, we're finished
                if is_server or not cert_is_valid:
                    return cert_is_valid
        
                # Certificate is OK.  Since this is the client side of an SSL
                # connection, we need to verify that the name field in the cert
                # matches the desired hostname.  This is our defense against
                # man-in-the-middle attacks.
        
                hostname = sock.get_hostname()
                try:
                    # If the cert fails validation it will raise an exception
                    cert_is_valid = cert.verify_hostname(hostname)
                except Exception, e:
                    cert_is_valid = False
                    return cert_is_valid
        
                return cert_is_valid
        """
        pass

    def set_certificate_db(self, certdb): # real signature unknown; restored from __doc__
        """
        set_certificate_db(certdb)
        
        :Parameters:
            certdb : CertDB object
                The certification database as a CertDB object
        
        Sets the Certificate Database on a specific SSLSocket.
        """
        pass

    def set_cipher_pref(self, cipher, enabled): # real signature unknown; restored from __doc__
        """
        set_cipher_pref(cipher, enabled)
        
        :Parameters:
            cipher : integer
                The cipher suite enumeration (e.g. SSL_RSA_WITH_NULL_MD5, etc.)
            enabled : bool or int
                True enables, False disables
        
        Sets preference for the specified SSL2, SSL3, or TLS cipher on the
        socket. A cipher suite is used only if the policy allows it and the
        preference for it is set to True.
        
        This function must be called once for each cipher you want to enable
        or disable by default.
        
        Note, which cipher suites are permitted or disallowed are modified by
        previous calls to one or more of the SSL Export Policy Functions.
        """
        pass

    def set_client_auth_data_callback(self, callback, *user_data): # real signature unknown; restored from __doc__
        """
        set_client_auth_data_callback(callback, [user_data1, ...])
        
        :Parameters:
            callback : function pointer
                callback to invoke
            user_dataN:
                zero or more caller supplied parameters which will be passed to the callback
        
        The callback has the following signature::
            
            callback(ca_names, [user_data1, ...]) -> (Certificate, PrivateKey)
        
        ca_names
            Sequence of CA distinguished names that the server accepts. Each
            item in the sequence must be a SecItem object containing a
            distinguished name.
        user_dataN
            zero or more caller supplied optional parameters
        
        The callback returns Certificate and PrivateKey if successful,
        or None if the callback failed.
        
        Defines a callback function for SSL to use in a client application
        when a server asks for client authentication information. This
        callback function is required if your client application is going to
        support client authentication.
        
        The callback function set with SSLSocket.set_client_auth_data_callback()
        is used to get information from a client application when
        authentication is requested by the server. The callback function
        retrieves the client's private key and certificate. SSL provides an
        implementation of this callback function; see NSS_GetClientAuthData
        for details. Unlike SSL_AuthCertificate, NSS_GetClientAuthData is not
        a default callback function. You must set it explicitly with
        SSLSocket.set_client_auth_data_callback() if you want to use it.
        
        Example::
            
            def client_auth_data_callback(ca_names, chosen_nickname, password, certdb):
                cert = None
                if chosen_nickname:
                    try:
                        cert = nss.find_cert_from_nickname(chosen_nickname, password)
                        priv_key = nss.find_key_by_any_cert(cert, password)
                        return cert, priv_key
                    except NSPRError, e:
                        return False
                else:
                    nicknames = nss.get_cert_nicknames(certdb, nss.SEC_CERT_NICKNAMES_USER)
                    for nickname in nicknames:
                        try:
                            cert = nss.find_cert_from_nickname(nickname, password)
                            if cert.check_valid_times():
                                if cert.has_signer_in_ca_names(ca_names):
                                    priv_key = nss.find_key_by_any_cert(cert, password)
                                    return cert, priv_key
                        except NSPRError, e:
                            pass
                    return False
            
            sock = ssl.SSLSocket(net_addr.family)
            sock.set_client_auth_data_callback(client_auth_data_callback, nickname, password, nss.get_default_certdb())
        """
        pass

    def set_handshake_callback(self, callback, *user_data): # real signature unknown; restored from __doc__
        """
        set_handshake_callback(callback, [user_data1, ...])
        
        :Parameters:
            callback : function pointer
                callback to invoke
            user_dataN:
                zero or more caller supplied parameters which will be passed to the callback
        
        The callback has the following signature::
            
            callback(socket, [user_data1, ...])
        
        socket
            the SSL socket the handshake has completed on
        user_dataN
            zero or more caller supplied optional parameters
        
        Sets up a callback function used by SSL to inform either a client
        application or a server application when the handshake is completed.
        
        Example::
            
            def handshake_callback(sock):
                print 'handshake complete, peer = %s' % (sock.get_peer_name())
            
            sock = ssl.SSLSocket(net_addr.family)
            sock.set_handshake_callback(handshake_callback)
        """
        pass

    def set_hostname(self, url): # real signature unknown; restored from __doc__
        """
        set_hostname(url)
        
        :Parameters:
            url : string
                A string specifying the desired server's domain name.
        
        The client application's certificate authentication callback function
        needs to compare the domain name in the server's certificate against
        the domain name of the server the client was attempting to
        contact. This step is vital because it is the client's only protection
        against a man-in-the-middle attack. The client application uses
        SSLSocket.set_hostname() to set the domain name of the desired server
        before performing the first SSL handshake. The client application's
        certificate authentication callback function gets this string by
        calling SSLSocket.get_hostname().
        """
        pass

    def set_pkcs11_pin_arg(self, *user_dataN): # real signature unknown; restored from __doc__
        """
        set_pkcs11_pin_arg([user_dataN, ...])
        
        :Parameters:
            user_dataN : object ...
                zero or more caller supplied parameters which will be passed
                to the pk11.password_callback()
        """
        pass

    def set_sock_peer_id(self, id): # real signature unknown; restored from __doc__
        """
        set_sock_peer_id(id)
        
        :Parameters:
            id : integer
                An ID number assigned by the application to keep track of the SSL
                session associated with the peer.
        
        Associates a peer ID with a socket to facilitate looking up the SSL
        session when it is tunneling through a proxy.
        
        SSL peers frequently reconnect after a relatively short time has
        passed. To avoid the overhead of repeating the full SSL handshake in
        situations like this, the SSL protocol supports the use of a session
        cache, which retains information about each connection for some
        predetermined length of time.
        
        For example, a client session cache includes the hostname and port
        number of each server the client connects with, plus additional
        information such as the master secret generated during the SSL
        handshake. For a direct connection with a server, the hostname and
        port number are sufficient for the client to identify the server as
        one for which it has an entry in its session cache. However, the
        situation is more complicated if the client is on an intranet and is
        connecting to a server on the Internet through a proxy. In this case,
        the client first connects to the proxy, and the client and proxy
        exchange messages specified by the proxy protocol that allow the
        proxy, in turn, to connect to the requested server on behalf of the
        client. This arrangement is known as SSL tunneling.
        
        Client session cache entries for SSL connections that tunnel through a
        particular proxy all have the same hostname and port number--that is,
        the hostname and port number of the proxy. To determine whether a
        particular server with which the client is attempting to connect has
        an entry in the session cache, the session cache needs some additional
        information that identifies that server. This additional identifying
        information is known as a peer ID. The peer ID is associated with a
        socket, and must be set before the SSL handshake occurs--that is,
        before the SSL handshake is initiated by a call to a function such as
        SSLSocket.read() or SSLSocket.force_handshake(). To set the peer ID,
        you use SSLSocket.set_sock_peer_id().
        
        In summary, SSL uses three pieces of information to identify a
        server's entry in the client session cache: the hostname, port number,
        and peer ID. In the case of a client that is tunneling through a
        proxy, the hostname and port number identify the proxy, and the peer
        ID identifies the desired server. It is recommended that the client
        set the peer ID to a string that consists of the server's hostname and
        port number, like this:'www.hostname.com:387'. This convention
        guarantees that each server has a unique entry in the client session
        cache.
        """
        pass

    def set_ssl_option(self, option, value): # real signature unknown; restored from __doc__
        """
        set_ssl_option(option, value)
        
        Sets a single configuration parameter on this socket. Call once for
        each parameter you want to change. The configuration parameters are
        listed below.
        
        SSL_SECURITY (default=True)
            Enables use of security protocol. *WARNING: If you turn this option
            off, the session will not be an SSL session and will not have
            certificate-based authentication, tamper detection, or encryption.*
        SSL_REQUEST_CERTIFICATE: (default=False)
            Is a server option that requests a client to authenticate itself.
        SSL_REQUIRE_CERTIFICATE: (default=SSL_REQUIRE_FIRST_HANDSHAKE)
            Is a server option that requires a client to authenticate itself (only
            if SSL_REQUEST_CERTIFICATE is also on). If client does not provide
            certificate, the connection terminates.
        SSL_HANDSHAKE_AS_CLIENT: (default=False)
            Controls the behavior of SSLSocket.accept(),. If this option is off,
            the SSLSocket.accept() configures the SSL socket to handshake as a
            server. If it is on, then SSLSocket.accept() configures the SSL socket
            to handshake as a client, even though it accepted the connection as a
            TCP server.
        SSL_HANDSHAKE_AS_SERVER: (default=False)
            Controls the behavior of SSLSocket.connect(). If this option is off,
            then SSLSocket.connect() configures the SSL socket to handshake as a
            client. If it is on, then SSLSocket.connect() configures the SSL
            socket to handshake as a server, even though it connected as a TCP
            client.
        SSL_ENABLE_FDX: (default=False)
            Tells the SSL library whether the application will have two threads,
            one reading and one writing, or just one thread doing reads and writes
            alternately. The factory setting for this option (which is the
            default, unless the application changes the default) is off, which
            means that the application will not do simultaneous reads and
            writes. An application that needs to do simultaneous reads and writes
            should set this to True.
        
            In NSS 2.8, the SSL_ENABLE_FDX option only affects the behavior of
            nonblocking SSL sockets. See the description below for more
            information on this option.
        SSL_ENABLE_SSL3: (default=True)
            Enables the application to communicate with SSL v3. If you turn this
            option off, an attempt to establish a connection with a peer that
            understands only SSL v3 will fail.
        SSL_ENABLE_SSL2: (default=True)
            Enables the application to communicate with SSL v2. If you turn this
            option off, an attempt to establish a connection with a peer that
            understands only SSL v2 will fail.
        SSL_ENABLE_TLS: (default=True)
            Is a peer of the SSL_ENABLE_SSL2 and SSL_ENABLE_SSL3 options. The IETF
            standard Transport Layer Security (TLS) protocol, RFC 2246, is a
            modified version of SSL3. It uses the SSL version number 3.1,
            appearing to be a 'minor' revision of SSL3.0. NSS 2.8 supports TLS in
            addition to SSL2 and SSL3. You can think of it as 'SSL_ENABLE_SSL3.1.'
            See the description below for more information about this option.
        SSL_V2_COMPATIBLE_HELLO: (default=True)
            Tells the SSL library whether or not to send SSL3 client hello
            messages in SSL2-compatible format. If set to True, it will;
            otherwise, it will not. See the description below for more information
            on this option.
        SSL_NO_CACHE: (default=False)
            Disallows use of the session cache. Factory setting is off. If you
            turn this option on, this socket will be unable to resume a session
            begun by another socket. When this socket's session is finished, no
            other socket will be able to resume the session begun by this socket.
        SSL_ROLLBACK_DETECTION: (default=True)
            Disables detection of a rollback attack. Factory setting is on. You
            must turn this option off to interoperate with TLS clients ( such as
            certain versions of Microsoft Internet Explorer) that do not conform
            to the TLS specification regarding rollback attacks. Important:
            turning this option off means that your code will not comply with the
            TLS 3.1 and SSL 3.0 specifications regarding rollback attack and will
            therefore be vulnerable to this form of attack.
            
        Keep the following in mind when deciding on the operating parameters
        you want to use with a particular socket.
        
        Turning on SSL_REQUIRE_CERTIFICATE will have no effect unless
        SSL_REQUEST_CERTIFICATE is also turned on. If you enable
        SSL_REQUEST_CERTIFICATE, then you should explicitly enable or disable
        SSL_REQUIRE_CERTIFICATE rather than allowing it to default. Enabling
        the SSL_REQUIRE_CERTIFICATE option is not recommended. If the client
        has no certificate and this option is enabled, the client's connection
        terminates with an error. The user is likely to think something is
        wrong with either the client or the server, and is unlikely to realize
        that the problem is the lack of a certificate. It is better to allow
        the SSL handshake to complete and then return an error message to the
        client that informs the user of the need for a certificate.
        
        The SSL protocol is defined to be able to handle simultaneous two-way
        communication between applications at each end of an SSL
        connection. Two-way simultaneous communication is also known as'Full
        Duplex', abbreviated FDX. However, most application protocols that use
        SSL are not two-way simultaneous, but two-way alternate, also known as
        'Half Dupled'; that is, each end takes turns sending, and each end is
        either sending, or receiving, but not both at the same time. For an
        application to do full duplex, it would have two threads sharing the
        socket; one doing all the reading and the other doing all the writing.
        
        The SSL_ENABLE_FDX option tells the SSL library whether the
        application will have two threads, one reading and one writing, or
        just one thread doing reads and writes alternately.
        
        If an SSL3 client hello message is sent to a server that only
        understands SSL2 and not SSL3, then the server will interpret the SSL3
        client hello as a very large message, and the connection will usually
        seem to 'hang' while the SSL2 server expects more data that will never
        arrive. For this reason, the SSL3 spec allows SSL3 client hellos to be
        sent in SSL2 format, and it recommends that SSL3 servers all accept
        SSL3 client hellos in SSL2 format. When an SSL2-only server receives
        an SSL3 client hello in SSL2 format, it can (and probably will)
        negotiate the protocol version correctly, not causing a 'hang'.
        
        Some applications may wish to force SSL3 client hellos to be sent in
        SSL3 format, not in SSL2-compatible format. They might wish to do this
        if they knew, somehow, that the server does not understand
        SSL2-compatible client hello messages.
        
        SSL_V2_COMPATIBLE_HELLO tells the SSL library whether or not to send
        SSL3 client hello messages in SSL2-compatible format. Note that
        calling SSLSocket.set_ssl_option() to set SSL_V2_COMPATIBLE_HELLO to
        False implicitly also sets the SSL_ENABLE_SSL2 option to False for
        that SSL socket. Calling SSL_EnableDefault to change the application
        default setting for SSL_V2_COMPATIBLE_HELLO to False implicitly also
        sets the default value for SSL_ENABLE_SSL2 option to False for that
        application.
        
        The options SSL_ENABLE_SSL2, SSL_ENABLE_SSL3, and SSL_ENABLE_TLS can
        each be set to True or False independently of each other. NSS 2.8 and
        later versions will negotiate the highest protocol version with the
        peer application from among the set of protocols that are commonly
        enabled in both applications.
        
        Note that SSL3 and TLS share the same set of cipher suites. When both
        SSL3 and TLS are enabled, all SSL3/TLS cipher suites that are enabled
        are enabled for both SSL3 and TLS.
        
        When an application imports a socket into SSL after the TCP connection
        on that socket has already been established, it must call
        SSLSocket.reset_handshake() to indicate whether the socket is for a
        client or server. At first glance this may seem unnecessary, since
        SSLSocket.set_ssl_option() can set SSL_HANDSHAKE_AS_CLIENT or
        SSL_HANDSHAKE_AS_SERVER. However, these settings control the behavior
        of SSLSocket.connect() and SSLSocket.accept() only; if you don't call
        one of those functions after importing a non-SSL socket with
        SSL_Import (as in the case of an already established TCP connection),
        SSL still needs to know whether the application is functioning as a
        client or server.
        
        If a socket file descriptor is imported as an SSL socket before it is
        connected, it is implicitly configured to handshake as a client or
        handshake as a server when the connection is made. If the application
        calls SSLSocket.connect() (connecting as a TCP client), then the SSL
        socket is (by default) configured to handshake as an SSL client. If
        the application calls SSLSocket.accept() (connecting the socket as a
        TCP server) then the SSL socket is (by default) configured to
        handshake as an SSL server. SSL_HANDSHAKE_AS_CLIENT and
        SSL_HANDSHAKE_AS_SERVER control this implicit configuration. Both
        SSL_HANDSHAKE_AS_CLIENT and SSL_HANDSHAKE_AS_SERVER are initially set
        to off--that is, the process default for both values is False when the
        process begins. The process default can be changed from the initial
        values by using SSL_EnableDefault, and the value for a particular
        socket can be changed by using SSLSocket.set_ssl_option().
        
        If a socket that is already connected gets imported into SSL after it
        has been connected (that is, after SSLSocket.accept() or
        SSLSocket.connect() has returned), then no implicit SSL handshake
        configuration as a client or server will have been done by
        SSLSocket.connect() or SSLSocket.accept() on that socket. In this
        case, a call to SSLSocket.reset_handshake() is required to explicitly
        configure the socket to handshake as a client or as a server. If
        SSLSocket.reset_handshake() is not called to explicitly configure the
        socket handshake, a crash is likely to occur when the first I/O
        operation is done on the socket after it is imported into SSL.
        """
        pass

    def __init__(self, family=None, type=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


# variables with complex values

ssl_implemented_ciphers = (
    49195,
    49199,
    49162,
    49161,
    49171,
    49187,
    49191,
    49172,
    49160,
    49170,
    49159,
    49169,
    158,
    51,
    50,
    103,
    69,
    68,
    57,
    56,
    107,
    136,
    135,
    22,
    19,
    102,
    49156,
    49166,
    49157,
    49167,
    49155,
    49165,
    49154,
    49164,
    156,
    47,
    60,
    65,
    53,
    61,
    132,
    150,
    65279,
    10,
    5,
    4,
    21,
    18,
    65278,
    9,
    100,
    98,
    3,
    6,
    49158,
    49168,
    49163,
    49153,
    2,
    59,
    1,
    65281,
    65283,
    65287,
    65286,
    65282,
    65284,
)

_C_API = None # (!) real value is ''

