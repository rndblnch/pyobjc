from PyObjCTools.TestSupport import TestCase, min_sdk_level

import Virtualization  # noqa: F401


class TestVZUSBDevice(TestCase):
    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("VZUSBDevice")
