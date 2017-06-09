# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from wildcardmedia.multipler.testing import WILDCARDMEDIA_MULTIPLER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that wildcardmedia.multipler is properly installed."""

    layer = WILDCARDMEDIA_MULTIPLER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if wildcardmedia.multipler is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'wildcardmedia.multipler'))

    def test_browserlayer(self):
        """Test that IWildcardmediaMultiplerLayer is registered."""
        from wildcardmedia.multipler.interfaces import (
            IWildcardmediaMultiplerLayer)
        from plone.browserlayer import utils
        self.assertIn(IWildcardmediaMultiplerLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = WILDCARDMEDIA_MULTIPLER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['wildcardmedia.multipler'])

    def test_product_uninstalled(self):
        """Test if wildcardmedia.multipler is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'wildcardmedia.multipler'))

    def test_browserlayer_removed(self):
        """Test that IWildcardmediaMultiplerLayer is removed."""
        from wildcardmedia.multipler.interfaces import \
            IWildcardmediaMultiplerLayer
        from plone.browserlayer import utils
        self.assertNotIn(IWildcardmediaMultiplerLayer, utils.registered_layers())
