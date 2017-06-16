# -*- coding: utf-8 -*-

from zope.interface import implements
from wildcard.media.adapter import IVideoEmbedCode
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile


class MultiplerEmbedCode(object):
    """ Wildcard.media - Multipler
    """

    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('templates/multiplerembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()

    def getVideoURL(self):
        return self.context.video_url
