# encoding: utf-8
# module nss.error
# from /usr/lib64/python2.6/site-packages/nss/error.so
# by generator 1.136
"""
This module defines the NSPR errors and provides functions to
manipulate them.
NSPR Error Constants:

SSL_ERROR_EXPORT_ONLY_SERVER: Unable to communicate securely.  Peer does not support high-grade encryption.

SSL_ERROR_US_ONLY_SERVER: Unable to communicate securely.  Peer requires high-grade encryption which is not supported.

SSL_ERROR_NO_CYPHER_OVERLAP: Cannot communicate securely with peer: no common encryption algorithm(s).

SSL_ERROR_NO_CERTIFICATE: Unable to find the certificate or key necessary for authentication.

SSL_ERROR_BAD_CERTIFICATE: Unable to communicate securely with peer: peers's certificate was rejected.

SSL_ERROR_BAD_CLIENT: The server has encountered bad data from the client.

SSL_ERROR_BAD_SERVER: The client has encountered bad data from the server.

SSL_ERROR_UNSUPPORTED_CERTIFICATE_TYPE: Unsupported certificate type.

SSL_ERROR_UNSUPPORTED_VERSION: Peer using unsupported version of security protocol.

SSL_ERROR_WRONG_CERTIFICATE: Client authentication failed: private key in key database does not match public key in certificate database.

SSL_ERROR_BAD_CERT_DOMAIN: Unable to communicate securely with peer: requested domain name does not match the server's certificate.

SSL_ERROR_SSL2_DISABLED: Peer only supports SSL version 2, which is locally disabled.

SSL_ERROR_BAD_MAC_READ: SSL received a record with an incorrect Message Authentication Code.

SSL_ERROR_BAD_MAC_ALERT: SSL peer reports incorrect Message Authentication Code.

SSL_ERROR_BAD_CERT_ALERT: SSL peer cannot verify your certificate.

SSL_ERROR_REVOKED_CERT_ALERT: SSL peer rejected your certificate as revoked.

SSL_ERROR_EXPIRED_CERT_ALERT: SSL peer rejected your certificate as expired.

SSL_ERROR_SSL_DISABLED: Cannot connect: SSL is disabled.

SSL_ERROR_FORTEZZA_PQG: Cannot connect: SSL peer is in another FORTEZZA domain.

SSL_ERROR_UNKNOWN_CIPHER_SUITE: An unknown SSL cipher suite has been requested.

SSL_ERROR_NO_CIPHERS_SUPPORTED: No cipher suites are present and enabled in this program.

SSL_ERROR_BAD_BLOCK_PADDING: SSL received a record with bad block padding.

SSL_ERROR_RX_RECORD_TOO_LONG: SSL received a record that exceeded the maximum permissible length.

SSL_ERROR_TX_RECORD_TOO_LONG: SSL attempted to send a record that exceeded the maximum permissible length.

SSL_ERROR_RX_MALFORMED_HELLO_REQUEST: SSL received a malformed Hello Request handshake message.

SSL_ERROR_RX_MALFORMED_CLIENT_HELLO: SSL received a malformed Client Hello handshake message.

SSL_ERROR_RX_MALFORMED_SERVER_HELLO: SSL received a malformed Server Hello handshake message.

SSL_ERROR_RX_MALFORMED_CERTIFICATE: SSL received a malformed Certificate handshake message.

SSL_ERROR_RX_MALFORMED_SERVER_KEY_EXCH: SSL received a malformed Server Key Exchange handshake message.

SSL_ERROR_RX_MALFORMED_CERT_REQUEST: SSL received a malformed Certificate Request handshake message.

SSL_ERROR_RX_MALFORMED_HELLO_DONE: SSL received a malformed Server Hello Done handshake message.

SSL_ERROR_RX_MALFORMED_CERT_VERIFY: SSL received a malformed Certificate Verify handshake message.

SSL_ERROR_RX_MALFORMED_CLIENT_KEY_EXCH: SSL received a malformed Client Key Exchange handshake message.

SSL_ERROR_RX_MALFORMED_FINISHED: SSL received a malformed Finished handshake message.

SSL_ERROR_RX_MALFORMED_CHANGE_CIPHER: SSL received a malformed Change Cipher Spec record.

SSL_ERROR_RX_MALFORMED_ALERT: SSL received a malformed Alert record.

SSL_ERROR_RX_MALFORMED_HANDSHAKE: SSL received a malformed Handshake record.

SSL_ERROR_RX_MALFORMED_APPLICATION_DATA: SSL received a malformed Application Data record.

SSL_ERROR_RX_UNEXPECTED_HELLO_REQUEST: SSL received an unexpected Hello Request handshake message.

SSL_ERROR_RX_UNEXPECTED_CLIENT_HELLO: SSL received an unexpected Client Hello handshake message.

SSL_ERROR_RX_UNEXPECTED_SERVER_HELLO: SSL received an unexpected Server Hello handshake message.

SSL_ERROR_RX_UNEXPECTED_CERTIFICATE: SSL received an unexpected Certificate handshake message.

SSL_ERROR_RX_UNEXPECTED_SERVER_KEY_EXCH: SSL received an unexpected Server Key Exchange handshake message.

SSL_ERROR_RX_UNEXPECTED_CERT_REQUEST: SSL received an unexpected Certificate Request handshake message.

SSL_ERROR_RX_UNEXPECTED_HELLO_DONE: SSL received an unexpected Server Hello Done handshake message.

SSL_ERROR_RX_UNEXPECTED_CERT_VERIFY: SSL received an unexpected Certificate Verify handshake message.

SSL_ERROR_RX_UNEXPECTED_CLIENT_KEY_EXCH: SSL received an unexpected Client Key Exchange handshake message.

SSL_ERROR_RX_UNEXPECTED_FINISHED: SSL received an unexpected Finished handshake message.

SSL_ERROR_RX_UNEXPECTED_CHANGE_CIPHER: SSL received an unexpected Change Cipher Spec record.

SSL_ERROR_RX_UNEXPECTED_ALERT: SSL received an unexpected Alert record.

SSL_ERROR_RX_UNEXPECTED_HANDSHAKE: SSL received an unexpected Handshake record.

SSL_ERROR_RX_UNEXPECTED_APPLICATION_DATA: SSL received an unexpected Application Data record.

SSL_ERROR_RX_UNKNOWN_RECORD_TYPE: SSL received a record with an unknown content type.

SSL_ERROR_RX_UNKNOWN_HANDSHAKE: SSL received a handshake message with an unknown message type.

SSL_ERROR_RX_UNKNOWN_ALERT: SSL received an alert record with an unknown alert description.

SSL_ERROR_CLOSE_NOTIFY_ALERT: SSL peer has closed this connection.

SSL_ERROR_HANDSHAKE_UNEXPECTED_ALERT: SSL peer was not expecting a handshake message it received.

SSL_ERROR_DECOMPRESSION_FAILURE_ALERT: SSL peer was unable to successfully decompress an SSL record it received.

SSL_ERROR_HANDSHAKE_FAILURE_ALERT: SSL peer was unable to negotiate an acceptable set of security parameters.

SSL_ERROR_ILLEGAL_PARAMETER_ALERT: SSL peer rejected a handshake message for unacceptable content.

SSL_ERROR_UNSUPPORTED_CERT_ALERT: SSL peer does not support certificates of the type it received.

SSL_ERROR_CERTIFICATE_UNKNOWN_ALERT: SSL peer had some unspecified issue with the certificate it received.

SSL_ERROR_GENERATE_RANDOM_FAILURE: SSL experienced a failure of its random number generator.

SSL_ERROR_SIGN_HASHES_FAILURE: Unable to digitally sign data required to verify your certificate.

SSL_ERROR_EXTRACT_PUBLIC_KEY_FAILURE: SSL was unable to extract the public key from the peer's certificate.

SSL_ERROR_SERVER_KEY_EXCHANGE_FAILURE: Unspecified failure while processing SSL Server Key Exchange handshake.

SSL_ERROR_CLIENT_KEY_EXCHANGE_FAILURE: Unspecified failure while processing SSL Client Key Exchange handshake.

SSL_ERROR_ENCRYPTION_FAILURE: Bulk data encryption algorithm failed in selected cipher suite.

SSL_ERROR_DECRYPTION_FAILURE: Bulk data decryption algorithm failed in selected cipher suite.

SSL_ERROR_SOCKET_WRITE_FAILURE: Attempt to write encrypted data to underlying socket failed.

SSL_ERROR_MD5_DIGEST_FAILURE: MD5 digest function failed.

SSL_ERROR_SHA_DIGEST_FAILURE: SHA-1 digest function failed.

SSL_ERROR_MAC_COMPUTATION_FAILURE: MAC computation failed.

SSL_ERROR_SYM_KEY_CONTEXT_FAILURE: Failure to create Symmetric Key context.

SSL_ERROR_SYM_KEY_UNWRAP_FAILURE: Failure to unwrap the Symmetric key in Client Key Exchange message.

SSL_ERROR_PUB_KEY_SIZE_LIMIT_EXCEEDED: SSL Server attempted to use domestic-grade public key with export cipher suite.

SSL_ERROR_IV_PARAM_FAILURE: PKCS11 code failed to translate an IV into a param.

SSL_ERROR_INIT_CIPHER_SUITE_FAILURE: Failed to initialize the selected cipher suite.

SSL_ERROR_SESSION_KEY_GEN_FAILURE: Client failed to generate session keys for SSL session.

SSL_ERROR_NO_SERVER_KEY_FOR_ALG: Server has no key for the attempted key exchange algorithm.

SSL_ERROR_TOKEN_INSERTION_REMOVAL: PKCS#11 token was inserted or removed while operation was in progress.

SSL_ERROR_TOKEN_SLOT_NOT_FOUND: No PKCS#11 token could be found to do a required operation.

SSL_ERROR_NO_COMPRESSION_OVERLAP: Cannot communicate securely with peer: no common compression algorithm(s).

SSL_ERROR_HANDSHAKE_NOT_COMPLETED: Cannot initiate another SSL handshake until current handshake is complete.

SSL_ERROR_BAD_HANDSHAKE_HASH_VALUE: Received incorrect handshakes hash values from peer.

SSL_ERROR_CERT_KEA_MISMATCH: The certificate provided cannot be used with the selected key exchange algorithm.

SSL_ERROR_NO_TRUSTED_SSL_CLIENT_CA: No certificate authority is trusted for SSL client authentication.

SSL_ERROR_SESSION_NOT_FOUND: Client's SSL session ID not found in server's session cache.

SSL_ERROR_DECRYPTION_FAILED_ALERT: Peer was unable to decrypt an SSL record it received.

SSL_ERROR_RECORD_OVERFLOW_ALERT: Peer received an SSL record that was longer than is permitted.

SSL_ERROR_UNKNOWN_CA_ALERT: Peer does not recognize and trust the CA that issued your certificate.

SSL_ERROR_ACCESS_DENIED_ALERT: Peer received a valid certificate, but access was denied.

SSL_ERROR_DECODE_ERROR_ALERT: Peer could not decode an SSL handshake message.

SSL_ERROR_DECRYPT_ERROR_ALERT: Peer reports failure of signature verification or key exchange.

SSL_ERROR_EXPORT_RESTRICTION_ALERT: Peer reports negotiation not in compliance with export regulations.

SSL_ERROR_PROTOCOL_VERSION_ALERT: Peer reports incompatible or unsupported protocol version.

SSL_ERROR_INSUFFICIENT_SECURITY_ALERT: Server requires ciphers more secure than those supported by client.

SSL_ERROR_INTERNAL_ERROR_ALERT: Peer reports it experienced an internal error.

SSL_ERROR_USER_CANCELED_ALERT: Peer user canceled handshake.

SSL_ERROR_NO_RENEGOTIATION_ALERT: Peer does not permit renegotiation of SSL security parameters.

SSL_ERROR_SERVER_CACHE_NOT_CONFIGURED: SSL server cache not configured and not disabled for this socket.

SSL_ERROR_UNSUPPORTED_EXTENSION_ALERT: SSL peer does not support requested TLS hello extension.

SSL_ERROR_CERTIFICATE_UNOBTAINABLE_ALERT: SSL peer could not obtain your certificate from the supplied URL.

SSL_ERROR_UNRECOGNIZED_NAME_ALERT: SSL peer has no certificate for the requested DNS name.

SSL_ERROR_BAD_CERT_STATUS_RESPONSE_ALERT: SSL peer was unable to get an OCSP response for its certificate.

SSL_ERROR_BAD_CERT_HASH_VALUE_ALERT: SSL peer reported bad certificate hash value.

SEC_ERROR_IO: An I/O error occurred during security authorization.

SEC_ERROR_LIBRARY_FAILURE: security library failure.

SEC_ERROR_BAD_DATA: security library: received bad data.

SEC_ERROR_OUTPUT_LEN: security library: output length error.

SEC_ERROR_INPUT_LEN: security library has experienced an input length error.

SEC_ERROR_INVALID_ARGS: security library: invalid arguments.

SEC_ERROR_INVALID_ALGORITHM: security library: invalid algorithm.

SEC_ERROR_INVALID_AVA: security library: invalid AVA.

SEC_ERROR_INVALID_TIME: Improperly formatted time string.

SEC_ERROR_BAD_DER: security library: improperly formatted DER-encoded message.

SEC_ERROR_BAD_SIGNATURE: Peer's certificate has an invalid signature.

SEC_ERROR_EXPIRED_CERTIFICATE: Peer's Certificate has expired.

SEC_ERROR_REVOKED_CERTIFICATE: Peer's Certificate has been revoked.

SEC_ERROR_UNKNOWN_ISSUER: Peer's Certificate issuer is not recognized.

SEC_ERROR_BAD_KEY: Peer's public key is invalid.

SEC_ERROR_BAD_PASSWORD: The security password entered is incorrect.

SEC_ERROR_RETRY_PASSWORD: New password entered incorrectly.  Please try again.

SEC_ERROR_NO_NODELOCK: security library: no nodelock.

SEC_ERROR_BAD_DATABASE: security library: bad database.

SEC_ERROR_NO_MEMORY: security library: memory allocation failure.

SEC_ERROR_UNTRUSTED_ISSUER: Peer's certificate issuer has been marked as not trusted by the user.

SEC_ERROR_UNTRUSTED_CERT: Peer's certificate has been marked as not trusted by the user.

SEC_ERROR_DUPLICATE_CERT: Certificate already exists in your database.

SEC_ERROR_DUPLICATE_CERT_NAME: Downloaded certificate's name duplicates one already in your database.

SEC_ERROR_ADDING_CERT: Error adding certificate to database.

SEC_ERROR_FILING_KEY: Error refiling the key for this certificate.

SEC_ERROR_NO_KEY: The private key for this certificate cannot be found in key database

SEC_ERROR_CERT_VALID: This certificate is valid.

SEC_ERROR_CERT_NOT_VALID: This certificate is not valid.

SEC_ERROR_CERT_NO_RESPONSE: Cert Library: No Response

SEC_ERROR_EXPIRED_ISSUER_CERTIFICATE: The certificate issuer's certificate has expired.  Check your system date and time.

SEC_ERROR_CRL_EXPIRED: The CRL for the certificate's issuer has expired.  Update it or check your system date and time.

SEC_ERROR_CRL_BAD_SIGNATURE: The CRL for the certificate's issuer has an invalid signature.

SEC_ERROR_CRL_INVALID: New CRL has an invalid format.

SEC_ERROR_EXTENSION_VALUE_INVALID: Certificate extension value is invalid.

SEC_ERROR_EXTENSION_NOT_FOUND: Certificate extension not found.

SEC_ERROR_CA_CERT_INVALID: Issuer certificate is invalid.

SEC_ERROR_PATH_LEN_CONSTRAINT_INVALID: Certificate path length constraint is invalid.

SEC_ERROR_CERT_USAGES_INVALID: Certificate usages field is invalid.

SEC_INTERNAL_ONLY: **Internal ONLY module**

SEC_ERROR_INVALID_KEY: The key does not support the requested operation.

SEC_ERROR_UNKNOWN_CRITICAL_EXTENSION: Certificate contains unknown critical extension.

SEC_ERROR_OLD_CRL: New CRL is not later than the current one.

SEC_ERROR_NO_EMAIL_CERT: Not encrypted or signed: you do not yet have an email certificate.

SEC_ERROR_NO_RECIPIENT_CERTS_QUERY: Not encrypted: you do not have certificates for each of the recipients.

SEC_ERROR_NOT_A_RECIPIENT: Cannot decrypt: you are not a recipient, or matching certificate and private key not found.

SEC_ERROR_PKCS7_KEYALG_MISMATCH: Cannot decrypt: key encryption algorithm does not match your certificate.

SEC_ERROR_PKCS7_BAD_SIGNATURE: Signature verification failed: no signer found, too many signers found, or improper or corrupted data.

SEC_ERROR_UNSUPPORTED_KEYALG: Unsupported or unknown key algorithm.

SEC_ERROR_DECRYPTION_DISALLOWED: Cannot decrypt: encrypted using a disallowed algorithm or key size.

XP_SEC_FORTEZZA_BAD_CARD: Fortezza card has not been properly initialized.  Please remove it and return it to your issuer.

XP_SEC_FORTEZZA_NO_CARD: No Fortezza cards Found

XP_SEC_FORTEZZA_NONE_SELECTED: No Fortezza card selected

XP_SEC_FORTEZZA_MORE_INFO: Please select a personality to get more info on

XP_SEC_FORTEZZA_PERSON_NOT_FOUND: Personality not found

XP_SEC_FORTEZZA_NO_MORE_INFO: No more information on that Personality

XP_SEC_FORTEZZA_BAD_PIN: Invalid Pin

XP_SEC_FORTEZZA_PERSON_ERROR: Couldn't initialize Fortezza personalities.

SEC_ERROR_NO_KRL: No KRL for this site's certificate has been found.

SEC_ERROR_KRL_EXPIRED: The KRL for this site's certificate has expired.

SEC_ERROR_KRL_BAD_SIGNATURE: The KRL for this site's certificate has an invalid signature.

SEC_ERROR_REVOKED_KEY: The key for this site's certificate has been revoked.

SEC_ERROR_KRL_INVALID: New KRL has an invalid format.

SEC_ERROR_NEED_RANDOM: security library: need random data.

SEC_ERROR_NO_MODULE: security library: no security module can perform the requested operation.

SEC_ERROR_NO_TOKEN: The security card or token does not exist, needs to be initialized, or has been removed.

SEC_ERROR_READ_ONLY: security library: read-only database.

SEC_ERROR_NO_SLOT_SELECTED: No slot or token was selected.

SEC_ERROR_CERT_NICKNAME_COLLISION: A certificate with the same nickname already exists.

SEC_ERROR_KEY_NICKNAME_COLLISION: A key with the same nickname already exists.

SEC_ERROR_SAFE_NOT_CREATED: error while creating safe object

SEC_ERROR_BAGGAGE_NOT_CREATED: error while creating baggage object

XP_JAVA_REMOVE_PRINCIPAL_ERROR: Couldn't remove the principal

XP_JAVA_DELETE_PRIVILEGE_ERROR: Couldn't delete the privilege

XP_JAVA_CERT_NOT_EXISTS_ERROR: This principal doesn't have a certificate

SEC_ERROR_BAD_EXPORT_ALGORITHM: Required algorithm is not allowed.

SEC_ERROR_EXPORTING_CERTIFICATES: Error attempting to export certificates.

SEC_ERROR_IMPORTING_CERTIFICATES: Error attempting to import certificates.

SEC_ERROR_PKCS12_DECODING_PFX: Unable to import.  Decoding error.  File not valid.

SEC_ERROR_PKCS12_INVALID_MAC: Unable to import.  Invalid MAC.  Incorrect password or corrupt file.

SEC_ERROR_PKCS12_UNSUPPORTED_MAC_ALGORITHM: Unable to import.  MAC algorithm not supported.

SEC_ERROR_PKCS12_UNSUPPORTED_TRANSPORT_MODE: Unable to import.  Only password integrity and privacy modes supported.

SEC_ERROR_PKCS12_CORRUPT_PFX_STRUCTURE: Unable to import.  File structure is corrupt.

SEC_ERROR_PKCS12_UNSUPPORTED_PBE_ALGORITHM: Unable to import.  Encryption algorithm not supported.

SEC_ERROR_PKCS12_UNSUPPORTED_VERSION: Unable to import.  File version not supported.

SEC_ERROR_PKCS12_PRIVACY_PASSWORD_INCORRECT: Unable to import.  Incorrect privacy password.

SEC_ERROR_PKCS12_CERT_COLLISION: Unable to import.  Same nickname already exists in database.

SEC_ERROR_USER_CANCELLED: The user pressed cancel.

SEC_ERROR_PKCS12_DUPLICATE_DATA: Not imported, already in database.

SEC_ERROR_MESSAGE_SEND_ABORTED: Message not sent.

SEC_ERROR_INADEQUATE_KEY_USAGE: Certificate key usage inadequate for attempted operation.

SEC_ERROR_INADEQUATE_CERT_TYPE: Certificate type not approved for application.

SEC_ERROR_CERT_ADDR_MISMATCH: Address in signing certificate does not match address in message headers.

SEC_ERROR_PKCS12_UNABLE_TO_IMPORT_KEY: Unable to import.  Error attempting to import private key.

SEC_ERROR_PKCS12_IMPORTING_CERT_CHAIN: Unable to import.  Error attempting to import certificate chain.

SEC_ERROR_PKCS12_UNABLE_TO_LOCATE_OBJECT_BY_NAME: Unable to export.  Unable to locate certificate or key by nickname.

SEC_ERROR_PKCS12_UNABLE_TO_EXPORT_KEY: Unable to export.  Private Key could not be located and exported.

SEC_ERROR_PKCS12_UNABLE_TO_WRITE: Unable to export.  Unable to write the export file.

SEC_ERROR_PKCS12_UNABLE_TO_READ: Unable to import.  Unable to read the import file.

SEC_ERROR_PKCS12_KEY_DATABASE_NOT_INITIALIZED: Unable to export.  Key database corrupt or deleted.

SEC_ERROR_KEYGEN_FAIL: Unable to generate public/private key pair.

SEC_ERROR_INVALID_PASSWORD: Password entered is invalid.  Please pick a different one.

SEC_ERROR_RETRY_OLD_PASSWORD: Old password entered incorrectly.  Please try again.

SEC_ERROR_BAD_NICKNAME: Certificate nickname already in use.

SEC_ERROR_NOT_FORTEZZA_ISSUER: Peer FORTEZZA chain has a non-FORTEZZA Certificate.

SEC_ERROR_CANNOT_MOVE_SENSITIVE_KEY: A sensitive key cannot be moved to the slot where it is needed.

SEC_ERROR_JS_INVALID_MODULE_NAME: Invalid module name.

SEC_ERROR_JS_INVALID_DLL: Invalid module path/filename

SEC_ERROR_JS_ADD_MOD_FAILURE: Unable to add module

SEC_ERROR_JS_DEL_MOD_FAILURE: Unable to delete module

SEC_ERROR_OLD_KRL: New KRL is not later than the current one.

SEC_ERROR_CKL_CONFLICT: New CKL has different issuer than current CKL.  Delete current CKL.

SEC_ERROR_CERT_NOT_IN_NAME_SPACE: The Certifying Authority for this certificate is not permitted to issue a certificate with this name.

SEC_ERROR_KRL_NOT_YET_VALID: The key revocation list for this certificate is not yet valid.

SEC_ERROR_CRL_NOT_YET_VALID: The certificate revocation list for this certificate is not yet valid.

SEC_ERROR_UNKNOWN_CERT: The requested certificate could not be found.

SEC_ERROR_UNKNOWN_SIGNER: The signer's certificate could not be found.

SEC_ERROR_CERT_BAD_ACCESS_LOCATION: The location for the certificate status server has invalid format.

SEC_ERROR_OCSP_UNKNOWN_RESPONSE_TYPE: The OCSP response cannot be fully decoded; it is of an unknown type.

SEC_ERROR_OCSP_BAD_HTTP_RESPONSE: The OCSP server returned unexpected/invalid HTTP data.

SEC_ERROR_OCSP_MALFORMED_REQUEST: The OCSP server found the request to be corrupted or improperly formed.

SEC_ERROR_OCSP_SERVER_ERROR: The OCSP server experienced an internal error.

SEC_ERROR_OCSP_TRY_SERVER_LATER: The OCSP server suggests trying again later.

SEC_ERROR_OCSP_REQUEST_NEEDS_SIG: The OCSP server requires a signature on this request.

SEC_ERROR_OCSP_UNAUTHORIZED_REQUEST: The OCSP server has refused this request as unauthorized.

SEC_ERROR_OCSP_UNKNOWN_RESPONSE_STATUS: The OCSP server returned an unrecognizable status.

SEC_ERROR_OCSP_UNKNOWN_CERT: The OCSP server has no status for the certificate.

SEC_ERROR_OCSP_NOT_ENABLED: You must enable OCSP before performing this operation.

SEC_ERROR_OCSP_NO_DEFAULT_RESPONDER: You must set the OCSP default responder before performing this operation.

SEC_ERROR_OCSP_MALFORMED_RESPONSE: The response from the OCSP server was corrupted or improperly formed.

SEC_ERROR_OCSP_UNAUTHORIZED_RESPONSE: The signer of the OCSP response is not authorized to give status for this certificate.

SEC_ERROR_OCSP_FUTURE_RESPONSE: The OCSP response is not yet valid (contains a date in the future).

SEC_ERROR_OCSP_OLD_RESPONSE: The OCSP response contains out-of-date information.

SEC_ERROR_DIGEST_NOT_FOUND: The CMS or PKCS #7 Digest was not found in signed message.

SEC_ERROR_UNSUPPORTED_MESSAGE_TYPE: The CMS or PKCS #7 Message type is unsupported.

SEC_ERROR_MODULE_STUCK: PKCS #11 module could not be removed because it is still in use.

SEC_ERROR_BAD_TEMPLATE: Could not decode ASN.1 data. Specified template was invalid.

SEC_ERROR_CRL_NOT_FOUND: No matching CRL was found.

SEC_ERROR_REUSED_ISSUER_AND_SERIAL: You are attempting to import a cert with the same issuer/serial as an existing cert, but that is not the same cert.

SEC_ERROR_BUSY: NSS could not shutdown. Objects are still in use.

SEC_ERROR_EXTRA_INPUT: DER-encoded message contained extra unused data.

SEC_ERROR_UNSUPPORTED_ELLIPTIC_CURVE: Unsupported elliptic curve.

SEC_ERROR_UNSUPPORTED_EC_POINT_FORM: Unsupported elliptic curve point form.

SEC_ERROR_UNRECOGNIZED_OID: Unrecognized Object Identifier.

SEC_ERROR_OCSP_INVALID_SIGNING_CERT: Invalid OCSP signing certificate in OCSP response.

SEC_ERROR_REVOKED_CERTIFICATE_CRL: Certificate is revoked in issuer's certificate revocation list.

SEC_ERROR_REVOKED_CERTIFICATE_OCSP: Issuer's OCSP responder reports certificate is revoked.

SEC_ERROR_CRL_INVALID_VERSION: Issuer's Certificate Revocation List has an unknown version number.

SEC_ERROR_CRL_V1_CRITICAL_EXTENSION: Issuer's V1 Certificate Revocation List has a critical extension.

SEC_ERROR_CRL_UNKNOWN_CRITICAL_EXTENSION: Issuer's V2 Certificate Revocation List has an unknown critical extension.

SEC_ERROR_UNKNOWN_OBJECT_TYPE: Unknown object type specified.

SEC_ERROR_INCOMPATIBLE_PKCS11: PKCS #11 driver violates the spec in an incompatible way.

SEC_ERROR_NO_EVENT: No new slot event is available at this time.

SEC_ERROR_CRL_ALREADY_EXISTS: CRL already exists.

SEC_ERROR_NOT_INITIALIZED: NSS is not initialized.

SEC_ERROR_TOKEN_NOT_LOGGED_IN: The operation failed because the PKCS#11 token is not logged in.

SEC_ERROR_OCSP_RESPONDER_CERT_INVALID: OCSP Trusted Responder Cert is invalid.

SEC_ERROR_OCSP_BAD_SIGNATURE: OCSP response has an invalid signature.

PR_OUT_OF_MEMORY_ERROR: Memory allocation attempt failed.

PR_BAD_DESCRIPTOR_ERROR: Invalid file descriptor.

PR_WOULD_BLOCK_ERROR: The operation would have blocked.

PR_ACCESS_FAULT_ERROR: Invalid memory address argument.

PR_INVALID_METHOD_ERROR: Invalid function for file type.

PR_ILLEGAL_ACCESS_ERROR: Invalid memory address argument.

PR_UNKNOWN_ERROR: Some unknown error has occurred.

PR_PENDING_INTERRUPT_ERROR: Operation interrupted by another thread.

PR_NOT_IMPLEMENTED_ERROR: function not implemented.

PR_IO_ERROR: I/O function error.

PR_IO_TIMEOUT_ERROR: I/O operation timed out.

PR_IO_PENDING_ERROR: I/O operation on busy file descriptor.

PR_DIRECTORY_OPEN_ERROR: The directory could not be opened.

PR_INVALID_ARGUMENT_ERROR: Invalid function argument.

PR_ADDRESS_NOT_AVAILABLE_ERROR: Network address not available (in use?).

PR_ADDRESS_NOT_SUPPORTED_ERROR: Network address type not supported.

PR_IS_CONNECTED_ERROR: Already connected.

PR_BAD_ADDRESS_ERROR: Network address is invalid.

PR_ADDRESS_IN_USE_ERROR: Local Network address is in use.

PR_CONNECT_REFUSED_ERROR: Connection refused by peer.

PR_NETWORK_UNREACHABLE_ERROR: Network address is presently unreachable.

PR_CONNECT_TIMEOUT_ERROR: Connection attempt timed out.

PR_NOT_CONNECTED_ERROR: Network file descriptor is not connected.

PR_LOAD_LIBRARY_ERROR: Failure to load dynamic library.

PR_UNLOAD_LIBRARY_ERROR: Failure to unload dynamic library.

PR_FIND_SYMBOL_ERROR: Symbol not found in any of the loaded dynamic libraries.

PR_INSUFFICIENT_RESOURCES_ERROR: Insufficient system resources.

PR_DIRECTORY_LOOKUP_ERROR: A directory lookup on a network address has failed.

PR_TPD_RANGE_ERROR: Attempt to access a TPD key that is out of range.

PR_PROC_DESC_TABLE_FULL_ERROR: Process open FD table is full.

PR_SYS_DESC_TABLE_FULL_ERROR: System open FD table is full.

PR_NOT_SOCKET_ERROR: Network operation attempted on non-network file descriptor.

PR_NOT_TCP_SOCKET_ERROR: TCP-specific function attempted on a non-TCP file descriptor.

PR_SOCKET_ADDRESS_IS_BOUND_ERROR: TCP file descriptor is already bound.

PR_NO_ACCESS_RIGHTS_ERROR: Access Denied.

PR_OPERATION_NOT_SUPPORTED_ERROR: The requested operation is not supported by the platform.

PR_PROTOCOL_NOT_SUPPORTED_ERROR: The host operating system does not support the protocol requested.

PR_REMOTE_FILE_ERROR: Access to the remote file has been severed.

PR_BUFFER_OVERFLOW_ERROR: The value requested is too large to be stored in the data buffer provided.

PR_CONNECT_RESET_ERROR: TCP connection reset by peer.

PR_RANGE_ERROR: Unused.

PR_DEADLOCK_ERROR: The operation would have deadlocked.

PR_FILE_IS_LOCKED_ERROR: The file is already locked.

PR_FILE_TOO_BIG_ERROR: Write would result in file larger than the system allows.

PR_NO_DEVICE_SPACE_ERROR: The device for storing the file is full.

PR_PIPE_ERROR: Unused.

PR_NO_SEEK_DEVICE_ERROR: Unused.

PR_IS_DIRECTORY_ERROR: Cannot perform a normal file operation on a directory.

PR_LOOP_ERROR: Symbolic link loop.

PR_NAME_TOO_LONG_ERROR: File name is too long.

PR_FILE_NOT_FOUND_ERROR: File not found.

PR_NOT_DIRECTORY_ERROR: Cannot perform directory operation on a normal file.

PR_READ_ONLY_FILESYSTEM_ERROR: Cannot write to a read-only file system.

PR_DIRECTORY_NOT_EMPTY_ERROR: Cannot delete a directory that is not empty.

PR_FILESYSTEM_MOUNTED_ERROR: Cannot delete or rename a file object while the file system is busy.

PR_NOT_SAME_DEVICE_ERROR: Cannot rename a file to a file system on another device.

PR_DIRECTORY_CORRUPTED_ERROR: The directory object in the file system is corrupted.

PR_FILE_EXISTS_ERROR: Cannot create or rename a filename that already exists.

PR_MAX_DIRECTORY_ENTRIES_ERROR: Directory is full.  No additional filenames may be added.

PR_INVALID_DEVICE_STATE_ERROR: The required device was in an invalid state.

PR_DEVICE_IS_LOCKED_ERROR: The device is locked.

PR_NO_MORE_FILES_ERROR: No more entries in the directory.

PR_END_OF_FILE_ERROR: Encountered end of file.

PR_FILE_SEEK_ERROR: Seek error.

PR_FILE_IS_BUSY_ERROR: The file is busy.

PR_IN_PROGRESS_ERROR: Operation is still in progress (probably a non-blocking connect).

PR_ALREADY_INITIATED_ERROR: Operation has already been initiated (probably a non-blocking connect).

PR_GROUP_EMPTY_ERROR: The wait group is empty.

PR_INVALID_STATE_ERROR: Object state improper for request.

PR_NETWORK_DOWN_ERROR: Network is down.

PR_SOCKET_SHUTDOWN_ERROR: The socket was previously shut down.

PR_CONNECT_ABORTED_ERROR: TCP Connection aborted.

PR_HOST_UNREACHABLE_ERROR: Host is unreachable.

PR_MAX_ERROR: Placeholder for the end of the list
"""
# no imports

# Variables with simple values

PR_ACCESS_FAULT_ERROR = -5997

PR_ADDRESS_IN_USE_ERROR = -5982

PR_ADDRESS_NOT_AVAILABLE_ERROR = -5986

PR_ADDRESS_NOT_SUPPORTED_ERROR = -5985

PR_ALREADY_INITIATED_ERROR = -5933

PR_BAD_ADDRESS_ERROR = -5983

PR_BAD_DESCRIPTOR_ERROR = -5999

PR_BUFFER_OVERFLOW_ERROR = -5962

PR_CONNECT_ABORTED_ERROR = -5928

PR_CONNECT_REFUSED_ERROR = -5981

PR_CONNECT_RESET_ERROR = -5961

PR_CONNECT_TIMEOUT_ERROR = -5979

PR_DEADLOCK_ERROR = -5959

PR_DEVICE_IS_LOCKED_ERROR = -5940

PR_DIRECTORY_CORRUPTED_ERROR = -5944

PR_DIRECTORY_LOOKUP_ERROR = -5973

PR_DIRECTORY_NOT_EMPTY_ERROR = -5947

PR_DIRECTORY_OPEN_ERROR = -5988

PR_END_OF_FILE_ERROR = -5938

PR_FILESYSTEM_MOUNTED_ERROR = -5946

PR_FILE_EXISTS_ERROR = -5943

PR_FILE_IS_BUSY_ERROR = -5936

PR_FILE_IS_LOCKED_ERROR = -5958

PR_FILE_NOT_FOUND_ERROR = -5950

PR_FILE_SEEK_ERROR = -5937

PR_FILE_TOO_BIG_ERROR = -5957

PR_FIND_SYMBOL_ERROR = -5975

PR_GROUP_EMPTY_ERROR = -5932

PR_HOST_UNREACHABLE_ERROR = -5927

PR_ILLEGAL_ACCESS_ERROR = -5995

PR_INSUFFICIENT_RESOURCES_ERROR = -5974

PR_INVALID_ARGUMENT_ERROR = -5987

PR_INVALID_DEVICE_STATE_ERROR = -5941

PR_INVALID_METHOD_ERROR = -5996

PR_INVALID_STATE_ERROR = -5931

PR_IN_PROGRESS_ERROR = -5934

PR_IO_ERROR = -5991

PR_IO_PENDING_ERROR = -5989

PR_IO_TIMEOUT_ERROR = -5990

PR_IS_CONNECTED_ERROR = -5984

PR_IS_DIRECTORY_ERROR = -5953

PR_LOAD_LIBRARY_ERROR = -5977

PR_LOOP_ERROR = -5952

PR_MAX_DIRECTORY_ENTRIES_ERROR = -5942

PR_MAX_ERROR = -5924

PR_NAME_TOO_LONG_ERROR = -5951

PR_NETWORK_DOWN_ERROR = -5930

PR_NETWORK_UNREACHABLE_ERROR = -5980

PR_NOT_CONNECTED_ERROR = -5978

PR_NOT_DIRECTORY_ERROR = -5949

PR_NOT_IMPLEMENTED_ERROR = -5992

PR_NOT_SAME_DEVICE_ERROR = -5945

PR_NOT_SOCKET_ERROR = -5969

PR_NOT_TCP_SOCKET_ERROR = -5968

PR_NO_ACCESS_RIGHTS_ERROR = -5966

PR_NO_DEVICE_SPACE_ERROR = -5956

PR_NO_MORE_FILES_ERROR = -5939

PR_NO_SEEK_DEVICE_ERROR = -5954

PR_OPERATION_NOT_SUPPORTED_ERROR = -5965

PR_OUT_OF_MEMORY_ERROR = -6000

PR_PENDING_INTERRUPT_ERROR = -5993

PR_PIPE_ERROR = -5955

PR_PROC_DESC_TABLE_FULL_ERROR = -5971

PR_PROTOCOL_NOT_SUPPORTED_ERROR = -5964

PR_RANGE_ERROR = -5960

PR_READ_ONLY_FILESYSTEM_ERROR = -5948

PR_REMOTE_FILE_ERROR = -5963

PR_SOCKET_ADDRESS_IS_BOUND_ERROR = -5967

PR_SOCKET_SHUTDOWN_ERROR = -5929

PR_SYS_DESC_TABLE_FULL_ERROR = -5970

PR_TPD_RANGE_ERROR = -5972

PR_UNKNOWN_ERROR = -5994

PR_UNLOAD_LIBRARY_ERROR = -5976

PR_WOULD_BLOCK_ERROR = -5998

SEC_ERROR_ADDING_CERT = -8168

SEC_ERROR_BAD_DATA = -8190
SEC_ERROR_BAD_DATABASE = -8174
SEC_ERROR_BAD_DER = -8183

SEC_ERROR_BAD_EXPORT_ALGORITHM = -8117

SEC_ERROR_BAD_KEY = -8178
SEC_ERROR_BAD_NICKNAME = -8089
SEC_ERROR_BAD_PASSWORD = -8177
SEC_ERROR_BAD_SIGNATURE = -8182
SEC_ERROR_BAD_TEMPLATE = -8056

SEC_ERROR_BAGGAGE_NOT_CREATED = -8121

SEC_ERROR_BUSY = -8053

SEC_ERROR_CANNOT_MOVE_SENSITIVE_KEY = -8087

SEC_ERROR_CA_CERT_INVALID = -8156

SEC_ERROR_CERT_ADDR_MISMATCH = -8100

SEC_ERROR_CERT_BAD_ACCESS_LOCATION = -8075

SEC_ERROR_CERT_NICKNAME_COLLISION = -8124

SEC_ERROR_CERT_NOT_IN_NAME_SPACE = -8080

SEC_ERROR_CERT_NOT_VALID = -8164

SEC_ERROR_CERT_NO_RESPONSE = -8163

SEC_ERROR_CERT_USAGES_INVALID = -8154

SEC_ERROR_CERT_VALID = -8165

SEC_ERROR_CKL_CONFLICT = -8081

SEC_ERROR_CRL_ALREADY_EXISTS = -8039

SEC_ERROR_CRL_BAD_SIGNATURE = -8160

SEC_ERROR_CRL_EXPIRED = -8161
SEC_ERROR_CRL_INVALID = -8159

SEC_ERROR_CRL_INVALID_VERSION = -8045

SEC_ERROR_CRL_NOT_FOUND = -8055

SEC_ERROR_CRL_NOT_YET_VALID = -8078

SEC_ERROR_CRL_UNKNOWN_CRITICAL_EXTENSION = -8043

SEC_ERROR_CRL_V1_CRITICAL_EXTENSION = -8044

SEC_ERROR_DECRYPTION_DISALLOWED = -8143

SEC_ERROR_DIGEST_NOT_FOUND = -8059

SEC_ERROR_DUPLICATE_CERT = -8170

SEC_ERROR_DUPLICATE_CERT_NAME = -8169

SEC_ERROR_EXPIRED_CERTIFICATE = -8181

SEC_ERROR_EXPIRED_ISSUER_CERTIFICATE = -8162

SEC_ERROR_EXPORTING_CERTIFICATES = -8116

SEC_ERROR_EXTENSION_NOT_FOUND = -8157

SEC_ERROR_EXTENSION_VALUE_INVALID = -8158

SEC_ERROR_EXTRA_INPUT = -8052

SEC_ERROR_FILING_KEY = -8167

SEC_ERROR_IMPORTING_CERTIFICATES = -8115

SEC_ERROR_INADEQUATE_CERT_TYPE = -8101

SEC_ERROR_INADEQUATE_KEY_USAGE = -8102

SEC_ERROR_INCOMPATIBLE_PKCS11 = -8041

SEC_ERROR_INPUT_LEN = -8188

SEC_ERROR_INVALID_ALGORITHM = -8186
SEC_ERROR_INVALID_ARGS = -8187
SEC_ERROR_INVALID_AVA = -8185
SEC_ERROR_INVALID_KEY = -8152
SEC_ERROR_INVALID_PASSWORD = -8091
SEC_ERROR_INVALID_TIME = -8184

SEC_ERROR_IO = -8192

SEC_ERROR_JS_ADD_MOD_FAILURE = -8084

SEC_ERROR_JS_DEL_MOD_FAILURE = -8083

SEC_ERROR_JS_INVALID_DLL = -8085

SEC_ERROR_JS_INVALID_MODULE_NAME = -8086

SEC_ERROR_KEYGEN_FAIL = -8092

SEC_ERROR_KEY_NICKNAME_COLLISION = -8123

SEC_ERROR_KRL_BAD_SIGNATURE = -8132

SEC_ERROR_KRL_EXPIRED = -8133
SEC_ERROR_KRL_INVALID = -8130

SEC_ERROR_KRL_NOT_YET_VALID = -8079

SEC_ERROR_LIBRARY_FAILURE = -8191

SEC_ERROR_MESSAGE_SEND_ABORTED = -8103

SEC_ERROR_MODULE_STUCK = -8057

SEC_ERROR_NEED_RANDOM = -8129

SEC_ERROR_NOT_A_RECIPIENT = -8147

SEC_ERROR_NOT_FORTEZZA_ISSUER = -8088

SEC_ERROR_NOT_INITIALIZED = -8038

SEC_ERROR_NO_EMAIL_CERT = -8149

SEC_ERROR_NO_EVENT = -8040
SEC_ERROR_NO_KEY = -8166
SEC_ERROR_NO_KRL = -8134
SEC_ERROR_NO_MEMORY = -8173
SEC_ERROR_NO_MODULE = -8128
SEC_ERROR_NO_NODELOCK = -8175

SEC_ERROR_NO_RECIPIENT_CERTS_QUERY = -8148

SEC_ERROR_NO_SLOT_SELECTED = -8125

SEC_ERROR_NO_TOKEN = -8127

SEC_ERROR_OCSP_BAD_HTTP_RESPONSE = -8073

SEC_ERROR_OCSP_BAD_SIGNATURE = -8035

SEC_ERROR_OCSP_FUTURE_RESPONSE = -8061

SEC_ERROR_OCSP_INVALID_SIGNING_CERT = -8048

SEC_ERROR_OCSP_MALFORMED_REQUEST = -8072
SEC_ERROR_OCSP_MALFORMED_RESPONSE = -8063

SEC_ERROR_OCSP_NOT_ENABLED = -8065

SEC_ERROR_OCSP_NO_DEFAULT_RESPONDER = -8064

SEC_ERROR_OCSP_OLD_RESPONSE = -8060

SEC_ERROR_OCSP_REQUEST_NEEDS_SIG = -8069

SEC_ERROR_OCSP_RESPONDER_CERT_INVALID = -8036

SEC_ERROR_OCSP_SERVER_ERROR = -8071

SEC_ERROR_OCSP_TRY_SERVER_LATER = -8070

SEC_ERROR_OCSP_UNAUTHORIZED_REQUEST = -8068
SEC_ERROR_OCSP_UNAUTHORIZED_RESPONSE = -8062

SEC_ERROR_OCSP_UNKNOWN_CERT = -8066

SEC_ERROR_OCSP_UNKNOWN_RESPONSE_STATUS = -8067
SEC_ERROR_OCSP_UNKNOWN_RESPONSE_TYPE = -8074

SEC_ERROR_OLD_CRL = -8150
SEC_ERROR_OLD_KRL = -8082

SEC_ERROR_OUTPUT_LEN = -8189

SEC_ERROR_PATH_LEN_CONSTRAINT_INVALID = -8155

SEC_ERROR_PKCS12_CERT_COLLISION = -8106

SEC_ERROR_PKCS12_CORRUPT_PFX_STRUCTURE = -8110

SEC_ERROR_PKCS12_DECODING_PFX = -8114

SEC_ERROR_PKCS12_DUPLICATE_DATA = -8104

SEC_ERROR_PKCS12_IMPORTING_CERT_CHAIN = -8098

SEC_ERROR_PKCS12_INVALID_MAC = -8113

SEC_ERROR_PKCS12_KEY_DATABASE_NOT_INITIALIZED = -8093

SEC_ERROR_PKCS12_PRIVACY_PASSWORD_INCORRECT = -8107

SEC_ERROR_PKCS12_UNABLE_TO_EXPORT_KEY = -8096

SEC_ERROR_PKCS12_UNABLE_TO_IMPORT_KEY = -8099

SEC_ERROR_PKCS12_UNABLE_TO_LOCATE_OBJECT_BY_NAME = -8097

SEC_ERROR_PKCS12_UNABLE_TO_READ = -8094
SEC_ERROR_PKCS12_UNABLE_TO_WRITE = -8095

SEC_ERROR_PKCS12_UNSUPPORTED_MAC_ALGORITHM = -8112

SEC_ERROR_PKCS12_UNSUPPORTED_PBE_ALGORITHM = -8109

SEC_ERROR_PKCS12_UNSUPPORTED_TRANSPORT_MODE = -8111

SEC_ERROR_PKCS12_UNSUPPORTED_VERSION = -8108

SEC_ERROR_PKCS7_BAD_SIGNATURE = -8145

SEC_ERROR_PKCS7_KEYALG_MISMATCH = -8146

SEC_ERROR_READ_ONLY = -8126

SEC_ERROR_RETRY_OLD_PASSWORD = -8090

SEC_ERROR_RETRY_PASSWORD = -8176

SEC_ERROR_REUSED_ISSUER_AND_SERIAL = -8054

SEC_ERROR_REVOKED_CERTIFICATE = -8180

SEC_ERROR_REVOKED_CERTIFICATE_CRL = -8047
SEC_ERROR_REVOKED_CERTIFICATE_OCSP = -8046

SEC_ERROR_REVOKED_KEY = -8131

SEC_ERROR_SAFE_NOT_CREATED = -8122

SEC_ERROR_TOKEN_NOT_LOGGED_IN = -8037

SEC_ERROR_UNKNOWN_CERT = -8077

SEC_ERROR_UNKNOWN_CRITICAL_EXTENSION = -8151

SEC_ERROR_UNKNOWN_ISSUER = -8179

SEC_ERROR_UNKNOWN_OBJECT_TYPE = -8042

SEC_ERROR_UNKNOWN_SIGNER = -8076

SEC_ERROR_UNRECOGNIZED_OID = -8049

SEC_ERROR_UNSUPPORTED_EC_POINT_FORM = -8050

SEC_ERROR_UNSUPPORTED_ELLIPTIC_CURVE = -8051

SEC_ERROR_UNSUPPORTED_KEYALG = -8144

SEC_ERROR_UNSUPPORTED_MESSAGE_TYPE = -8058

SEC_ERROR_UNTRUSTED_CERT = -8171
SEC_ERROR_UNTRUSTED_ISSUER = -8172

SEC_ERROR_USER_CANCELLED = -8105

SEC_INTERNAL_ONLY = -8153

SSL_ERROR_ACCESS_DENIED_ALERT = -12194

SSL_ERROR_BAD_BLOCK_PADDING = -12264

SSL_ERROR_BAD_CERTIFICATE = -12284

SSL_ERROR_BAD_CERT_ALERT = -12271
SSL_ERROR_BAD_CERT_DOMAIN = -12276

SSL_ERROR_BAD_CERT_HASH_VALUE_ALERT = -12180

SSL_ERROR_BAD_CERT_STATUS_RESPONSE_ALERT = -12181

SSL_ERROR_BAD_CLIENT = -12282

SSL_ERROR_BAD_HANDSHAKE_HASH_VALUE = -12201

SSL_ERROR_BAD_MAC_ALERT = -12272
SSL_ERROR_BAD_MAC_READ = -12273

SSL_ERROR_BAD_SERVER = -12281

SSL_ERROR_CERTIFICATE_UNKNOWN_ALERT = -12224

SSL_ERROR_CERTIFICATE_UNOBTAINABLE_ALERT = -12183

SSL_ERROR_CERT_KEA_MISMATCH = -12200

SSL_ERROR_CLIENT_KEY_EXCHANGE_FAILURE = -12219

SSL_ERROR_CLOSE_NOTIFY_ALERT = -12230

SSL_ERROR_DECODE_ERROR_ALERT = -12193

SSL_ERROR_DECOMPRESSION_FAILURE_ALERT = -12228

SSL_ERROR_DECRYPTION_FAILED_ALERT = -12197

SSL_ERROR_DECRYPTION_FAILURE = -12217

SSL_ERROR_DECRYPT_ERROR_ALERT = -12192

SSL_ERROR_ENCRYPTION_FAILURE = -12218

SSL_ERROR_EXPIRED_CERT_ALERT = -12269

SSL_ERROR_EXPORT_ONLY_SERVER = -12288

SSL_ERROR_EXPORT_RESTRICTION_ALERT = -12191

SSL_ERROR_EXTRACT_PUBLIC_KEY_FAILURE = -12221

SSL_ERROR_FORTEZZA_PQG = -12267

SSL_ERROR_GENERATE_RANDOM_FAILURE = -12223

SSL_ERROR_HANDSHAKE_FAILURE_ALERT = -12227

SSL_ERROR_HANDSHAKE_NOT_COMPLETED = -12202

SSL_ERROR_HANDSHAKE_UNEXPECTED_ALERT = -12229

SSL_ERROR_ILLEGAL_PARAMETER_ALERT = -12226

SSL_ERROR_INIT_CIPHER_SUITE_FAILURE = -12208

SSL_ERROR_INSUFFICIENT_SECURITY_ALERT = -12189

SSL_ERROR_INTERNAL_ERROR_ALERT = -12188

SSL_ERROR_IV_PARAM_FAILURE = -12209

SSL_ERROR_MAC_COMPUTATION_FAILURE = -12213

SSL_ERROR_MD5_DIGEST_FAILURE = -12215

SSL_ERROR_NO_CERTIFICATE = -12285

SSL_ERROR_NO_CIPHERS_SUPPORTED = -12265

SSL_ERROR_NO_COMPRESSION_OVERLAP = -12203

SSL_ERROR_NO_CYPHER_OVERLAP = -12286

SSL_ERROR_NO_RENEGOTIATION_ALERT = -12186

SSL_ERROR_NO_SERVER_KEY_FOR_ALG = -12206

SSL_ERROR_NO_TRUSTED_SSL_CLIENT_CA = -12199

SSL_ERROR_PROTOCOL_VERSION_ALERT = -12190

SSL_ERROR_PUB_KEY_SIZE_LIMIT_EXCEEDED = -12210

SSL_ERROR_RECORD_OVERFLOW_ALERT = -12196

SSL_ERROR_REVOKED_CERT_ALERT = -12270

SSL_ERROR_RX_MALFORMED_ALERT = -12250

SSL_ERROR_RX_MALFORMED_APPLICATION_DATA = -12248

SSL_ERROR_RX_MALFORMED_CERTIFICATE = -12258

SSL_ERROR_RX_MALFORMED_CERT_REQUEST = -12256
SSL_ERROR_RX_MALFORMED_CERT_VERIFY = -12254

SSL_ERROR_RX_MALFORMED_CHANGE_CIPHER = -12251

SSL_ERROR_RX_MALFORMED_CLIENT_HELLO = -12260

SSL_ERROR_RX_MALFORMED_CLIENT_KEY_EXCH = -12253

SSL_ERROR_RX_MALFORMED_FINISHED = -12252
SSL_ERROR_RX_MALFORMED_HANDSHAKE = -12249

SSL_ERROR_RX_MALFORMED_HELLO_DONE = -12255
SSL_ERROR_RX_MALFORMED_HELLO_REQUEST = -12261

SSL_ERROR_RX_MALFORMED_SERVER_HELLO = -12259

SSL_ERROR_RX_MALFORMED_SERVER_KEY_EXCH = -12257

SSL_ERROR_RX_RECORD_TOO_LONG = -12263

SSL_ERROR_RX_UNEXPECTED_ALERT = -12236

SSL_ERROR_RX_UNEXPECTED_APPLICATION_DATA = -12234

SSL_ERROR_RX_UNEXPECTED_CERTIFICATE = -12244

SSL_ERROR_RX_UNEXPECTED_CERT_REQUEST = -12242
SSL_ERROR_RX_UNEXPECTED_CERT_VERIFY = -12240

SSL_ERROR_RX_UNEXPECTED_CHANGE_CIPHER = -12237

SSL_ERROR_RX_UNEXPECTED_CLIENT_HELLO = -12246

SSL_ERROR_RX_UNEXPECTED_CLIENT_KEY_EXCH = -12239

SSL_ERROR_RX_UNEXPECTED_FINISHED = -12238
SSL_ERROR_RX_UNEXPECTED_HANDSHAKE = -12235

SSL_ERROR_RX_UNEXPECTED_HELLO_DONE = -12241
SSL_ERROR_RX_UNEXPECTED_HELLO_REQUEST = -12247

SSL_ERROR_RX_UNEXPECTED_SERVER_HELLO = -12245

SSL_ERROR_RX_UNEXPECTED_SERVER_KEY_EXCH = -12243

SSL_ERROR_RX_UNKNOWN_ALERT = -12231
SSL_ERROR_RX_UNKNOWN_HANDSHAKE = -12232

SSL_ERROR_RX_UNKNOWN_RECORD_TYPE = -12233

SSL_ERROR_SERVER_CACHE_NOT_CONFIGURED = -12185

SSL_ERROR_SERVER_KEY_EXCHANGE_FAILURE = -12220

SSL_ERROR_SESSION_KEY_GEN_FAILURE = -12207

SSL_ERROR_SESSION_NOT_FOUND = -12198

SSL_ERROR_SHA_DIGEST_FAILURE = -12214

SSL_ERROR_SIGN_HASHES_FAILURE = -12222

SSL_ERROR_SOCKET_WRITE_FAILURE = -12216

SSL_ERROR_SSL2_DISABLED = -12274

SSL_ERROR_SSL_DISABLED = -12268

SSL_ERROR_SYM_KEY_CONTEXT_FAILURE = -12212

SSL_ERROR_SYM_KEY_UNWRAP_FAILURE = -12211

SSL_ERROR_TOKEN_INSERTION_REMOVAL = -12205

SSL_ERROR_TOKEN_SLOT_NOT_FOUND = -12204

SSL_ERROR_TX_RECORD_TOO_LONG = -12262

SSL_ERROR_UNKNOWN_CA_ALERT = -12195

SSL_ERROR_UNKNOWN_CIPHER_SUITE = -12266

SSL_ERROR_UNRECOGNIZED_NAME_ALERT = -12182

SSL_ERROR_UNSUPPORTED_CERTIFICATE_TYPE = -12280

SSL_ERROR_UNSUPPORTED_CERT_ALERT = -12225

SSL_ERROR_UNSUPPORTED_EXTENSION_ALERT = -12184

SSL_ERROR_UNSUPPORTED_VERSION = -12279

SSL_ERROR_USER_CANCELED_ALERT = -12187

SSL_ERROR_US_ONLY_SERVER = -12287

SSL_ERROR_WRONG_CERTIFICATE = -12277

XP_JAVA_CERT_NOT_EXISTS_ERROR = -8118

XP_JAVA_DELETE_PRIVILEGE_ERROR = -8119

XP_JAVA_REMOVE_PRINCIPAL_ERROR = -8120

XP_SEC_FORTEZZA_BAD_CARD = -8142
XP_SEC_FORTEZZA_BAD_PIN = -8136

XP_SEC_FORTEZZA_MORE_INFO = -8139

XP_SEC_FORTEZZA_NONE_SELECTED = -8140

XP_SEC_FORTEZZA_NO_CARD = -8141

XP_SEC_FORTEZZA_NO_MORE_INFO = -8137

XP_SEC_FORTEZZA_PERSON_ERROR = -8135

XP_SEC_FORTEZZA_PERSON_NOT_FOUND = -8138

# functions

def get_nspr_error_string(number): # real signature unknown; restored from __doc__
    """
    get_nspr_error_string(number) -> string
    
    Given an NSPR error number, returns it's string description
    """
    return ""

# classes

class NSPRError(EnvironmentError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

_C_API = None # (!) real value is ''

