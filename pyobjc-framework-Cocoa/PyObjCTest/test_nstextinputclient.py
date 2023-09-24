import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextInputClientHelper(AppKit.NSObject):
    def insertText_replacementRange_(self, txt, rng):
        pass

    def doCommandBySelector_(self, sel):
        pass

    def setMarkedText_selectedRange_replacementRange_(self, txt, rng1, rng2):
        pass

    def selectedRange(self):
        return 1

    def markedRange(self):
        return 1

    def hasMarkedText(self):
        return 1

    def attributedSubstringForProposedRange_actualRange_(self, rng1, rng2):
        return 1

    def firstRectForCharacterRange_actualRange_(self, rng1, rng2):
        return 1

    def characterIndexForPoint_(self, pt):
        return 1

    def fractionOfDistanceThroughGlyphForPoint_(self, pt):
        return 1

    def baselineDeltaForCharacterAtIndex_(self, idx):
        return 1

    def windowLevel(self):
        return 1

    def drawsVerticallyForCharacterAtIndex_(self, i):
        return 1

    def preferredTextAccessoryPlacement(self):
        return 1

    def selectionRect(self):
        return 1

    def documentVisibleRect(self):
        return 1


class TestNSTextInputClient(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSTextCursorAccessoryPlacement)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementUnspecified, 0)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementBackward, 1)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementForward, 2)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementInvisible, 3)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementCenter, 4)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementOffscreenLeft, 5)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementOffscreenTop, 6)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementOffscreenRight, 7)
        self.assertEqual(AppKit.NSTextCursorAccessoryPlacementOffscreenBottom, 8)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertProtocolExists("NSTextInputClient")
        self.assertArgHasType(
            TestNSTextInputClientHelper.insertText_replacementRange_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.doCommandBySelector_, 0, objc._C_SEL
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_,
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.setMarkedText_selectedRange_replacementRange_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.selectedRange, AppKit.NSRange.__typestr__
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.markedRange, AppKit.NSRange.__typestr__
        )
        self.assertResultIsBOOL(TestNSTextInputClientHelper.hasMarkedText)
        self.assertArgHasType(
            TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.attributedSubstringForProposedRange_actualRange_,
            1,
            b"o^" + AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_,
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.firstRectForCharacterRange_actualRange_,
            1,
            b"o^" + AppKit.NSRange.__typestr__,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.characterIndexForPoint_, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.characterIndexForPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.fractionOfDistanceThroughGlyphForPoint_,
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.baselineDeltaForCharacterAtIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.windowLevel, objc._C_NSInteger
        )

        self.assertResultIsBOOL(
            TestNSTextInputClientHelper.drawsVerticallyForCharacterAtIndex_
        )
        self.assertArgHasType(
            TestNSTextInputClientHelper.drawsVerticallyForCharacterAtIndex_,
            0,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSTextInputClientHelper.preferredTextAccessoryPlacement,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.selectionRect, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(
            TestNSTextInputClientHelper.documentVisibleRect, AppKit.NSRect.__typestr__
        )
