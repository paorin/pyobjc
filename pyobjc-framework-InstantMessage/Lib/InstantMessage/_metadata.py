# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:39:21 2021
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
constants = """$IMAVManagerStateChangedNotification$IMAVManagerURLToShareChangedNotification$IMCapabilityAudioConference$IMCapabilityDirectIM$IMCapabilityFileSharing$IMCapabilityFileTransfer$IMCapabilityText$IMCapabilityVideoConference$IMMyStatusChangedNotification$IMPersonAVBusyKey$IMPersonCapabilitiesKey$IMPersonEmailKey$IMPersonFirstNameKey$IMPersonIdleSinceKey$IMPersonInfoChangedNotification$IMPersonLastNameKey$IMPersonPictureDataKey$IMPersonScreenNameKey$IMPersonServiceNameKey$IMPersonStatusChangedNotification$IMPersonStatusKey$IMPersonStatusMessageKey$IMServiceStatusChangedNotification$IMStatusImagesChangedAppearanceNotification$"""
enums = """$IMAVInactive@0$IMAVPending@4$IMAVRequested@1$IMAVRunning@5$IMAVShuttingDown@2$IMAVStartingUp@3$IMPersonStatusAvailable@4$IMPersonStatusAway@3$IMPersonStatusIdle@2$IMPersonStatusNoStatus@5$IMPersonStatusOffline@1$IMPersonStatusUnknown@0$IMServiceStatusDisconnected@1$IMServiceStatusLoggedIn@4$IMServiceStatusLoggedOut@0$IMServiceStatusLoggingIn@3$IMServiceStatusLoggingOut@2$IMVideoOptimizationDefault@0$IMVideoOptimizationReplacement@2$IMVideoOptimizationStills@1$"""
misc.update({})
functions = {"IMComparePersonStatus": (b"qQQ",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"IMAVControl", b"isEnabled", {"retval": {"type": b"Z"}})
    r(b"IMAVControl", b"setAction:", {"arguments": {2: {"sel_of_type": b"v@:@"}}})
    r(b"IMAVControl", b"setEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"NSObject",
        b"getOpenGLBufferContext:pixelFormat:",
        {
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"^^{_CGLContextObject=}", "type_modifier": b"o"},
                3: {"type": b"^^{_CGLPixelFormatObject=}", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"getPixelBufferPixelFormat:",
        {
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"^I", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"renderIntoOpenGLBuffer:onScreen:forTime:",
        {
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": "^{__CVBuffer=}"},
                3: {"type": b"^i", "type_modifier": b"n"},
                4: {
                    "type": b"^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                    "type_modifier": b"n",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"renderIntoPixelBuffer:forTime:",
        {
            "retval": {"type": "Z"},
            "arguments": {
                2: {"type": "^{__CVBuffer=}"},
                3: {
                    "type": b"^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                    "type_modifier": b"n",
                },
            },
        },
    )
finally:
    objc._updatingMetadata(False)
protocols = {
    "IMVideoDataSource": objc.informal_protocol(
        "IMVideoDataSource",
        [
            objc.selector(
                None,
                b"renderIntoPixelBuffer:forTime:",
                b"Z@:^{__CVBuffer=}^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                isRequired=False,
            ),
            objc.selector(
                None, b"getPixelBufferPixelFormat:", b"v@:^I", isRequired=False
            ),
            objc.selector(
                None,
                b"getOpenGLBufferContext:pixelFormat:",
                b"v@:^^{_CGLContextObject=}^^{_CGLPixelFormatObject=}",
                isRequired=False,
            ),
            objc.selector(
                None,
                b"renderIntoOpenGLBuffer:onScreen:forTime:",
                b"Z@:^{__CVBuffer=}^i^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                isRequired=False,
            ),
        ],
    )
}
expressions = {}

# END OF FILE
