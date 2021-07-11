# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:18:56 2021
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
enums = """$AVCaptureViewControlsStyleDefault@0$AVCaptureViewControlsStyleFloating@1$AVCaptureViewControlsStyleInline@0$AVCaptureViewControlsStyleInlineDeviceSelection@2$AVPlayerViewControlsStyleDefault@1$AVPlayerViewControlsStyleFloating@2$AVPlayerViewControlsStyleInline@1$AVPlayerViewControlsStyleMinimal@3$AVPlayerViewControlsStyleNone@0$AVPlayerViewTrimCancelButton@1$AVPlayerViewTrimOKButton@0$AVRoutePickerViewButtonStateActive@2$AVRoutePickerViewButtonStateActiveHighlighted@3$AVRoutePickerViewButtonStateNormal@0$AVRoutePickerViewButtonStateNormalHighlighted@1$"""
misc.update({})
aliases = {
    "AVKIT_ONLY_EXTERN": "AVKIT_EXTERN",
    "AVPlayerViewControlsStyleDefault": "AVPlayerViewControlsStyleInline",
    "AVCaptureViewControlsStyleDefault": "AVCaptureViewControlsStyleInline",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AVCaptureView",
        b"setSession:showVideoPreview:showAudioPreview:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type": b"Z"}}},
    )
    r(
        b"AVPictureInPictureController",
        b"canStartPictureInPictureAutomaticallyFromInline",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"canStopPictureInPicture",
        {"retval": {"type": "Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"isPictureInPictureActive",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"isPictureInPicturePossible",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"isPictureInPictureSupported",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"isPictureInPictureSuspended",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"requiresLinearPlayback",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"AVPictureInPictureController",
        b"setCanStartPictureInPictureAutomaticallyFromInline:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AVPictureInPictureController",
        b"setRequiresLinearPlayback:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"AVPlayerView", b"allowsPictureInPicturePlayback", {"retval": {"type": b"Z"}})
    r(
        b"AVPlayerView",
        b"beginTrimmingWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    }
                }
            }
        },
    )
    r(b"AVPlayerView", b"canBeginTrimming", {"retval": {"type": b"Z"}})
    r(b"AVPlayerView", b"isReadyForDisplay", {"retval": {"type": b"Z"}})
    r(
        b"AVPlayerView",
        b"setAllowsPictureInPicturePlayback:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AVPlayerView",
        b"setShowsFrameSteppingButtons:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AVPlayerView",
        b"setShowsFullScreenToggleButton:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AVPlayerView",
        b"setShowsSharingServiceButton:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"AVPlayerView", b"setShowsTimecodes:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"AVPlayerView",
        b"setUpdatesNowPlayingInfoCenter:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"AVPlayerView", b"showsFrameSteppingButtons", {"retval": {"type": b"Z"}})
    r(b"AVPlayerView", b"showsFullScreenToggleButton", {"retval": {"type": b"Z"}})
    r(b"AVPlayerView", b"showsSharingServiceButton", {"retval": {"type": b"Z"}})
    r(b"AVPlayerView", b"showsTimecodes", {"retval": {"type": b"Z"}})
    r(b"AVPlayerView", b"updatesNowPlayingInfoCenter", {"retval": {"type": "Z"}})
    r(b"AVRoutePickerView", b"isRoutePickerButtonBordered", {"retval": {"type": "Z"}})
    r(
        b"AVRoutePickerView",
        b"setRoutePickerButtonBordered:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"NSObject",
        b"captureView:startRecordingToFileOutput:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureController:didTransitionToRenderSize:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"{_CMVideoDimensions=ii}"}},
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureController:failedToStartPictureInPictureWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureController:setPlaying:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"Z"}},
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureController:skipByInterval:completionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"{_CMTime=qiIq}"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerDidStartPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerDidStopPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerIsPlaybackPaused:",
        {"required": True, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerTimeRangeForPlayback:",
        {
            "required": True,
            "retval": {"type": b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}"},
            "arguments": {2: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerWillStartPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"pictureInPictureControllerWillStopPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerView:failedToStartPictureInPictureWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"playerView:restoreUserInterfaceForFullScreenExitWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"playerViewDidEnterFullScreen:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewDidExitFullScreen:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewDidStartPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewDidStopPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewShouldAutomaticallyDismissAtPictureInPictureStart:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewWillEnterFullScreen:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewWillExitFullScreen:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewWillStartPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"playerViewWillStopPictureInPicture:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"routePickerViewDidEndPresentingRoutes:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"routePickerViewWillBeginPresentingRoutes:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
