# This file is generated by objective.metadata
#
# Last update: Fri Nov 15 12:08:25 2024
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
constants = """$ODFrameworkErrorDomain$ODSessionProxyAddress$ODSessionProxyPassword$ODSessionProxyPort$ODSessionProxyUsername$ODTrustTypeAnonymous$ODTrustTypeJoined$ODTrustTypeUsingCredentials$"""
enums = """$ODPacketEncryptionAllow@1$ODPacketEncryptionDisabled@0$ODPacketEncryptionRequired@2$ODPacketEncryptionSSL@3$ODPacketSigningAllow@1$ODPacketSigningDisabled@0$ODPacketSigningRequired@2$kODErrorCredentialsAccountLocked@5305$kODErrorCredentialsAccountTemporarilyLocked@5304$kODErrorCredentialsContactPrimary@5204$kODErrorPolicyOutOfRange@6001$kODErrorPolicyUnsupported@6000$kODExpirationTimeExpired@0$kODExpirationTimeNeverExpires@-1$"""
misc.update({})
misc.update({})
misc.update({})
aliases = {"kODErrorCredentialsContactMaster": "kODErrorCredentialsContactPrimary"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"query:foundResults:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"ODConfiguration",
        b"addTrustType:trustAccount:trustPassword:username:password:joinExisting:error:",
        {
            "retval": {"type": b"Z"},
            "arguments": {7: {"type": b"Z"}, 8: {"type_modifier": b"o"}},
        },
    )
    r(b"ODConfiguration", b"hideRegistration", {"retval": {"type": b"Z"}})
    r(b"ODConfiguration", b"manInTheMiddleProtection", {"retval": {"type": b"Z"}})
    r(
        b"ODConfiguration",
        b"removeTrustUsingUsername:password:deleteTrustAccount:error:",
        {
            "retval": {"type": b"Z"},
            "arguments": {4: {"type": b"Z"}, 5: {"type_modifier": b"o"}},
        },
    )
    r(
        b"ODConfiguration",
        b"saveUsingAuthorization:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"ODConfiguration", b"setHideRegistration:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"ODConfiguration",
        b"setManInTheMiddleProtection:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"ODConfiguration", b"trustUsesKerberosKeytab", {"retval": {"type": b"Z"}})
    r(b"ODConfiguration", b"trustUsesMutualAuthentication", {"retval": {"type": b"Z"}})
    r(b"ODConfiguration", b"trustUsesSystemKeychain", {"retval": {"type": b"Z"}})
    r(
        b"ODNode",
        b"accountPoliciesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"addAccountPolicy:toCategory:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"createRecordWithRecordType:name:attributes:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"customCall:sendData:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"customFunction:payload:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"initWithSession:name:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"initWithSession:type:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"nodeDetailsForKeys:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"nodeWithSession:name:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"nodeWithSession:type:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"passwordContentCheck:forRecordName:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"policiesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"recordWithRecordType:name:attributes:error:",
        {"arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"removeAccountPolicy:fromCategory:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"removePolicy:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"setAccountPolicies:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"setCredentialsUsingKerberosCache:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"setCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                5: {"type_modifier": b"o"},
                6: {"type_modifier": b"o"},
                7: {"type_modifier": b"o"},
            },
        },
    )
    r(
        b"ODNode",
        b"setCredentialsWithRecordType:recordName:password:error:",
        {"retval": {"type": b"Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"setPolicies:error:",
        {"retval": {"type": "Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"setPolicy:value:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"subnodeNamesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"supportedAttributesForRecordType:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"supportedPoliciesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"supportedRecordTypesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODNode",
        b"unreachableSubnodeNamesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODQuery",
        b"initWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:",
        {"arguments": {9: {"type_modifier": b"o"}}},
    )
    r(
        b"ODQuery",
        b"queryWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:",
        {"arguments": {9: {"type_modifier": b"o"}}},
    )
    r(
        b"ODQuery",
        b"resultsAllowingPartial:error:",
        {"arguments": {2: {"type": b"Z"}, 3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"accountPoliciesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"addAccountPolicy:toCategory:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"addMemberRecord:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"addValue:toAttribute:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"authenticationAllowedAndReturnError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"changePassword:toPassword:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"deleteRecordAndReturnError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"effectivePoliciesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"isMemberRecord:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"passwordChangeAllowed:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"passwordPolicyAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"policiesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"recordDetailsForAttributes:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"removeAccountPolicy:fromCategory:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"removeMemberRecord:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"removePolicy:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"removeValue:fromAttribute:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"removeValuesForAttribute:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setAccountPolicies:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setNodeCredentials:password:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setNodeCredentialsUsingKerberosCache:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setNodeCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                5: {"type_modifier": b"o"},
                6: {"type_modifier": b"o"},
                7: {"type_modifier": b"o"},
            },
        },
    )
    r(
        b"ODRecord",
        b"setPolicies:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setPolicy:value:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"setValue:forAttribute:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"supportedPoliciesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"synchronizeAndReturnError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"valuesForAttribute:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODRecord",
        b"verifyExtendedWithAuthenticationType:authenticationItems:continueItems:context:error:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                4: {"type_modifier": b"o"},
                5: {"type_modifier": b"o"},
                6: {"type_modifier": b"o"},
            },
        },
    )
    r(
        b"ODRecord",
        b"verifyPassword:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"ODRecord", b"willAuthenticationsExpire:", {"retval": {"type": b"Z"}})
    r(b"ODRecord", b"willPasswordExpire:", {"retval": {"type": b"Z"}})
    r(
        b"ODSession",
        b"addConfiguration:authorization:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"configurationAuthorizationAllowingUserInteraction:error:",
        {"arguments": {2: {"type": b"Z"}, 3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"deleteConfiguration:authorization:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"deleteConfigurationWithNodename:authorization:error:",
        {"retval": {"type": "Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"initWithOptions:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"nodeNamesAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"ODSession",
        b"sessionWithOptions:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("ODNode", b"initWithSession:name:error:")
objc.registerNewKeywordsFromSelector("ODNode", b"initWithSession:type:error:")
objc.registerNewKeywordsFromSelector(
    "ODQuery",
    b"initWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:",
)
objc.registerNewKeywordsFromSelector("ODSession", b"initWithOptions:error:")
expressions = {}

# END OF FILE
