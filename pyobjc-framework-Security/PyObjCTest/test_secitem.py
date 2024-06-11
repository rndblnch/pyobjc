import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestAuthorizationDB(TestCase):
    @min_os_level("10.7")
    def test_constants_10_6(self):
        self.assertIsInstance(Security.kSecClass, str)
        self.assertIsInstance(Security.kSecClassInternetPassword, str)
        self.assertIsInstance(Security.kSecAttrCreationDate, str)
        self.assertIsInstance(Security.kSecAttrModificationDate, str)
        self.assertIsInstance(Security.kSecAttrDescription, str)
        self.assertIsInstance(Security.kSecAttrComment, str)
        self.assertIsInstance(Security.kSecAttrCreator, str)
        self.assertIsInstance(Security.kSecAttrType, str)
        self.assertIsInstance(Security.kSecAttrLabel, str)
        self.assertIsInstance(Security.kSecAttrIsInvisible, str)
        self.assertIsInstance(Security.kSecAttrIsNegative, str)
        self.assertIsInstance(Security.kSecAttrAccount, str)
        self.assertIsInstance(Security.kSecAttrService, str)
        self.assertIsInstance(Security.kSecAttrGeneric, str)
        self.assertIsInstance(Security.kSecAttrSecurityDomain, str)
        self.assertIsInstance(Security.kSecAttrServer, str)
        self.assertIsInstance(Security.kSecAttrProtocol, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationType, str)
        self.assertIsInstance(Security.kSecAttrPort, str)
        self.assertIsInstance(Security.kSecAttrPath, str)
        self.assertIsInstance(Security.kSecAttrSubject, str)
        self.assertIsInstance(Security.kSecAttrIssuer, str)
        self.assertIsInstance(Security.kSecAttrSerialNumber, str)
        self.assertIsInstance(Security.kSecAttrSubjectKeyID, str)
        self.assertIsInstance(Security.kSecAttrPublicKeyHash, str)
        self.assertIsInstance(Security.kSecAttrCertificateType, str)
        self.assertIsInstance(Security.kSecAttrCertificateEncoding, str)
        self.assertIsInstance(Security.kSecAttrKeyClass, str)
        self.assertIsInstance(Security.kSecAttrApplicationLabel, str)
        self.assertIsInstance(Security.kSecAttrIsPermanent, str)
        self.assertIsInstance(Security.kSecAttrIsSensitive, str)
        self.assertIsInstance(Security.kSecAttrIsExtractable, str)
        self.assertIsInstance(Security.kSecAttrApplicationTag, str)
        self.assertIsInstance(Security.kSecAttrKeyType, str)
        self.assertIsInstance(Security.kSecAttrKeySizeInBits, str)
        self.assertIsInstance(Security.kSecAttrEffectiveKeySize, str)
        self.assertIsInstance(Security.kSecAttrCanEncrypt, str)
        self.assertIsInstance(Security.kSecAttrCanDecrypt, str)
        self.assertIsInstance(Security.kSecAttrCanDerive, str)
        self.assertIsInstance(Security.kSecAttrCanSign, str)
        self.assertIsInstance(Security.kSecAttrCanVerify, str)
        self.assertIsInstance(Security.kSecAttrCanWrap, str)
        self.assertIsInstance(Security.kSecAttrCanUnwrap, str)
        self.assertIsInstance(Security.kSecAttrProtocolFTP, str)
        self.assertIsInstance(Security.kSecAttrProtocolFTPAccount, str)
        self.assertIsInstance(Security.kSecAttrProtocolHTTP, str)
        self.assertIsInstance(Security.kSecAttrProtocolIRC, str)
        self.assertIsInstance(Security.kSecAttrProtocolNNTP, str)
        self.assertIsInstance(Security.kSecAttrProtocolPOP3, str)
        self.assertIsInstance(Security.kSecAttrProtocolSMTP, str)
        self.assertIsInstance(Security.kSecAttrProtocolSOCKS, str)
        self.assertIsInstance(Security.kSecAttrProtocolIMAP, str)
        self.assertIsInstance(Security.kSecAttrProtocolLDAP, str)
        self.assertIsInstance(Security.kSecAttrProtocolAppleTalk, str)
        self.assertIsInstance(Security.kSecAttrProtocolAFP, str)
        self.assertIsInstance(Security.kSecAttrProtocolTelnet, str)
        self.assertIsInstance(Security.kSecAttrProtocolSSH, str)
        self.assertIsInstance(Security.kSecAttrProtocolFTPS, str)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPS, str)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPProxy, str)
        self.assertIsInstance(Security.kSecAttrProtocolHTTPSProxy, str)
        self.assertIsInstance(Security.kSecAttrProtocolFTPProxy, str)
        self.assertIsInstance(Security.kSecAttrProtocolSMB, str)
        self.assertIsInstance(Security.kSecAttrProtocolRTSP, str)
        self.assertIsInstance(Security.kSecAttrProtocolRTSPProxy, str)
        self.assertIsInstance(Security.kSecAttrProtocolDAAP, str)
        self.assertIsInstance(Security.kSecAttrProtocolEPPC, str)
        self.assertIsInstance(Security.kSecAttrProtocolIPP, str)
        self.assertIsInstance(Security.kSecAttrProtocolNNTPS, str)
        self.assertIsInstance(Security.kSecAttrProtocolLDAPS, str)
        self.assertIsInstance(Security.kSecAttrProtocolTelnetS, str)
        self.assertIsInstance(Security.kSecAttrProtocolIMAPS, str)
        self.assertIsInstance(Security.kSecAttrProtocolIRCS, str)
        self.assertIsInstance(Security.kSecAttrProtocolPOP3S, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeNTLM, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeMSN, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeDPA, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeRPA, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTTPBasic, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTTPDigest, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeHTMLForm, str)
        self.assertIsInstance(Security.kSecAttrAuthenticationTypeDefault, str)
        self.assertIsInstance(Security.kSecMatchPolicy, str)
        self.assertIsInstance(Security.kSecMatchItemList, str)
        self.assertIsInstance(Security.kSecMatchSearchList, str)
        self.assertIsInstance(Security.kSecMatchIssuers, str)
        self.assertIsInstance(Security.kSecMatchEmailAddressIfPresent, str)
        self.assertIsInstance(Security.kSecMatchSubjectContains, str)
        self.assertIsInstance(Security.kSecMatchTrustedOnly, str)
        self.assertIsInstance(Security.kSecMatchValidOnDate, str)
        self.assertIsInstance(Security.kSecMatchLimit, str)
        self.assertIsInstance(Security.kSecMatchLimitOne, str)
        self.assertIsInstance(Security.kSecMatchLimitAll, str)
        self.assertIsInstance(Security.kSecReturnData, str)
        self.assertIsInstance(Security.kSecReturnAttributes, str)
        self.assertIsInstance(Security.kSecReturnRef, str)
        self.assertIsInstance(Security.kSecReturnPersistentRef, str)
        self.assertIsInstance(Security.kSecValueData, str)
        self.assertIsInstance(Security.kSecValueRef, str)
        self.assertIsInstance(Security.kSecValuePersistentRef, str)
        self.assertIsInstance(Security.kSecUseItemList, str)
        self.assertIsInstance(Security.kSecMatchCaseInsensitive, str)

    @min_os_level("10.7")
    def test_constants_10_7(self):
        self.assertIsInstance(Security.kSecClassGenericPassword, str)
        self.assertIsInstance(Security.kSecClassCertificate, str)
        self.assertIsInstance(Security.kSecClassKey, str)
        self.assertIsInstance(Security.kSecClassIdentity, str)
        self.assertIsInstance(Security.kSecAttrAccess, str)
        self.assertIsInstance(Security.kSecAttrPRF, str)
        self.assertIsInstance(Security.kSecAttrSalt, str)
        self.assertIsInstance(Security.kSecAttrRounds, str)
        self.assertIsInstance(Security.kSecAttrKeyClassPublic, str)
        self.assertIsInstance(Security.kSecAttrKeyClassPrivate, str)
        self.assertIsInstance(Security.kSecAttrKeyClassSymmetric, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeRSA, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeDSA, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeAES, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeDES, str)
        self.assertIsInstance(Security.kSecAttrKeyType3DES, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeRC4, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeRC2, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeCAST, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeECDSA, str)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA1, str)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA224, str)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA256, str)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA384, str)
        self.assertIsInstance(Security.kSecAttrPRFHmacAlgSHA512, str)
        self.assertIsInstance(Security.kSecMatchSubjectStartsWith, str)
        self.assertIsInstance(Security.kSecMatchSubjectEndsWith, str)
        self.assertIsInstance(Security.kSecMatchSubjectWholeString, str)
        self.assertIsInstance(Security.kSecMatchDiacriticInsensitive, str)
        self.assertIsInstance(Security.kSecMatchWidthInsensitive, str)
        self.assertIsInstance(Security.kSecUseKeychain, str)

    @min_os_level("10.9")
    def test_constants_10_9(self):
        self.assertIsInstance(Security.kSecAttrAccessible, str)
        self.assertIsInstance(Security.kSecAttrAccessGroup, str)
        self.assertIsInstance(Security.kSecAttrSynchronizable, str)
        self.assertIsInstance(Security.kSecAttrSynchronizableAny, str)
        self.assertIsInstance(Security.kSecAttrAccessibleWhenUnlocked, str)
        self.assertIsInstance(Security.kSecAttrAccessibleAfterFirstUnlock, str)
        self.assertIsInstance(Security.kSecAttrAccessibleAlways, str)
        self.assertIsInstance(
            Security.kSecAttrAccessibleWhenUnlockedThisDeviceOnly, str
        )
        self.assertIsInstance(
            Security.kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, str
        )
        self.assertIsInstance(Security.kSecAttrAccessibleAlwaysThisDeviceOnly, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeEC, str)

    @min_os_level("10.10")
    def test_constants_10_10(self):
        self.assertIsInstance(Security.kSecAttrAccessControl, str)
        self.assertIsInstance(
            Security.kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly, str
        )
        self.assertIsInstance(Security.kSecUseOperationPrompt, str)
        self.assertIsInstance(Security.kSecUseNoAuthenticationUI, str)

    @min_os_level("10.11")
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kSecAttrSyncViewHint, str)
        self.assertIsInstance(Security.kSecUseAuthenticationUI, str)
        self.assertIsInstance(Security.kSecUseAuthenticationContext, str)
        self.assertIsInstance(Security.kSecUseAuthenticationUIAllow, str)
        self.assertIsInstance(Security.kSecUseAuthenticationUIFail, str)
        self.assertIsInstance(Security.kSecUseAuthenticationUISkip, str)

    @min_os_level("10.12")
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecAttrTokenID, str)
        self.assertIsInstance(Security.kSecAttrKeyTypeECSECPrimeRandom, str)
        self.assertIsInstance(Security.kSecAttrTokenIDSecureEnclave, str)
        self.assertIsInstance(Security.kSecAttrAccessGroupToken, str)

    @min_os_level("10.13")
    def test_constants_10_13(self):
        self.assertIsInstance(Security.kSecAttrPersistantReference, str)
        self.assertIsInstance(Security.kSecAttrPersistentReference, str)

    @min_os_level("10.15")
    def test_constants_10_15(self):
        self.assertIsInstance(Security.kSecUseDataProtectionKeychain, str)

    @min_os_level("15.0")
    def test_constants_15_0(self):
        self.assertIsInstance(Security.kSecMatchHostOrSubdomainOfHost, str)

    @min_os_level("10.6")
    def test_functions(self):
        self.assertResultHasType(Security.SecItemCopyMatching, objc._C_INT)
        self.assertArgHasType(Security.SecItemCopyMatching, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecItemCopyMatching, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecItemCopyMatching, 1)

        self.assertResultHasType(Security.SecItemAdd, objc._C_INT)
        self.assertArgHasType(Security.SecItemAdd, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecItemAdd, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecItemAdd, 1)

        self.assertResultHasType(Security.SecItemUpdate, objc._C_INT)
        self.assertArgHasType(Security.SecItemUpdate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecItemUpdate, 1, objc._C_ID)

        self.assertResultHasType(Security.SecItemDelete, objc._C_INT)
        self.assertArgHasType(Security.SecItemDelete, 0, objc._C_ID)
