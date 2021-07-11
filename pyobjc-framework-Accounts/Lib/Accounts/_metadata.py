# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:20:09 2021
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a


else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$ACAccountStoreDidChangeNotification$ACAccountTypeIdentifierFacebook$ACAccountTypeIdentifierLinkedIn$ACAccountTypeIdentifierSinaWeibo$ACAccountTypeIdentifierTencentWeibo$ACAccountTypeIdentifierTwitter$ACErrorDomain$ACFacebookAppIdKey$ACFacebookAppVersionKey$ACFacebookAudienceEveryone$ACFacebookAudienceFriends$ACFacebookAudienceKey$ACFacebookAudienceOnlyMe$ACFacebookPermissionGroupKey$ACFacebookPermissionGroupRead$ACFacebookPermissionGroupReadWrite$ACFacebookPermissionGroupWrite$ACFacebookPermissionsKey$ACLinkedInAppIdKey$ACLinkedInPermissionsKey$ACTencentWeiboAppIdKey$"""
enums = """$ACAccountCredentialRenewResultFailed@2$ACAccountCredentialRenewResultRejected@1$ACAccountCredentialRenewResultRenewed@0$ACErrorAccessDeniedByProtectionPolicy@10$ACErrorAccessInfoInvalid@8$ACErrorAccountAlreadyExists@5$ACErrorAccountAuthenticationFailed@3$ACErrorAccountMissingRequiredProperty@2$ACErrorAccountNotFound@6$ACErrorAccountTypeInvalid@4$ACErrorClientPermissionDenied@9$ACErrorCoreDataSaveFailed@18$ACErrorCredentialItemNotExpired@23$ACErrorCredentialItemNotFound@22$ACErrorCredentialNotFound@11$ACErrorDeniedByPlugin@17$ACErrorFailedSerializingAccountInfo@19$ACErrorFetchCredentialFailed@12$ACErrorInvalidClientBundleID@16$ACErrorInvalidCommand@20$ACErrorMissingTransportMessageID@21$ACErrorPermissionDenied@7$ACErrorRemoveCredentialFailed@14$ACErrorStoreCredentialFailed@13$ACErrorUnknown@1$ACErrorUpdatingNonexistentAccount@15$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"ACAccountStore",
        b"removeAccount:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ACAccountStore",
        b"renewCredentialsForAccount:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": sel32or64(b"i", b"q")},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ACAccountStore",
        b"requestAccessToAccountsWithType:options:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ACAccountStore",
        b"requestAccessToAccountsWithType:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"ACAccountStore",
        b"saveAccount:withCompletionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"ACAccountType", b"accessGranted", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
