# This file is generated by objective.metadata
#
# Last update: Thu Dec  2 21:15:24 2021
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
misc.update(
    {
        "ColorSyncMD5": objc.createStructType(
            "ColorSync.ColorSyncMD5", b"{_ColorSyncMD5=[16C]}", ["digest"]
        )
    }
)
constants = """$kCMMApplyTransformProcName$kCMMCreateTransformPropertyProcName$kCMMInitializeLinkProfileProcName$kCMMInitializeTransformProcName$kColorSyncACESCGLinearProfile$kColorSyncAdobeRGB1998Profile$kColorSyncBestQuality$kColorSyncBlackPointCompensation$kColorSyncCameraDeviceClass$kColorSyncConversion1DLut$kColorSyncConversion3DLut$kColorSyncConversionBPC$kColorSyncConversionChannelID$kColorSyncConversionGridPoints$kColorSyncConversionInpChan$kColorSyncConversionMatrix$kColorSyncConversionNDLut$kColorSyncConversionOutChan$kColorSyncConversionParamCurve0$kColorSyncConversionParamCurve1$kColorSyncConversionParamCurve2$kColorSyncConversionParamCurve3$kColorSyncConversionParamCurve4$kColorSyncConvertQuality$kColorSyncConvertThreadCount$kColorSyncConvertUseExtendedRange$kColorSyncConvertUseVectorUnit$kColorSyncCustomProfiles$kColorSyncDCIP3Profile$kColorSyncDeviceClass$kColorSyncDeviceDefaultProfileID$kColorSyncDeviceDescription$kColorSyncDeviceDescriptions$kColorSyncDeviceHostScope$kColorSyncDeviceID$kColorSyncDeviceModeDescription$kColorSyncDeviceModeDescriptions$kColorSyncDeviceProfileID$kColorSyncDeviceProfileIsCurrent$kColorSyncDeviceProfileIsDefault$kColorSyncDeviceProfileIsFactory$kColorSyncDeviceProfileURL$kColorSyncDeviceProfilesNotification$kColorSyncDeviceRegisteredNotification$kColorSyncDeviceUnregisteredNotification$kColorSyncDeviceUserScope$kColorSyncDisplayDeviceClass$kColorSyncDisplayDeviceProfilesNotification$kColorSyncDisplayP3Profile$kColorSyncDraftQuality$kColorSyncExtendedRange$kColorSyncFactoryProfiles$kColorSyncFixedPointRange$kColorSyncGenericCMYKProfile$kColorSyncGenericGrayGamma22Profile$kColorSyncGenericGrayProfile$kColorSyncGenericLabProfile$kColorSyncGenericRGBProfile$kColorSyncGenericXYZProfile$kColorSyncITUR2020Profile$kColorSyncITUR709Profile$kColorSyncNormalQuality$kColorSyncPreferredCMM$kColorSyncPrinterDeviceClass$kColorSyncProfile$kColorSyncProfileCacheSeed$kColorSyncProfileClass$kColorSyncProfileColorSpace$kColorSyncProfileComputerDomain$kColorSyncProfileDescription$kColorSyncProfileHeader$kColorSyncProfileHostScope$kColorSyncProfileMD5Digest$kColorSyncProfilePCS$kColorSyncProfileRepositoryChangeNotification$kColorSyncProfileURL$kColorSyncProfileUserDomain$kColorSyncProfileUserScope$kColorSyncROMMRGBProfile$kColorSyncRegistrationUpdateWindowServer$kColorSyncRenderingIntent$kColorSyncRenderingIntentAbsolute$kColorSyncRenderingIntentPerceptual$kColorSyncRenderingIntentRelative$kColorSyncRenderingIntentSaturation$kColorSyncRenderingIntentUseProfileHeader$kColorSyncSRGBProfile$kColorSyncScannerDeviceClass$kColorSyncSigAToB0Tag$kColorSyncSigAToB1Tag$kColorSyncSigAToB2Tag$kColorSyncSigAbstractClass$kColorSyncSigBToA0Tag$kColorSyncSigBToA1Tag$kColorSyncSigBToA2Tag$kColorSyncSigBlueColorantTag$kColorSyncSigBlueTRCTag$kColorSyncSigCmykData$kColorSyncSigColorSpaceClass$kColorSyncSigCopyrightTag$kColorSyncSigDeviceMfgDescTag$kColorSyncSigDeviceModelDescTag$kColorSyncSigDisplayClass$kColorSyncSigGamutTag$kColorSyncSigGrayData$kColorSyncSigGrayTRCTag$kColorSyncSigGreenColorantTag$kColorSyncSigGreenTRCTag$kColorSyncSigInputClass$kColorSyncSigLabData$kColorSyncSigLinkClass$kColorSyncSigMediaBlackPointTag$kColorSyncSigMediaWhitePointTag$kColorSyncSigNamedColor2Tag$kColorSyncSigNamedColorClass$kColorSyncSigOutputClass$kColorSyncSigPreview0Tag$kColorSyncSigPreview1Tag$kColorSyncSigPreview2Tag$kColorSyncSigProfileDescriptionTag$kColorSyncSigProfileSequenceDescTag$kColorSyncSigRedColorantTag$kColorSyncSigRedTRCTag$kColorSyncSigRgbData$kColorSyncSigTechnologyTag$kColorSyncSigViewingCondDescTag$kColorSyncSigViewingConditionsTag$kColorSyncSigXYZData$kColorSyncTranformInfo$kColorSyncTransformCodeFragmentMD5$kColorSyncTransformCodeFragmentType$kColorSyncTransformCreator$kColorSyncTransformDeviceToDevice$kColorSyncTransformDeviceToPCS$kColorSyncTransformDstSpace$kColorSyncTransformFullConversionData$kColorSyncTransformGamutCheck$kColorSyncTransformInfo$kColorSyncTransformPCSToDevice$kColorSyncTransformPCSToPCS$kColorSyncTransformParametricConversionData$kColorSyncTransformProfileSequnce$kColorSyncTransformSimplifiedConversionData$kColorSyncTransformSrcSpace$kColorSyncTransformTag$kColorSyncWaitForCacheReply$"""
enums = """$COLORSYNC_MD5_LENGTH@16$kColorSync10BitInteger@8$kColorSync16BitFloat@4$kColorSync16BitInteger@3$kColorSync1BitGamut@1$kColorSync32BitFloat@7$kColorSync32BitInteger@5$kColorSync32BitNamedColorIndex@6$kColorSync8BitInteger@2$kColorSyncAlphaFirst@4$kColorSyncAlphaInfoMask@31$kColorSyncAlphaLast@3$kColorSyncAlphaNone@0$kColorSyncAlphaNoneSkipFirst@6$kColorSyncAlphaNoneSkipLast@5$kColorSyncAlphaPremultipliedFirst@2$kColorSyncAlphaPremultipliedLast@1$kColorSyncByteOrder16Big@12288$kColorSyncByteOrder16Little@4096$kColorSyncByteOrder32Big@16384$kColorSyncByteOrder32Little@8192$kColorSyncByteOrderDefault@0$kColorSyncByteOrderMask@28672$"""
misc.update(
    {
        "COLORSYNC_PROFILE_INSTALL_ENTITLEMENT": b"com.apple.developer.ColorSync.profile.install"
    }
)
functions = {
    "ColorSyncProfileCopyDescriptionString": (
        b"^{__CFString=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMCopyLocalizedName": (
        b"^{__CFString=}^{ColorSyncCMM=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateLink": (
        b"^{ColorSyncProfile=}^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCreateCodeFragment": (
        b"@^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateDisplayTransferTablesFromVCGT": (
        b"^{__CFData=}^{ColorSyncProfile=}n^L",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"comment": "Unclear if this is correct"}},
        },
    ),
    "CGDisplayGetDisplayIDFromUUID": (b"I^{__CFUUID=}",),
    "ColorSyncProfileCreateDeviceProfile": (
        b"^{ColorSyncProfile=}^{__CFString=}^{__CFUUID=}@",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"comment": "CFTypeRef"}},
        },
    ),
    "ColorSyncProfileCopyHeader": (
        b"^{__CFData=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCopyTagSignatures": (
        b"^{__CFArray=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMGetTypeID": (b"Q",),
    "ColorSyncProfileCreateWithURL": (
        b"^{ColorSyncProfile=}^{__CFURL=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncProfileVerify": (
        b"B^{ColorSyncProfile=}^^{__CFError=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
                2: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "ColorSyncProfileIsMatrixBased": (b"B^{ColorSyncProfile=}",),
    "ColorSyncTransformConvert": (
        b"B^{ColorSyncTransform=}QQ^vIIQ^vIIQ^{__CFDictionary=}",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o", "c_array_of_variable_length": True},
                7: {"type_modifier": "n", "c_array_of_variable_length": True},
            }
        },
    ),
    "ColorSyncCMMCreate": (
        b"^{ColorSyncCMM=}^{__CFBundle=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncTransformGetProfileSequence": (b"^{__CFArray=}^{ColorSyncTransform=}",),
    "ColorSyncProfileCreateWithDisplayID": (
        b"^{ColorSyncProfile=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateMutableCopy": (
        b"^{ColorSyncProfile=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGDisplayCreateUUIDFromDisplayID": (
        b"^{__CFUUID=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileInstall": (
        b"B^{ColorSyncProfile=}^{__CFString=}^{__CFString=}^^{__CFError=}",
        "",
        {
            "arguments": {
                3: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileSetTag": (b"v^{ColorSyncProfile=}^{__CFString=}^{__CFData=}",),
    "ColorSyncTransformCreate": (
        b"^{ColorSyncTransform=}^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCopyTag": (
        b"^{__CFData=}^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncIterateDeviceProfiles": (
        b"v^?^v",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{__CFDictionary=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "ColorSyncProfileGetURL": (
        b"^{__CFURL=}^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncTransformSetProperty": (b"v^{ColorSyncTransform=}@@",),
    "ColorSyncProfileUninstall": (
        b"B^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncUnregisterDevice": (b"B^{__CFString=}^{__CFUUID=}",),
    "ColorSyncDeviceCopyDeviceInfo": (
        b"^{__CFDictionary=}^{__CFString=}^{__CFUUID=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateMutable": (
        b"^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncIterateInstalledProfiles": (
        b"v^?N^I^v^^{__CFError=}",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{__CFDictionary=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                },
                3: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "ColorSyncProfileIsPQBased": (b"B^{ColorSyncProfile=}",),
    "ColorSyncProfileCopyData": (
        b"^{__CFData=}^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncIterateInstalledCMMs": (
        b"v^?^v",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{ColorSyncCMM=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "ColorSyncDeviceSetCustomProfiles": (
        b"B^{__CFString=}^{__CFUUID=}^{__CFDictionary=}",
    ),
    "ColorSyncProfileIsHLGBased": (b"B^{ColorSyncProfile=}",),
    "ColorSyncCMMGetBundle": (b"^{__CFBundle=}^{ColorSyncCMM=}",),
    "ColorSyncIterateInstalledProfilesWithOptions": (
        b"v^?^I^v^{__CFDictionary=}^^{__CFError=}",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{__CFDictionary=}"},
                            1: {"type": b"^v"},
                        },
                    }
                },
                1: {"type_modifier": "N"},
                4: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "ColorSyncProfileGetTypeID": (b"Q",),
    "ColorSyncProfileCreateWithName": (
        b"^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncTransformGetTypeID": (b"Q",),
    "ColorSyncProfileGetDisplayTransferFormulaFromVCGT": (
        b"B^{ColorSyncProfile=}o^fo^fo^fo^fo^fo^fo^fo^fo^f",
    ),
    "ColorSyncProfileIsWideGamut": (b"B^{ColorSyncProfile=}",),
    "ColorSyncRegisterDevice": (b"B^{__CFString=}^{__CFUUID=}^{__CFDictionary=}",),
    "ColorSyncProfileEstimateGammaWithDisplayID": (
        b"fi^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileGetMD5": (b"{_ColorSyncMD5=[16C]}^{ColorSyncProfile=}",),
    "ColorSyncProfileRemoveTag": (b"v^{ColorSyncProfile=}^{__CFString=}",),
    "ColorSyncProfileContainsTag": (
        b"B^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileEstimateGamma": (
        b"f^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileCreate": (
        b"^{ColorSyncProfile=}^{__CFData=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncProfileSetHeader": (b"v^{ColorSyncProfile=}^{__CFData=}",),
    "ColorSyncTransformCopyProperty": (
        b"@^{ColorSyncTransform=}@^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMCopyCMMIdentifier": (
        b"^{__CFString=}^{ColorSyncCMM=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "CSEXTERN_DESKTOP": "CSEXTERN",
    "ColorSyncMutableProfileRef": "ColorSyncProfileRef",
    "CS_UNAVAILABLE_PUBLIC_EMBEDDED": "CS_UNAVAILABLE_EMBEDDED",
}
cftypes = [
    ("ColorSyncCMMRef", b"^{ColorSyncCMM=}", "ColorSyncCMMGetTypeID", None),
    ("ColorSyncProfileRef", b"^{ColorSyncProfile=}", "ColorSyncProfileGetTypeID", None),
    (
        "ColorSyncTransformRef",
        b"^{ColorSyncTransform=}",
        "ColorSyncTransformGetTypeID",
        None,
    ),
]
expressions = {}

# END OF FILE
