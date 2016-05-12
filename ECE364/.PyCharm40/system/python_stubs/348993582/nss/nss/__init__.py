# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

# Variables with simple values

AsDottedDecimal = 9
AsEnum = 5
AsEnumDescription = 7
AsEnumName = 6
AsIndex = 8
AsLabeledString = 4
AsObject = 0
AsString = 1
AsTypeEnum = 3
AsTypeString = 2

certDirectoryName = 5
certDNSName = 3
certEDIPartyName = 6
certificateUsageAnyCA = 2048
certificateUsageCheckAllUsages = 0
certificateUsageEmailRecipient = 32
certificateUsageEmailSigner = 16
certificateUsageObjectSigner = 64
certificateUsageProtectedObjectSigner = 512
certificateUsageSSLCA = 8
certificateUsageSSLClient = 1
certificateUsageSSLServer = 2
certificateUsageSSLServerWithStepUp = 4
certificateUsageStatusResponder = 1024
certificateUsageUserCertImport = 128
certificateUsageVerifyCA = 256
certIPAddress = 8
certOtherName = 1
certRegisterID = 9
certRFC822Name = 2
certURI = 7
certX400Address = 4

CKA_AC_ISSUER = 131

CKA_ALLOWED_MECHANISMS = 1073743360

CKA_ALWAYS_AUTHENTICATE = 514
CKA_ALWAYS_SENSITIVE = 357

CKA_APPLICATION = 16

CKA_ATTR_TYPES = 133

CKA_AUTH_PIN_FLAGS = 513

CKA_BASE = 306

CKA_BITS_PER_PIXEL = 1030

CKA_CERTIFICATE_CATEGORY = 135
CKA_CERTIFICATE_TYPE = 128

CKA_CHAR_COLUMNS = 1028
CKA_CHAR_ROWS = 1027
CKA_CHAR_SETS = 1152

CKA_CHECK_VALUE = 144

CKA_CLASS = 0
CKA_COEFFICIENT = 296
CKA_COLOR = 1029
CKA_DECRYPT = 261

CKA_DEFAULT_CMS_ATTRIBUTES = 1282

CKA_DERIVE = 268

CKA_ECDSA_PARAMS = 384

CKA_EC_PARAMS = 384
CKA_EC_POINT = 385

CKA_ENCODING_METHODS = 1153

CKA_ENCRYPT = 260

CKA_END_DATE = 273

CKA_EXPONENT_1 = 294
CKA_EXPONENT_2 = 295

CKA_EXTRACTABLE = 354

CKA_HASH_OF_ISSUER_PUBLIC_KEY = 139

CKA_HASH_OF_SUBJECT_PUBLIC_KEY = 138

CKA_HAS_RESET = 770

CKA_HW_FEATURE_TYPE = 768

CKA_ID = 258
CKA_ISSUER = 129

CKA_JAVA_MIDP_SECURITY_DOMAIN = 136

CKA_KEY_GEN_MECHANISM = 358

CKA_KEY_TYPE = 256

CKA_LABEL = 3
CKA_LOCAL = 355

CKA_MECHANISM_TYPE = 1280

CKA_MIME_TYPES = 1154

CKA_MODIFIABLE = 368
CKA_MODULUS = 288

CKA_MODULUS_BITS = 289

CKA_NEVER_EXTRACTABLE = 356

CKA_OBJECT_ID = 18

CKA_OWNER = 132

CKA_PIXEL_X = 1024
CKA_PIXEL_Y = 1025

CKA_PRIME = 304

CKA_PRIME_1 = 292
CKA_PRIME_2 = 293
CKA_PRIME_BITS = 307

CKA_PRIVATE = 2

CKA_PRIVATE_EXPONENT = 291

CKA_PUBLIC_EXPONENT = 290

CKA_REQUIRED_CMS_ATTRIBUTES = 1281

CKA_RESET_ON_INIT = 769

CKA_RESOLUTION = 1026

CKA_SECONDARY_AUTH = 512

CKA_SENSITIVE = 259

CKA_SERIAL_NUMBER = 130

CKA_SIGN = 264

CKA_SIGN_RECOVER = 265

CKA_START_DATE = 272

CKA_SUBJECT = 257
CKA_SUBPRIME = 305

CKA_SUBPRIME_BITS = 308

CKA_SUB_PRIME_BITS = 308

CKA_SUPPORTED_CMS_ATTRIBUTES = 1283

CKA_TOKEN = 1
CKA_TRUSTED = 134
CKA_UNWRAP = 263

CKA_UNWRAP_TEMPLATE = 1073742354

CKA_URL = 137
CKA_VALUE = 17

CKA_VALUE_BITS = 352
CKA_VALUE_LEN = 353

CKA_VENDOR_DEFINED = 2147483648

CKA_VERIFY = 266

CKA_VERIFY_RECOVER = 267

CKA_WRAP = 262

CKA_WRAP_TEMPLATE = 1073742353

CKA_WRAP_WITH_TRUSTED = 528

CKM_AES_CBC = 4226

CKM_AES_CBC_ENCRYPT_DATA = 4357

CKM_AES_CBC_PAD = 4229

CKM_AES_ECB = 4225

CKM_AES_ECB_ENCRYPT_DATA = 4356

CKM_AES_KEY_GEN = 4224

CKM_AES_MAC = 4227

CKM_AES_MAC_GENERAL = 4228

CKM_BATON_CBC128 = 4147
CKM_BATON_COUNTER = 4148
CKM_BATON_ECB128 = 4145
CKM_BATON_ECB96 = 4146

CKM_BATON_KEY_GEN = 4144

CKM_BATON_SHUFFLE = 4149
CKM_BATON_WRAP = 4150

CKM_BLOWFISH_CBC = 4241

CKM_BLOWFISH_KEY_GEN = 4240

CKM_CAMELLIA_CBC = 1362

CKM_CAMELLIA_CBC_ENCRYPT_DATA = 1367

CKM_CAMELLIA_CBC_PAD = 1365

CKM_CAMELLIA_ECB = 1361

CKM_CAMELLIA_ECB_ENCRYPT_DATA = 1366

CKM_CAMELLIA_KEY_GEN = 1360

CKM_CAMELLIA_MAC = 1363

CKM_CAMELLIA_MAC_GENERAL = 1364

CKM_CAST128_CBC = 802

CKM_CAST128_CBC_PAD = 805

CKM_CAST128_ECB = 801

CKM_CAST128_KEY_GEN = 800

CKM_CAST128_MAC = 803

CKM_CAST128_MAC_GENERAL = 804

CKM_CAST3_CBC = 786

CKM_CAST3_CBC_PAD = 789

CKM_CAST3_ECB = 785

CKM_CAST3_KEY_GEN = 784

CKM_CAST3_MAC = 787

CKM_CAST3_MAC_GENERAL = 788

CKM_CAST5_CBC = 802

CKM_CAST5_CBC_PAD = 805

CKM_CAST5_ECB = 801

CKM_CAST5_KEY_GEN = 800

CKM_CAST5_MAC = 803

CKM_CAST5_MAC_GENERAL = 804

CKM_CAST_CBC = 770

CKM_CAST_CBC_PAD = 773

CKM_CAST_ECB = 769

CKM_CAST_KEY_GEN = 768

CKM_CAST_MAC = 771

CKM_CAST_MAC_GENERAL = 772

CKM_CDMF_CBC = 322

CKM_CDMF_CBC_PAD = 325

CKM_CDMF_ECB = 321

CKM_CDMF_KEY_GEN = 320

CKM_CDMF_MAC = 323

CKM_CDMF_MAC_GENERAL = 324

CKM_CMS_SIG = 1280

CKM_CONCATENATE_BASE_AND_DATA = 866
CKM_CONCATENATE_BASE_AND_KEY = 864

CKM_CONCATENATE_DATA_AND_BASE = 867

CKM_DES2_KEY_GEN = 304

CKM_DES3_CBC = 307

CKM_DES3_CBC_ENCRYPT_DATA = 4355

CKM_DES3_CBC_PAD = 310

CKM_DES3_ECB = 306

CKM_DES3_ECB_ENCRYPT_DATA = 4354

CKM_DES3_KEY_GEN = 305

CKM_DES3_MAC = 308

CKM_DES3_MAC_GENERAL = 309

CKM_DES_CBC = 290

CKM_DES_CBC_ENCRYPT_DATA = 4353

CKM_DES_CBC_PAD = 293

CKM_DES_CFB64 = 338
CKM_DES_CFB8 = 339
CKM_DES_ECB = 289

CKM_DES_ECB_ENCRYPT_DATA = 4352

CKM_DES_KEY_GEN = 288

CKM_DES_MAC = 291

CKM_DES_MAC_GENERAL = 292

CKM_DES_OFB64 = 336
CKM_DES_OFB8 = 337

CKM_DH_PKCS_DERIVE = 33

CKM_DH_PKCS_KEY_PAIR_GEN = 32

CKM_DH_PKCS_PARAMETER_GEN = 8193

CKM_DSA = 17

CKM_DSA_KEY_PAIR_GEN = 16

CKM_DSA_PARAMETER_GEN = 8192

CKM_DSA_SHA1 = 18

CKM_ECDH1_COFACTOR_DERIVE = 4177

CKM_ECDH1_DERIVE = 4176

CKM_ECDSA = 4161

CKM_ECDSA_KEY_PAIR_GEN = 4160

CKM_ECDSA_SHA1 = 4162

CKM_ECMQV_DERIVE = 4178

CKM_EC_KEY_PAIR_GEN = 4160

CKM_EXTRACT_KEY_FROM_KEY = 869

CKM_FASTHASH = 4208

CKM_FORTEZZA_TIMESTAMP = 4128

CKM_GENERIC_SECRET_KEY_GEN = 848

CKM_IDEA_CBC = 834

CKM_IDEA_CBC_PAD = 837

CKM_IDEA_ECB = 833

CKM_IDEA_KEY_GEN = 832

CKM_IDEA_MAC = 835

CKM_IDEA_MAC_GENERAL = 836

CKM_JUNIPER_CBC128 = 4194
CKM_JUNIPER_COUNTER = 4195
CKM_JUNIPER_ECB128 = 4193

CKM_JUNIPER_KEY_GEN = 4192

CKM_JUNIPER_SHUFFLE = 4196
CKM_JUNIPER_WRAP = 4197

CKM_KEA_KEY_DERIVE = 4113

CKM_KEA_KEY_PAIR_GEN = 4112

CKM_KEY_WRAP_LYNKS = 1024

CKM_KEY_WRAP_SET_OAEP = 1025

CKM_MD2 = 512

CKM_MD2_HMAC = 513

CKM_MD2_HMAC_GENERAL = 514

CKM_MD2_KEY_DERIVATION = 913

CKM_MD2_RSA_PKCS = 4

CKM_MD5 = 528

CKM_MD5_HMAC = 529

CKM_MD5_HMAC_GENERAL = 530

CKM_MD5_KEY_DERIVATION = 912

CKM_MD5_RSA_PKCS = 5

CKM_PBA_SHA1_WITH_SHA1_HMAC = 960

CKM_PBE_MD2_DES_CBC = 928

CKM_PBE_MD5_CAST128_CBC = 932

CKM_PBE_MD5_CAST3_CBC = 931

CKM_PBE_MD5_CAST5_CBC = 932

CKM_PBE_MD5_CAST_CBC = 930

CKM_PBE_MD5_DES_CBC = 929

CKM_PBE_SHA1_CAST128_CBC = 933

CKM_PBE_SHA1_CAST5_CBC = 933

CKM_PBE_SHA1_DES2_EDE_CBC = 937

CKM_PBE_SHA1_DES3_EDE_CBC = 936

CKM_PBE_SHA1_RC2_128_CBC = 938

CKM_PBE_SHA1_RC2_40_CBC = 939

CKM_PBE_SHA1_RC4_128 = 934
CKM_PBE_SHA1_RC4_40 = 935

CKM_PKCS5_PBKD2 = 944

CKM_RC2_CBC = 258

CKM_RC2_CBC_PAD = 261

CKM_RC2_ECB = 257

CKM_RC2_KEY_GEN = 256

CKM_RC2_MAC = 259

CKM_RC2_MAC_GENERAL = 260

CKM_RC4 = 273

CKM_RC4_KEY_GEN = 272

CKM_RC5_CBC = 818

CKM_RC5_CBC_PAD = 821

CKM_RC5_ECB = 817

CKM_RC5_KEY_GEN = 816

CKM_RC5_MAC = 819

CKM_RC5_MAC_GENERAL = 820

CKM_RIPEMD128 = 560

CKM_RIPEMD128_HMAC = 561

CKM_RIPEMD128_HMAC_GENERAL = 562

CKM_RIPEMD128_RSA_PKCS = 7

CKM_RIPEMD160 = 576

CKM_RIPEMD160_HMAC = 577

CKM_RIPEMD160_HMAC_GENERAL = 578

CKM_RIPEMD160_RSA_PKCS = 8

CKM_RSA_9796 = 2
CKM_RSA_PKCS = 1

CKM_RSA_PKCS_KEY_PAIR_GEN = 0

CKM_RSA_PKCS_OAEP = 9
CKM_RSA_PKCS_PSS = 13

CKM_RSA_X9_31 = 11

CKM_RSA_X9_31_KEY_PAIR_GEN = 10

CKM_RSA_X_509 = 3

CKM_SEED_CBC = 1618

CKM_SEED_CBC_ENCRYPT_DATA = 1623

CKM_SEED_CBC_PAD = 1621

CKM_SEED_ECB = 1617

CKM_SEED_ECB_ENCRYPT_DATA = 1622

CKM_SEED_KEY_GEN = 1616

CKM_SEED_MAC = 1619

CKM_SEED_MAC_GENERAL = 1620

CKM_SHA1_KEY_DERIVATION = 914

CKM_SHA1_RSA_PKCS = 6

CKM_SHA1_RSA_PKCS_PSS = 14

CKM_SHA1_RSA_X9_31 = 12

CKM_SHA224 = 597

CKM_SHA224_HMAC = 598

CKM_SHA224_HMAC_GENERAL = 599

CKM_SHA224_KEY_DERIVATION = 918

CKM_SHA224_RSA_PKCS = 70

CKM_SHA224_RSA_PKCS_PSS = 71

CKM_SHA256 = 592

CKM_SHA256_HMAC = 593

CKM_SHA256_HMAC_GENERAL = 594

CKM_SHA256_KEY_DERIVATION = 915

CKM_SHA256_RSA_PKCS = 64

CKM_SHA256_RSA_PKCS_PSS = 67

CKM_SHA384 = 608

CKM_SHA384_HMAC = 609

CKM_SHA384_HMAC_GENERAL = 610

CKM_SHA384_KEY_DERIVATION = 916

CKM_SHA384_RSA_PKCS = 65

CKM_SHA384_RSA_PKCS_PSS = 68

CKM_SHA512 = 624

CKM_SHA512_HMAC = 625

CKM_SHA512_HMAC_GENERAL = 626

CKM_SHA512_KEY_DERIVATION = 917

CKM_SHA512_RSA_PKCS = 66

CKM_SHA512_RSA_PKCS_PSS = 69

CKM_SHA_1 = 544

CKM_SHA_1_HMAC = 545

CKM_SHA_1_HMAC_GENERAL = 546

CKM_SKIPJACK_CBC64 = 4098
CKM_SKIPJACK_CFB16 = 4102
CKM_SKIPJACK_CFB32 = 4101
CKM_SKIPJACK_CFB64 = 4100
CKM_SKIPJACK_CFB8 = 4103
CKM_SKIPJACK_ECB64 = 4097

CKM_SKIPJACK_KEY_GEN = 4096

CKM_SKIPJACK_OFB64 = 4099

CKM_SKIPJACK_PRIVATE_WRAP = 4105

CKM_SKIPJACK_RELAYX = 4106
CKM_SKIPJACK_WRAP = 4104

CKM_SSL3_KEY_AND_MAC_DERIVE = 882

CKM_SSL3_MASTER_KEY_DERIVE = 881

CKM_SSL3_MASTER_KEY_DERIVE_DH = 883

CKM_SSL3_MD5_MAC = 896

CKM_SSL3_PRE_MASTER_KEY_GEN = 880

CKM_SSL3_SHA1_MAC = 897

CKM_TLS_KEY_AND_MAC_DERIVE = 886

CKM_TLS_MASTER_KEY_DERIVE = 885

CKM_TLS_MASTER_KEY_DERIVE_DH = 887

CKM_TLS_PRE_MASTER_KEY_GEN = 884

CKM_TLS_PRF = 888

CKM_TWOFISH_CBC = 4243

CKM_TWOFISH_KEY_GEN = 4242

CKM_WTLS_CLIENT_KEY_AND_MAC_DERIVE = 981

CKM_WTLS_MASTER_KEY_DERIVE = 977

CKM_WTLS_MASTER_KEY_DERIVE_DH_ECC = 978

CKM_WTLS_PRE_MASTER_KEY_GEN = 976

CKM_WTLS_PRF = 979

CKM_WTLS_SERVER_KEY_AND_MAC_DERIVE = 980

CKM_X9_42_DH_DERIVE = 49

CKM_X9_42_DH_HYBRID_DERIVE = 50

CKM_X9_42_DH_KEY_PAIR_GEN = 48

CKM_X9_42_DH_PARAMETER_GEN = 8194

CKM_X9_42_MQV_DERIVE = 51

CKM_XOR_BASE_AND_DATA = 868

crlEntryReasonAaCompromise = 10
crlEntryReasonAffiliationChanged = 3
crlEntryReasonCaCompromise = 2
crlEntryReasoncertificatedHold = 6
crlEntryReasonCessationOfOperation = 5
crlEntryReasonKeyCompromise = 1
crlEntryReasonPrivilegeWithdrawn = 9
crlEntryReasonRemoveFromCRL = 8
crlEntryReasonSuperseded = 4
crlEntryReasonUnspecified = 0

CRL_DECODE_ADOPT_HEAP_DER = 8

CRL_DECODE_DEFAULT_OPTIONS = 0

CRL_DECODE_DONT_COPY_DER = 1

CRL_DECODE_KEEP_BAD_CRL = 4

CRL_DECODE_SKIP_ENTRIES = 2

CRL_IMPORT_BYPASS_CHECKS = 1

CRL_IMPORT_DEFAULT_OPTIONS = 0

dhKey = 4

dsaKey = 2

ecKey = 6

fortezzaKey = 3

generalName = 1

HEX_SEPARATOR_DEFAULT = ':'

keaKey = 5

NSS_INIT_COOPERATE = 960
NSS_INIT_FORCEOPEN = 8
NSS_INIT_NOCERTDB = 2
NSS_INIT_NOMODDB = 4
NSS_INIT_NOPK11FINALIZE = 256
NSS_INIT_NOROOTINIT = 16
NSS_INIT_OPTIMIZESPACE = 32
NSS_INIT_PK11RELOAD = 128
NSS_INIT_PK11THREADSAFE = 64
NSS_INIT_READONLY = 1
NSS_INIT_RESERVED = 512

nullKey = 0

OCTETS_PER_LINE_DEFAULT = 16

PK11_DIS_COULD_NOT_INIT_TOKEN = 2

PK11_DIS_NONE = 0

PK11_DIS_TOKEN_NOT_PRESENT = 4

PK11_DIS_TOKEN_VERIFY_FAILED = 3

PK11_DIS_USER_SELECTED = 1

PK11_OriginDerive = 1
PK11_OriginFortezzaHack = 3
PK11_OriginGenerated = 2
PK11_OriginNULL = 0
PK11_OriginUnwrap = 4

PKCS12_DES_56 = 131089

PKCS12_DES_EDE3_168 = 131090

PKCS12_RC2_CBC_128 = 131074
PKCS12_RC2_CBC_40 = 131073

PKCS12_RC4_128 = 131082
PKCS12_RC4_40 = 131081

relativeDistinguishedName = 2

rsaKey = 1

secCertTimeExpired = 1
secCertTimeNotValidYet = 2
secCertTimeValid = 0

SEC_CERT_NICKNAMES_ALL = 1
SEC_CERT_NICKNAMES_CA = 4
SEC_CERT_NICKNAMES_SERVER = 3
SEC_CERT_NICKNAMES_USER = 2

SEC_CRL_TYPE = 1

SEC_KRL_TYPE = 0

SEC_OID_AES_128_CBC = 184
SEC_OID_AES_128_ECB = 183

SEC_OID_AES_128_KEY_WRAP = 197

SEC_OID_AES_192_CBC = 186
SEC_OID_AES_192_ECB = 185

SEC_OID_AES_192_KEY_WRAP = 198

SEC_OID_AES_256_CBC = 188
SEC_OID_AES_256_ECB = 187

SEC_OID_AES_256_KEY_WRAP = 199

SEC_OID_ANSIX962_ECDSA_SHA1_SIGNATURE = 201

SEC_OID_ANSIX962_ECDSA_SHA224_SIGNATURE = 277

SEC_OID_ANSIX962_ECDSA_SHA256_SIGNATURE = 278

SEC_OID_ANSIX962_ECDSA_SHA384_SIGNATURE = 279

SEC_OID_ANSIX962_ECDSA_SHA512_SIGNATURE = 280

SEC_OID_ANSIX962_ECDSA_SIGNATURE_RECOMMENDED_DIGEST = 275

SEC_OID_ANSIX962_ECDSA_SIGNATURE_SPECIFIED_DIGEST = 276

SEC_OID_ANSIX962_ECDSA_SIGNATURE_WITH_SHA1_DIGEST = 201

SEC_OID_ANSIX962_EC_C2ONB191V4 = 229
SEC_OID_ANSIX962_EC_C2ONB191V5 = 230
SEC_OID_ANSIX962_EC_C2ONB239V4 = 235
SEC_OID_ANSIX962_EC_C2ONB239V5 = 236
SEC_OID_ANSIX962_EC_C2PNB163V1 = 222
SEC_OID_ANSIX962_EC_C2PNB163V2 = 223
SEC_OID_ANSIX962_EC_C2PNB163V3 = 224
SEC_OID_ANSIX962_EC_C2PNB176V1 = 225
SEC_OID_ANSIX962_EC_C2PNB208W1 = 231
SEC_OID_ANSIX962_EC_C2PNB272W1 = 237
SEC_OID_ANSIX962_EC_C2PNB304W1 = 238
SEC_OID_ANSIX962_EC_C2PNB368W1 = 240
SEC_OID_ANSIX962_EC_C2TNB191V1 = 226
SEC_OID_ANSIX962_EC_C2TNB191V2 = 227
SEC_OID_ANSIX962_EC_C2TNB191V3 = 228
SEC_OID_ANSIX962_EC_C2TNB239V1 = 232
SEC_OID_ANSIX962_EC_C2TNB239V2 = 233
SEC_OID_ANSIX962_EC_C2TNB239V3 = 234
SEC_OID_ANSIX962_EC_C2TNB359V1 = 239
SEC_OID_ANSIX962_EC_C2TNB431R1 = 241
SEC_OID_ANSIX962_EC_PRIME192V1 = 202
SEC_OID_ANSIX962_EC_PRIME192V2 = 203
SEC_OID_ANSIX962_EC_PRIME192V3 = 204
SEC_OID_ANSIX962_EC_PRIME239V1 = 205
SEC_OID_ANSIX962_EC_PRIME239V2 = 206
SEC_OID_ANSIX962_EC_PRIME239V3 = 207
SEC_OID_ANSIX962_EC_PRIME256V1 = 208

SEC_OID_ANSIX962_EC_PUBLIC_KEY = 200

SEC_OID_ANSIX9_DSA_SIGNATURE = 124

SEC_OID_ANSIX9_DSA_SIGNATURE_WITH_SHA1_DIGEST = 125

SEC_OID_AVA_COMMON_NAME = 41

SEC_OID_AVA_COUNTRY_NAME = 42

SEC_OID_AVA_DC = 48

SEC_OID_AVA_DN_QUALIFIER = 47

SEC_OID_AVA_GENERATION_QUALIFIER = 270

SEC_OID_AVA_GIVEN_NAME = 268

SEC_OID_AVA_HOUSE_IDENTIFIER = 271

SEC_OID_AVA_INITIALS = 269
SEC_OID_AVA_LOCALITY = 43

SEC_OID_AVA_ORGANIZATIONAL_UNIT_NAME = 46

SEC_OID_AVA_ORGANIZATION_NAME = 45

SEC_OID_AVA_POSTAL_ADDRESS = 265
SEC_OID_AVA_POSTAL_CODE = 266

SEC_OID_AVA_POST_OFFICE_BOX = 267

SEC_OID_AVA_PSEUDONYM = 272

SEC_OID_AVA_SERIAL_NUMBER = 262

SEC_OID_AVA_STATE_OR_PROVINCE = 44

SEC_OID_AVA_STREET_ADDRESS = 263

SEC_OID_AVA_SURNAME = 261
SEC_OID_AVA_TITLE = 264

SEC_OID_BOGUS_DSA_SIGNATURE_WITH_SHA1_DIGEST = 126

SEC_OID_BOGUS_KEY_USAGE = 173

SEC_OID_CAMELLIA_128_CBC = 288

SEC_OID_CAMELLIA_192_CBC = 289

SEC_OID_CAMELLIA_256_CBC = 290

SEC_OID_CERT_RENEWAL_LOCATOR = 177

SEC_OID_CMS_3DES_KEY_WRAP = 180

SEC_OID_CMS_EPHEMERAL_STATIC_DIFFIE_HELLMAN = 179

SEC_OID_CMS_RC2_KEY_WRAP = 181

SEC_OID_DES_CBC = 10
SEC_OID_DES_CFB = 12
SEC_OID_DES_ECB = 9
SEC_OID_DES_EDE = 14

SEC_OID_DES_EDE3_CBC = 7

SEC_OID_DES_MAC = 13
SEC_OID_DES_OFB = 11

SEC_OID_EXT_KEY_USAGE_CLIENT_AUTH = 147

SEC_OID_EXT_KEY_USAGE_CODE_SIGN = 148

SEC_OID_EXT_KEY_USAGE_EMAIL_PROTECT = 149

SEC_OID_EXT_KEY_USAGE_SERVER_AUTH = 146

SEC_OID_EXT_KEY_USAGE_TIME_STAMP = 150

SEC_OID_FORTEZZA_SKIPJACK = 153

SEC_OID_HMAC_SHA1 = 294
SEC_OID_HMAC_SHA224 = 295
SEC_OID_HMAC_SHA256 = 296
SEC_OID_HMAC_SHA384 = 297
SEC_OID_HMAC_SHA512 = 298

SEC_OID_ISO_SHA1_WITH_RSA_SIGNATURE = 301

SEC_OID_ISO_SHA_WITH_RSA_SIGNATURE = 15

SEC_OID_MD2 = 1
SEC_OID_MD4 = 2
SEC_OID_MD5 = 3

SEC_OID_MISSI_ALT_KEA = 59

SEC_OID_MISSI_DSS = 57

SEC_OID_MISSI_DSS_OLD = 55

SEC_OID_MISSI_KEA = 58

SEC_OID_MISSI_KEA_DSS = 56

SEC_OID_MISSI_KEA_DSS_OLD = 54

SEC_OID_MS_SMIME_ENCRYPTION_KEY_PREFERENCE = 190

SEC_OID_NETSCAPE_AOLSCREENNAME = 260
SEC_OID_NETSCAPE_NICKNAME = 175

SEC_OID_NETSCAPE_RECOVERY_REQUEST = 176

SEC_OID_NETSCAPE_SMIME_KEA = 152

SEC_OID_NS_CERT_EXT_BASE_URL = 64

SEC_OID_NS_CERT_EXT_CA_CERT_URL = 68

SEC_OID_NS_CERT_EXT_CA_CRL_URL = 67

SEC_OID_NS_CERT_EXT_CA_POLICY_URL = 70

SEC_OID_NS_CERT_EXT_CA_REVOCATION_URL = 66

SEC_OID_NS_CERT_EXT_CERT_RENEWAL_TIME = 77
SEC_OID_NS_CERT_EXT_CERT_RENEWAL_URL = 69

SEC_OID_NS_CERT_EXT_CERT_TYPE = 63

SEC_OID_NS_CERT_EXT_COMMENT = 75

SEC_OID_NS_CERT_EXT_ENTITY_LOGO = 72

SEC_OID_NS_CERT_EXT_HOMEPAGE_URL = 71

SEC_OID_NS_CERT_EXT_ISSUER_LOGO = 61

SEC_OID_NS_CERT_EXT_LOST_PASSWORD_URL = 76

SEC_OID_NS_CERT_EXT_NETSCAPE_OK = 60

SEC_OID_NS_CERT_EXT_REVOCATION_URL = 65

SEC_OID_NS_CERT_EXT_SCOPE_OF_USE = 178

SEC_OID_NS_CERT_EXT_SSL_SERVER_NAME = 74

SEC_OID_NS_CERT_EXT_SUBJECT_LOGO = 62

SEC_OID_NS_CERT_EXT_USER_PICTURE = 73

SEC_OID_NS_KEY_USAGE_GOVT_APPROVED = 78

SEC_OID_NS_TYPE_CERT_SEQUENCE = 53

SEC_OID_NS_TYPE_GIF = 49
SEC_OID_NS_TYPE_HTML = 52
SEC_OID_NS_TYPE_JPEG = 50
SEC_OID_NS_TYPE_URL = 51

SEC_OID_OCSP_RESPONDER = 151

SEC_OID_PKCS12 = 100

SEC_OID_PKCS12_BAG_IDS = 103

SEC_OID_PKCS12_CERT_AND_CRL_BAG_ID = 111

SEC_OID_PKCS12_CERT_BAG_IDS = 104

SEC_OID_PKCS12_ENVELOPING_IDS = 108

SEC_OID_PKCS12_ESPVK_IDS = 102

SEC_OID_PKCS12_KEY_BAG_ID = 110

SEC_OID_PKCS12_KEY_USAGE = 81

SEC_OID_PKCS12_MODE_IDS = 101

SEC_OID_PKCS12_OIDS = 105

SEC_OID_PKCS12_PBE_IDS = 106

SEC_OID_PKCS12_PBE_WITH_SHA1_AND_128_BIT_RC2_CBC = 118

SEC_OID_PKCS12_PBE_WITH_SHA1_AND_128_BIT_RC4 = 115

SEC_OID_PKCS12_PBE_WITH_SHA1_AND_40_BIT_RC2_CBC = 119

SEC_OID_PKCS12_PBE_WITH_SHA1_AND_40_BIT_RC4 = 116

SEC_OID_PKCS12_PBE_WITH_SHA1_AND_TRIPLE_DES_CBC = 117

SEC_OID_PKCS12_PKCS8_KEY_SHROUDING = 109

SEC_OID_PKCS12_PKCS8_SHROUDED_KEY_BAG_ID = 161

SEC_OID_PKCS12_RSA_ENCRYPTION_WITH_128_BIT_RC4 = 120

SEC_OID_PKCS12_RSA_ENCRYPTION_WITH_40_BIT_RC4 = 121

SEC_OID_PKCS12_RSA_ENCRYPTION_WITH_TRIPLE_DES = 122

SEC_OID_PKCS12_RSA_SIGNATURE_WITH_SHA1_DIGEST = 123

SEC_OID_PKCS12_SAFE_CONTENTS_ID = 160

SEC_OID_PKCS12_SDSI_CERT_BAG = 114

SEC_OID_PKCS12_SECRET_BAG_ID = 112

SEC_OID_PKCS12_SIGNATURE_IDS = 107

SEC_OID_PKCS12_V1_CERT_BAG_ID = 164

SEC_OID_PKCS12_V1_CRL_BAG_ID = 165

SEC_OID_PKCS12_V1_KEY_BAG_ID = 162

SEC_OID_PKCS12_V1_PKCS8_SHROUDED_KEY_BAG_ID = 163

SEC_OID_PKCS12_V1_SAFE_CONTENTS_BAG_ID = 167

SEC_OID_PKCS12_V1_SECRET_BAG_ID = 166

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_128_BIT_RC2_CBC = 158

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_128_BIT_RC4 = 154

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_2KEY_TRIPLE_DES_CBC = 157

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_3KEY_TRIPLE_DES_CBC = 156

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_40_BIT_RC2_CBC = 159

SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_40_BIT_RC4 = 155

SEC_OID_PKCS12_X509_CERT_CRL_BAG = 113

SEC_OID_PKCS1_MD2_WITH_RSA_ENCRYPTION = 17

SEC_OID_PKCS1_MD4_WITH_RSA_ENCRYPTION = 18

SEC_OID_PKCS1_MD5_WITH_RSA_ENCRYPTION = 19

SEC_OID_PKCS1_RSA_ENCRYPTION = 16

SEC_OID_PKCS1_SHA1_WITH_RSA_ENCRYPTION = 20

SEC_OID_PKCS1_SHA256_WITH_RSA_ENCRYPTION = 194

SEC_OID_PKCS1_SHA384_WITH_RSA_ENCRYPTION = 195

SEC_OID_PKCS1_SHA512_WITH_RSA_ENCRYPTION = 196

SEC_OID_PKCS5_PBES2 = 292

SEC_OID_PKCS5_PBE_WITH_MD2_AND_DES_CBC = 21

SEC_OID_PKCS5_PBE_WITH_MD5_AND_DES_CBC = 22

SEC_OID_PKCS5_PBE_WITH_SHA1_AND_DES_CBC = 23

SEC_OID_PKCS5_PBKDF2 = 291
SEC_OID_PKCS5_PBMAC1 = 293

SEC_OID_PKCS7 = 24

SEC_OID_PKCS7_DATA = 25

SEC_OID_PKCS7_DIGESTED_DATA = 29

SEC_OID_PKCS7_ENCRYPTED_DATA = 30

SEC_OID_PKCS7_ENVELOPED_DATA = 27

SEC_OID_PKCS7_SIGNED_DATA = 26

SEC_OID_PKCS7_SIGNED_ENVELOPED_DATA = 28

SEC_OID_PKCS9_CHALLENGE_PASSWORD = 37

SEC_OID_PKCS9_CONTENT_TYPE = 33

SEC_OID_PKCS9_COUNTER_SIGNATURE = 36

SEC_OID_PKCS9_EMAIL_ADDRESS = 31

SEC_OID_PKCS9_EXTENDED_CERTIFICATE_ATTRIBUTES = 39

SEC_OID_PKCS9_EXTENSION_REQUEST = 274

SEC_OID_PKCS9_FRIENDLY_NAME = 171

SEC_OID_PKCS9_LOCAL_KEY_ID = 172

SEC_OID_PKCS9_MESSAGE_DIGEST = 34

SEC_OID_PKCS9_SDSI_CERT = 169

SEC_OID_PKCS9_SIGNING_TIME = 35

SEC_OID_PKCS9_SMIME_CAPABILITIES = 40

SEC_OID_PKCS9_UNSTRUCTURED_ADDRESS = 38
SEC_OID_PKCS9_UNSTRUCTURED_NAME = 32

SEC_OID_PKCS9_X509_CERT = 168
SEC_OID_PKCS9_X509_CRL = 170

SEC_OID_PKIX_CA_ISSUERS = 273
SEC_OID_PKIX_CA_REPOSITORY = 300

SEC_OID_PKIX_CPS_POINTER_QUALIFIER = 128

SEC_OID_PKIX_OCSP = 130

SEC_OID_PKIX_OCSP_ARCHIVE_CUTOFF = 136

SEC_OID_PKIX_OCSP_BASIC_RESPONSE = 131

SEC_OID_PKIX_OCSP_CRL = 133
SEC_OID_PKIX_OCSP_NONCE = 132

SEC_OID_PKIX_OCSP_NO_CHECK = 135

SEC_OID_PKIX_OCSP_RESPONSE = 134

SEC_OID_PKIX_OCSP_SERVICE_LOCATOR = 137

SEC_OID_PKIX_REGCTRL_AUTHENTICATOR = 139

SEC_OID_PKIX_REGCTRL_OLD_CERT_ID = 142

SEC_OID_PKIX_REGCTRL_PKIPUBINFO = 140

SEC_OID_PKIX_REGCTRL_PKI_ARCH_OPTIONS = 141

SEC_OID_PKIX_REGCTRL_PROTOCOL_ENC_KEY = 143

SEC_OID_PKIX_REGCTRL_REGTOKEN = 138

SEC_OID_PKIX_REGINFO_CERT_REQUEST = 145

SEC_OID_PKIX_REGINFO_UTF8_PAIRS = 144

SEC_OID_PKIX_TIMESTAMPING = 299

SEC_OID_PKIX_USER_NOTICE_QUALIFIER = 129

SEC_OID_RC2_CBC = 5

SEC_OID_RC4 = 6

SEC_OID_RC5_CBC_PAD = 8

SEC_OID_RFC1274_MAIL = 99
SEC_OID_RFC1274_UID = 98

SEC_OID_SDN702_DSA_SIGNATURE = 189

SEC_OID_SECG_EC_SECP112R1 = 209
SEC_OID_SECG_EC_SECP112R2 = 210
SEC_OID_SECG_EC_SECP128R1 = 211
SEC_OID_SECG_EC_SECP128R2 = 212
SEC_OID_SECG_EC_SECP160K1 = 213
SEC_OID_SECG_EC_SECP160R1 = 214
SEC_OID_SECG_EC_SECP160R2 = 215
SEC_OID_SECG_EC_SECP192K1 = 216
SEC_OID_SECG_EC_SECP192R1 = 202
SEC_OID_SECG_EC_SECP224K1 = 217
SEC_OID_SECG_EC_SECP224R1 = 218
SEC_OID_SECG_EC_SECP256K1 = 219
SEC_OID_SECG_EC_SECP256R1 = 208
SEC_OID_SECG_EC_SECP384R1 = 220
SEC_OID_SECG_EC_SECP521R1 = 221
SEC_OID_SECG_EC_SECT113R1 = 242
SEC_OID_SECG_EC_SECT113R2 = 243
SEC_OID_SECG_EC_SECT131R1 = 244
SEC_OID_SECG_EC_SECT131R2 = 245
SEC_OID_SECG_EC_SECT163K1 = 246
SEC_OID_SECG_EC_SECT163R1 = 247
SEC_OID_SECG_EC_SECT163R2 = 248
SEC_OID_SECG_EC_SECT193R1 = 249
SEC_OID_SECG_EC_SECT193R2 = 250
SEC_OID_SECG_EC_SECT233K1 = 251
SEC_OID_SECG_EC_SECT233R1 = 252
SEC_OID_SECG_EC_SECT239K1 = 253
SEC_OID_SECG_EC_SECT283K1 = 254
SEC_OID_SECG_EC_SECT283R1 = 255
SEC_OID_SECG_EC_SECT409K1 = 256
SEC_OID_SECG_EC_SECT409R1 = 257
SEC_OID_SECG_EC_SECT571K1 = 258
SEC_OID_SECG_EC_SECT571R1 = 259

SEC_OID_SHA1 = 4
SEC_OID_SHA256 = 191
SEC_OID_SHA384 = 192
SEC_OID_SHA512 = 193

SEC_OID_SMIME_ENCRYPTION_KEY_PREFERENCE = 182

SEC_OID_UNKNOWN = 0

SEC_OID_VERISIGN_USER_NOTICES = 127

SEC_OID_X500_RSA_ENCRYPTION = 97

SEC_OID_X509_AUTH_INFO_ACCESS = 93

SEC_OID_X509_AUTH_KEY_ID = 91

SEC_OID_X509_BASIC_CONSTRAINTS = 85

SEC_OID_X509_CERTIFICATE_POLICIES = 88

SEC_OID_X509_CERT_ISSUER = 284

SEC_OID_X509_CRL_DIST_POINTS = 87

SEC_OID_X509_CRL_NUMBER = 94

SEC_OID_X509_DELTA_CRL_INDICATOR = 282

SEC_OID_X509_EXT_KEY_USAGE = 92

SEC_OID_X509_FRESHEST_CRL = 285

SEC_OID_X509_HOLD_INSTRUCTION_CODE = 281

SEC_OID_X509_INHIBIT_ANY_POLICY = 286

SEC_OID_X509_INVALID_DATE = 96

SEC_OID_X509_ISSUER_ALT_NAME = 84

SEC_OID_X509_ISSUING_DISTRIBUTION_POINT = 283

SEC_OID_X509_KEY_USAGE = 81

SEC_OID_X509_NAME_CONSTRAINTS = 86

SEC_OID_X509_POLICY_CONSTRAINTS = 90
SEC_OID_X509_POLICY_MAPPINGS = 89

SEC_OID_X509_PRIVATE_KEY_USAGE_PERIOD = 82

SEC_OID_X509_REASON_CODE = 95

SEC_OID_X509_SUBJECT_ALT_NAME = 83

SEC_OID_X509_SUBJECT_DIRECTORY_ATTR = 79

SEC_OID_X509_SUBJECT_INFO_ACCESS = 287

SEC_OID_X509_SUBJECT_KEY_ID = 80

SEC_OID_X942_DIFFIE_HELMAN_KEY = 174

ssl_kea_dh = 2
ssl_kea_ecdh = 4
ssl_kea_fortezza = 3
ssl_kea_null = 0
ssl_kea_rsa = 1

# functions

def algtag_to_mechanism(algtag): # real signature unknown; restored from __doc__
    """
    algtag_to_mechanism(algtag) -> mechanism
    
    :Parameters:
        algtag : int
            algorithm tag (e.g. SEC_OID_*)
    
    Returns the key mechanism enumeration constant (CKM_*)
    given an algorithm tag. Throws a KeyError exception if the 
    algorithm tag is invalid.
    """
    pass

def cert_crl_reason_from_name(*args, **kwargs): # real signature unknown
    """
    crl_reason_from_name(name) -> int
    
    :Parameters:
        name : string
            name of CERTCRLEntryReasonCode constant
    
    Given the name of a CERTCRLEntryReasonCode constant
    return it's integer constant
    The string comparison is case insensitive and will match with
    or without the crlEntry prefix
    """
    pass

def cert_crl_reason_name(*args, **kwargs): # real signature unknown
    """
    crl_reason_name(reason) -> string
    
    :Parameters:
        reason : int
            CERTCRLEntryReasonCode constant
    
    Given a CERTCRLEntryReasonCode constant
    return it's name as a string
    """
    pass

def cert_general_name_type_from_name(*args, **kwargs): # real signature unknown
    """
    general_name_type_from_name(name) -> int
    
    :Parameters:
        name : string
            name of CERTGeneralNameType constant
    
    Given the name of a CERTGeneralNameType constant
    return it's integer constant
    The string comparison is case insensitive and will match with
    or without the cert prefix
    """
    pass

def cert_general_name_type_name(*args, **kwargs): # real signature unknown
    """
    general_name_type_name(type) -> string
    
    :Parameters:
        type : int
            CERTGeneralNameType constant
    
    Given a CERTGeneralNameType constant
    return it's name as a string
    """
    pass

def cert_usage_flags(flags): # real signature unknown; restored from __doc__
    """
    cert_usage_flags(flags) -> ['flag_name', ...]
    
    :Parameters:
        flags : int
            certificateUsage* bit flags
    
    Given an integer with certificateUsage*
    (e.g. nss.certificateUsageSSLServer) bit flags return a sorted
    list of their string names.
    """
    pass

def create_context_by_sym_key(mechanism, operation, sym_key, sec_param=None): # real signature unknown; restored from __doc__
    """
    create_context_by_sym_key(mechanism, operation, sym_key, sec_param=None) -> PK11Context
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        operation : int
            type of operation this context will be doing. A (CKA_*) constant
            (e.g. CKA_ENCRYPT, CKA_DECRYPT, CKA_SIGN, CKA_VERIFY, CKA_DIGEST)
        sym_key : PK11SymKey object
            symmetric key
        sec_param : SecItem object or None
            mechanism parameters used to build this context or None.
    
    Create a context from a symmetric key)
    """
    return PK11Context

def create_digest_context(hash_alg): # real signature unknown; restored from __doc__
    """
    create_digest_context(hash_alg) -> PK11Context
    
    :Parameters:
        hash_alg : int
            hash algorithm enumeration (SEC_OID_*)
            e.g.: SEC_OID_MD5, SEC_OID_SHA1, SEC_OID_SHA256, SEC_OID_SHA512, etc.
    
    Create a context for performing digest (hash) operations)
    """
    return PK11Context

def data_to_hex(data, octets_per_line=0, separator=None): # real signature unknown; restored from __doc__
    """
    data_to_hex(data, octets_per_line=0, separator=':') -> string or list of strings
    
    :Parameters:
        data : buffer
            Binary data
        octets_per_line : integer
            Number of octets formatted on one line, if 0 then
            return a single string instead of an array of lines
        separator : string
            String used to seperate each octet
            If None it will be as if the empty string had been
            passed and no separator will be used.
    
    Format the binary data as hex string(s).
    Either a list of strings is returned or a single string.
    
    If octets_per_line is greater than zero then a list of
    strings will be returned where each string contains
    octets_per_line number of octets (except for the last
    string in the list which will contain the remainder of the
    octets). Returning a list of "lines" makes it convenient
    for a caller to format a block of hexadecimal data with line
    wrapping. If octets_per_line is greater than zero indicating
    a list result is desired a list is always returned even if
    the number of octets would produce only a single line.
    
    If octets_per_line is zero then a single string is returned,
    (no line splitting is performed). This is the default.
    
    The separator string is used to separate each octet. If None
    it will be as if the empty string had been passed and no
    separator will be used.
    """
    return ""

def decode_der_crl(der_crl, type=None, decode_options=None): # real signature unknown; restored from __doc__
    """
    decode_der_crl(der_crl, type=SEC_CRL_TYPE, decode_options=CRL_DECODE_DEFAULT_OPTIONS) -> SignedCRL
    
    :Parameters:
        der_crl : SecItem object
            DER encoded CRL data encapsulated in a SECItem.
        type : int
            revocation list type
            
            may be one of:
              - SEC_CRL_TYPE
              - SEC_KRL_TYPE
        decode_options : int
            bit-wise OR of the following flags:
              - CRL_DECODE_DONT_COPY_DER
              - CRL_DECODE_SKIP_ENTRIES
              - CRL_DECODE_KEEP_BAD_CRL
              - CRL_DECODE_ADOPT_HEAP_DER
            
            or use CRL_DECODE_DEFAULT_OPTIONS
    """
    return SignedCRL

def der_universal_secitem_fmt_lines(sec_item, level=0, octets_per_line=0, separator=None): # real signature unknown; restored from __doc__
    """
    der_universal_secitem_fmt_lines(sec_item, level=0, octets_per_line=0, separator=':') -> list of (indent, string) tuples
    
    :Parameters:
        sec_item : SecItem object
            A SecItem containing a DER encoded ASN1 universal type
        level : integer
            Initial indentation level, all subsequent indents are relative
            to this starting level.
        octets_per_line : integer
            Number of octets formatted on one line, if 0 then
            return a single string instead of an array of lines
        separator : string
            String used to seperate each octet
            If None it will be as if the empty string had been
            passed and no separator will be used.
    
    Given a SecItem in DER format which encodes a ASN.1 universal
    type convert the item to a string and return a list of
    (indent, string) tuples.
    """
    return []

def dump_certificate_cache_info(): # real signature unknown; restored from __doc__
    """
    dump_certificate_cache_info()
    
    Dump the contents of the certificate cache and the temporary
    cert store to stdout.
    
    Use this as a debugging aid to detect leaked references of certs at
    shutdown time. For example if `nss.nss_shutdown()` throws a
    SEC_ERROR_BUSY exception.
    """
    pass

def find_cert_from_nickname(nickname, *user_data): # real signature unknown; restored from __doc__
    """
    find_cert_from_nickname(nickname, [user_data1, ...]) -> Certificate
    
    :Parameters:
        nickname : string
            certificate nickname to search for
        user_dataN : object ...
            zero or more caller supplied parameters which will
            be passed to the password callback function
    
    A nickname is an alias for a certificate subject. There may be
    multiple certificates with the same subject, and hence the same
    nickname. This function will return the newest certificate that
    matches the subject, based on the NotBefore / NotAfter fields of the
    certificate.
    """
    return Certificate

def find_key_by_any_cert(cert, *user_data): # real signature unknown; restored from __doc__
    """
    find_key_by_any_cert(cert, [user_data1, ...]) -> Certificate
    
    :Parameters:
        cert : Certificate object
            certificate whose private key is being searched for
        user_dataN : object ...
            zero or more caller supplied parameters which will
            be passed to the password callback function
    
    Finds the private key associated with a specified certificate in any
    available slot.
    """
    return Certificate

def find_slot_by_name(name): # real signature unknown; restored from __doc__
    """
    find_slot_by_name(name) -> `PK11Slot`
    
    :Parameters:
        name : string
            slot name
    
    Given a slot name return a `PK11Slot` object.
    """
    pass

def fingerprint_format_lines(data, level=0): # real signature unknown; restored from __doc__
    """
    fingerprint_format_lines(data, level=0) -> 
    
    :Parameters:
        data : SecItem or str or any buffer compatible object
            Data to initialize the certificate request from, must be in DER format
        level : integer
            Initial indentation level, all subsequent indents are relative
            to this starting level.
    
    Generates digests of data (i.e. fingerprint) and formats
    it into line tuples for text output.
    """
    pass

def generate_new_param(mechanism, sym_key=None): # real signature unknown; restored from __doc__
    """
    generate_new_param(mechanism, sym_key=None) -> SecItem
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        sym_key : PK11SymKey object or None
            symmetric key or None
    
    Return a SecItem containing a encryption param.
    """
    return SecItem

def generate_random(num_bytes): # real signature unknown; restored from __doc__
    """
    generate_random(num_bytes) -> string
    
    :Parameters:
        num_bytes : integer
            Number of num_bytes to generate (must be non-negative)
    
    Generates random data..
    """
    return ""

def get_best_slot(mechanism, *user_data): # real signature unknown; restored from __doc__
    """
    get_best_slot(mechanism, [user_data1, ...]) -> PK11Slot
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        user_dataN : object ...
            zero or more caller supplied parameters which will
            be passed to the password callback function
    
    Find the best slot which supports the given mechanism.
    """
    return PK11Slot

def get_block_size(mechanism, sec_param=None): # real signature unknown; restored from __doc__
    """
    get_block_size(mechanism, sec_param=None) -> int
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        sec_param : SecItem object or None
            mechanism parameters used to build this context or None.
    
    Get the mechanism block size
    """
    return 0

def get_cert_nicknames(certdb, what, *user_data): # real signature unknown; restored from __doc__
    """
    get_cert_nicknames(certdb, what, [user_data1, ...]) -> name0, ...
    
    :Parameters:
        certdb : CertDB object
            CertDB certificate database object
        what : integer
            one of:
                - SEC_CERT_NICKNAMES_ALL
                - SEC_CERT_NICKNAMES_USER
                - SEC_CERT_NICKNAMES_SERVER
                - SEC_CERT_NICKNAMES_CA
        user_dataN : object
            zero or more caller supplied parameters which will
            be passed to the password callback function
    
    Returns a tuple of the nicknames of the certificates in a specified
    certificate database.
    """
    pass

def get_default_certdb(): # real signature unknown; restored from __doc__
    """
    get_default_certdb()
    
    Returns the default certificate database as a CertDB object
    """
    pass

def get_internal_key_slot(): # real signature unknown; restored from __doc__
    """
    get_internal_key_slot() -> PK11Slot
    
    Get the default internal key slot.
    """
    return PK11Slot

def get_internal_slot(): # real signature unknown; restored from __doc__
    """
    get_internal_slot() -> PK11Slot
    
    Get the default internal slot.
    """
    return PK11Slot

def get_iv_length(mechanism): # real signature unknown; restored from __doc__
    """
    get_iv_length(mechanism) -> algtag
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
    
    Returns the length of the mechanism's initialization vector.
    """
    pass

def get_pad_mechanism(mechanism): # real signature unknown; restored from __doc__
    """
    get_pad_mechanism(mechanism) -> int
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
    
    Determine appropriate mechanism to use when padding is required.
    If the mechanism does not map to a padding mechanism return the mechanism.
    """
    return 0

def hash_buf(hash_alg, data): # real signature unknown; restored from __doc__
    """
    hash_buf(hash_alg, data) --> digest
    
    :Parameters:
        hash_alg : int
            hash algorithm enumeration (SEC_OID_*)
            e.g.: SEC_OID_MD5, SEC_OID_SHA1, SEC_OID_SHA256, SEC_OID_SHA512, etc.
        data : buffer or string
            buffer the digest will be computed for
    
    Computes a digest according to the hash_alg type.
    Return the digest data as buffer object.
    
    Note, if a hexidecimal string representation is desired then pass
    result to data_to_hex()
    """
    pass

def import_crl(slot, der_crl, url, type, import_options, decode_options, *user_data): # real signature unknown; restored from __doc__
    """
    import_crl(slot, der_crl, url, type, import_options, decode_options, [user_data1, ...]) -> SignedCRL
    
    :Parameters:
        slot : PK11Slot object
            designated PK11 slot
        der_crl : SecItem object
            signed DER CRL data encapsulated in a SecItem object.
        url : string
            URL of the CRL
        type : int
            revocation list type
            
            may be one of:
              - SEC_CRL_TYPE
              - SEC_KRL_TYPE
            
        import_options : int
            bit-wise OR of the following flags:
              - CRL_IMPORT_BYPASS_CHECKS
            
            or use CRL_IMPORT_DEFAULT_OPTIONS
        decode_options : int
            bit-wise OR of the following flags:
              - CRL_DECODE_DONT_COPY_DER
              - CRL_DECODE_SKIP_ENTRIES
              - CRL_DECODE_KEEP_BAD_CRL
              - CRL_DECODE_ADOPT_HEAP_DER
            
            or use CRL_DECODE_DEFAULT_OPTIONS
        user_dataN : object
            zero or more caller supplied parameters which will
            be passed to the password callback function
    """
    return SignedCRL

def import_sym_key(slot, mechanism, origin, operation, key_data, *user_data): # real signature unknown; restored from __doc__
    """
    import_sym_key(slot, mechanism, origin, operation, key_data, [user_data1, ...]) -> PK11SymKey
    
    :Parameters:
        slot : PK11Slot object
            designated PK11 slot
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        origin : int
            PK11 origin enumeration (PK11Origin*)
            e.g. PK11_OriginDerive, PK11_OriginUnwrap, etc.
        operation : int
            type of operation this context will be doing. A (CKA_*) constant
            (e.g. CKA_ENCRYPT, CKA_DECRYPT, CKA_SIGN, CKA_VERIFY, CKA_DIGEST)
        key_data: SecItem object
            key data encapsulated in a SECItem used to build the symmetric key.
        user_dataN : object ...
            zero or more caller supplied parameters which will
            be passed to the password callback function
    
    Create a PK11SymKey from data)
    """
    return PK11SymKey

def indented_format(line_fmt_tuples, indent_len=4): # real signature unknown; restored from __doc__
    """
    indented_format(line_fmt_tuples, indent_len=4) -> string
    
    The function supports the display of complex objects which may be
    composed of other complex objects. There is often a need to output
    section headers or single strings and lists of <attribute,value> pairs
    (the attribute in this discussion is called a label), or even blank
    lines. All of these items should line up in columns at different
    indentation levels in order to visually see the structure.
    
    It would not be flexible enough to have object formatting routines
    which simply returned a single string with all the indentation and
    formatting pre-applied. The indentation width may not be what is
    desired. Or more importantly you might not be outputting to text
    display. It might be a GUI which desires to display the
    information. Most GUI's want to handle each string seperately and
    control indentation and the visibility of each item (e.g. a tree
    control).
    
    At the same time we want to satisfy the need for easy and simple text
    output. This routine will do that, e.g.:
    
        print indented_format(obj.format_lines())
    
    To accomodate necessary flexibility the object formatting methods
    (format_lines()) return a list of tuples. Each tuple represents a
    single line with the first tuple item being the indentation level for
    the line. There may be 0,1 or 2 additional strings in the tuple which
    are to be output on the line. A single string are usually one of two
    things, either a section header or data that has been continuted onto
    multiple lines. Two strings usually represent a <attribute,value> pair
    with the first string being a label (e.g. attribute name).
    
    Each tuple may be:
    
        (int,)
            1-value tuple, no strings, e.g. blank line.
    
        (int, string)
            2-value tuple, output string at indent level.
    
        (int, string, string)
            3-value tuple, first string is a label, second string is a
            value.  Starting at the indent level output the label, then
            follow with the value. By keeping the label separate from the
            value the ouput formatter may elect to align the values in
            vertical columns for adjacent lines.
    
    Example::
                                         
        # This list of tuples,
    
        [(0, 'Constraints'),
         (1, 'min:', '0')
         (1, 'max:', '100'),
         (1, 'Filter Data'),
         (2, 'ab bc de f0 12 34 56 78 9a bc de f0')
         (2, '12 34 56 78 9a bc de f0 12 34 56 78')
        ]
    
        # would product this output
    
        Constraints
            min: 0
            max: 100
            Filter Data:
               ab bc de f0 12 34 56 78 9a bc de f0
               12 34 56 78 9a bc de f0 12 34 56 78
    
    :Parameters:
        line_fmt_tuples : [(level, ...),...]
            A list of tuples. First tuple value is the indentation level
            followed by optional strings for the line.
        indent_len : int
            Number of space characters repeated for each level and
            prepended to the line string.
    """
    return ""

def is_fips(): # real signature unknown; restored from __doc__
    """
    pk11_is_fips() -> bool
    
    Returns True if the internal module has FIPS enabled, False otherwise.
    """
    return False

def key_mechanism_type_from_name(name): # real signature unknown; restored from __doc__
    """
    key_mechanism_type_from_name(name) -> int
    
    :Parameters:
        name : string
            name of key mechanism enumeration constant (CKM_*)
    
    Given the name of a key mechanism enumeration constant (CKM_*)
    return it's integer constant
    The string comparison is case insensitive and will match with
    or without the CKM\_ prefix
    """
    return 0

def key_mechanism_type_name(mechanism): # real signature unknown; restored from __doc__
    """
    key_mechanism_type_name(mechanism) -> string
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
    
    Given a key mechanism enumeration constant (CKM_*)
    return it's name as a string
    """
    return ""

def make_line_fmt_tuples(level, obj): # real signature unknown; restored from __doc__
    """
    make_line_fmt_tuples(level, obj) -> [(level, str), ...]
    
    :Parameters:
        obj : object
            If obj is a tuple or list then each member will be wrapped
            in a 2-tuple of (level, str). If obj is a scalar object
            then obj will be wrapped in a 2-tuple of (level, obj)
        level : integer
            Initial indentation level, all subsequent indents are relative
            to this starting level.
    
    Return a list of line formatted tuples sutible to passing to
    `indented_format()`. Each tuple consists of a integer
    level value and a string object. This is equivalent to:
    [(level, str(x)) for x in obj].
    As a special case convenience if obj is a scalar object (i.e.
    not a list or tuple) then [(level, str(obj))] will be returned.
    """
    pass

def md5_digest(data): # real signature unknown; restored from __doc__
    """
    md5_digest(data) --> digest
    
    :Parameters:
        data : buffer or string
            buffer the digest will be computed for
    
    Returns 16 octet MD5 digest data as buffer object.
    
    Note, if a hexidecimal string representation is desired then pass
    result to data_to_hex()
    """
    pass

def mechanism_to_algtag(mechanism): # real signature unknown; restored from __doc__
    """
    mechanism_to_algtag(mechanism) -> algtag
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
    
    Returns the algtag given key mechanism enumeration constant (CKM_*)
    Throws an KeyError exception if the mechanism is invalid.
    """
    pass

def need_pw_init(): # real signature unknown; restored from __doc__
    """
    pk11_need_pw_init() -> bool
    
    Returns True if the internal slot needs to be initialized, False otherwise.
    
    The internal slot token should be initalized if:
    
    The token is not initialized
    
       `PK11Slot.need_login()` == True and `PK11Slot.need_user_init()` == True
    
    Or
    
    The token has a NULL password.
    
       `PK11Slot.need_login()` == False and `PK11Slot.need_user_init()` == False
    
    +------------------+------------------------+---------------------+
    |CKF_LOGIN_REQUIRED|CKF_USER_PIN_INITIALIZED|CKF_TOKEN_INITIALIZED|
    +==================+========================+=====================+
    |      False       |         False          |        True         |
    +------------------+------------------------+---------------------+
    |       True       |         False          |        False        |
    +------------------+------------------------+---------------------+
    |      False       |          True          |        True         |
    +------------------+------------------------+---------------------+
    |       True       |          True          |        True         |
    +------------------+------------------------+---------------------+
    
    `PK11Slot.need_login()` == CKF_LOGIN_REQUIRED
    
    `PK11Slot.need_user_init()` == !CKF_USER_PIN_INITIALIZED
    """
    return False

def nss_init(cert_dir): # real signature unknown; restored from __doc__
    """
    nss_init(cert_dir)
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
    
    Sets up configuration files and performs other tasks required to run
    Network Security Services. `nss.nss_init()` differs from
    `nss.nss_init_read_write()` because the internal PK11 slot (see
    `nss.get_internal_slot()`) is created in Read Only (RO) mode as
    opposed to Read Write (RW) mode.
    """
    pass

def nss_initialize(cert_dir=None, cert_prefix=None, key_prefix=None, secmod_name=None, flags=0): # real signature unknown; restored from __doc__
    """
    nss_initialize(cert_dir=None, cert_prefix=None, key_prefix=None, secmod_name=None, flags=0)
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
     
        cert_prefix : string
            Prefix added to the beginning of the certificate database,
            for example,"https-server1-".
    
        key_prefix : string
            Prefix added to the beginning of the key database,
            for example, "https-server1-".
    
        secmod_name : string
            Name of the security module database,
            usually "secmod.db".
    
        flags
            Bit flags that specify how NSS should be initialized.
    
    `nss_initialize()` initializes NSS. It is more flexible than `nss_init()`,
    `nss_init_read_write()`, and `nss_init_nodb()`. If any of those simpler NSS
    initialization functions suffices for your needs, call that instead.
    
    By default `nss_initialize()` and `nss_init_context()` open the
    internal PK11 slot (see `get_internal_slot()`) in Read Write (RW) mode
    as opposed to `nss_init()` which opens it in Read Only (RO) mode. If
    you want RO mode you pass the `NSS_INIT_READONLY` flag.
    
    The flags parameter is a bitwise OR of the following flags:
    
    NSS_INIT_READONLY
        Open the databases read only.
    
    NSS_INIT_NOCERTDB
        Don't open the cert DB and key DB's, just initialize the volatile
        certdb.
    
    NSS_INIT_NOMODDB
        Don't open the security module DB, just initialize the PKCS #11 module.
    
    NSS_INIT_FORCEOPEN
        Continue to force initializations even if the databases cannot be
        opened.
    
    NSS_INIT_NOROOTINIT
        Don't try to look for the root certs module automatically.
    
    NSS_INIT_OPTIMIZESPACE
        Optimize for space instead of speed. Use smaller tables and caches.
    
    NSS_INIT_PK11THREADSAFE
        Only load PKCS#11 modules that are thread-safe, i.e., that support
        locking - either OS locking or NSS-provided locks . If a PKCS#11 module
        isn't thread-safe, don't serialize its calls; just don't load it
        instead. This is necessary if another piece of code is using the same
        PKCS#11 modules that NSS is accessing without going through NSS, for
        example, the Java SunPKCS11 provider.
    
    NSS_INIT_PK11RELOAD
        Ignore the CKR_CRYPTOKI_ALREADY_INITIALIZED error when loading PKCS#11
        modules. This is necessary if another piece of code is using the same
        PKCS#11 modules that NSS is accessing without going through NSS, for
        example, Java SunPKCS11 provider.
    
    NSS_INIT_NOPK11FINALIZE
        Never call C_Finalize on any PKCS#11 module. This may be necessary in
        order to ensure continuous operation and proper shutdown sequence if
        another piece of code is using the same PKCS#11 modules that NSS is
        accessing without going through NSS, for example, Java SunPKCS11
        provider. The following limitation applies when this is set :
        SECMOD_WaitForAnyTokenEvent will not use C_WaitForSlotEvent, in order
        to prevent the need for C_Finalize. This call will be emulated instead.
    
    NSS_INIT_RESERVED
        Currently has no effect, but may be used in the future to trigger
        better cooperation between PKCS#11 modules used by both NSS and the
        Java SunPKCS11 provider. This should occur after a new flag is defined
        for C_Initialize by the PKCS#11 working group.
    
    NSS_INIT_COOPERATE
        Sets the above four recommended options for applications that use both
        NSS and the Java SunPKCS11 provider.
    
    Hint: You can obtain a printable representation of the flags via `nss_init_flags`.
    """
    pass

def nss_init_context(cert_dir=None, cert_prefix=None, key_prefix=None, secmod_name=None, init_params=None, flags=0): # real signature unknown; restored from __doc__
    """
    nss_init_context(cert_dir=None, cert_prefix=None, key_prefix=None, secmod_name=None, init_params=None, flags=0) -> `InitContext`
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
     
        cert_prefix : string
            Prefix added to the beginning of the certificate database,
            for example,"https-server1-".
    
        key_prefix : string
            Prefix added to the beginning of the key database,
            for example, "https-server1-".
    
        secmod_name : string
            Name of the security module database,
            usually "secmod.db".
    
        init_params : `InitContext` object
            Object with a set of initialization parameters.
            See `InitContext`.
    
        flags
            Bit flags that specify how NSS should be initialized.
    
    `nss_init_context()` initializes NSS within a context and returns a
    `InitContext` object. Contexts are used when multiple entities within
    a single process wish to use NSS without colliding such as
    libraries.
    
    By default `nss_initialize()` and `nss_init_context()` open the
    internal PK11 slot (see `get_internal_slot()`) in Read Write (RW) mode
    as opposed to `nss_init()` which opens it in Read Only (RO) mode. If
    you want RO mode you pass the `NSS_INIT_READONLY` flag.
    
    The flags parameter is a bitwise OR of the following flags:
    
    NSS_INIT_READONLY
        Open the databases read only.
    
    NSS_INIT_NOCERTDB
        Don't open the cert DB and key DB's, just initialize the volatile
        certdb.
    
    NSS_INIT_NOMODDB
        Don't open the security module DB, just initialize the PKCS #11 module.
    
    NSS_INIT_FORCEOPEN
        Continue to force initializations even if the databases cannot be
        opened.
    
    NSS_INIT_NOROOTINIT
        Don't try to look for the root certs module automatically.
    
    NSS_INIT_OPTIMIZESPACE
        Optimize for space instead of speed. Use smaller tables and caches.
    
    NSS_INIT_PK11THREADSAFE
        Only load PKCS#11 modules that are thread-safe, i.e., that support
        locking - either OS locking or NSS-provided locks . If a PKCS#11 module
        isn't thread-safe, don't serialize its calls; just don't load it
        instead. This is necessary if another piece of code is using the same
        PKCS#11 modules that NSS is accessing without going through NSS, for
        example, the Java SunPKCS11 provider.
    
    NSS_INIT_PK11RELOAD
        Ignore the CKR_CRYPTOKI_ALREADY_INITIALIZED error when loading PKCS#11
        modules. This is necessary if another piece of code is using the same
        PKCS#11 modules that NSS is accessing without going through NSS, for
        example, Java SunPKCS11 provider.
    
    NSS_INIT_NOPK11FINALIZE
        Never call C_Finalize on any PKCS#11 module. This may be necessary in
        order to ensure continuous operation and proper shutdown sequence if
        another piece of code is using the same PKCS#11 modules that NSS is
        accessing without going through NSS, for example, Java SunPKCS11
        provider. The following limitation applies when this is set :
        SECMOD_WaitForAnyTokenEvent will not use C_WaitForSlotEvent, in order
        to prevent the need for C_Finalize. This call will be emulated instead.
    
    NSS_INIT_RESERVED
        Currently has no effect, but may be used in the future to trigger
        better cooperation between PKCS#11 modules used by both NSS and the
        Java SunPKCS11 provider. This should occur after a new flag is defined
        for C_Initialize by the PKCS#11 working group.
    
    NSS_INIT_COOPERATE
        Sets the above four recommended options for applications that use both
        NSS and the Java SunPKCS11 provider.
    
    Hint: You can obtain a printable representation of the flags via `nss_init_flags`.
    """
    pass

def nss_init_flags(flags): # real signature unknown; restored from __doc__
    """
    nss_init_flags(flags) -> ['flag_name', ...]
    
    :Parameters:
        flags : int
            NSS_INIT* bit flags
    
    Given an integer with NSS_INIT*
    (e.g. nss.NSS_INIT_READONLY) bit flags return a sorted
    list of their string names.
    """
    pass

def nss_init_nodb(): # real signature unknown; restored from __doc__
    """
    nss_init_nodb()
    
    Performs tasks required to run Network Security Services without setting up
    configuration files. Important: This NSS function is not intended for use with
    SSL, which requires that the certificate and key database files be opened.
    
    nss_init_nodb opens only the temporary database and the internal PKCS #112
    module. Unlike nss_init, nss_init_nodb allows applications that do not have
    access to storage for databases to run raw crypto, hashing, and certificate
    functions. nss_init_nodb is not idempotent, so call it only once. The policy
    flags for all cipher suites are turned off by default, disallowing all cipher
    suites. Therefore, an application cannot use NSS to perform any cryptographic
    operations until after it enables appropriate cipher suites by calling one of
    the SSL Export Policy Functions.
    """
    pass

def nss_init_read_write(cert_dir): # real signature unknown; restored from __doc__
    """
    nss_init_read_write(cert_dir)
    
    :Parameters:
        cert_dir : string
            Pathname of the directory where the certificate, key, and
            security module databases reside.
    
    Sets up configuration files and performs other tasks required to run
    Network Security Services. `nss.nss_init_read_write()` differs from
    `nss.nss_init()` because the internal PK11 slot (see
    `nss.get_internal_slot()`) is created in Read Write (RW) mode as
    opposed to Read Only (RO) mode.
    """
    pass

def nss_is_initialized(): # real signature unknown; restored from __doc__
    """
    nss_is_initialized() --> bool
    
    Returns whether Network Security Services has already been initialized or not.
    """
    pass

def nss_shutdown(): # real signature unknown; restored from __doc__
    """
    nss_shutdown()
    
    Closes the key and certificate databases that were opened by nss_init().
    
    NSS can only shutdown successfully if all NSS objects have been
    released, otherwise nss_shutdown will fail with the error code
    SEC_ERROR_BUSY. Here are some tips to make sure nss_shutdown will
    succeed. [1]_
    
    * If the process is a SSL client make sure you call
      `ssl.clear_session_cache`.
    
    * If the process is a SSL server make sure you call
      `ssl.shutdown_server_session_id_cache()`.
    
    * Make sure all sockets have been closed, open SSL sockets hold
      references NSS objects.
    
    * Explicitly delete Python objects which contain NSS objects using the
      del command. [2]_
    
    * Use `nss.dump_certificate_cache_info()` to provide information about
      which cached objects may still persist and be responsible for
      preventing a full NSS shutdown.
    
    .. [1] If the leaked objects are subsequently released after
           nss_shutdown is called NSS can be reinitialized with the
           various NSS initialization routines. In this cass teh
           SEC_ERROR_BUSY error can be thought of as an informatiive
           warning.
    
    .. [2] This Python binding to NSS wraps each NSS object inside a
           Python object. Like NSS objects Python objects are reference
           counted. When the last reference to the Python object
           disappears the Python object is destroyed. The destructor for a
           Python object wrapping an NSS object releases the NSS reference
           to the NSS object. Thus if any Python objects which wrap NSS
           objects remain "live" nss_shutdown will fail. Python objects
           are typically released by the Python interpretor when the
           variable holding the object is assigned a new object or when
           the variable holding the object goes out of scope. This means
           you may need to manually delete some objects using the del
           command rather relying on Python's automatic garbage
           collection. Consider this example:
    
           def foo():
               nss.nss_init(certdir)
               sock = ssl.SSLSocket()
               nss.nss_shutdown()
    
           When nss_shutown() is called the sock object is still alive and
           holds references to NSS objects. The sock object won't be
           released by Python until it goes out of scope when the function
           exits. Thus the shutdown will fail with SEC_ERROR_BUSY. But you
           can explicitly force the sock object to be released by
           explictily deleting it, for example:
    
           def foo():
               nss.nss_init(certdir)
               sock = ssl.SSLSocket()
               del sock
               nss.nss_shutdown()
    
           Another way to avoid this issue is to arrange your code such
           that nss_shutdown is called from a location in your code which
           is not in scope for any NSS objects created. This also implies
           you shouldn't assign NSS objects to globals.
    """
    pass

def nss_shutdown_context(context): # real signature unknown; restored from __doc__
    """
    nss_shutdown_context(context) -> 
    
    :Parameters:
        context : `InitContext` object
            A `InitContext` returned from a previous
            call to `nss_init_context`.
    
    xxx
    """
    pass

def oid_dotted_decimal(oid): # real signature unknown; restored from __doc__
    """
    oid_dotted_decimal(oid) -> string
    
    :Parameters:
         oid : may be one of integer, string, SecItem
             May be one of:
             
             * integer:: A SEC OID enumeration constant, also known as a tag
               (i.e. SEC_OID_*) for example SEC_OID_AVA_COMMON_NAME.
             * string:: A string in dotted decimal representation, for example
               'OID.2.5.4.3'. The 'OID.' prefix is optional.
               Or a string for the tag name (e.g. 'SEC_OID_AVA_COMMON_NAME')
               The 'SEC_OID\_' prefix is optional. Or one of the canonical
               abbreviations (e.g. 'cn'). Case is not significant.
             * SecItem:: A SecItem object encapsulating the OID in 
               DER format.
    
    Given an oid return it's tag constant as a string.
    """
    return ""

def oid_str(oid): # real signature unknown; restored from __doc__
    """
    oid_str(oid) -> string
    
    :Parameters:
         oid : may be one of integer, string, SecItem
             May be one of:
             
             * integer:: A SEC OID enumeration constant, also known as a tag
               (i.e. SEC_OID_*) for example SEC_OID_AVA_COMMON_NAME.
             * string:: A string in dotted decimal representation, for example
               'OID.2.5.4.3'. The 'OID.' prefix is optional.
               Or a string for the tag name (e.g. 'SEC_OID_AVA_COMMON_NAME')
               The 'SEC_OID\_' prefix is optional. Or one of the canonical
               abbreviations (e.g. 'cn'). Case is not significant.
             * SecItem:: A SecItem object encapsulating the OID in 
               DER format.
    
    Given an oid return it's description as a string.
    """
    return ""

def oid_tag(oid): # real signature unknown; restored from __doc__
    """
    oid_tag(oid) -> int
    
    :Parameters:
         oid : may be one of integer, string, SecItem
             May be one of:
             
             * integer:: A SEC OID enumeration constant, also known as a tag
               (i.e. SEC_OID_*) for example SEC_OID_AVA_COMMON_NAME.
             * string:: A string in dotted decimal representation, for example
               'OID.2.5.4.3'. The 'OID.' prefix is optional.
               Or a string for the tag name (e.g. 'SEC_OID_AVA_COMMON_NAME')
               The 'SEC_OID\_' prefix is optional. Or one of the canonical
               abbreviations (e.g. 'cn'). Case is not significant.
             * SecItem:: A SecItem object encapsulating the OID in 
               DER format.
    
    Given an oid return it's tag constant.
    """
    return 0

def oid_tag_name(oid): # real signature unknown; restored from __doc__
    """
    oid_tag_name(oid) -> string
    
    :Parameters:
         oid : may be one of integer, string, SecItem
             May be one of:
             
             * integer:: A SEC OID enumeration constant, also known as a tag
               (i.e. SEC_OID_*) for example SEC_OID_AVA_COMMON_NAME.
             * string:: A string in dotted decimal representation, for example
               'OID.2.5.4.3'. The 'OID.' prefix is optional.
               Or a string for the tag name (e.g. 'SEC_OID_AVA_COMMON_NAME')
               The 'SEC_OID\_' prefix is optional. Or one of the canonical
               abbreviations (e.g. 'cn'). Case is not significant.
             * SecItem:: A SecItem object encapsulating the OID in 
               DER format.
    
    Given an oid return it's tag constant as a string.
    """
    return ""

def param_from_algid(algid): # real signature unknown; restored from __doc__
    """
    param_from_algid(algid) -> SecItem
    
    :Parameters:
        algid : AlgorithmID object
            algorithm id
    
    Return a SecItem containing a encryption param derived from a AlgorithmID.
    """
    return SecItem

def param_from_iv(mechanism, iv=None): # real signature unknown; restored from __doc__
    """
    param_from_iv(mechanism, iv=None) -> SecItem
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
        iv : SecItem object
            initialization vector. If there is no initialization vector you may also pass
            None or an empty SecItem object (e.g. SecItem())
    
    Return a SecItem to be used as the initialization vector for encryption/decryption.
    """
    return SecItem

def pk11_attribute_type_from_name(name): # real signature unknown; restored from __doc__
    """
    pk11_attribute_type_from_name(name) -> int
    
    :Parameters:
        name : string
            name of PK11 attribute type constant (CKA_*)
    
    Given the name of a PK11 attribute type constant (CKA_*)
    return it's integer constant
    The string comparison is case insensitive and will match with
    or without the CKA\_ prefix
    """
    return 0

def pk11_attribute_type_name(type): # real signature unknown; restored from __doc__
    """
    pk11_attribute_type_name(type) -> string
    
    :Parameters:
        type : int
            PK11 attribute type constant (CKA_*)
    
    Given a PK11 attribute type constant (CKA_*)
    return it's name as a string
    """
    return ""

def pk11_disabled_reason_name(reason): # real signature unknown; restored from __doc__
    """
    pk11_disabled_reason_name(reason) -> string
    
    :Parameters:
        reason : int
            PK11 slot disabled reason constant (PK11_DIS_*)
    
    Given a PK11 slot disabled reason constant (PK11_DIS_*)
    return the constant as a string.
    """
    return ""

def pk11_disabled_reason_str(reason): # real signature unknown; restored from __doc__
    """
    pk11_disabled_reason_str(reason) -> string
    
    :Parameters:
        reason : int
            PK11 slot disabled reason constant (PK11_DIS_*)
    
    Given a PK11 slot disabled reason constant (PK11_DIS_*)
    return a descriptive string
    """
    return ""

def pk11_logout_all(): # real signature unknown; restored from __doc__
    """
    pk11_logout_all()
    
    Logout of every slot for all modules.
    """
    pass

def pkcs12_cipher_from_name(name): # real signature unknown; restored from __doc__
    """
    pkcs12_cipher_from_name(name) -> int
    
    :Parameters:
        name : string
            name of PKCS12_* constant
    
    Given the name of a PKCS12_* constant
    return it's integer constant
    The string comparison is case insensitive and will match with
    or without the PKCS12\_ prefix
    """
    return 0

def pkcs12_cipher_name(cipher): # real signature unknown; restored from __doc__
    """
    pkcs12_cipher_name(cipher) -> string
    
    :Parameters:
        cipher : int
            PKCS12_* constant
    
    Given a PKCS12_* constant
    return it's name as a string
    """
    return ""

def pkcs12_enable_all_ciphers(): # real signature unknown; restored from __doc__
    """
    pkcs12_enable_all_ciphers()
    
    Enables all PKCS12 ciphers, which are: 
        - `PKCS12_RC2_CBC_40` 
        - `PKCS12_RC2_CBC_128` 
        - `PKCS12_RC4_40` 
        - `PKCS12_RC4_128` 
        - `PKCS12_DES_56` 
        - `PKCS12_DES_EDE3_168`
    """
    pass

def pkcs12_enable_cipher(cipher, enabled): # real signature unknown; restored from __doc__
    """
    pkcs12_enable_cipher(cipher, enabled)
    
    :Parameters:
        cipher : integer
            The PKCS12 cipher suite enumeration (e.g. `PKCS12_DES_EDE3_168`, etc.)
        enabled : bool or int
            True enables, False disables
    
    The cipher may be one of: 
        - PKCS12_RC2_CBC_40 
        - PKCS12_RC2_CBC_128 
        - PKCS12_RC4_40 
        - PKCS12_RC4_128 
        - PKCS12_DES_56 
        - PKCS12_DES_EDE3_168
    """
    pass

def pkcs12_export(nickname, pkcs12_password, key_cipher=None, cert_cipher=None, pin_args=None): # real signature unknown; restored from __doc__
    """
    pkcs12_export(nickname, pkcs12_password, key_cipher=SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_3KEY_TRIPLE_DES_CBC, cert_cipher=SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_40_BIT_RC2_CBC, pin_args=None) 
    
    :Parameters:
        nickname : string
            Certificate nickname to search for.
        pkcs12_password : string
            The password used to protect the pkcs12_file.
        key_cipher : int
            A SEC OID TAG enumerated constant selecting the
            encryption for the private key (see below).
            Also see `nss.pkcs12_map_cipher()` for an alternative
            method to select the encryption cipher.
        cert_cipher : int
            A SEC OID TAG enumerated constant selecting the
            encryption for the certificates (see below).
            Also see `nss.pkcs12_map_cipher()` for an alternative
            method to select the encryption cipher.
        pin_args : tuple
            Extra parameters which will
            be passed to the password callback function.
    
    pkcs12_export() is used to export a certificate and private key pair
    from the NSS database in a protected manner. It produces the binary
    content of what is typically called a .p12 file (e.g. PKCS12). This
    function does not write the file, if you want to write a .p12 file
    you must write it's output to a file, for example:
    
    ::
    
        pkcs12_data = nss.pkcs12_export(nickname, pkcs12_file_password)
        f = open(p12_file_path, 'w')
        f.write(pkcs12_data)
        f.close()
    
    Password Based Encryption
    -------------------------
    
    PKCS #12 provides for not only the protection of the private keys but
    also the certificate and meta-data associated with the keys. Password
    based encryption is used to protect private keys (i.e. key_cipher) on
    export to a PKCS #12 file and also the entire package when allowed
    (i.e. cert_cipher). If no algorithm is specified it defaults to using
    'PKCS #12 V2 PBE With SHA-1 And 3KEY Triple DES-CBC' for private key
    encryption. For historical export control reasons 'PKCS #12 V2 PBE
    With SHA-1 And 40 Bit RC2 CBC' is the default for the overall package
    encryption when not in FIPS mode and no package encryption when in
    FIPS mode. The private key is always protected with strong encryption
    by default.
    
    A list of ciphers follows, the term is the SEC OID TAG followd by a
    friendly description.
    
    * symmetric CBC ciphers for PKCS #5 V2:
        SEC_OID_DES_CBC
            DES-CBC.
        SEC_OID_RC2_CBC
            RC2-CBC.
        SEC_OID_RC5_CBC_PAD
            RC5-CBCPad.
        SEC_OID_DES_EDE3_CBC
            DES-EDE3-CBC.
        SEC_OID_AES_128_CBC
            AES-128-CBC.
        SEC_OID_AES_192_CBC
            AES-192-CBC.
        SEC_OID_AES_256_CBC
            AES-256-CBC.
        SEC_OID_CAMELLIA_128_CBC
            CAMELLIA-128-CBC.
        SEC_OID_CAMELLIA_192_CBC
            CAMELLIA-192-CBC.
        SEC_OID_CAMELLIA_256_CBC
            CAMELLIA-256-CBC.
    
    * PKCS #12 PBE Ciphers:
        SEC_OID_PKCS12_PBE_WITH_SHA1_AND_128_BIT_RC4
            PKCS #12 PBE With SHA-1 and 128 Bit RC4.
        SEC_OID_PKCS12_PBE_WITH_SHA1_AND_40_BIT_RC4
            PKCS #12 PBE With SHA-1 and 40 Bit RC4.
        SEC_OID_PKCS12_PBE_WITH_SHA1_AND_TRIPLE_DES_CBC
            PKCS #12 PBE With SHA-1 and Triple DES-CBC.
        SEC_OID_PKCS12_PBE_WITH_SHA1_AND_128_BIT_RC2_CBC
            PKCS #12 PBE With SHA-1 and 128 Bit RC2 CBC.
        SEC_OID_PKCS12_PBE_WITH_SHA1_AND_40_BIT_RC2_CBC
            PKCS #12 PBE With SHA-1 and 40 Bit RC2 CBC.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_128_BIT_RC4
            PKCS #12 V2 PBE With SHA-1 And 128 Bit RC4.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_40_BIT_RC4
            PKCS #12 V2 PBE With SHA-1 And 40 Bit RC4.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_3KEY_TRIPLE_DES_CBC
            PKCS #12 V2 PBE With SHA-1 And 3KEY Triple DES-CBC.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_2KEY_TRIPLE_DES_CBC
            PKCS #12 V2 PBE With SHA-1 And 2KEY Triple DES-CBC.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_128_BIT_RC2_CBC
            PKCS #12 V2 PBE With SHA-1 And 128 Bit RC2 CBC.
        SEC_OID_PKCS12_V2_PBE_WITH_SHA1_AND_40_BIT_RC2_CBC
            PKCS #12 V2 PBE With SHA-1 And 40 Bit RC2 CBC.
    
    * PKCS #5 PBE Ciphers:
        SEC_OID_PKCS5_PBE_WITH_MD2_AND_DES_CBC
            PKCS #5 Password Based Encryption with MD2 and DES-CBC.
        SEC_OID_PKCS5_PBE_WITH_MD5_AND_DES_CBC
            PKCS #5 Password Based Encryption with MD5 and DES-CBC.
        SEC_OID_PKCS5_PBE_WITH_SHA1_AND_DES_CBC
            PKCS #5 Password Based Encryption with SHA-1 and DES-CBC.
    """
    pass

def pkcs12_map_cipher(cipher, key_length=0): # real signature unknown; restored from __doc__
    """
    pkcs12_map_cipher(cipher, key_length=0) -> int
    
    :Parameters:
        cipher : may be one of integer, string or SecItem
            May be one of:
    
            * integer:: A SEC OID enumeration constant, also known as a tag
              (i.e. SEC_OID_*) for example SEC_OID_DES_EDE3_CBC.
            * string:: A string for the tag name
              (e.g. 'SEC_OID_DES_EDE3_CBC') The 'SEC_OID\_' prefix is
              optional. A string in dotted decimal representation, for
              example 'OID.2.5.4.3'. The 'OID.' prefix is optional.  Case
              is not significant.
            * SecItem:: A SecItem object encapsulating the OID in 
              DER format.
        key_length : int
            The number of bits in the key. If zero a default will be selected.
    
    Given an cipher and optionally a key length, map that to a PKCS12 encryption
    method returned as a SEC_OID tag.
    """
    return 0

def pkcs12_set_nickname_collision_callback(callback): # real signature unknown; restored from __doc__
    """
    pkcs12_set_nickname_collision_callback(callback)
    
    :Parameters:
        callback : function pointer
            The callback function
    
    When importing a certificate via a `PKCS12Decoder` object and the
    nickname is not set or collides with an existing nickname in the NSS
    database then this callback is invoked to resolve the problem. If no
    nickname collision callback has been set then an internal default
    callback will be used instead which calls the NSS function CERT_MakeCANickname
    (available in the Python binding as `Certificate.make_ca_nickname()`).
    
    The callback has the signature::
        
        nickname_collision_callback(old_nickname, cert) --> new_nickname, cancel
    
    old_nickname
        the preious nickname or None if previous did not exist
    cert
        the `Certificate` object being imported.
    
    The callback returns 2 values, the new nickname, and a boolean.
    
        new_nickname
            The new nickname to try or None
    
        cancel
            boolean indicating if collision resolution should be cancelled
    """
    pass

def pkcs12_set_preferred_cipher(cipher, enabled): # real signature unknown; restored from __doc__
    """
    pkcs12_set_preferred_cipher(cipher, enabled)
    
    :Parameters:
        cipher : integer
            The PKCS12 cipher suite enumeration (e.g. `PKCS12_DES_EDE3_168`, etc.)
        enabled : bool or int
            True enables, False disables
    
    This function enables or disables the preferred flag on a 
    PKCS cipher. The default preferred cipher is `PKCS12_RC2_CBC_40`.
    
    The cipher may be one of: 
        - `PKCS12_RC2_CBC_40` 
        - `PKCS12_RC2_CBC_128` 
        - `PKCS12_RC4_40` 
        - `PKCS12_RC4_128` 
        - `PKCS12_DES_56` 
        - `PKCS12_DES_EDE3_168`
    """
    pass

def pub_wrap_sym_key(mechanism, pub_key, sym_key): # real signature unknown; restored from __doc__
    """
    pub_wrap_sym_key(mechanism, pub_key, sym_key) -> SecItem
    
    :Parameters:
        mechanism : int
            CK_MECHANISM_TYPE enumerated constant
        pub_key : `PublicKey` object
            Public key used to wrap.
        sym_key : `PK11SymKey` object
            Symmetric key that will be wrapped.
    :returns:
        Wrapped symmetric key as SecItem
    
    Wraps a public key wrap (which only RSA can do).
    """
    return SecItem

def read_der_from_file(file, ascii=False): # real signature unknown; restored from __doc__
    """
    read_der_from_file(file, ascii=False) -> SecItem
    
    :Parameters:
        file : file name or file object
            If string treat as file path to open and read,
            if file object read from file object.
        ascii : boolean
            If True treat file contents as ascii data.
            If PEM delimiters are found strip them.
            Then base64 decode the contents.
    
    Read the contents of a file and return as a SecItem object.
    If file is a string then treat it as a file pathname and open
    and read the contents of that file. If file is a file object
    then read the contents from the file object
    
    If the file contents begin with a PEM header then treat the
    the file as PEM encoded and decode the payload into DER form.
    Otherwise the file contents is assumed to already be in DER form.
    The returned SecItem contains the DER contents of the file.
    """
    return SecItem

def read_hex(input, separators=None): # real signature unknown; restored from __doc__
    """
    read_hex(input, separators=" ,:\t\n") -> buffer
    
    :Parameters:
        input : string
            string containing hexadecimal data
        separators : string or None
            string containing set of separator characters
            Any character encountered during parsing which is in
            this string will be skipped and considered a separator
            between pairs of hexadecimal characters.
    
    Parse a string containing hexadecimal data and return a buffer
    object containing the binary octets. Each octet in the string is
    represented as a pair of case insensitive hexadecimal characters
    (0123456789abcdef). Each octet must be a pair of
    characters. Octets may optionally be preceded by 0x or 0X. Octets
    may be separated by separator characters specified in the
    separators string. The separators string is a set of
    characters. Any character in the separators character set will be
    ignored when it occurs between octets. If no separators should be
    considered then pass an empty string.
    
    Using the default separators each of these strings is valid input
    representing the same 8 octet sequence:
    
    01, 23, 45, 67, 89, ab, cd, ef
    01, 23, 45, 67, 89, AB, CD, EF
    0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef
    01:23:45:67:89:ab:cd:ef
    0123456789abcdef
    01 23 45 67 89 ab cd ef
    0x010x230x450x670x890xab0xcd0xef
    """
    return buffer(*(), **{})

def set_password_callback(callback): # real signature unknown; restored from __doc__
    """
    set_password_callback(callback)
    
    :Parameters:
        callback : function pointer
            The callback function
            
    The callback has the signature::
        
        password_callback(slot, retry, [user_data1, ...])
    
    slot
        PK11Slot object
    retry
        boolean indicating if this is a retry
    user_dataN
        zero or more caller supplied optional parameters
    """
    pass

def sha1_digest(data): # real signature unknown; restored from __doc__
    """
    sha1_digest(data) --> digest
    
    :Parameters:
        data : buffer or string
            buffer the digest will be computed for
    
    Returns 20 octet SHA1 digest data as buffer object.
    
    Note, if a hexidecimal string representation is desired then pass
    result to data_to_hex()
    """
    pass

def sha256_digest(data): # real signature unknown; restored from __doc__
    """
    sha256_digest(data) --> digest
    
    :Parameters:
        data : buffer or string
            buffer the digest will be computed for
    
    Returns 32 octet SHA256 digest data as buffer object.
    
    Note, if a hexidecimal string representation is desired then pass
    result to data_to_hex()
    """
    pass

def sha512_digest(data): # real signature unknown; restored from __doc__
    """
    sha512_digest(data) --> digest
    
    :Parameters:
        data : buffer or string
            buffer the digest will be computed for
    
    Returns 64 octet SHA512 digest data as buffer object.
    
    Note, if a hexidecimal string representation is desired then pass
    result to data_to_hex()
    """
    pass

def token_exists(mechanism): # real signature unknown; restored from __doc__
    """
    pk11_token_exists(mechanism) -> bool
    
    :Parameters:
        mechanism : int
            key mechanism enumeration constant (CKM_*)
    
    Return True if a token is available which can perform
    the desired mechanism, False otherwise.
    """
    return False

def x509_alt_name(sec_item, repr_kind=None): # real signature unknown; restored from __doc__
    """
    x509_alt_name(sec_item, repr_kind=AsString) -> (SecItem, ...)
    
    :Parameters:
        sec_item : SecItem object
            A SecItem containing a DER encoded alternative name extension.
        repr_kind : RepresentationKind constant
            Specifies what the contents of the returned tuple will be.
            May be one of:
    
            AsObject
                The general name as a nss.GeneralName object
            AsString
                The general name as a string.
                (e.g. "http://crl.geotrust.com/crls/secureca.crl")
            AsTypeString
                The general name type as a string.
                 (e.g. "URI")
            AsTypeEnum
                The general name type as a general name type enumerated constant.
                 (e.g. nss.certURI )
            AsLabeledString
                The general name as a string with it's type prepended.
                (e.g. "URI: http://crl.geotrust.com/crls/secureca.crl"
    
    Return a tuple of GeneralNames according the representation kind.
    """
    pass

def x509_ext_key_usage(sec_item, repr_kind=None): # real signature unknown; restored from __doc__
    """
    x509_ext_key_usage(sec_item, repr_kind=AsString) -> (obj, ...)
    
    :Parameters:
        sec_item : SecItem object
            A SecItem containing a DER encoded sequence of OID's
        repr_kind : RepresentationKind constant
            Specifies what the contents of the returned tuple will be.
            May be one of:
    
            AsObject
                Each extended key usage will be a SecItem object embedding
                the OID in DER format.
            AsString
                Each extended key usage will be a descriptive string.
                (e.g. "TLS Web Server Authentication Certificate")
            AsDottedDecimal
                Each extended key usage will be OID rendered as a dotted decimal string.
                (e.g. "OID.1.3.6.1.5.5.7.3.1")
            AsEnum
                Each extended key usage will be OID tag enumeration constant (int).
                (e.g. nss.SEC_OID_EXT_KEY_USAGE_SERVER_AUTH)
    
    Return a tuple of OID's according the representation kind.
    """
    pass

def x509_key_usage(bitstr, repr_kind=None): # real signature unknown; restored from __doc__
    """
    x509_key_usage(bitstr, repr_kind=AsEnumDescription) -> (str, ...)
    
    :Parameters:
        bitstr : SecItem object
            A SecItem containing a DER encoded bit string.
        repr_kind : RepresentationKind constant
            Specifies what the contents of the returned tuple will be.
            May be one of:
    
            AsEnum
                The enumerated constant.
                (e.g. nss.KU_DIGITAL_SIGNATURE)
            AsEnumDescription
                A friendly human readable description of the enumerated constant as a string.
                 (e.g. "Digital Signature")
            AsIndex
                The bit position within the bit string.
    
    Return a tuple of string name for each enabled bit in the key
    usage bit string.
    """
    pass

# classes

from AlgorithmID import AlgorithmID
from AuthKeyID import AuthKeyID
from AVA import AVA
from BasicConstraints import BasicConstraints
from CertDB import CertDB
from Certificate import Certificate
from CertificateExtension import CertificateExtension
from CertificateRequest import CertificateRequest
from CRLDistributionPoint import CRLDistributionPoint
from CRLDistributionPts import CRLDistributionPts
from DN import DN
from DSAPublicKey import DSAPublicKey
from GeneralName import GeneralName
from InitContext import InitContext
from InitParameters import InitParameters
from KEYPQGParams import KEYPQGParams
from PK11Context import PK11Context
from PK11Slot import PK11Slot
from PK11SymKey import PK11SymKey
from PKCS12DecodeItem import PKCS12DecodeItem
from PKCS12Decoder import PKCS12Decoder
from PrivateKey import PrivateKey
from PublicKey import PublicKey
from RDN import RDN
from RSAGenParams import RSAGenParams
from RSAPublicKey import RSAPublicKey
from SecItem import SecItem
from SignedCRL import SignedCRL
from SignedData import SignedData
from SubjectPublicKeyInfo import SubjectPublicKeyInfo
# variables with complex values

_C_API = None # (!) real value is ''

