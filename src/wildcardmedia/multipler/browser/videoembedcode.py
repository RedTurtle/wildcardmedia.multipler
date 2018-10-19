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
            # LE BESTEMMIE PER RISOLVERE QUESTA COSA. I link di multipler sono
            # variabili e dobbiamo trovare se matchano. In caso positivo,
            # estrarre il codice identificativo del video, che è alla fine del
            # file name.

            # string_match = re.search('(?<=https://multipler.lepida.it/Internos/video/)\w+', self.context.video_url)  # noqa
            # string_match = re.search(r'https?://multipler.lepida.it/[a-zA-Z]*/video/', self.context.video_url)  # noqa
            # string_match = self.context.video_url[:string_match.start()] + self.context.video_url[string_match.end():]  # noqa
            try:
                string_match = re.search(
                    r'https?://multipler.lepida.it/[a-zA-Z]*/video/',
                    self.context.video_url
                )

                string_match = self.context.video_url[:string_match.start()] + self.context.video_url[string_match.end():]  # noqa

                if string_match:
                    site_code_string = string_match.split("_")[0]
                    video_code_ID = string_match.split("_")[1][:-4]
                    base_link = "https://multipler.lepida.it/{}/video/thumbs/".format(site_code_string)  # noqa
                    return base_link + site_code_string + "_" + video_code_ID + ".jpg"  # noqa
                else:
                    return ""
            except Exception as err:
                return ""
