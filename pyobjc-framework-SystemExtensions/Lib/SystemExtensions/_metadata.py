# This file is generated by objective.metadata
#
# Last update: Thu Nov 14 08:58:58 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

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
constants = """$NSSystemExtensionUsageDescriptionKey$OSBundleUsageDescriptionKey$OSRelatedKernelExtensionKey$OSSystemExtensionErrorDomain$"""
enums = """$OSSystemExtensionErrorAuthorizationRequired@13$OSSystemExtensionErrorCodeSignatureInvalid@8$OSSystemExtensionErrorDuplicateExtensionIdentifer@6$OSSystemExtensionErrorExtensionMissingIdentifier@5$OSSystemExtensionErrorExtensionNotFound@4$OSSystemExtensionErrorForbiddenBySystemPolicy@10$OSSystemExtensionErrorMissingEntitlement@2$OSSystemExtensionErrorRequestCanceled@11$OSSystemExtensionErrorRequestSuperseded@12$OSSystemExtensionErrorUnknown@1$OSSystemExtensionErrorUnknownExtensionCategory@7$OSSystemExtensionErrorUnsupportedParentBundleLocation@3$OSSystemExtensionErrorValidationFailed@9$OSSystemExtensionReplacementActionCancel@0$OSSystemExtensionReplacementActionReplace@1$OSSystemExtensionRequestCompleted@0$OSSystemExtensionRequestWillCompleteAfterReboot@1$"""
misc.update(
    {
        "OSSystemExtensionRequestResult": NewType(
            "OSSystemExtensionRequestResult", int
        ),
        "OSSystemExtensionReplacementAction": NewType(
            "OSSystemExtensionReplacementAction", int
        ),
        "OSSystemExtensionErrorCode": NewType("OSSystemExtensionErrorCode", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"request:actionForReplacingExtension:withExtension:",
        {
            "required": True,
            "retval": {"type": b"q"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"request:didFailWithError:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"request:didFinishWithResult:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}},
        },
    )
    r(
        b"NSObject",
        b"request:foundProperties:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"requestNeedsUserApproval:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"systemExtensionWillBecomeDisabled:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"systemExtensionWillBecomeEnabled:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"systemExtensionWillBecomeInactive:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"OSSystemExtensionProperties",
        b"isAwaitingUserApproval",
        {"retval": {"type": "Z"}},
    )
    r(b"OSSystemExtensionProperties", b"isEnabled", {"retval": {"type": "Z"}})
    r(b"OSSystemExtensionProperties", b"isUninstalling", {"retval": {"type": "Z"}})
    r(
        b"OSSystemExtensionsWorkspace",
        b"addObserver:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
