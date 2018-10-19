# -*- coding: utf-8 -*-

from wildcard.media.adapter import IVideoEmbedCode
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import implements

import re
import urllib


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

    def getPosterURL(self):
        """ Generiamo la URL della cover generata dal servizio di multipler.

        Nel caso in cui ci sia impostata una lead image sull'oggetto, quella
        ha la precedenza su quella generata automaticamente dal servizio di
        streaming multipler. Questo per evitare che se un video ha una cover
        che è stata generata come un fotogramma nero, si può impostare una
        grafica più sensata...
        """

        if self.context.image:
            return self.context.absolute_url() + "/@@download/image/" + urllib.quote(self.context.image.filename)  # noqa
            # ${context/absolute_url}/@@download/image/${context/image/filename}
            # return None
        else:
            # https://multipler.lepida.it/Internos/video/
            # string_match = re.search('(?<=https://multipler.lepida.it/Internos/video/)\w+', self.context.video_url)  # noqa
            try:
                string_match = re.search(
                    '(?<=https://multipler.lepida.it/Internos/video/)\w+',
                    self.context.video_url
                )

                if string_match.group():
                    multipler_code = string_match.group()
                    site_code_string = multipler_code.split("_")[0]
                    video_code_ID = multipler_code.split("_")[1]
                    base_link = "https://multipler.lepida.it/Internos/video/thumbs/"  # noqa
                    return base_link + site_code_string + "_" + video_code_ID + ".jpg"  # noqa
                else:
                    return ""
            except Exception as err:
                return ""
