# This file is generated by objective.metadata
#
# Last update: Sat May 11 10:09:54 2024
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
constants = """$CHHapticAudioResourceKeyLoopEnabled$CHHapticAudioResourceKeyUseVolumeEnvelope$CHHapticDynamicParameterIDAudioAttackTimeControl$CHHapticDynamicParameterIDAudioBrightnessControl$CHHapticDynamicParameterIDAudioDecayTimeControl$CHHapticDynamicParameterIDAudioPanControl$CHHapticDynamicParameterIDAudioPitchControl$CHHapticDynamicParameterIDAudioReleaseTimeControl$CHHapticDynamicParameterIDAudioVolumeControl$CHHapticDynamicParameterIDHapticAttackTimeControl$CHHapticDynamicParameterIDHapticDecayTimeControl$CHHapticDynamicParameterIDHapticIntensityControl$CHHapticDynamicParameterIDHapticReleaseTimeControl$CHHapticDynamicParameterIDHapticSharpnessControl$CHHapticEventParameterIDAttackTime$CHHapticEventParameterIDAudioBrightness$CHHapticEventParameterIDAudioPan$CHHapticEventParameterIDAudioPitch$CHHapticEventParameterIDAudioVolume$CHHapticEventParameterIDDecayTime$CHHapticEventParameterIDHapticIntensity$CHHapticEventParameterIDHapticSharpness$CHHapticEventParameterIDReleaseTime$CHHapticEventParameterIDSustained$CHHapticEventTypeAudioContinuous$CHHapticEventTypeAudioCustom$CHHapticEventTypeHapticContinuous$CHHapticEventTypeHapticTransient$CHHapticPatternKeyEvent$CHHapticPatternKeyEventDuration$CHHapticPatternKeyEventParameters$CHHapticPatternKeyEventType$CHHapticPatternKeyEventWaveformLoopEnabled$CHHapticPatternKeyEventWaveformPath$CHHapticPatternKeyEventWaveformUseVolumeEnvelope$CHHapticPatternKeyParameter$CHHapticPatternKeyParameterCurve$CHHapticPatternKeyParameterCurveControlPoints$CHHapticPatternKeyParameterID$CHHapticPatternKeyParameterValue$CHHapticPatternKeyPattern$CHHapticPatternKeyTime$CHHapticPatternKeyVersion$"""
enums = """$CHHapticEngineFinishedActionLeaveEngineRunning@2$CHHapticEngineFinishedActionStopEngine@1$CHHapticEngineStoppedReasonApplicationSuspended@2$CHHapticEngineStoppedReasonAudioSessionInterrupt@1$CHHapticEngineStoppedReasonEngineDestroyed@5$CHHapticEngineStoppedReasonGameControllerDisconnect@6$CHHapticEngineStoppedReasonIdleTimeout@3$CHHapticEngineStoppedReasonNotifyWhenFinished@4$CHHapticEngineStoppedReasonSystemError@-1$CHHapticErrorCodeBadEventEntry@-4830$CHHapticErrorCodeBadParameterEntry@-4831$CHHapticErrorCodeEngineNotRunning@-4805$CHHapticErrorCodeEngineStartTimeout@-4808$CHHapticErrorCodeFileNotFound@-4851$CHHapticErrorCodeInsufficientPower@-4897$CHHapticErrorCodeInvalidAudioResource@-4824$CHHapticErrorCodeInvalidAudioSession@-4815$CHHapticErrorCodeInvalidEngineParameter@-4816$CHHapticErrorCodeInvalidEventDuration@-4823$CHHapticErrorCodeInvalidEventTime@-4822$CHHapticErrorCodeInvalidEventType@-4821$CHHapticErrorCodeInvalidParameterType@-4820$CHHapticErrorCodeInvalidPatternData@-4813$CHHapticErrorCodeInvalidPatternDictionary@-4814$CHHapticErrorCodeInvalidPatternPlayer@-4812$CHHapticErrorCodeInvalidTime@-4840$CHHapticErrorCodeMemoryError@-4899$CHHapticErrorCodeNotSupported@-4809$CHHapticErrorCodeOperationNotPermitted@-4806$CHHapticErrorCodeResourceNotAvailable@-4825$CHHapticErrorCodeServerInitFailed@-4810$CHHapticErrorCodeServerInterrupted@-4811$CHHapticErrorCodeUnknownError@-4898$CHHapticTimeImmediate@0.0$"""
misc.update(
    {
        "CHHapticEngineFinishedAction": NewType("CHHapticEngineFinishedAction", int),
        "CHHapticErrorCode": NewType("CHHapticErrorCode", int),
        "CHHapticEngineStoppedReason": NewType("CHHapticEngineStoppedReason", int),
    }
)
misc.update(
    {
        "CHHapticEventParameterID": NewType("CHHapticEventParameterID", str),
        "CHHapticEventType": NewType("CHHapticEventType", str),
        "CHHapticPatternKey": NewType("CHHapticPatternKey", str),
        "CHHapticDynamicParameterID": NewType("CHHapticDynamicParameterID", str),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"CHHapticEngine",
        b"createAdvancedPlayerWithPattern:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"createPlayerWithPattern:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"initAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"initWithAudioSession:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"CHHapticEngine", b"isAutoShutdownEnabled", {"retval": {"type": b"Z"}})
    r(b"CHHapticEngine", b"isMutedForAudio", {"retval": {"type": b"Z"}})
    r(b"CHHapticEngine", b"isMutedForHaptics", {"retval": {"type": b"Z"}})
    r(
        b"CHHapticEngine",
        b"notifyWhenPlayersFinished:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"q"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CHHapticEngine",
        b"playPatternFromData:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"playPatternFromURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"CHHapticEngine", b"playsAudioOnly", {"retval": {"type": b"Z"}})
    r(b"CHHapticEngine", b"playsHapticsOnly", {"retval": {"type": b"Z"}})
    r(
        b"CHHapticEngine",
        b"registerAudioResource:options:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"resetHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}},
                }
            }
        },
    )
    r(b"CHHapticEngine", b"setAutoShutdownEnabled:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CHHapticEngine", b"setIsMutedForAudio:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CHHapticEngine", b"setIsMutedForHaptics:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CHHapticEngine", b"setPlaysAudioOnly:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CHHapticEngine", b"setPlaysHapticsOnly:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"CHHapticEngine",
        b"setResetHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"CHHapticEngine",
        b"setStoppedHandler:",
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
    r(
        b"CHHapticEngine",
        b"startAndReturnError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticEngine",
        b"startWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CHHapticEngine",
        b"stopWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CHHapticEngine",
        b"stoppedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                }
            }
        },
    )
    r(
        b"CHHapticEngine",
        b"unregisterAudioResource:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticPattern",
        b"exportDictionaryAndReturnError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticPattern",
        b"initWithContentsOfURL:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticPattern",
        b"initWithDictionary:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticPattern",
        b"initWithEvents:parameterCurves:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"CHHapticPattern",
        b"initWithEvents:parameters:error:",
        {"arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"NSObject",
        b"attributesForDynamicParameter:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"attributesForEventParameter:eventType:error:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"cancelAndReturnError:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"completionHandler",
        {
            "required": True,
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                },
                "type": b"@?",
            },
        },
    )
    r(b"NSObject", b"defaultValue", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"isMuted", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"loopEnabled", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"loopEnd", {"required": True, "retval": {"type": b"d"}})
    r(b"NSObject", b"maxValue", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"minValue", {"required": True, "retval": {"type": b"f"}})
    r(
        b"NSObject",
        b"pauseAtTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(b"NSObject", b"playbackRate", {"required": True, "retval": {"type": b"f"}})
    r(
        b"NSObject",
        b"resumeAtTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"scheduleParameterCurve:atTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"d"},
                4: {"type": b"^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"seekToOffset:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"sendParameters:atTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"d"},
                4: {"type": b"^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"setCompletionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                }
            },
        },
    )
    r(
        b"NSObject",
        b"setIsMuted:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"setLoopEnabled:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"setLoopEnd:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"d"}}},
    )
    r(
        b"NSObject",
        b"setPlaybackRate:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"startAtTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(
        b"NSObject",
        b"stopAtTime:error:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"d"}, 3: {"type": b"^@", "type_modifier": b"o"}},
        },
    )
    r(b"NSObject", b"supportsAudio", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"supportsHaptics", {"required": True, "retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "CHHapticDynamicParameter", b"initWithParameterID:value:relativeTime:"
)
objc.registerNewKeywordsFromSelector("CHHapticEngine", b"initAndReturnError:")
objc.registerNewKeywordsFromSelector("CHHapticEngine", b"initWithAudioSession:error:")
objc.registerNewKeywordsFromSelector(
    "CHHapticEvent", b"initWithAudioResourceID:parameters:relativeTime:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticEvent", b"initWithAudioResourceID:parameters:relativeTime:duration:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticEvent", b"initWithEventType:parameters:relativeTime:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticEvent", b"initWithEventType:parameters:relativeTime:duration:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticEventParameter", b"initWithParameterID:value:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticParameterCurve", b"initWithParameterID:controlPoints:relativeTime:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticParameterCurveControlPoint", b"initWithRelativeTime:value:"
)
objc.registerNewKeywordsFromSelector("CHHapticPattern", b"initWithContentsOfURL:error:")
objc.registerNewKeywordsFromSelector("CHHapticPattern", b"initWithDictionary:error:")
objc.registerNewKeywordsFromSelector(
    "CHHapticPattern", b"initWithEvents:parameterCurves:error:"
)
objc.registerNewKeywordsFromSelector(
    "CHHapticPattern", b"initWithEvents:parameters:error:"
)
expressions = {"CHHapticTimeImmediate": "(NSTimeInterval)0.0f"}

# END OF FILE
