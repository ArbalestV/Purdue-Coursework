# encoding: utf-8
# module nss.io
# from /usr/lib64/python2.6/site-packages/nss/io.so
# by generator 1.136
""" This module implements the NSPR IO functions """
# no imports

# Variables with simple values

PR_AF_INET = 2
PR_AF_INET6 = 10
PR_AF_LOCAL = 1
PR_AF_UNSPEC = 0

PR_AI_ADDRCONFIG = 32
PR_AI_ALL = 8
PR_AI_DEFAULT = 48
PR_AI_NOCANONNAME = 32768
PR_AI_V4MAPPED = 16

PR_DESC_FILE = 1
PR_DESC_LAYERED = 4
PR_DESC_PIPE = 5

PR_DESC_SOCKET_TCP = 2
PR_DESC_SOCKET_UDP = 3

PR_INTERVAL_MAX = 100000
PR_INTERVAL_MIN = 1000

PR_INTERVAL_NO_TIMEOUT = 4294967295
PR_INTERVAL_NO_WAIT = 0

PR_IpAddrAny = 1
PR_IpAddrLoopback = 2
PR_IpAddrNull = 0
PR_IpAddrV4Mapped = 3

PR_POLL_ERR = 8
PR_POLL_EXCEPT = 4
PR_POLL_HUP = 32
PR_POLL_NVAL = 16
PR_POLL_READ = 1
PR_POLL_WRITE = 2

PR_SHUTDOWN_BOTH = 2
PR_SHUTDOWN_RCV = 0
PR_SHUTDOWN_SEND = 1

PR_SockOpt_AddMember = 8
PR_SockOpt_Broadcast = 15
PR_SockOpt_DropMember = 9
PR_SockOpt_IpTimeToLive = 6
PR_SockOpt_IpTypeOfService = 7
PR_SockOpt_Keepalive = 3
PR_SockOpt_Linger = 1
PR_SockOpt_MaxSegment = 14
PR_SockOpt_McastInterface = 10
PR_SockOpt_McastLoopback = 12
PR_SockOpt_McastTimeToLive = 11
PR_SockOpt_NoDelay = 13
PR_SockOpt_Nonblocking = 0
PR_SockOpt_RecvBufferSize = 4
PR_SockOpt_Reuseaddr = 2
PR_SockOpt_SendBufferSize = 5

# functions

def addr_family_name(family): # real signature unknown; restored from __doc__
    """
    addr_family_name(family) -> string
    
    :Parameters:
        family : int
            An address family constant, (i.e. PR_AF_INET)
    
    Given an address family constant returns the string name.
    """
    return ""

def get_proto_by_name(*args, **kwargs): # real signature unknown
    """ Returns the protocol number given the protocol's name. Raises exception if lookup fails. """
    pass

def get_proto_by_number(number): # real signature unknown; restored from __doc__
    """
    Returns the protocol name and a tuple of aliases given the protocol's number.
    name, aliases = get_proto_by_number(number)
    Raises an exception if the lookup fails.
    """
    pass

def htonl(*args, **kwargs): # real signature unknown
    """ 32 bit conversion from host to network """
    pass

def htons(*args, **kwargs): # real signature unknown
    """ 16 bit conversion from host to network """
    pass

def interval_now(): # real signature unknown; restored from __doc__
    """
    You can use the value returned by interval_now() to establish epochs
    and to determine intervals (that is, compute the difference
    between two times)
    """
    pass

def interval_to_microseconds(*args, **kwargs): # real signature unknown
    """ Converts platform-dependent intervals to standard clock microseconds """
    pass

def interval_to_milliseconds(*args, **kwargs): # real signature unknown
    """ Converts platform-dependent intervals to standard clock milliseconds """
    pass

def interval_to_seconds(*args, **kwargs): # real signature unknown
    """ Converts platform-dependent intervals to standard clock seconds """
    pass

def microseconds_to_interval(*args, **kwargs): # real signature unknown
    """ Converts standard clock microseconds to platform-dependent intervals. """
    pass

def milliseconds_to_interval(*args, **kwargs): # real signature unknown
    """ Converts standard clock milliseconds to platform-dependent intervals. """
    pass

def ntohl(*args, **kwargs): # real signature unknown
    """ 32 bit conversion from network to host """
    pass

def ntohs(*args, **kwargs): # real signature unknown
    """ 16 bit conversion from network to host """
    pass

def seconds_to_interval(*args, **kwargs): # real signature unknown
    """ Converts standard clock seconds to platform-dependent intervals. """
    pass

def ticks_per_second(): # real signature unknown; restored from __doc__
    """
    An integer between 1000 and 100000 indicating the number of ticks per
    second counted by PRIntervalTime on the current platform.
    
    The value returned by ticks_per_second() lies between PR_INTERVAL_MIN
    and PR_INTERVAL_MAX.
    """
    pass

# classes

class AddrInfo(object):
    """
    AddrInfo(hostname, family=PR_AF_UNSPEC, flags=PR_AI_ADDRCONFIG)
    
    :Parameters:
        hostname : str or unicode object
            Either a hostname or an address string (dotted-decimal for IPv4
            or a hex string for IPv6.
        family : int
            May be:
                 -  PR_AF_UNSPEC
                 -  PR_AF_INET.
        flags : int
            May be either:
                - PR_AI_ADDRCONFIG
                - PR_AI_ADDRCONFIG | PR_AI_NOCANONNAME
    
            Include PR_AI_NOCANONNAME to suppress the determination of
            the canonical name corresponding to hostname.
    
    An object used to encapsulate network address information for a
    specific host.
    
    After successful initialization the AddrInfo object will contain
    an ordered sequence of `NetworkAddress` objects which may be
    accessed via iteration or indexing. It is suggested you try connecting
    with the each `NetworkAddress` object in sequential order until
    one succeeds.
    
    Example Usage::
    
        try:
            addr_info = io.AddrInfo(hostname)
        except Exception, e:
            print "ERROR: could not resolve address for %s" % hostname
            return
        for net_addr in addr_info:
            net_addr.port = port
            sock = io.Socket(net_addr.family)
            try:
                sock.connect(net_addr, timeout=io.seconds_to_interval(1))
                return
            except Exception, e:
                pass
         print "ERROR: could not connect to %s at port %d" % (hostname, port)
    
    Note, the NSPR interface to getaddrinfo() does not provide a way to
    select just IPv6 addresses. The solution is filter them yourself, e.g.::
    
        for net_addr in addr_info:
           if net_addr.family != io.PR_AF_INET6: continue
    """
    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, hostname, family=None, flags=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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

    canonical_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the canonical name associated with the IP address or None if not known"""

    hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the hostname this object was initialized from"""



class HostEntry(object):
    """
    HostEntry(addr)
    
    :Parameters:
        addr : string or NetworkAddr object
            May be either a string or a NetworkAddr object.
                - If addr is string it is equivalent to GetHostByName.
                - If addr is a NetworkAddress object it is equivalent to GetHostByAddr.
    
    A HostEntry contains an official name of the host, a set of aliases
    for the host name, an address family and a set of network addresses (all
    within the single address family).
    
    After successful initialization the HostEntry object will contain
    an unordered sequence of `NetworkAddress` objects which may be
    accessed via iteration or indexing. It is suggested you try connecting
    with the each `NetworkAddress` object in sequential order until
    one succeeds.
    
    Example Usage::
    
        host_entry = io.HostEntry(hostname)
        for net_addr in host_entry:
            net_addr.port = port
            sock = io.Socket(net_addr.family)
            try:
                sock.connect(net_addr, timeout=io.seconds_to_interval(1))
                break
            except Exception, e:
                pass
    
    **WARNING:** HostEntry only supports IPv4 lookups and it's address
    list is unordered, HostEntry should be considered *deprecated*. Use
    `AddrInfo` instead.
    """
    def get_network_address(self, port=0): # real signature unknown; restored from __doc__
        """
        get_network_address(port=0)
        
        :Parameters:
            port : integer
                optional port value specifying the port to associate with the NetworkAddress.
        
        Returns the first network address associated with this HostEntry as a
        NetworkAddress object. Equivalent to get_network_addresses()[0]. Note,
        may return None if the HostEntry does not have address associated with
        it.
        """
        pass

    def get_network_addresses(self, port=0): # real signature unknown; restored from __doc__
        """
        get_network_addresses(port=0)
        
        Return a tuple of all possible network address associated with this
        HostEntry. Each item in the returned tuple is a NetworkAddress object.
        """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, addr): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    aliases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of aliases for host"""

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """address family (e.g. PR_AF_INET, etc.)"""

    hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """official name of host"""



class NetworkAddress(object):
    """
    NetworkAddress(addr, port=0, family=PR_AF_INET)
    
    :Parameters:
        addr : string or integer
            may be an int or a string.
        port : integer
            port number
        family : integer
            one of:
                - PR_AF_INET
                - PR_AF_INET6
    
    If addr argument is a string it may be either a numeric address or a
    DNS host name and is passed to the `AddrInfo` constructor along with
    the family parameter. The first address in the `AddrInfo` object is
    selected. If you need more fine grained control over which address is
    selected from the `AddrInfo` object then invoke `AddrInfo` and select
    one of the `NetworkAddress` it provides.
    
    If the addr argument is an integer it may be one of the following constants:
    
    PR_IpAddrNull
        Do not set the IP address, only set the port.
        NetworkAddress(PR_IpAddrNull, 123) is equivalent to NetworkAddress(port=123)
    
    PR_IpAddrAny
        Assign logical PR_INADDR_ANY to IP address. This wildcard value is typically
        used to establish a socket on which to listen for incoming connection requests.
    
    PR_IpAddrLoopback
        Assign logical PR_INADDR_LOOPBACK. A client can use this value to connect to
        itself without knowing the host's network address.
    PR_IpAddrV4Mapped
        Use IPv4 mapped address
    
    The optional port argument sets the port number in the NetworkAddress object.
    The port number may be modfied later by assigning to the port attribute.
    
    Example::
        
        netaddr = nss.io.NetworkAddress('www.python.org')
        print '%s %s' % (netaddr, netaddr.hostname)
        netaddr = nss.io.NetworkAddress('82.94.237.218')
        print '%s %s' % (netaddr, netaddr.hostname)
        
        Output:
        82.94.237.218:0 www.python.org
        82.94.237.218:0 dinsdale.python.org
    
    **WARNING:** NetworkAddress initialization from a string only works with IPv4
    and its use should be considered *deprecated*. Use `AddrInfo` instead.
    """
    def set_from_string(self, addr, family=None): # real signature unknown; restored from __doc__
        """
        set_from_string(addr, family=PR_AF_INET)
        
        :Parameters:
            addr : string
                the address string to convert
            family : integer
                one of:
                    - PR_AF_INET
                    - PR_AF_INET6
                    - PR_AF_UNSPEC
        
        Reinitializes the NetworkAddress object given a string.
        Identical to constructing nss.io.NetworkAddress() with a
        string value (see `NetworkAddress` constructor for documentation).
        
        **WARNING:** NetworkAddress initialization from a string only works with IPv4
        and its use should be considered *deprecated*. Use `AddrInfo` instead.
        """
        pass

    def __init__(self, addr, port=0, family=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """address as string"""

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """address family (e.g. PR_AF_INET, etc.)"""

    hostentry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """HostEntry object representing this NetworkAddress (Warning: Deprecated, use AddrInfo instead)"""

    hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If an address string was used to construct this NetworkAddress then return the canonical hostname if available, otherwise the original address string"""

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """network address port"""



class Socket(object):
    """
    Socket(family=PR_AF_INET, type=PR_DESC_SOCKET_TCP)
    
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
    
    Create a new NSPR socket:
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

    def accept_read(self, amount, timeout=None): # real signature unknown; restored from __doc__
        """
        accept_read(amount, timeout=PR_INTERVAL_NO_TIMEOUT) -> (Socket, NetworkAddress, buf)
        
        :Parameters:
            amount : integer
                the maximum number of bytes to receive
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.accept_read() combines the behavior of Socket.accept() and
        Socket.recv(). It accepts a new connection and after it performs an
        initial read on the new socket as Socket.recv() would it returns the
        newly created Socket and NetworkAddress objects for the peer as well
        as a buffer of data.
        
        Socket.accept_read() returns a tuple containing a new Socket object, a
        new Networkaddress object for the peer, and a bufer containing data
        from the first read on the Socket object.
        """
        pass

    def bind(self, addr): # real signature unknown; restored from __doc__
        """
        bind(addr)
        
        :Parameters:
            addr : NetworkAddress object
                address to bind to
        
        When a new socket is created, it has no address bound to
        it. Socket.bind() assigns the specified network address to the
        socket. If you do not care about the exact IP address assigned to the
        socket, create a NetworkAddress object using PR_INADDR_ANY. If you do
        not care about the TCP/UDP port assigned to the socket, set the port
        value of the NetworkAddress object to 0.
        
        Note that if Socket.connect() is invoked on a socket that is not
        bound, it implicitly binds an arbitrary address to the socket.
        
        Call Socket.get_sock_name to obtain the address (name) bound to a
        socket.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the socket.
        """
        pass

    def connect(self, addr, timeout=None): # real signature unknown; restored from __doc__
        """
        connect(addr, timeout=PR_INTERVAL_NO_TIMEOUT)
        
        :Parameters:
            addr : NetworkAddress object
                address to connect to
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.connect() is usually invoked on a TCP socket, but it may also
        be invoked on a UDP socket. Both cases are discussed here.
        
        If the socket is a TCP socket, Socket.connect() establishes a TCP
        connection to the peer. If the socket is not bound, it will be bound
        to an arbitrary local address.
        
        Socket.connect() blocks until either the connection is successfully
        established or an error occurs. If the timeout parameter is not
        PR_INTERVAL_NO_TIMEOUT and the connection setup cannot complete before
        the time limit, Socket.connect() fails with the error code
        PR_IO_TIMEOUT_ERROR.
        
        If the socket is a UDP socket, there is no connection setup to speak
        of, since UDP is connectionless. If Socket.connect() is invoked on a
        UDP socket, it has an overloaded meaning: Socket.connect() merely
        saves the specified address as the default peer address for the
        socket, so that subsequently one can send and receive datagrams from
        the socket using Socket.send() and Socket.recv() instead of the usual
        Socket.send_to() and Socket.recv_from().
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> integer
        
        Return the integer file descriptor of the socket.
        """
        return 0

    def get_peer_name(self): # real signature unknown; restored from __doc__
        """
        get_peer_name() -> NetworkAddress
        
        Return the network address for the connected peer socket.
        """
        return NetworkAddress

    def get_socket_option(self, option): # real signature unknown; restored from __doc__
        """
        get_socket_option(option)
        
        The method return values varies depending on the option, see below:
        
        Set socket to non-blocking IO
            ::
                
                get_socket_option(PR_SockOpt_Nonblocking) -> bool
        
        Time to linger on close if data is present in socket send buffer. 
            ::
                
                get_socket_option(PR_SockOpt_Linger) -> (polarity, interval)
        
        Allow local address reuse
            ::
                
                get_socket_option(PR_SockOpt_Reuseaddr) -> bool
        
        Keep connections alive
            ::
                
                get_socket_option(PR_SockOpt_Keepalive) -> bool
        
        Allow IP multicast loopback
            ::
                
                get_socket_option(PR_SockOpt_McastLoopback) -> bool
        
        Disable Nagle algorithm. Don't delay send to coalesce packets. 
            ::
                
                get_socket_option(PR_SockOpt_NoDelay) -> bool
        
        Enable broadcast
            ::
                
                get_socket_option(PR_SockOpt_Broadcast) -> bool
        
        Receive buffer size. 
            ::
                
                get_socket_option(PR_SockOpt_RecvBufferSize) -> size
        
        Send buffer size. 
            ::
                
                get_socket_option(PR_SockOpt_SendBufferSize) -> size
        
        Maximum segment size
            ::
                
                get_socket_option(PR_SockOpt_MaxSegment) -> size
        
        IP Time to Live
            ::
                
                get_socket_option(PR_SockOpt_IpTimeToLive) -> interval
        
        IP type of service and precedence
            ::
                
                get_socket_option(PR_SockOpt_IpTypeOfService) -> tos
        
        Add an IP group membership
            ::
                
                get_socket_option(PR_SockOpt_AddMember) -> (mcaddr, ifaddr)
        
        - mcaddr is a NetworkAddress object representing the IP multicast address of group
        - ifaddr is a NetworkAddress object representing the local IP address of the interface
        
        Drop an IP group membership
            ::
                
                get_socket_option(PR_SockOpt_DropMember) -> (mcaddr, ifaddr)
        
        - mcaddr is a NetworkAddress object representing the IP multicast address of group
        - ifaddr is a NetworkAddress object representing the local IP address of the interface
        
        Multicast Time to Live
            ::
                
                get_socket_option(PR_SockOpt_McastTimeToLive) -> interval
        
        Multicast interface address
            ::
                
                get_socket_option(PR_SockOpt_McastInterface) -> ifaddr
        
        - ifaddr is a NetworkAddress object representing the multicast interface address
        """
        pass

    def get_sock_name(self): # real signature unknown; restored from __doc__
        """
        get_sock_name() -> NetworkAddress
        
        Return the network address for this socket.
        """
        return NetworkAddress

    def import_tcp_socket(self, osfd): # real signature unknown; restored from __doc__
        """
        import_tcp_socket(osfd) -> Socket
        :Parameters:
            osfd : integer
                file descriptor of the SOCK_STREAM socket to import
        
        Returns a Socket object that uses the specified socket file descriptor for
        communication.
        """
        return Socket

    def listen(self, backlog=5): # real signature unknown; restored from __doc__
        """
        listen(backlog=5)
        
        :Parameters:
            backlog : integer
                The maximum length of the queue of pending connections.
        
        Socket.listen() turns the specified socket into a rendezvous
        socket. It creates a queue for pending connections and starts to
        listen for connection requests on the socket. The maximum size of the
        queue for pending connections is specified by the backlog
        parameter. Pending connections may be accepted by calling
        Socket.accept().
        """
        pass

    def makefile(self, mode=None, buffersize=None): # real signature unknown; restored from __doc__
        """
        makefile([mode[, buffersize]]) -> file object
        
        :Parameters:
            mode : string
                mode string identical to open(), e.g. 'r','w','rb', etc.
            buffersize : integer
                file buffer size
        
        Return a regular file object corresponding to the socket.
        The mode and buffersize arguments are as for the built-in open() function.
        """
        return file('/dev/null')

    def new_tcp_pair(self): # real signature unknown; restored from __doc__
        """
        new_tcp_pair() -> (Socket, Socket)
        
        Returns a pair of connected TCP sockets: data written to one can be read from
        the other and vice versa.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def poll(self, poll_descs, timeout): # real signature unknown; restored from __doc__
        """
        poll(poll_descs, timeout) -> (flags, ...)
        
        :Parameters:
            poll_descs : sequence of (Socket, flags) sequences
                flags is a bitwise OR of PR_POLL_* flags
            timeout : interval time
                how long to block
        
        Wait until at least one of the Socket objects is ready for the action in
        flags.  Return a sequence of flags values, each representing the state of
        the corresponding Socket in poll_descs.
        """
        pass

    def read(self, size=-1): # real signature unknown; restored from __doc__
        """
        read(size=-1)
        
        :Parameters:
            size : integer
                If specified and non-negative the maximum number of bytes to receive
                otherwise read till EOF
        
        If the length of the returned buffer is 0 this indicates the network
        connection is closed.
        """
        pass

    def readline(self, size=None): # real signature unknown; restored from __doc__
        """
        readline([size]) -> buf
        
        :Parameters:
            size : integer
                optional, read at most size bytes
        
        Read one entire line from the socket. If the size argument is present
        and non-negative, it is a maximum byte count (including the trailing
        newline) and an incomplete line may be returned. An empty string is
        returned on EOF (connection close). Note: Unlike stdio's fgets(), the
        returned string may contain null characters ('
        """
        pass

    def readlines(self, sizehint=None): # real signature unknown; restored from __doc__
        """
        readlines([sizehint]) -> [buf]
        
        :Parameters:
            sizehint : integer
                optional, read approximately sizehint bytes before returning
        
        Read until EOF using Socket.readline() and return a list containing
        the lines thus read. If the optional sizehint argument is present and
        non-negative, instead of reading up to EOF, whole lines totalling
        approximately sizehint bytes are read.
        """
        pass

    def recv(self, amount, timeout=None): # real signature unknown; restored from __doc__
        """
        recv(amount, timeout=PR_INTERVAL_NO_TIMEOUT) -> buf
        
        :Parameters:
            amount : integer
                the maximum number of bytes to receive
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.recv() blocks until some positive number of bytes are
        transferred, a timeout occurs, or an error occurs. No more than amount
        bytes will be transferred.
        
        If the length of the returned buffer is 0 this indicates the network
        connection is closed.
        """
        pass

    def recv_from(self, amount, addr, timeout=None): # real signature unknown; restored from __doc__
        """
        recv_from(amount, addr, timeout=PR_INTERVAL_NO_TIMEOUT) -> buf
        
        :Parameters:
            amount : integer
                the maximum number of bytes to receive
            addr : NetworkAddress object
                a NetworkAddress object to receive from
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.recv_from() blocks until some positive number of bytes are
        transferred, a timeout occurs, or an error occurs. No more than amount
        bytes will be transferred.
        
        If the length of the returned buffer is 0 this indicates the network
        connection is closed.
        
        Note: Socket.recv_from() is usually used with a UDP socket.
        """
        pass

    def send(self, buf, timeout=None): # real signature unknown; restored from __doc__
        """
        send(buf, timeout=PR_INTERVAL_NO_TIMEOUT) -> amount
        
        :Parameters:
            buf : buffer
                a buffer of data to transmit
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.send() blocks until all bytes are sent (unless the socket is in
        non-blocking mode), a timeout occurs, or an error occurs. In the case
        of a timeout or an error then a nss.error.NSPRError will be raised.
        
        The function returns the number of bytes actually transmitted.
        """
        pass

    def sendall(self, buf, timeout=None): # real signature unknown; restored from __doc__
        """
        sendall(buf, timeout=PR_INTERVAL_NO_TIMEOUT) -> amount
        
        :Parameters:
            buf : buffer
                a buffer of data to transmit
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.sendall() blocks until all bytes are sent (unless the socket is in
        non-blocking mode), a timeout occurs, or an error occurs. In the case
        of a timeout or an error then a nss.error.NSPRError will be raised.
        
        The function returns the number of bytes actually transmitted.
        """
        pass

    def send_to(self, buf, addr, timeout=None): # real signature unknown; restored from __doc__
        """
        send_to(buf, addr, timeout=PR_INTERVAL_NO_TIMEOUT) -> amount
        
        :Parameters:
            buf : buffer
                a buffer of data to transmit
            addr : NetworkAddress object
                a NetworkAddress object to send to
            timeout : integer
                optional timeout value expressed as a NSPR interval
        
        Socket.send_to() blocks until all bytes are sent (unless the socket is in
        non-blocking mode), a timeout occurs, or an error occurs. In the case
        of a timeout or an error then a nss.error.NSPRError will be raised.
        
        The function returns the number of bytes actually transmitted.
        
        Note: Socket.send_to() is usually used with a UDP socket.
        """
        pass

    def set_socket_option(self, option, *more): # real signature unknown; restored from __doc__
        """
        set_socket_option(option, ...)
        
        The method signature varies depending on the option, see below:
        
        Set socket to non-blocking IO
            ::
                
                set_socket_option(PR_SockOpt_Nonblocking, bool)
        
        Time to linger on close if data is present in socket send buffer. 
            ::
                
                set_socket_option(PR_SockOpt_Linger, polarity, interval)
        
        Allow local address reuse
            ::
                
                set_socket_option(PR_SockOpt_Reuseaddr, bool)
        
        Keep connections alive
            ::
                
                set_socket_option(PR_SockOpt_Keepalive, bool)
        
        Allow IP multicast loopback
            ::
                
                set_socket_option(PR_SockOpt_McastLoopback, bool)
        
        Disable Nagle algorithm. Don't delay send to coalesce packets. 
            ::
                
                set_socket_option(PR_SockOpt_NoDelay, bool)
        
        Enable broadcast
            ::
                
                set_socket_option(PR_SockOpt_Broadcast, bool)
        
        Receive buffer size. 
            ::
                
                set_socket_option(PR_SockOpt_RecvBufferSize, size)
        
        Send buffer size. 
            ::
                
                set_socket_option(PR_SockOpt_SendBufferSize, size)
        
        Maximum segment size
            ::
                
                set_socket_option(PR_SockOpt_MaxSegment, size)
        
        IP Time to Live
            ::
                
                set_socket_option(PR_SockOpt_IpTimeToLive, interval)
        
        IP type of service and precedence
            ::
                
                set_socket_option(PR_SockOpt_IpTypeOfService, tos)
        
        Add an IP group membership
            ::
                
                set_socket_option(PR_SockOpt_AddMember, mcaddr, ifaddr)
        
        - mcaddr is a NetworkAddress object representing the IP multicast address of group
        - ifaddr is a NetworkAddress object representing the local IP address of the interface
        
        Drop an IP group membership
            ::
                
                set_socket_option(PR_SockOpt_DropMember, mcaddr, ifaddr)
        
        - mcaddr is a NetworkAddress object representing the IP multicast address of group
        - ifaddr is a NetworkAddress object representing the local IP address of the interface
        
        Multicast Time to Live
            ::
                
                set_socket_option(PR_SockOpt_McastTimeToLive, interval)
        
        Multicast interface address
            ::
                
                set_socket_option(PR_SockOpt_McastInterface, ifaddr)
        
        - ifaddr is a NetworkAddress object representing the multicast interface address
        """
        pass

    def shutdown(self, how=None): # real signature unknown; restored from __doc__
        """
        shutdown(how=PR_SHUTDOWN_BOTH)
        
        :Parameters:
            how : integer
                The kind of disallowed operations on the socket.
        
                May be one of the following the following:
                
                PR_SHUTDOWN_RCV
                    Further receives will be disallowed.
                PR_SHUTDOWN_SEND
                    Further sends will be disallowed.
                PR_SHUTDOWN_BOTH
                    Further sends and receives will be disallowed.
        """
        pass

    def __init__(self, family=None, type=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
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

    desc_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """socket description: PR_DESC_FILE, PR_DESC_SOCKET_TCP, PR_DESC_SOCKET_UDP, PR_DESC_LAYERED, PR_DESC_PIPE"""

    family = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """socket family: PR_AF_INET, PR_AF_INET6, PR_AF_LOCAL, PR_AF_UNSPEC"""

    netaddr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """NetworkAddress object bound to this socket"""



# variables with complex values

_C_API = None # (!) real value is ''

