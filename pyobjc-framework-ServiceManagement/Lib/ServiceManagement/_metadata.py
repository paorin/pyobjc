# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:52:51 2021
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
constants = """$kSMDomainSystemLaunchd$kSMDomainUserLaunchd$kSMErrorDomainFramework$kSMErrorDomainIPC$kSMErrorDomainLaunchd$kSMInfoKeyAuthorizedClients$kSMInfoKeyPrivilegedExecutables$"""
enums = """$kSMErrorAuthorizationFailure@4$kSMErrorInternalFailure@2$kSMErrorInvalidPlist@10$kSMErrorInvalidSignature@3$kSMErrorJobMustBeEnabled@9$kSMErrorJobNotFound@6$kSMErrorJobPlistNotFound@8$kSMErrorServiceUnavailable@7$kSMErrorToolNotValid@5$"""
misc.update(
    {
        "kSMRightModifySystemDaemons": b"com.apple.ServiceManagement.daemons.modify",
        "kSMRightBlessPrivilegedHelper": b"com.apple.ServiceManagement.blesshelper",
    }
)
functions = {
    "SMJobBless": (
        b"Z^{__CFString=}^{__CFString=}^{AuthorizationOpaqueRef=}^^{__CFError}",
        "",
        {
            "arguments": {
                3: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            }
        },
    ),
    "SMJobRemove": (
        b"Z^{__CFString=}^{__CFString=}^{AuthorizationOpaqueRef=}Z^^{__CFError}",
        "",
        {
            "arguments": {
                4: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            }
        },
    ),
    "SMJobCopyDictionary": (
        b"^{__CFDictionary=}^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SMJobSubmit": (
        b"Z^{__CFString=}^{__CFDictionary=}^{AuthorizationOpaqueRef=}^^{__CFError}",
        "",
        {
            "arguments": {
                3: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            }
        },
    ),
    "SMLoginItemSetEnabled": (b"Z^{__CFString=}Z",),
    "SMCopyAllJobDictionaries": (
        b"^{__CFArray=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
expressions = {}

# END OF FILE
