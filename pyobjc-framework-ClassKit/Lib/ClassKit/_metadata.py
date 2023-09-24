# This file is generated by objective.metadata
#
# Last update: Sat Jul  1 13:57:08 2023
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
constants = """$CLSContextTopicArtsAndMusic$CLSContextTopicComputerScienceAndEngineering$CLSContextTopicHealthAndFitness$CLSContextTopicLiteracyAndWriting$CLSContextTopicMath$CLSContextTopicScience$CLSContextTopicSocialScience$CLSContextTopicWorldLanguage$CLSErrorCodeDomain$CLSErrorObjectKey$CLSErrorSuccessfulObjectsKey$CLSErrorUnderlyingErrorsKey$CLSPredicateKeyPathDateCreated$CLSPredicateKeyPathIdentifier$CLSPredicateKeyPathParent$CLSPredicateKeyPathTitle$CLSPredicateKeyPathTopic$CLSPredicateKeyPathUniversalLinkURL$"""
enums = """$CLSBinaryValueTypeCorrectIncorrect@3$CLSBinaryValueTypePassFail@1$CLSBinaryValueTypeTrueFalse@0$CLSBinaryValueTypeYesNo@2$CLSContextTypeApp@1$CLSContextTypeAudio@14$CLSContextTypeBook@11$CLSContextTypeChallenge@7$CLSContextTypeChapter@2$CLSContextTypeCourse@16$CLSContextTypeCustom@17$CLSContextTypeDocument@13$CLSContextTypeExercise@9$CLSContextTypeGame@12$CLSContextTypeLesson@10$CLSContextTypeLevel@4$CLSContextTypeNone@0$CLSContextTypePage@5$CLSContextTypeQuiz@8$CLSContextTypeSection@3$CLSContextTypeTask@6$CLSContextTypeVideo@15$CLSErrorCodeAuthorizationDenied@4$CLSErrorCodeClassKitUnavailable@1$CLSErrorCodeDatabaseInaccessible@5$CLSErrorCodeInvalidAccountCredentials@10$CLSErrorCodeInvalidArgument@2$CLSErrorCodeInvalidCreate@7$CLSErrorCodeInvalidModification@3$CLSErrorCodeInvalidUpdate@8$CLSErrorCodeLimits@6$CLSErrorCodeNone@0$CLSErrorCodePartialFailure@9$CLSProgressReportingCapabilityKindBinary@2$CLSProgressReportingCapabilityKindDuration@0$CLSProgressReportingCapabilityKindPercent@1$CLSProgressReportingCapabilityKindQuantity@3$CLSProgressReportingCapabilityKindScore@4$"""
misc.update(
    {
        "CLSBinaryValueType": NewType("CLSBinaryValueType", int),
        "CLSErrorCode": NewType("CLSErrorCode", int),
        "CLSContextType": NewType("CLSContextType", int),
        "CLSProgressReportingCapabilityKind": NewType(
            "CLSProgressReportingCapabilityKind", int
        ),
    }
)
misc.update({"CLSContextTopic": NewType("CLSContextTopic", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"CLSActivity",
        b"contextsMatchingPredicate:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"CLSActivity", b"isStarted", {"retval": {"type": b"Z"}})
    r(b"CLSBinaryItem", b"setValue:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CLSBinaryItem", b"value", {"retval": {"type": b"Z"}})
    r(
        b"CLSContext",
        b"descendantMatchingIdentifierPath:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"CLSContext", b"isActive", {"retval": {"type": b"Z"}})
    r(b"CLSContext", b"isAssignable", {"retval": {"type": b"Z"}})
    r(b"CLSContext", b"setAssignable:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"CLSDataStore",
        b"contextsMatchingIdentifierPath:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLSDataStore",
        b"contextsMatchingPredicate:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLSDataStore",
        b"fetchActivityForURL:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CLSDataStore",
        b"saveWithCompletion:",
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
        b"NSObject",
        b"createContextForIdentifier:parentContext:parentIdentifierPath:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"updateDescendantsOfContext:completion:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(b"NSUserActivity", b"isClassKitDeepLink", {"retval": {"type": b"Z"}})
    r(
        b"null",
        b"contextsMatchingIdentifierPath:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"contextsMatchingPredicate:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"fetchActivityForURL:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"null", b"isStarted", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
