from PyObjCTools.TestSupport import TestCase
import BackgroundAssets
import objc


class TestBADownloaderHelper(BackgroundAssets.NSObject):
    def download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_(
        self, a, b, c, d
    ):
        pass

    def download_didReceiveChallenge_completionHandler_(self, a, b, c):
        pass


class TestBADownloadManager(TestCase):
    def test_protocols(self):
        objc.protocolNamed("BADownloadManagerDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            1,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            2,
            objc._C_LNG_LNG,
        )
        self.assertArgHasType(
            TestBADownloaderHelper.download_didWriteBytes_totalBytesWritten_totalBytesExpectedToWrite_,
            3,
            objc._C_LNG_LNG,
        )

        self.assertArgIsBlock(
            TestBADownloaderHelper.download_didReceiveChallenge_completionHandler_,
            2,
            b"v" + objc._C_NSUInteger + b"@",
        )

    def test_methods(self):
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.fetchCurrentDownloadsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsOut(
            BackgroundAssets.BADownloadManager.scheduleDownload_error_, 1
        )
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.performWithExclusiveControl_, 0, b"v@"
        )
        self.assertArgIsBlock(
            BackgroundAssets.BADownloadManager.performWithExclusiveControlBeforeDate_completion_,
            1,
            b"vZ@",
        )

        self.assertResultIsBOOL(
            BackgroundAssets.BADownloadManager.startForegroundDownload_error_
        )
        self.assertArgIsOut(
            BackgroundAssets.BADownloadManager.startForegroundDownload_error_, 1
        )

        self.assertResultIsBOOL(
            BackgroundAssets.BADownloadManager.cancelDownload_error_
        )
        self.assertArgIsOut(BackgroundAssets.BADownloadManager.cancelDownload_error_, 1)
