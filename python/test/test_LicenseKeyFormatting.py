from unittest import TestCase

from LicenseKeyFormatting import licenseKeyFormatting


class Test(TestCase):
    def test_license_key_formatting(self):
        self.assertEquals("5F3Z-2E9W", licenseKeyFormatting("5F3Z-2e-9-w", 4))
        self.assertEquals("5F3-Z2E9", licenseKeyFormatting("5F3Z-2e-9", 4))
