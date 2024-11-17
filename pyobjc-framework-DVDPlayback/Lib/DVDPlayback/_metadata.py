# This file is generated by objective.metadata
#
# Last update: Fri Nov 15 12:46:37 2024
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
constants = """$$"""
enums = """$kDVDAMGMDomain@5$kDVDAspectRatio16x9@3$kDVDAspectRatio4x3@1$kDVDAspectRatio4x3PanAndScan@2$kDVDAspectRatioLetterBox@4$kDVDAspectRatioUninitialized@0$kDVDAudioAC3Format@1$kDVDAudioDDPlusFormat@8$kDVDAudioDTSFormat@5$kDVDAudioDTSHDFormat@9$kDVDAudioExtensionCodeDirectorsComment1@3$kDVDAudioExtensionCodeDirectorsComment2@4$kDVDAudioExtensionCodeNVisualImpaired@2$kDVDAudioExtensionCodeNormalCaptions@1$kDVDAudioExtensionCodeNotSpecified@0$kDVDAudioMLPFormat@7$kDVDAudioMPEG1Format@2$kDVDAudioMPEG2Format@3$kDVDAudioModeProLogic@1$kDVDAudioModeSPDIF@2$kDVDAudioModeUninitialized@0$kDVDAudioPCMFormat@4$kDVDAudioSDDSFormat@6$kDVDAudioUnknownFormat@0$kDVDButtonIndexNone@-1$kDVDErrorAlreadyPlaying@-70006$kDVDErrorAuthentification@-70025$kDVDErrorDisplayAuthentification@-70034$kDVDErrorDontNeedWakeup@-70009$kDVDErrorGraphicsDevice@-70018$kDVDErrorInitializingLib@-70002$kDVDErrorInvalidBookmarkForMedia@-70032$kDVDErrorInvalidBookmarkSize@-70031$kDVDErrorInvalidBookmarkVersion@-70030$kDVDErrorInvalidRegionCode@-70020$kDVDErrorIsAlreadySleeping@-70008$kDVDErrorMismatchedRegionCode@-70022$kDVDErrorMissingDrive@-70012$kDVDErrorMissingGraphicsDevice@-70017$kDVDErrorNavigation@-70029$kDVDErrorNoAudioOutputDevice@-70027$kDVDErrorNoFatalErrCallBack@-70007$kDVDErrorNoMoreRegionSets@-70023$kDVDErrorNoValidBookmarkForLastPlay@-70033$kDVDErrorNoValidMedia@-70015$kDVDErrorNotAllowedDuringPlayback@-70004$kDVDErrorNotSupportedConfiguration@-70013$kDVDErrorNotSupportedFunction@-70014$kDVDErrorOutOfVideoMemory@-70026$kDVDErrorPlaybackOpen@-70019$kDVDErrorRgnMgrInstall@-70021$kDVDErrorSystem@-70028$kDVDErrorTimeOutOfRange@-70010$kDVDErrorUnassignedGrafPort@-70005$kDVDErrorUninitializedLib@-70003$kDVDErrorUnknown@-70001$kDVDErrorUserActionNoOp@-70011$kDVDErrorWrongParam@-70016$kDVDErrordRegionCodeUninitialized@-70024$kDVDEventAngle@4$kDVDEventAngleNumbers@23$kDVDEventAudioStream@5$kDVDEventAudioStreamNumbers@22$kDVDEventBitrate@9$kDVDEventCCInfo@25$kDVDEventChapterTime@26$kDVDEventDisplayMode@7$kDVDEventDomain@8$kDVDEventError@24$kDVDEventGPRM@18$kDVDEventMenuCalled@15$kDVDEventPGC@17$kDVDEventPTT@2$kDVDEventParental@16$kDVDEventPlayback@11$kDVDEventRegionMismatch@19$kDVDEventScanSpeed@14$kDVDEventStill@10$kDVDEventStreams@13$kDVDEventSubpictureStream@6$kDVDEventSubpictureStreamNumbers@21$kDVDEventTitle@1$kDVDEventTitleTime@20$kDVDEventValidUOP@3$kDVDEventVideoStandard@12$kDVDFPDomain@0$kDVDFormatNTSC@1$kDVDFormatNTSC_HDTV@3$kDVDFormatPAL@2$kDVDFormatPAL_HDTV@4$kDVDFormatUninitialized@0$kDVDLanguageCodeAbkhazian@1633820704$kDVDLanguageCodeAfar@1633755168$kDVDLanguageCodeAfrikaans@1634082848$kDVDLanguageCodeAlbanian@1936793632$kDVDLanguageCodeAmharic@1634541600$kDVDLanguageCodeArabic@1634869280$kDVDLanguageCodeArmenian@1752768544$kDVDLanguageCodeAssamese@1634934816$kDVDLanguageCodeAymara@1635328032$kDVDLanguageCodeAzerbaijani@1635393568$kDVDLanguageCodeBashkir@1650532384$kDVDLanguageCodeBasque@1702174752$kDVDLanguageCodeBengali@1651384352$kDVDLanguageCodeBhutani@1685725216$kDVDLanguageCodeBihari@1650991136$kDVDLanguageCodeBislama@1651056672$kDVDLanguageCodeBreton@1651646496$kDVDLanguageCodeBulgarian@1650925600$kDVDLanguageCodeBurmese@1836654624$kDVDLanguageCodeByelorussian@1650794528$kDVDLanguageCodeCambodian@1802313760$kDVDLanguageCodeCatalan@1667309600$kDVDLanguageCodeChinese@2053644320$kDVDLanguageCodeCorsican@1668227104$kDVDLanguageCodeCroatian@1752309792$kDVDLanguageCodeCzech@1668489248$kDVDLanguageCodeDanish@1684086816$kDVDLanguageCodeDutch@1852579872$kDVDLanguageCodeEnglish@1701716000$kDVDLanguageCodeEsperanto@1701781536$kDVDLanguageCodeEstonian@1702109216$kDVDLanguageCodeFaeroese@1718558752$kDVDLanguageCodeFiji@1718231072$kDVDLanguageCodeFinnish@1718165536$kDVDLanguageCodeFrench@1718755360$kDVDLanguageCodeFrisian@1719214112$kDVDLanguageCodeGalician@1735139360$kDVDLanguageCodeGeorgian@1801527328$kDVDLanguageCodeGerman@1684348960$kDVDLanguageCodeGreek@1701584928$kDVDLanguageCodeGreenlandic@1802248224$kDVDLanguageCodeGuarani@1735270432$kDVDLanguageCodeGujarati@1735729184$kDVDLanguageCodeHausa@1751195680$kDVDLanguageCodeHebrew@1769414688$kDVDLanguageCodeHindi@1751719968$kDVDLanguageCodeHungarian@1752506400$kDVDLanguageCodeIcelandic@1769152544$kDVDLanguageCodeIndonesian@1768824864$kDVDLanguageCodeInterlingua@1767972896$kDVDLanguageCodeInterlingue@1768235040$kDVDLanguageCodeInupiak@1768628256$kDVDLanguageCodeIrish@1734418464$kDVDLanguageCodeItalian@1769218080$kDVDLanguageCodeJapanese@1784750112$kDVDLanguageCodeJavanese@1786191904$kDVDLanguageCodeKannada@1802379296$kDVDLanguageCodeKashmiri@1802706976$kDVDLanguageCodeKazakh@1802182688$kDVDLanguageCodeKinyarwanda@1920409632$kDVDLanguageCodeKirghiz@1803100192$kDVDLanguageCodeKirundi@1919819808$kDVDLanguageCodeKorean@1802444832$kDVDLanguageCodeKurdish@1802838048$kDVDLanguageCodeLaothian@1819222048$kDVDLanguageCodeLatin@1818304544$kDVDLanguageCodeLatvian@1819680800$kDVDLanguageCodeLingala@1819156512$kDVDLanguageCodeLithuanian@1819549728$kDVDLanguageCodeMacedonian@1835737120$kDVDLanguageCodeMalagasy@1835474976$kDVDLanguageCodeMalay@1836261408$kDVDLanguageCodeMalayalam@1835802656$kDVDLanguageCodeMaltese@1836326944$kDVDLanguageCodeMaori@1835606048$kDVDLanguageCodeMarathi@1836195872$kDVDLanguageCodeMoldavian@1835999264$kDVDLanguageCodeMongolian@1835933728$kDVDLanguageCodeNauru@1851858976$kDVDLanguageCodeNepali@1852121120$kDVDLanguageCodeNone@808460320$kDVDLanguageCodeNorwegian@1852776480$kDVDLanguageCodeOccitan@1868767264$kDVDLanguageCodeOriya@1869750304$kDVDLanguageCodeOromo@1869422624$kDVDLanguageCodePashto@1886593056$kDVDLanguageCodePersian@1717641248$kDVDLanguageCodePolish@1886134304$kDVDLanguageCodePortugese@1886658592$kDVDLanguageCodePunjabi@1885413408$kDVDLanguageCodeQuechua@1903501344$kDVDLanguageCodeRhaetoRomance@1919754272$kDVDLanguageCodeRomanian@1919885344$kDVDLanguageCodeRussian@1920278560$kDVDLanguageCodeSamoan@1936531488$kDVDLanguageCodeSangro@1936138272$kDVDLanguageCodeSanskrit@1935745056$kDVDLanguageCodeScotsGaelic@1734615072$kDVDLanguageCodeSerbian@1936859168$kDVDLanguageCodeSerboCroatian@1936203808$kDVDLanguageCodeSesotho@1936990240$kDVDLanguageCodeSetswana@1953374240$kDVDLanguageCodeShona@1936597024$kDVDLanguageCodeSindhi@1935941664$kDVDLanguageCodeSinghalese@1936269344$kDVDLanguageCodeSiswati@1936924704$kDVDLanguageCodeSlovak@1936400416$kDVDLanguageCodeSlovenian@1936465952$kDVDLanguageCodeSomali@1936662560$kDVDLanguageCodeSpanish@1702043680$kDVDLanguageCodeSudanese@1937055776$kDVDLanguageCodeSwahili@1937186848$kDVDLanguageCodeSwedish@1937121312$kDVDLanguageCodeTagalog@1953243168$kDVDLanguageCodeTajik@1952915488$kDVDLanguageCodeTamil@1952522272$kDVDLanguageCodeTatar@1953767456$kDVDLanguageCodeTelugu@1952784416$kDVDLanguageCodeThai@1952981024$kDVDLanguageCodeTibetan@1651449888$kDVDLanguageCodeTigrinya@1953046560$kDVDLanguageCodeTonga@1953439776$kDVDLanguageCodeTsonga@1953701920$kDVDLanguageCodeTurkish@1953636384$kDVDLanguageCodeTurkmen@1953177632$kDVDLanguageCodeTwi@1953964064$kDVDLanguageCodeUkranian@1969954848$kDVDLanguageCodeUninitialized@1061101600$kDVDLanguageCodeUrdu@1970413600$kDVDLanguageCodeUzbek@1970937888$kDVDLanguageCodeVietnamese@1986600992$kDVDLanguageCodeVolapuk@1986994208$kDVDLanguageCodeWelsh@1668882464$kDVDLanguageCodeWolof@2003771424$kDVDLanguageCodeXhosa@2020089888$kDVDLanguageCodeYiddish@1785274400$kDVDLanguageCodeYoruba@2037325856$kDVDLanguageCodeZulu@2054496288$kDVDLanguageNoPreference@707403808$kDVDMenuAngle@4$kDVDMenuAudio@3$kDVDMenuNone@6$kDVDMenuPTT@5$kDVDMenuRoot@1$kDVDMenuSubPicture@2$kDVDMenuTitle@0$kDVDRegionCode1@254$kDVDRegionCode2@253$kDVDRegionCode3@251$kDVDRegionCode4@247$kDVDRegionCode5@239$kDVDRegionCode6@223$kDVDRegionCode7@191$kDVDRegionCode8@127$kDVDRegionCodeUninitialized@255$kDVDSTOPDomain@4$kDVDScanDirectionBackward@1$kDVDScanDirectionForward@0$kDVDScanRate16x@16$kDVDScanRate1x@1$kDVDScanRate2x@2$kDVDScanRate32x@32$kDVDScanRate4x@4$kDVDScanRate8x@8$kDVDScanRateOneEigth@-8$kDVDScanRateOneFourth@-4$kDVDScanRateOneHalf@-2$kDVDStateIdle@6$kDVDStatePaused@3$kDVDStatePlaying@1$kDVDStatePlayingSlow@7$kDVDStatePlayingStill@2$kDVDStateScanning@5$kDVDStateStopped@4$kDVDStateUnknown@0$kDVDSubpictureExtensionCodeCaption4Children@3$kDVDSubpictureExtensionCodeCaptionBiggerSize@2$kDVDSubpictureExtensionCodeCaptionNormalSize@1$kDVDSubpictureExtensionCodeClosedCaption4Children@7$kDVDSubpictureExtensionCodeClosedCaptionBiggerSize@6$kDVDSubpictureExtensionCodeClosedCaptionNormalSize@5$kDVDSubpictureExtensionCodeForcedCaption@9$kDVDSubpictureExtensionCodeNotSpecified@0$kDVDSubpictureExtensionDirectorsComment4Children@15$kDVDSubpictureExtensionDirectorsCommentBiggerSize@14$kDVDSubpictureExtensionDirectorsCommentNormalSize@13$kDVDTTDomain@3$kDVDTTGRDomain@6$kDVDTimeCodeChapterDurationSeconds@6$kDVDTimeCodeChapterElapsedSeconds@4$kDVDTimeCodeChapterRemainingSeconds@5$kDVDTimeCodeElapsedSeconds@1$kDVDTimeCodeRemainingSeconds@2$kDVDTimeCodeTitleDurationSeconds@3$kDVDTimeCodeUninitialized@0$kDVDUOPAngleChange@4194304$kDVDUOPAudioStreamChange@1048576$kDVDUOPBackwardScan@512$kDVDUOPButton@131072$kDVDUOPForwardScan@256$kDVDUOPGoUp@16$kDVDUOPKaraokeModeChange@8388608$kDVDUOPMenuCallAngle@16384$kDVDUOPMenuCallAudio@8192$kDVDUOPMenuCallPTT@32768$kDVDUOPMenuCallRoot@2048$kDVDUOPMenuCallSubPicture@4096$kDVDUOPMenuCallTitle@1024$kDVDUOPNextPGSearch@128$kDVDUOPPTTPlaySearch@2$kDVDUOPPauseOff@67108864$kDVDUOPPauseOn@524288$kDVDUOPPrevTopPGSearch@64$kDVDUOPResume@65536$kDVDUOPScanOff@33554432$kDVDUOPStillOff@262144$kDVDUOPStop@8$kDVDUOPSubPictureStreamChange@2097152$kDVDUOPTimePTTSearch@32$kDVDUOPTimePlaySearch@1$kDVDUOPTitlePlay@4$kDVDUOPVideoModeChange@16777216$kDVDUserNavigationEnter@5$kDVDUserNavigationMoveDown@2$kDVDUserNavigationMoveLeft@3$kDVDUserNavigationMoveRight@4$kDVDUserNavigationMoveUp@1$kDVDVMGMDomain@1$kDVDVTSMDomain@2$"""
misc.update(
    {
        "DVDScanRate": NewType("DVDScanRate", int),
        "DVDEventCode": NewType("DVDEventCode", int),
        "DVDUserNavigation": NewType("DVDUserNavigation", int),
        "DVDFormat": NewType("DVDFormat", int),
        "DVDDomainCode": NewType("DVDDomainCode", int),
        "DVDScanDirection": NewType("DVDScanDirection", int),
        "DVDAspectRatio": NewType("DVDAspectRatio", int),
        "DVDAudioFormat": NewType("DVDAudioFormat", int),
        "DVDState": NewType("DVDState", int),
        "DVDMenu": NewType("DVDMenu", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "DVDIsDisplayingSubPicture": (
        b"i^Z",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDGoToMenu": (b"iI",),
    "DVDSetDefaultSubPictureLanguageCode": (b"iII",),
    "DVDDoUserNavigation": (b"iI",),
    "DVDOpenMediaVolume": (
        b"i^{FSRef=[80C]}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "DVDDoButtonActivate": (b"ii",),
    "DVDGetTimeEventRate": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetDiscRegionCode": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSetChapter": (b"iS",),
    "DVDSetVideoDisplay": (b"iI",),
    "DVDSetFatalErrorCallBack": (
        b"i^?^v",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"i"}, 1: {"type": b"^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "DVDOpenMediaFileWithURL": (b"i^{__CFURL=}",),
    "DVDGetNumAngles": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSleep": (b"i",),
    "DVDStepFrame": (b"ic",),
    "DVDIsOnMenu": (
        b"i^Z^I",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDOpenMediaFile": (
        b"i^{FSRef=[80C]}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "DVDHasPreviousChapter": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetTitle": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetAngle": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetAudioOutputModeCapabilities": (
        b"i^i",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDUpdateVideo": (b"i", "", {"variadic": False}),
    "DVDIsSupportedDisplay": (b"iI^Z", "", {"arguments": {1: {"type_modifier": "o"}}}),
    "DVDGetButtonPosition": (
        b"iI^{CGRect={CGPoint=dd}{CGSize=dd}}^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "DVDGetVideoWindowID": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDIsPlaying": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSetVideoWindowRef": (b"i^{OpaqueWindowPtr=}",),
    "DVDGetAudioLanguageCodeByStream": (
        b"iS^I^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "DVDScan": (b"isc",),
    "DVDGetVideoDisplay": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetDriveRegionCode": (
        b"i^I^s",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDSetTitle": (b"iS",),
    "DVDIsMuted": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDHasMenu": (b"iI^Z", "", {"arguments": {1: {"type_modifier": "o"}}}),
    "DVDSetTimeEventRate": (b"iI",),
    "DVDGetNumTitles": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetAspectRatio": (b"i^s", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetAudioOutputMode": (b"i^i", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGotoBookmark": (
        b"i^vI",
        "",
        {"arguments": {0: {"c_array_length_in_arg": 1, "type_modifier": "n"}}},
    ),
    "DVDGetNativeVideoSize": (
        b"i^S^S",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDDispose": (b"i", "", {"variadic": False}),
    "DVDGetChapter": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetState": (b"i^i", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetVideoWindowRef": (
        b"i^^{OpaqueWindowPtr=}",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDOpenMediaVolumeWithURL": (b"i^{__CFURL=}",),
    "DVDMute": (b"iZ",),
    "DVDGetSPDIFDataOutDevice": (
        b"i^I",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDGetVideoCGBounds": (
        b"i^{CGRect={CGPoint=dd}{CGSize=dd}}",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDGetSPDIFDataOutDeviceCount": (
        b"i^I",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDGetLastPlayBookmark": (
        b"i^v^I",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": 1, "type_modifier": "o"},
                1: {"type_modifier": "N"},
            }
        },
    ),
    "DVDSwitchToDisplay": (b"iI^Z", "", {"arguments": {1: {"type_modifier": "o"}}}),
    "DVDIsPaused": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDIsRegisteredEventCallBack": (
        b"Z^v",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDClearLastPlayBookmark": (b"i", "", {"variadic": False}),
    "DVDSetAngle": (b"iS",),
    "DVDGetSubPictureLanguageCodeByStream": (
        b"iS^I^I",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "DVDGetSPDIFDataOutDeviceCFName": (
        b"iI^^{__CFString=}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "DVDEnableWebAccess": (b"iZ",),
    "DVDSetLastPlayBookmark": (
        b"i^vI",
        "",
        {"arguments": {0: {"c_array_length_in_arg": 1, "type_modifier": "n"}}},
    ),
    "DVDGetSubPictureLanguageCode": (
        b"i^I^I",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDSetSubPictureStream": (b"iS",),
    "DVDPreviousChapter": (b"i", "", {"variadic": False}),
    "DVDIdle": (b"i", "", {"variadic": False}),
    "DVDDoMenuCGClick": (
        b"i^{CGPoint=dd}^i",
        "",
        {"arguments": {0: {"type_modifier": "n"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDGetMediaUniqueID": (b"i[8C]",),
    "DVDGetAudioStream": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGetAudioLanguageCode": (
        b"i^I^I",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDSetTime": (b"isIS",),
    "DVDReturnToTitle": (b"i", "", {"variadic": False}),
    "DVDGetFormatStandard": (b"i^s", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDInitialize": (b"i", "", {"variadic": False}),
    "DVDUnregisterEventCallBack": (b"i^v",),
    "DVDSetAspectRatio": (b"is",),
    "DVDPlay": (b"i", "", {"variadic": False}),
    "DVDResume": (b"i", "", {"variadic": False}),
    "DVDHasMedia": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSetDefaultMenuLanguageCode": (b"iI",),
    "DVDIsValidMediaRef": (
        b"i^{FSRef=[80C]}^Z",
        "",
        {"arguments": {0: {"type_modifier": "n"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDDisplaySubPicture": (b"iZ",),
    "DVDGetScanRate": (
        b"i^s^z",
        "",
        {"arguments": {0: {"type_modifier": "o"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDRegisterEventCallBack": (
        b"i^?^II^v^I",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"I"},
                            1: {"type": b"L"},
                            2: {"type": b"L"},
                            3: {"type": b"^v"},
                        },
                    },
                    "callable_retained": True,
                },
                1: {"type_modifier": "n"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "DVDSetAudioOutputMode": (b"ii",),
    "DVDSetDriveRegionCode": (b"iI^{AuthorizationOpaqueRef=}",),
    "DVDIsValidMediaURL": (
        b"i^{__CFURL=}^Z",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "DVDGetAudioVolume": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSetDefaultAudioLanguageCode": (b"iII",),
    "DVDSetAudioStream": (b"iS",),
    "DVDGetGPRMValue": (b"iI^I", "", {"arguments": {1: {"type_modifier": "o"}}}),
    "DVDGetNumAudioStreams": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDCloseMediaFile": (b"i", "", {"variadic": False}),
    "DVDCloseMediaVolume": (b"i", "", {"variadic": False}),
    "DVDWakeUp": (b"i",),
    "DVDGetAudioStreamFormatByStream": (
        b"iI^s^I^I^I",
        "",
        {
            "arguments": {
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "DVDSetVideoCGBounds": (
        b"i^{CGRect={CGPoint=dd}{CGSize=dd}}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "DVDPause": (b"i", "", {"variadic": False}),
    "DVDGetAudioStreamFormat": (
        b"i^s^I^I^I",
        "",
        {
            "arguments": {
                0: {"type_modifier": "o"},
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
            }
        },
    ),
    "DVDGetBookmark": (
        b"i^v^I",
        "",
        {
            "arguments": {
                0: {"c_array_length_in_arg": 1, "type_modifier": "o"},
                1: {"type_modifier": "N"},
            }
        },
    ),
    "DVDGetNumSubPictureStreams": (
        b"i^S",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDGetButtoninfo": (
        b"i^I^I^I^I^I",
        "",
        {
            "arguments": {
                0: {"type_modifier": "o"},
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "DVDGetMenuLanguageCode": (b"i^I", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDSetSPDIFDataOutDevice": (b"iI",),
    "DVDSetVideoWindowID": (b"iI",),
    "DVDDoMenuCGMouseOver": (
        b"i^{CGPoint=dd}^i",
        "",
        {"arguments": {0: {"type_modifier": "n"}, 1: {"type_modifier": "o"}}},
    ),
    "DVDNextChapter": (b"i", "", {"variadic": False}),
    "DVDGetTime": (
        b"is^I^S",
        "",
        {"arguments": {1: {"type_modifier": "o"}, 2: {"type_modifier": "o"}}},
    ),
    "DVDGetAudioVolumeInfo": (
        b"i^S^S^S",
        "",
        {
            "arguments": {
                0: {"type_modifier": "o"},
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
            }
        },
    ),
    "DVDGetMediaVolumeCFName": (
        b"i^^{__CFString=}",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "DVDHasNextChapter": (b"i^Z", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDGoBackOneLevel": (b"i", "", {"variadic": False}),
    "DVDGetSubPictureStream": (b"i^S", "", {"arguments": {0: {"type_modifier": "o"}}}),
    "DVDStop": (b"i", "", {"variadic": False}),
    "DVDSetAudioVolume": (b"iS",),
    "DVDGetNumChapters": (b"iS^S", "", {"arguments": {1: {"type_modifier": "o"}}}),
}
aliases = {"DVD_NONNULL": "__nonnull", "DVD_NULLABLE": "__nullable"}
expressions = {}

# END OF FILE
