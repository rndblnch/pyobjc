# This file is generated by objective.metadata
#
# Last update: Sat May 11 10:19:36 2024
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
constants = """$PHContentEditingInputCancelledKey$PHContentEditingInputErrorKey$PHContentEditingInputResultIsInCloudKey$PHImageCancelledKey$PHImageErrorKey$PHImageManagerMaximumSize@{CGSize=dd}$PHImageResultIsDegradedKey$PHImageResultIsInCloudKey$PHImageResultRequestIDKey$PHLivePhotoEditingErrorDomain$PHLivePhotoInfoCancelledKey$PHLivePhotoInfoErrorKey$PHLivePhotoInfoIsDegradedKey$PHLivePhotoShouldRenderAtPlaybackTime$PHLocalIdentifierNotFound$PHLocalIdentifiersErrorKey$PHPhotosErrorDomain$"""
enums = """$PHAccessLevelAddOnly@1$PHAccessLevelReadWrite@2$PHAssetBurstSelectionTypeAutoPick@1$PHAssetBurstSelectionTypeNone@0$PHAssetBurstSelectionTypeUserPick@2$PHAssetCollectionSubtypeAlbumCloudShared@101$PHAssetCollectionSubtypeAlbumImported@6$PHAssetCollectionSubtypeAlbumMyPhotoStream@100$PHAssetCollectionSubtypeAlbumRegular@2$PHAssetCollectionSubtypeAlbumSyncedAlbum@5$PHAssetCollectionSubtypeAlbumSyncedEvent@3$PHAssetCollectionSubtypeAlbumSyncedFaces@4$PHAssetCollectionSubtypeAny@9223372036854775807$PHAssetCollectionSubtypeSmartAlbumAllHidden@205$PHAssetCollectionSubtypeSmartAlbumAnimated@214$PHAssetCollectionSubtypeSmartAlbumBursts@207$PHAssetCollectionSubtypeSmartAlbumCinematic@218$PHAssetCollectionSubtypeSmartAlbumDepthEffect@212$PHAssetCollectionSubtypeSmartAlbumFavorites@203$PHAssetCollectionSubtypeSmartAlbumGeneric@200$PHAssetCollectionSubtypeSmartAlbumLivePhotos@213$PHAssetCollectionSubtypeSmartAlbumLongExposures@215$PHAssetCollectionSubtypeSmartAlbumPanoramas@201$PHAssetCollectionSubtypeSmartAlbumRAW@217$PHAssetCollectionSubtypeSmartAlbumRecentlyAdded@206$PHAssetCollectionSubtypeSmartAlbumScreenshots@211$PHAssetCollectionSubtypeSmartAlbumSelfPortraits@210$PHAssetCollectionSubtypeSmartAlbumSlomoVideos@208$PHAssetCollectionSubtypeSmartAlbumTimelapses@204$PHAssetCollectionSubtypeSmartAlbumUnableToUpload@216$PHAssetCollectionSubtypeSmartAlbumUserLibrary@209$PHAssetCollectionSubtypeSmartAlbumVideos@202$PHAssetCollectionTypeAlbum@1$PHAssetCollectionTypeMoment@3$PHAssetCollectionTypeSmartAlbum@2$PHAssetEditOperationContent@2$PHAssetEditOperationDelete@1$PHAssetEditOperationProperties@3$PHAssetMediaSubtypeNone@0$PHAssetMediaSubtypePhotoDepthEffect@16$PHAssetMediaSubtypePhotoHDR@2$PHAssetMediaSubtypePhotoLive@8$PHAssetMediaSubtypePhotoPanorama@1$PHAssetMediaSubtypePhotoScreenshot@4$PHAssetMediaSubtypeVideoCinematic@2097152$PHAssetMediaSubtypeVideoHighFrameRate@131072$PHAssetMediaSubtypeVideoStreamed@65536$PHAssetMediaSubtypeVideoTimelapse@262144$PHAssetMediaTypeAudio@3$PHAssetMediaTypeImage@1$PHAssetMediaTypeUnknown@0$PHAssetMediaTypeVideo@2$PHAssetPlaybackStyleImage@1$PHAssetPlaybackStyleImageAnimated@2$PHAssetPlaybackStyleLivePhoto@3$PHAssetPlaybackStyleUnsupported@0$PHAssetPlaybackStyleVideo@4$PHAssetPlaybackStyleVideoLooping@5$PHAssetResourceTypeAdjustmentBasePairedVideo@11$PHAssetResourceTypeAdjustmentBasePhoto@8$PHAssetResourceTypeAdjustmentBaseVideo@12$PHAssetResourceTypeAdjustmentData@7$PHAssetResourceTypeAlternatePhoto@4$PHAssetResourceTypeAudio@3$PHAssetResourceTypeFullSizePairedVideo@10$PHAssetResourceTypeFullSizePhoto@5$PHAssetResourceTypeFullSizeVideo@6$PHAssetResourceTypePairedVideo@9$PHAssetResourceTypePhoto@1$PHAssetResourceTypePhotoProxy@19$PHAssetResourceTypeVideo@2$PHAssetSourceTypeCloudShared@2$PHAssetSourceTypeNone@0$PHAssetSourceTypeUserLibrary@1$PHAssetSourceTypeiTunesSynced@4$PHAuthorizationStatusAuthorized@3$PHAuthorizationStatusDenied@2$PHAuthorizationStatusLimited@4$PHAuthorizationStatusNotDetermined@0$PHAuthorizationStatusRestricted@1$PHCollectionEditOperationAddContent@3$PHCollectionEditOperationCreateContent@4$PHCollectionEditOperationDelete@6$PHCollectionEditOperationDeleteContent@1$PHCollectionEditOperationRearrangeContent@5$PHCollectionEditOperationRemoveContent@2$PHCollectionEditOperationRename@7$PHCollectionListSubtypeAny@9223372036854775807$PHCollectionListSubtypeMomentListCluster@1$PHCollectionListSubtypeMomentListYear@2$PHCollectionListSubtypeRegularFolder@100$PHCollectionListSubtypeSmartFolderEvents@200$PHCollectionListSubtypeSmartFolderFaces@201$PHCollectionListTypeFolder@2$PHCollectionListTypeMomentList@1$PHCollectionListTypeSmartFolder@3$PHImageContentModeAspectFill@1$PHImageContentModeAspectFit@0$PHImageContentModeDefault@0$PHImageRequestOptionsDeliveryModeFastFormat@2$PHImageRequestOptionsDeliveryModeHighQualityFormat@1$PHImageRequestOptionsDeliveryModeOpportunistic@0$PHImageRequestOptionsResizeModeExact@2$PHImageRequestOptionsResizeModeFast@1$PHImageRequestOptionsResizeModeNone@0$PHImageRequestOptionsVersionCurrent@0$PHImageRequestOptionsVersionOriginal@2$PHImageRequestOptionsVersionUnadjusted@1$PHInvalidAssetResourceDataRequestID@0$PHInvalidImageRequestID@0$PHLivePhotoEditingErrorCodeAborted@1$PHLivePhotoEditingErrorCodeUnknown@0$PHLivePhotoFrameTypePhoto@0$PHLivePhotoFrameTypeVideo@1$PHLivePhotoRequestIDInvalid@0$PHObjectTypeAsset@1$PHObjectTypeAssetCollection@2$PHObjectTypeCollectionList@3$PHPhotosErrorAccessRestricted@3310$PHPhotosErrorAccessUserDenied@3311$PHPhotosErrorChangeNotSupported@3300$PHPhotosErrorIdentifierNotFound@3201$PHPhotosErrorInternalError@-1$PHPhotosErrorInvalid@-1$PHPhotosErrorInvalidResource@3302$PHPhotosErrorLibraryInFileProviderSyncRoot@5423$PHPhotosErrorLibraryVolumeOffline@3114$PHPhotosErrorMissingResource@3303$PHPhotosErrorMultipleIdentifiersFound@3202$PHPhotosErrorNetworkAccessRequired@3164$PHPhotosErrorNetworkError@3169$PHPhotosErrorNotEnoughSpace@3305$PHPhotosErrorOperationInterrupted@3301$PHPhotosErrorPersistentChangeDetailsUnavailable@3210$PHPhotosErrorPersistentChangeTokenExpired@3105$PHPhotosErrorRelinquishingLibraryBundleToWriter@3142$PHPhotosErrorRequestNotSupportedForAsset@3306$PHPhotosErrorSwitchingSystemPhotoLibrary@3143$PHPhotosErrorUserCancelled@3072$PHVideoRequestOptionsDeliveryModeAutomatic@0$PHVideoRequestOptionsDeliveryModeFastFormat@3$PHVideoRequestOptionsDeliveryModeHighQualityFormat@1$PHVideoRequestOptionsDeliveryModeMediumQualityFormat@2$PHVideoRequestOptionsVersionCurrent@0$PHVideoRequestOptionsVersionOriginal@1$"""
misc.update(
    {
        "PHLivePhotoEditingErrorCode": NewType("PHLivePhotoEditingErrorCode", int),
        "PHImageContentMode": NewType("PHImageContentMode", int),
        "PHVideoRequestOptionsDeliveryMode": NewType(
            "PHVideoRequestOptionsDeliveryMode", int
        ),
        "PHAuthorizationStatus": NewType("PHAuthorizationStatus", int),
        "PHAssetPlaybackStyle": NewType("PHAssetPlaybackStyle", int),
        "PHCollectionListSubtype": NewType("PHCollectionListSubtype", int),
        "PHAssetResourceType": NewType("PHAssetResourceType", int),
        "PHObjectType": NewType("PHObjectType", int),
        "PHAssetMediaSubtype": NewType("PHAssetMediaSubtype", int),
        "PHCollectionEditOperation": NewType("PHCollectionEditOperation", int),
        "UIImageOrientation": NewType("UIImageOrientation", int),
        "PHLivePhotoFrameType": NewType("PHLivePhotoFrameType", int),
        "PHAssetBurstSelectionType": NewType("PHAssetBurstSelectionType", int),
        "PHAssetSourceType": NewType("PHAssetSourceType", int),
        "PHAssetEditOperation": NewType("PHAssetEditOperation", int),
        "PHImageRequestOptionsDeliveryMode": NewType(
            "PHImageRequestOptionsDeliveryMode", int
        ),
        "PHAssetCollectionSubtype": NewType("PHAssetCollectionSubtype", int),
        "PHImageRequestOptionsVersion": NewType("PHImageRequestOptionsVersion", int),
        "PHVideoRequestOptionsVersion": NewType("PHVideoRequestOptionsVersion", int),
        "PHAssetCollectionType": NewType("PHAssetCollectionType", int),
        "PHAssetMediaType": NewType("PHAssetMediaType", int),
        "PHPhotosError": NewType("PHPhotosError", int),
        "PHImageRequestOptionsResizeMode": NewType(
            "PHImageRequestOptionsResizeMode", int
        ),
        "PHAccessLevel": NewType("PHAccessLevel", int),
        "PHCollectionListType": NewType("PHCollectionListType", int),
    }
)
misc.update({"PHLivePhotoEditingOption": NewType("PHLivePhotoEditingOption", str)})
misc.update({})
aliases = {
    "PHCollectionListSubtypeAny": "NSIntegerMax",
    "PHAssetCollectionSubtypeAny": "NSIntegerMax",
    "PHImageContentModeDefault": "PHImageContentModeAspectFit",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"NSObject", b"image", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"photoLibraryDidBecomeUnavailable:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"photoLibraryDidChange:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"renderScale", {"required": True, "retval": {"type": "d"}})
    r(b"NSObject", b"time", {"required": True, "retval": {"type": "{CMTime=qiIq}"}})
    r(b"NSObject", b"type", {"required": True, "retval": {"type": "q"}})
    r(b"PHAsset", b"canPerformEditOperation:", {"retval": {"type": "Z"}})
    r(b"PHAsset", b"hasAdjustments", {"retval": {"type": b"Z"}})
    r(b"PHAsset", b"isFavorite", {"retval": {"type": "Z"}})
    r(b"PHAsset", b"isHidden", {"retval": {"type": "Z"}})
    r(b"PHAsset", b"isSyncFailureHidden", {"retval": {"type": "Z"}})
    r(b"PHAsset", b"representsBurst", {"retval": {"type": "Z"}})
    r(
        b"PHAsset",
        b"requestContentEditingInputWithOptions:completionHandler:",
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
    r(b"PHAssetChangeRequest", b"isFavorite", {"retval": {"type": b"Z"}})
    r(b"PHAssetChangeRequest", b"isHidden", {"retval": {"type": b"Z"}})
    r(b"PHAssetChangeRequest", b"setFavorite:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PHAssetChangeRequest", b"setHidden:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"PHAssetCreationRequest",
        b"supportsAssetResourceTypes:",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PHAssetResourceCreationOptions",
        b"setShouldMoveFile:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PHAssetResourceCreationOptions", b"shouldMoveFile", {"retval": {"type": b"Z"}})
    r(
        b"PHAssetResourceManager",
        b"requestDataForAssetResource:options:dataReceivedHandler:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
            }
        },
    )
    r(
        b"PHAssetResourceManager",
        b"writeDataForAssetResource:toFile:options:completionHandler:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"PHAssetResourceRequestOptions",
        b"isNetworkAccessAllowed",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PHAssetResourceRequestOptions",
        b"setNetworkAccessAllowed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PHAssetResourceRequestOptions",
        b"setProgressHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"d"}},
                    }
                }
            }
        },
    )
    r(
        b"PHCachingImageManager",
        b"allowsCachingHighQualityImages",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PHCachingImageManager",
        b"setAllowsCachingHighQualityImages:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PHCollection", b"canContainAssets", {"retval": {"type": b"Z"}})
    r(b"PHCollection", b"canContainCollections", {"retval": {"type": b"Z"}})
    r(b"PHCollection", b"canPerformEditOperation:", {"retval": {"type": b"Z"}})
    r(
        b"PHContentEditingInputRequestOptions",
        b"isNetworkAccessAllowed",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PHContentEditingInputRequestOptions",
        b"progressHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"o^Z"},
                    },
                }
            }
        },
    )
    r(
        b"PHContentEditingInputRequestOptions",
        b"setCanHandleAdjustmentData:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"PHContentEditingInputRequestOptions",
        b"setNetworkAccessAllowed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PHContentEditingInputRequestOptions",
        b"setProgressHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"d"},
                            2: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHContentEditingOutput",
        b"renderedContentURLForType:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(b"PHFetchOptions", b"includeAllBurstAssets", {"retval": {"type": b"Z"}})
    r(b"PHFetchOptions", b"includeHiddenAssets", {"retval": {"type": "Z"}})
    r(
        b"PHFetchOptions",
        b"setIncludeAllBurstAssets:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PHFetchOptions", b"setIncludeHiddenAssets:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"PHFetchOptions",
        b"setWantsIncrementalChangeDetails:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"PHFetchOptions", b"wantsIncrementalChangeDetails", {"retval": {"type": "Z"}})
    r(b"PHFetchResult", b"containsObject:", {"retval": {"type": "Z"}})
    r(
        b"PHFetchResult",
        b"enumerateObjectsAtIndexes:options:usingBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"Q"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHFetchResult",
        b"enumerateObjectsUsingBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"Q"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHFetchResult",
        b"enumerateObjectsWithOptions:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"Q"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHFetchResultChangeDetails",
        b"enumerateMovesWithBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Q"},
                            2: {"type": b"Q"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHFetchResultChangeDetails",
        b"hasIncrementalChanges",
        {"retval": {"type": "Z"}},
    )
    r(b"PHFetchResultChangeDetails", b"hasMoves", {"retval": {"type": "Z"}})
    r(
        b"PHImageManager",
        b"requestAVAssetForVideo:options:resultHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHImageManager",
        b"requestExportSessionForVideo:options:exportPreset:resultHandler:",
        {
            "arguments": {
                5: {
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
        b"PHImageManager",
        b"requestImageDataAndOrientationForAsset:options:resultHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"I"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHImageManager",
        b"requestImageDataForAsset:options:resultHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"I"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHImageManager",
        b"requestImageForAsset:targetSize:contentMode:options:resultHandler:",
        {
            "arguments": {
                6: {
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
        b"PHImageManager",
        b"requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:",
        {
            "arguments": {
                6: {
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
        b"PHImageManager",
        b"requestPlayerItemForVideo:options:resultHandler:",
        {
            "arguments": {
                4: {
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
        b"PHImageRequestOptions",
        b"allowSecondaryDegradedImage",
        {"retval": {"type": b"Z"}},
    )
    r(b"PHImageRequestOptions", b"isNetworkAccessAllowed", {"retval": {"type": "Z"}})
    r(b"PHImageRequestOptions", b"isSynchronous", {"retval": {"type": "Z"}})
    r(
        b"PHImageRequestOptions",
        b"progressHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"@"},
                        3: {"type": b"o^Z"},
                        4: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"PHImageRequestOptions",
        b"setAllowSecondaryDegradedImage:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PHImageRequestOptions",
        b"setNetworkAccessAllowed:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"PHImageRequestOptions",
        b"setProgressHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"d"},
                            2: {"type": b"@"},
                            3: {"type": b"o^Z"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"PHImageRequestOptions", b"setSynchronous:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"PHLivePhoto",
        b"requestLivePhotoWithResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:",
        {
            "arguments": {
                6: {
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
        b"PHLivePhotoEditingContext",
        b"duration",
        {"retval": {"type": b"{_CMTime=qiIq}"}},
    )
    r(
        b"PHLivePhotoEditingContext",
        b"frameProcessor",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"o^@"},
                    },
                }
            }
        },
    )
    r(
        b"PHLivePhotoEditingContext",
        b"photoTime",
        {"retval": {"type": b"{_CMTime=qiIq}"}},
    )
    r(
        b"PHLivePhotoEditingContext",
        b"prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHLivePhotoEditingContext",
        b"saveLivePhotoToOutput:options:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHLivePhotoEditingContext",
        b"setFrameProcessor:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHLivePhotoRequestOptions",
        b"isNetworkAccessAllowed",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"PHLivePhotoRequestOptions",
        b"progressHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"@"},
                        3: {"type": b"o^Z"},
                        4: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"PHLivePhotoRequestOptions",
        b"setNetworkAccessAllowed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PHLivePhotoRequestOptions",
        b"setProgressHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"d"},
                            2: {"type": b"@"},
                            3: {"type": b"o^Z"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"PHObjectChangeDetails", b"assetContentChanged", {"retval": {"type": "Z"}})
    r(b"PHObjectChangeDetails", b"objectWasDeleted", {"retval": {"type": "Z"}})
    r(
        b"PHPersistentChange",
        b"changeDetailsForObjectType:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"PHPersistentChangeFetchResult",
        b"enumerateChangesWithBlock:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"PHPhotoLibrary",
        b"fetchPersistentChangesSinceToken:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"PHPhotoLibrary",
        b"performChanges:completionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"PHPhotoLibrary",
        b"performChangesAndWait:error:",
        {
            "retval": {"type": "Z"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                3: {"type_modifier": b"o"},
            },
        },
    )
    r(
        b"PHPhotoLibrary",
        b"requestAuthorization:",
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
        b"PHPhotoLibrary",
        b"requestAuthorizationForAccessLevel:handler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    }
                }
            }
        },
    )
    r(b"PHProject", b"hasProjectPreview", {"retval": {"type": "Z"}})
    r(b"PHVideoRequestOptions", b"isNetworkAccessAllowed", {"retval": {"type": b"Z"}})
    r(
        b"PHVideoRequestOptions",
        b"progressHandler",
        {
            "comment": "XXX",
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"d"},
                        2: {"type": b"@"},
                        3: {"type": b"o^Z"},
                        4: {"type": b"@"},
                    },
                }
            },
        },
    )
    r(
        b"PHVideoRequestOptions",
        b"setNetworkAccessAllowed:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PHVideoRequestOptions",
        b"setProgressHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"d"},
                            2: {"type": b"@"},
                            3: {"type": b"o^Z"},
                            4: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"null",
        b"requestContentEditingInputWithOptions:completionHandler:",
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
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "PHAdjustmentData", b"initWithFormatIdentifier:formatVersion:data:"
)
objc.registerNewKeywordsFromSelector("PHCloudIdentifier", b"initWithStringValue:")
objc.registerNewKeywordsFromSelector(
    "PHContentEditingOutput", b"initWithContentEditingInput:"
)
objc.registerNewKeywordsFromSelector(
    "PHContentEditingOutput", b"initWithPlaceholderForCreatedAsset:"
)
objc.registerNewKeywordsFromSelector(
    "PHLivePhotoEditingContext", b"initWithLivePhotoEditingInput:"
)
objc.registerNewKeywordsFromSelector("PHProjectChangeRequest", b"initWithProject:")
objc.registerNewKeywordsFromSelector("null", b"initWithPlaceholderForCreatedAsset:")
expressions = {}

# END OF FILE
