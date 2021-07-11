# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:30:36 2021
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
constants = """$$"""
enums = """$$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"CBIdentity", b"CSIdentity", {"retval": {"type": "^{__CSIdentity=}"}})
    r(b"CBIdentity", b"UUIDString", {"deprecated": 1011})
    r(
        b"CBIdentity",
        b"identityWithCSIdentity:",
        {"arguments": {2: {"type": "^{__CSIdentity=}"}}},
    )
    r(b"CBIdentity", b"identityWithUUIDString:authority:", {"deprecated": 1011})
    r(b"CBIdentity", b"isHidden", {"retval": {"type": "Z"}})
    r(b"CBIdentity", b"isMemberOfGroup:", {"retval": {"type": "Z"}})
    r(b"CBIdentity", b"members", {"deprecated": 1011})
    r(
        b"CBIdentityAuthority",
        b"CSIdentityAuthority",
        {"retval": {"type": "^{__CSIdentityAuthority=}"}},
    )
    r(
        b"CBIdentityAuthority",
        b"identityAuthorityWithCSIdentityAuthority:",
        {"arguments": {2: {"type": "^{__CSIdentityAuthority=}"}}},
    )
    r(b"CBIdentityPicker", b"allowsMultipleSelection", {"retval": {"type": "Z"}})
    r(
        b"CBIdentityPicker",
        b"runModalForWindow:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"I"}},
                    }
                }
            }
        },
    )
    r(
        b"CBIdentityPicker",
        b"runModalForWindow:modalDelegate:didEndSelector:contextInfo:",
        {
            "deprecated": 1011,
            "arguments": {
                4: {"sel_of_type": sel32or64(b"v@:@i^v", b"v@:@q^v")},
                5: {"type": "^v"},
            },
        },
    )
    r(
        b"CBIdentityPicker",
        b"setAllowsMultipleSelection:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"CBUserIdentity", b"authenticateWithPassword:", {"retval": {"type": "Z"}})
    r(
        b"CBUserIdentity",
        b"certificate",
        {"retval": {"type": "^{OpaqueSecCertificateRef=}"}},
    )
    r(b"CBUserIdentity", b"isEnabled", {"retval": {"type": "Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
