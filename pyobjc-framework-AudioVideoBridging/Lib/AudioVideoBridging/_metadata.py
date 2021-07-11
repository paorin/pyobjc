# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:22:47 2021
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
constants = """$AVBErrorDomain$AVBNullEUI64@Q$"""
enums = """$AVB17221ACMPFlagsClassB@1$AVB17221ACMPFlagsEncryptedPDU@32$AVB17221ACMPFlagsFastConnect@2$AVB17221ACMPFlagsNone@0$AVB17221ACMPFlagsSavedState@4$AVB17221ACMPFlagsStreamingConnectedListenersValid@128$AVB17221ACMPFlagsStreamingNoStreamReservationProtocol@256$AVB17221ACMPFlagsStreamingTalkerFailed@64$AVB17221ACMPFlagsStreamingUsingUDP@512$AVB17221ACMPFlagsStreamingWait@8$AVB17221ACMPFlagsSupportsEncrypted@16$AVB17221ACMPIPFlagNone@0$AVB17221ACMPMessageTypeConnectRXCommand@6$AVB17221ACMPMessageTypeConnectRXResponse@7$AVB17221ACMPMessageTypeConnectTXCommand@0$AVB17221ACMPMessageTypeConnectTXResponse@1$AVB17221ACMPMessageTypeDisconnectRXCommand@8$AVB17221ACMPMessageTypeDisconnectRXResponse@9$AVB17221ACMPMessageTypeDisconnectTXCommand@2$AVB17221ACMPMessageTypeDisconnectTXResponse@3$AVB17221ACMPMessageTypeGetRXStateCommand@10$AVB17221ACMPMessageTypeGetRXStateResponse@11$AVB17221ACMPMessageTypeGetTXConnectionCommand@12$AVB17221ACMPMessageTypeGetTXConnectionResponse@13$AVB17221ACMPMessageTypeGetTXStateCommand@4$AVB17221ACMPMessageTypeGetTXStateResponse@5$AVB17221ACMPStatusControllerNotAuthorized@16$AVB17221ACMPStatusIncompatibleRequest@17$AVB17221ACMPStatusListenerCanOnlyListenOnce@19$AVB17221ACMPStatusListenerExclusive@8$AVB17221ACMPStatusListenerInvalidConnection@18$AVB17221ACMPStatusListenerMisbehaving@14$AVB17221ACMPStatusListenerTalkerTimeout@7$AVB17221ACMPStatusListenerUnknownID@1$AVB17221ACMPStatusNoSuchConnection@11$AVB17221ACMPStatusNotConnected@10$AVB17221ACMPStatusNotSupported@31$AVB17221ACMPStatusSRPFace@15$AVB17221ACMPStatusStateUnavailable@9$AVB17221ACMPStatusSuccess@0$AVB17221ACMPStatusTalkerDestMACFail@3$AVB17221ACMPStatusTalkerExclusive@6$AVB17221ACMPStatusTalkerMisbehaving@13$AVB17221ACMPStatusTalkerNoBandwidth@5$AVB17221ACMPStatusTalkerNoStreamIndex@4$AVB17221ACMPStatusTalkerUnknownID@2$AVB17221ACMPStatusUnableToSendMessage@12$AVB17221ADPControllerCapabilitiesHasLayer3Proxy@2$AVB17221ADPControllerCapabilitiesImplemented@1$AVB17221ADPEntityCapabilitiesACMPAcquireWithAEM@262144$AVB17221ADPEntityCapabilitiesACMPAuthenticateWithAEM@524288$AVB17221ADPEntityCapabilitiesAEMAuthenticationRequired@4096$AVB17221ADPEntityCapabilitiesAEMAuthenticationSupported@2048$AVB17221ADPEntityCapabilitiesAEMIdenitifyControlIndexValid@16384$AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValid@32768$AVB17221ADPEntityCapabilitiesAEMPersistentAcquireSupported@8192$AVB17221ADPEntityCapabilitiesAEMSupported@8$AVB17221ADPEntityCapabilitiesASSupported@1024$AVB17221ADPEntityCapabilitiesAddressAccessSupported@2$AVB17221ADPEntityCapabilitiesAssociationIDSupported@32$AVB17221ADPEntityCapabilitiesAssociationIDValid@64$AVB17221ADPEntityCapabilitiesClassASupported@256$AVB17221ADPEntityCapabilitiesClassBSupported@512$AVB17221ADPEntityCapabilitiesDFUMode@1$AVB17221ADPEntityCapabilitiesEFUMode@1$AVB17221ADPEntityCapabilitiesEntityNotReady@131072$AVB17221ADPEntityCapabilitiesGPTPSupported@1024$AVB17221ADPEntityCapabilitiesGatewayEntity@4$AVB17221ADPEntityCapabilitiesGeneralControllerIgnore@65536$AVB17221ADPEntityCapabilitiesLegacyAVC@16$AVB17221ADPEntityCapabilitiesMultiplePTPInstances@16777216$AVB17221ADPEntityCapabilitiesSupportsUDPv4ATDECC@1048576$AVB17221ADPEntityCapabilitiesSupportsUDPv4Streaming@2097152$AVB17221ADPEntityCapabilitiesSupportsUDPv6ATDECC@4194304$AVB17221ADPEntityCapabilitiesSupportsUDPv6Streaming@8388608$AVB17221ADPEntityCapabilitiesVendorUniqueSupported@128$AVB17221ADPListenerCapabilitiesHasAudioSink@16384$AVB17221ADPListenerCapabilitiesHasControlSink@1024$AVB17221ADPListenerCapabilitiesHasMIDISink@8192$AVB17221ADPListenerCapabilitiesHasMediaClockSink@2048$AVB17221ADPListenerCapabilitiesHasOtherSink@512$AVB17221ADPListenerCapabilitiesHasSMPTESink@4096$AVB17221ADPListenerCapabilitiesHasVideoSink@32768$AVB17221ADPListenerCapabilitiesImplemented@1$AVB17221ADPTalkerCapabilitiesHasAudioSource@16384$AVB17221ADPTalkerCapabilitiesHasControlSource@1024$AVB17221ADPTalkerCapabilitiesHasMIDISource@8192$AVB17221ADPTalkerCapabilitiesHasMediaClockSource@2048$AVB17221ADPTalkerCapabilitiesHasOtherSource@512$AVB17221ADPTalkerCapabilitiesHasSMPTESource@4096$AVB17221ADPTalkerCapabilitiesHasVideoSource@32768$AVB17221ADPTalkerCapabilitiesImplemented@1$AVB17221AECPAddressAccessTLVModeExecute@2$AVB17221AECPAddressAccessTLVModeRead@0$AVB17221AECPAddressAccessTLVModeWrite@1$AVB17221AECPMessageTypeAEMCommand@0$AVB17221AECPMessageTypeAEMResponse@1$AVB17221AECPMessageTypeAddressAccessCommand@2$AVB17221AECPMessageTypeAddressAccessResponse@3$AVB17221AECPMessageTypeLegacyAVCCommand@4$AVB17221AECPMessageTypeLegacyAVCResponse@5$AVB17221AECPMessageTypeVendorUniqueCommand@6$AVB17221AECPMessageTypeVendorUniqueResponse@7$AVB17221AECPStatusAVCFailure@2$AVB17221AECPStatusAddressAccessAddressInvalid@4$AVB17221AECPStatusAddressAccessAddressTooHigh@3$AVB17221AECPStatusAddressAccessAddressTooLow@2$AVB17221AECPStatusAddressAccessDataInvalid@6$AVB17221AECPStatusAddressAccessTLVInvalid@5$AVB17221AECPStatusAddressAccessUnsupported@7$AVB17221AECPStatusBadArguments@7$AVB17221AECPStatusEntityAcquired@4$AVB17221AECPStatusEntityLocked@3$AVB17221AECPStatusEntityMisbehaving@10$AVB17221AECPStatusInProgress@9$AVB17221AECPStatusInsufficientPrivileges@6$AVB17221AECPStatusNoResources@8$AVB17221AECPStatusNoSuchDescriptor@2$AVB17221AECPStatusNotAuthorized@5$AVB17221AECPStatusNotImplemented@1$AVB17221AECPStatusNotSupported@11$AVB17221AECPStatusStreamIsRunning@12$AVB17221AECPStatusSuccess@0$AVB17221AEMCommandTypeAbortOperation@53$AVB17221AEMCommandTypeAcquireEntity@0$AVB17221AEMCommandTypeAddAudioMapping@44$AVB17221AEMCommandTypeAddSensorMapping@50$AVB17221AEMCommandTypeAddVideoMapping@47$AVB17221AEMCommandTypeAuthenticate@65$AVB17221AEMCommandTypeAuthenticateAddKey@55$AVB17221AEMCommandTypeAuthenticateAddKeyToChain@59$AVB17221AEMCommandTypeAuthenticateAddToken@63$AVB17221AEMCommandTypeAuthenticateDeleteKey@56$AVB17221AEMCommandTypeAuthenticateDeleteKeyFromChain@60$AVB17221AEMCommandTypeAuthenticateDeleteToken@64$AVB17221AEMCommandTypeAuthenticateGetIdentity@62$AVB17221AEMCommandTypeAuthenticateGetKey@58$AVB17221AEMCommandTypeAuthenticateGetKeyList@57$AVB17221AEMCommandTypeAuthenticateGetKeychainList@61$AVB17221AEMCommandTypeControllerAvailable@3$AVB17221AEMCommandTypeDeauthenticate@66$AVB17221AEMCommandTypeDecrementControl@27$AVB17221AEMCommandTypeDeregisterUnsolicitedNotification@37$AVB17221AEMCommandTypeDisableStreamEncryption@70$AVB17221AEMCommandTypeDisableTransportSecurity@68$AVB17221AEMCommandTypeEnableStreamEncryption@69$AVB17221AEMCommandTypeEnableTransportSecurity@67$AVB17221AEMCommandTypeEntityAvailable@2$AVB17221AEMCommandTypeGetASPath@40$AVB17221AEMCommandTypeGetAVBInfo@39$AVB17221AEMCommandTypeGetAssociationID@19$AVB17221AEMCommandTypeGetAudioMap@43$AVB17221AEMCommandTypeGetClockSource@23$AVB17221AEMCommandTypeGetConfiguration@7$AVB17221AEMCommandTypeGetControl@25$AVB17221AEMCommandTypeGetCounters@41$AVB17221AEMCommandTypeGetDynamicInfo@75$AVB17221AEMCommandTypeGetMatrix@33$AVB17221AEMCommandTypeGetMaxTransitTime@77$AVB17221AEMCommandTypeGetMemoryObjectLength@72$AVB17221AEMCommandTypeGetMixer@31$AVB17221AEMCommandTypeGetName@17$AVB17221AEMCommandTypeGetPTPInstanceExtendedInfo@82$AVB17221AEMCommandTypeGetPTPInstanceGrandmasterInfo@83$AVB17221AEMCommandTypeGetPTPInstanceInfo@81$AVB17221AEMCommandTypeGetPTPInstancePathCount@84$AVB17221AEMCommandTypeGetPTPInstancePathTrace@85$AVB17221AEMCommandTypeGetPTPInstancePerformanceMonitoringCount@86$AVB17221AEMCommandTypeGetPTPInstancePerformanceMonitoringRecord@87$AVB17221AEMCommandTypeGetPTPPortCurrentIntervals@91$AVB17221AEMCommandTypeGetPTPPortInfo@95$AVB17221AEMCommandTypeGetPTPPortInitialIntervals@89$AVB17221AEMCommandTypeGetPTPPortOverrides@97$AVB17221AEMCommandTypeGetPTPPortPDelayMonitoringCount@98$AVB17221AEMCommandTypeGetPTPPortPDelayMonitoringRecord@99$AVB17221AEMCommandTypeGetPTPPortPerformanceMonitoringCount@100$AVB17221AEMCommandTypeGetPTPPortPerformanceMonitoringRecord@101$AVB17221AEMCommandTypeGetPTPPortRemoteIntervals@93$AVB17221AEMCommandTypeGetPathLatency@102$AVB17221AEMCommandTypeGetSamplingRate@21$AVB17221AEMCommandTypeGetSamplingRateRange@79$AVB17221AEMCommandTypeGetSensorFormat@13$AVB17221AEMCommandTypeGetSensorMap@49$AVB17221AEMCommandTypeGetSignalSelector@29$AVB17221AEMCommandTypeGetStreamBackup@74$AVB17221AEMCommandTypeGetStreamFormat@9$AVB17221AEMCommandTypeGetStreamInfo@15$AVB17221AEMCommandTypeGetVideoFormat@11$AVB17221AEMCommandTypeGetVideoMap@46$AVB17221AEMCommandTypeIdentifyNotification@38$AVB17221AEMCommandTypeIncrementControl@26$AVB17221AEMCommandTypeLockEntity@1$AVB17221AEMCommandTypeOperationStatus@54$AVB17221AEMCommandTypeReadDescriptor@4$AVB17221AEMCommandTypeReboot@42$AVB17221AEMCommandTypeRegisterUnsolicitedNotification@36$AVB17221AEMCommandTypeRemoveAudioMapping@45$AVB17221AEMCommandTypeRemoveSensorMapping@51$AVB17221AEMCommandTypeRemoveVideoMapping@48$AVB17221AEMCommandTypeSetAssociationID@18$AVB17221AEMCommandTypeSetClockSource@22$AVB17221AEMCommandTypeSetConfiguration@6$AVB17221AEMCommandTypeSetControl@24$AVB17221AEMCommandTypeSetMatrix@32$AVB17221AEMCommandTypeSetMaxTransitTime@76$AVB17221AEMCommandTypeSetMemoryObjectLength@71$AVB17221AEMCommandTypeSetMixer@30$AVB17221AEMCommandTypeSetName@16$AVB17221AEMCommandTypeSetPTPInstanceInfo@80$AVB17221AEMCommandTypeSetPTPPortInfo@94$AVB17221AEMCommandTypeSetPTPPortInitialIntervals@88$AVB17221AEMCommandTypeSetPTPPortOverrides@96$AVB17221AEMCommandTypeSetPTPPortRemoteIntervals@92$AVB17221AEMCommandTypeSetSampingRateRange@78$AVB17221AEMCommandTypeSetSamplingRate@20$AVB17221AEMCommandTypeSetSensorFormat@12$AVB17221AEMCommandTypeSetSignalSelector@28$AVB17221AEMCommandTypeSetStreamBackup@73$AVB17221AEMCommandTypeSetStreamFormat@8$AVB17221AEMCommandTypeSetStreamInfo@14$AVB17221AEMCommandTypeSetVideoFormat@10$AVB17221AEMCommandTypeStartOperation@52$AVB17221AEMCommandTypeStartStreaming@34$AVB17221AEMCommandTypeStopStreaming@35$AVB17221AEMCommandTypeWriteDescriptor@5$AVB17221EntityPropertyChangedASGrandmasterID@2048$AVB17221EntityPropertyChangedAssociationID@32768$AVB17221EntityPropertyChangedAvailableIndex@1024$AVB17221EntityPropertyChangedControllerCapabilities@512$AVB17221EntityPropertyChangedEntityCapabilities@16$AVB17221EntityPropertyChangedEntityID@2$AVB17221EntityPropertyChangedEntityType@65536$AVB17221EntityPropertyChangedGPTPDomainNumber@524288$AVB17221EntityPropertyChangedGPTPGrandmasterID@2048$AVB17221EntityPropertyChangedGUID@2$AVB17221EntityPropertyChangedIdentifyControlIndex@131072$AVB17221EntityPropertyChangedInterfaceIndex@262144$AVB17221EntityPropertyChangedListenerCapabilities@256$AVB17221EntityPropertyChangedListenerStreamSinks@128$AVB17221EntityPropertyChangedMACAddress@4096$AVB17221EntityPropertyChangedModelID@8$AVB17221EntityPropertyChangedTalkerCapabilities@64$AVB17221EntityPropertyChangedTalkerStreamSources@32$AVB17221EntityPropertyChangedTimeToLive@1$AVB17221EntityPropertyChangedVendorID@4$AVBMACAddressSize@6$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AVB17221ACMPInterface",
        b"sendACMPCommandMessage:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            },
        },
    )
    r(
        b"AVB17221ACMPInterface",
        b"sendACMPResponseMessage:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"AVB17221ACMPInterface", b"setHandler:forEntityID:", {"retval": {"type": b"Z"}})
    r(b"AVB17221AECPAEMMessage", b"isControllerRequest", {"retval": {"type": b"Z"}})
    r(b"AVB17221AECPAEMMessage", b"isUnsolicited", {"retval": {"type": b"Z"}})
    r(
        b"AVB17221AECPAEMMessage",
        b"setControllerRequest:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"AVB17221AECPAEMMessage", b"setUnsolicited:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"AVB17221AECPInterface",
        b"sendCommand:toMACAddress:completionHandler:",
        {
            "retval": {"type": b"Z"},
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"@?"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            },
        },
    )
    r(
        b"AVB17221AECPInterface",
        b"sendResponse:toMACAddress:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"AVB17221AECPInterface",
        b"setCommandHandler:forEntityID:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVB17221AECPInterface",
        b"setResponseHandler:forControllerEntityID:",
        {"retval": {"type": b"Z"}},
    )
    r(b"AVB17221Entity", b"isLocalEntity", {"retval": {"type": b"Z"}})
    r(b"AVB17221Entity", b"setLocalEntity:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"AVB17221EntityDiscovery",
        b"addLocalEntity:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"AVB17221EntityDiscovery",
        b"changeEntityWithEntityID:toNewGPTPGrandmasterID:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(b"AVB17221EntityDiscovery", b"discoverEntities", {"retval": {"type": b"Z"}})
    r(b"AVB17221EntityDiscovery", b"discoverEntity:", {"retval": {"type": b"Z"}})
    r(
        b"AVB17221EntityDiscovery",
        b"removeLocalEntity:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"AVBCentralManager",
        b"streamingEnabledInterfacesOnly",
        {"retval": {"type": b"Z"}},
    )
    r(b"AVBIPAddress", b"representsIPv4Address", {"retval": {"type": b"Z"}})
    r(b"AVBInterface", b"isAVBCapableInterfaceNamed:", {"retval": {"type": b"Z"}})
    r(b"AVBInterface", b"isAVBEnabledOnInterfaceNamed:", {"retval": {"type": b"Z"}})
    r(b"AVBMACAddress", b"isMulticast", {"retval": {"type": b"Z"}})
    r(b"AVBMACAddress", b"setMulticast:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"NSObject",
        b"ACMPDidReceiveCommand:onInterface:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"ACMPDidReceiveResponse:onInterface:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"AECPDidReceiveCommand:onInterface:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"AECPDidReceiveResponse:onInterface:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didAddLocalEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didAddRemoteEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didRediscoverLocalEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didRediscoverRemoteEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didRemoveLocalEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didRemoveRemoteEntity:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didUpdateLocalEntity:changedProperties:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"Q"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"didUpdateRemoteEntity:changedProperties:on17221EntityDiscovery:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"Q"}, 4: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {
    "kAVB17221EntityPropertyChangedShouldntChangeMask": "(AVB17221EntityPropertyChangedEntityID | AVB17221EntityPropertyChangedVendorID | AVB17221EntityPropertyChangedModelID | AVB17221EntityPropertyChangedTalkerStreamSources | AVB17221EntityPropertyChangedTalkerCapabilities | AVB17221EntityPropertyChangedListenerStreamSinks | AVB17221EntityPropertyChangedListenerCapabilities | AVB17221EntityPropertyChangedControllerCapabilities | AVB17221EntityPropertyChangedMACAddress | AVB17221EntityPropertyChangedAssociationID | AVB17221EntityPropertyChangedEntityType | AVB17221EntityPropertyChangedIdentifyControlIndex | AVB17221EntityPropertyChangedInterfaceIndex)"
}

# END OF FILE
