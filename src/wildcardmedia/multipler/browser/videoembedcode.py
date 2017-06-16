# -*- coding: utf-8 -*-

from zope.interface import implements
from wildcard.media.adapter import IVideoEmbedCode
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile


class MultiplerEmbedCode(object):
    """ MultiplerEmbedCode
    Provides a way to have a html code to embed Lepida Multipler video in a web page

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://multipler.lepida.it/multipler/?id=8dda7049-f52a-4f89-b6f4-4e08e94e434e'
    ...     size = {'width': 425, 'height': 349}
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl
    ...     def getWidth(self):
    ...         return self.size['width']
    ...     def getHeight(self):
    ...         return self.size['height']

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()),
    ...                                         IVideoEmbedCode,
    ...                                         name = 'multipler.lepida.it')


    >>> print adapter()
    <object width="400" height="300" id="_player" name="_player" data="https://multipler.lepida.it/flowplayer-3.2.7.swf" type="application/x-shockwave-flash">
      <param name="movie" value="https://multipler.lepida.it/flowplayer-3.2.7.swf" />
      <param name="allowfullscreen" value="true" />
      <param name="allowscriptaccess" value="always" />
      <param
        name="flashvars"
        value='config={"clip":{"url":"https://multipler.lepida.it/test/video/test_1352.mp4",
        "provider": "pseudostreaming"},"plugins":{"pseudostreaming":{"url": "https://multipler.lepida.it/flowplayer.pseudostreaming-3.2.7.swf"}},
        "playlist":[
          {"url":"https://multipler.lepida.it/test/video/thumbs/test_1352.jpg", "scaling":"fit"},
          {"url":"https://multipler.lepida.it/test/video/test_1352.mp4", "autoPlay":false, "scaling":"fit"}
        ]}' />
        Video dal titolo compila riguardante compila
    </object>
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
