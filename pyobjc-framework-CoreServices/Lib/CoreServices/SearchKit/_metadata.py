# This file is generated by objective.metadata
#
# Last update: Sat Jul  1 13:58:51 2023
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
constants = """$kSKEndTermChars$kSKLanguageTypes$kSKMaximumTerms$kSKMinTermLength$kSKProximityIndexing$kSKStartTermChars$kSKStopWords$kSKSubstitutions$kSKTermChars$"""
enums = """$kSKDocumentStateAddPending@2$kSKDocumentStateDeletePending@3$kSKDocumentStateIndexed@1$kSKDocumentStateNotIndexed@0$kSKIndexInverted@1$kSKIndexInvertedVector@3$kSKIndexUnknown@0$kSKIndexVector@2$kSKSearchBooleanRanked@1$kSKSearchOptionDefault@0$kSKSearchOptionFindSimilar@4$kSKSearchOptionNoRelevanceScores@1$kSKSearchOptionSpaceMeansOR@2$kSKSearchPrefixRanked@3$kSKSearchRanked@0$kSKSearchRequiredRanked@2$"""
misc.update(
    {
        "SKDocumentIndexState": NewType("SKDocumentIndexState", int),
        "SKIndexType": NewType("SKIndexType", int),
        "SKSearchType": NewType("SKSearchType", int),
        "enum (unnamed at /Users/ronald/Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/SearchKit.framework/Headers/SKSearch.h:91:1)": NewType(
            "enum (unnamed at /Users/ronald/Applications/Xcode-beta.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.0.sdk/System/Library/Frameworks/CoreServices.framework/Frameworks/SearchKit.framework/Headers/SKSearch.h:91:1)",
            int,
        ),
    }
)
misc.update({})
misc.update({})
functions = {
    "SKIndexGetMaximumTermID": (b"q^{__SKIndex=}",),
    "SKDocumentGetName": (b"^{__CFString=}@",),
    "SKIndexRemoveDocument": (b"Z^{__SKIndex=}@",),
    "SKIndexCopyTermIDArrayForDocumentID": (
        b"^{__CFArray=}^{__SKIndex=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchGetTypeID": (b"Q",),
    "SKIndexDocumentIteratorCreate": (
        b"^{__SKIndexDocumentIterator=}^{__SKIndex=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentGetTypeID": (b"Q",),
    "SKSummaryGetParagraphSummaryInfo": (
        b"q^{__SKSummary=}q^q^q",
        "",
        {"arguments": {2: {"type_modifier": "o"}, 3: {"type_modifier": "o"}}},
    ),
    "SKSummaryGetParagraphCount": (b"q^{__SKSummary=}",),
    "SKIndexGetMaximumDocumentID": (b"q^{__SKIndex=}",),
    "SKSearchGroupCreate": (
        b"^{__SKSearchGroup=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexFlush": (b"Z^{__SKIndex=}",),
    "SKIndexCreateWithURL": (
        b"^{__SKIndex=}^{__CFURL=}^{__CFString=}I^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSummaryGetSentenceCount": (b"q^{__SKSummary=}",),
    "SKIndexGetMaximumBytesBeforeFlush": (b"q^{__SKIndex=}",),
    "SKIndexCopyDocumentIDArrayForTermID": (
        b"^{__CFArray=}^{__SKIndex=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchResultsCreateWithDocuments": (
        b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFArray=}q^v^?",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^{__SKIndex=}"},
                            1: {"type": b"@"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "SKSummaryCopyParagraphAtIndex": (
        b"^{__CFString=}^{__SKSummary=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentID": (b"q^{__SKIndex=}@",),
    "SKIndexOpenWithURL": (b"^{__SKIndex=}^{__CFURL=}^{__CFString=}Z",),
    "SKIndexCreateWithMutableData": (
        b"^{__SKIndex=}^{__CFData=}^{__CFString=}I^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyDocumentURLsForDocumentIDs": (
        b"v^{__SKIndex=}q^q^^{__CFURL=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {
                    "already_cfretained": True,
                    "c_array_length_in_arg": 1,
                    "type_modifier": "o",
                },
            },
        },
    ),
    "SKSearchResultsCreateWithQuery": (
        b"^{__SKSearchResults=}^{__SKSearchGroup=}^{__CFString=}Iq^v^?",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^{__SKIndex=}"},
                            1: {"type": b"@"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "SKIndexCompact": (b"Z^{__SKIndex=}",),
    "SKSearchGroupGetTypeID": (b"Q",),
    "SKSummaryCopySentenceAtIndex": (
        b"^{__CFString=}^{__SKSummary=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKSearchGroupCopyIndexes": (
        b"^{__CFArray=}^{__SKSearchGroup=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKLoadDefaultExtractorPlugIns": (b"v",),
    "SKIndexMoveDocument": (b"Z^{__SKIndex=}@@",),
    "SKIndexOpenWithData": (b"^{__SKIndex=}^{__CFData=}^{__CFString=}",),
    "SKIndexCopyDocumentProperties": (
        b"^{__CFDictionary=}^{__SKIndex=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyDocumentRefsForDocumentIDs": (
        b"v^{__SKIndex=}q^q^@",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {"c_array_length_in_arg": 1, "type_modifier": "o"},
            },
        },
    ),
    "SKIndexOpenWithMutableData": (b"^{__SKIndex=}^{__CFData=}^{__CFString=}",),
    "SKSearchResultsCopyMatchingTerms": (
        b"^{__CFArray=}^{__SKSearchResults=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentGetParent": (b"@@",),
    "SKSearchResultsGetTypeID": (b"Q",),
    "SKSummaryCreateWithString": (
        b"^{__SKSummary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentTermCount": (b"q^{__SKIndex=}q",),
    "SKIndexSetDocumentProperties": (b"v^{__SKIndex=}@^{__CFDictionary=}",),
    "SKSummaryGetSentenceSummaryInfo": (
        b"q^{__SKSummary=}q^q^q^q",
        "",
        {
            "arguments": {
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "SKDocumentCreate": (
        b"@^{__CFString=}@^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKDocumentCreateWithURL": (
        b"@^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexClose": (b"v^{__SKIndex=}",),
    "SKIndexGetDocumentTermFrequency": (b"q^{__SKIndex=}qq",),
    "SKIndexDocumentIteratorCopyNext": (
        b"@^{__SKIndexDocumentIterator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexRenameDocument": (b"Z^{__SKIndex=}@^{__CFString=}",),
    "SKSummaryGetTypeID": (b"Q",),
    "SKDocumentGetSchemeName": (b"^{__CFString=}@",),
    "SKDocumentCopyURL": (
        b"^{__CFURL=}@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetTypeID": (b"Q",),
    "SKSearchCancel": (b"v^{__SKSearch=}",),
    "SKIndexGetDocumentCount": (b"q^{__SKIndex=}",),
    "SKSummaryCopySentenceSummaryString": (
        b"^{__CFString=}^{__SKSummary=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetTermDocumentCount": (b"q^{__SKIndex=}q",),
    "SKIndexGetTermIDForTermString": (b"q^{__SKIndex=}^{__CFString=}",),
    "SKSummaryCopyParagraphSummaryString": (
        b"^{__CFString=}^{__SKSummary=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetDocumentState": (b"I^{__SKIndex=}@",),
    "SKSearchCreate": (
        b"^{__SKSearch=}^{__SKIndex=}^{__CFString=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexAddDocumentWithText": (b"Z^{__SKIndex=}@^{__CFString=}Z",),
    "SKIndexAddDocument": (b"Z^{__SKIndex=}@^{__CFString=}Z",),
    "SKIndexSetMaximumBytesBeforeFlush": (b"v^{__SKIndex=}q",),
    "SKSearchFindMatches": (
        b"Z^{__SKSearch=}q^q^fd^q",
        "",
        {
            "arguments": {
                2: {"c_array_length_in_arg": (1, 5), "type_modifier": "o"},
                3: {"c_array_length_in_arg": (1, 5), "type_modifier": "o"},
                5: {"type_modifier": "o"},
            }
        },
    ),
    "SKIndexCopyTermStringForTermID": (
        b"^{__CFString=}^{__SKIndex=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexGetAnalysisProperties": (b"^{__CFDictionary=}^{__SKIndex=}",),
    "SKSearchResultsGetCount": (b"q^{__SKSearchResults=}",),
    "SKSearchResultsGetInfoInRange": (
        b"q^{__SKSearchResults=}{CFRange=qq}^@^^{__SKIndex=}^f",
        "",
        {
            "arguments": {
                2: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
                3: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
                4: {
                    "c_array_length_in_arg": 1,
                    "c_array_length_in_result": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "SKIndexCopyDocumentForDocumentID": (
        b"@^{__SKIndex=}q",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "SKIndexCopyInfoForDocumentIDs": (
        b"v^{__SKIndex=}q^q^^{__CFString=}^q",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                2: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                3: {
                    "already_cfretained": True,
                    "c_array_length_in_arg": 1,
                    "type_modifier": "o",
                },
                4: {"c_array_length_in_arg": 1, "type_modifier": "o"},
            },
        },
    ),
    "SKIndexGetIndexType": (b"I^{__SKIndex=}",),
    "SKIndexDocumentIteratorGetTypeID": (b"Q",),
}
cftypes = [
    (
        "SKIndexDocumentIteratorRef",
        b"^{__SKIndexDocumentIterator=}",
        "SKIndexDocumentIteratorGetTypeID",
        None,
    ),
    ("SKIndexRef", b"^{__SKIndex=}", "SKIndexGetTypeID", None),
    ("SKSearchGroupRef", b"^{__SKSearchGroup=}", "SKSearchGroupGetTypeID", None),
    ("SKSearchRef", b"^{__SKSearch=}", "SKSearchGetTypeID", None),
    ("SKSearchResultsRef", b"^{__SKSearchResults=}", "SKSearchResultsGetTypeID", None),
    ("SKSummaryRef", b"^{__SKSummary=}", "SKSummaryGetTypeID", None),
    ("SKDocumentRef", b"@", "SKDocumentGetTypeID", None),
]
expressions = {}

# END OF FILE
