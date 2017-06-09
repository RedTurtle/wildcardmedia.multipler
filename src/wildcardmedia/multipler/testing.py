# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import wildcardmedia.multipler


class WildcardmediaMultiplerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=wildcardmedia.multipler)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'wildcardmedia.multipler:default')


WILDCARDMEDIA_MULTIPLER_FIXTURE = WildcardmediaMultiplerLayer()


WILDCARDMEDIA_MULTIPLER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WILDCARDMEDIA_MULTIPLER_FIXTURE,),
    name='WildcardmediaMultiplerLayer:IntegrationTesting'
)


WILDCARDMEDIA_MULTIPLER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WILDCARDMEDIA_MULTIPLER_FIXTURE,),
    name='WildcardmediaMultiplerLayer:FunctionalTesting'
)


WILDCARDMEDIA_MULTIPLER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        WILDCARDMEDIA_MULTIPLER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='WildcardmediaMultiplerLayer:AcceptanceTesting'
)
