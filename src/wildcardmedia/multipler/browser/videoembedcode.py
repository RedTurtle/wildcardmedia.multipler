# -*- coding: utf-8 -*-

from wildcard.media.adapter import IVideoEmbedCode
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import implements
from Products.Five import BrowserView

import re
import urllib
import logging

logger = logging.getLogger(__name__)


class MultiplerEmbedCode(object):
    """ Wildcard.media - Multipler
    """

    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile("templates/multiplerembedcode_template.pt")
    regexp_search = r"https?://multipler.lepida.it/[a-zA-Z]*/video/"
    base_link_template = "https://multipler.lepida.it/{}/video/thumbs/"

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()

    def getVideoURL(self):
        return self.context.video_url

    def getVideoInfos(self):
        # LE BESTEMMIE PER RISOLVERE QUESTA COSA. I link di multipler sono
        # variabili e dobbiamo trovare se matchano. In caso positivo,
        # estrarre il codice identificativo del video, che è alla fine del
        # file name.

        # string_match = re.search('(?<=https://multipler.lepida.it/Internos/video/)\w+', self.context.video_url)  # noqa
        # string_match = re.search(r'https?://multipler.lepida.it/[a-zA-Z]*/video/', self.context.video_url)  # noqa
        # string_match = self.context.video_url[:string_match.start()] + self.context.video_url[string_match.end():]  # noqa
        try:
            string_match = re.search(
                self.regexp_search, self.context.video_url,
            )

            string_match = (
                self.context.video_url[: string_match.start()]
                + self.context.video_url[string_match.end() :]
            )

            if not string_match:
                return {}
            return {
                "site_code_string": string_match.split("_")[0],
                "video_code_id": string_match.split("_")[1][:-4],
            }
        except Exception as e:
            logger.exception(e)
            return {}

    def getPosterURL(self):
        """ Generiamo la URL della cover generata dal servizio di multipler.

        Nel caso in cui ci sia impostata una lead image sull'oggetto, quella
        ha la precedenza su quella generata automaticamente dal servizio di
        streaming multipler. Questo per evitare che se un video ha una cover
        che è stata generata come un fotogramma nero, si può impostare una
        grafica più sensata...
        """

        if self.context.image:
            return (
                self.context.absolute_url()
                + "/@@download/image/"
                + urllib.quote(self.context.image.filename)
            )  # noqa
            # ${context/absolute_url}/@@download/image/${context/image/filename}
            # return None
        else:
            try:
                video_infos = self.getVideoInfos()
                if video_infos:
                    base_link = self.base_link_template.format(
                        video_infos.get("site_code_string", "")
                    )
                    return (
                        base_link
                        + video_infos.get("site_code_string", "")
                        + "_"
                        + video_infos.get("video_code_id", "")
                        + ".jpg"
                    )
                else:
                    return ""
            except Exception as e:
                logger.exception(e)
                return ""


class TestMultiplerEmbedCode(MultiplerEmbedCode):
    """
    """

    template = ViewPageTemplateFile(
        "templates/test_multiplerembedcode_template.pt"
    )
    regexp_search = r"https?://test-multipler.lepida.it/[a-zA-Z]*/test/video/"

    def getVideoInfos(self):
        try:
            string_match = re.search(
                self.regexp_search, self.context.video_url,
            )

            string_match = (
                self.context.video_url[: string_match.start()]
                + self.context.video_url[string_match.end() :]
            )

            if not string_match:
                return {}
            return {
                "video_id": string_match.split("/")[0],
                "video_file_id": string_match.split("/")[1],
            }
        except Exception as e:
            logger.exception(e)
            return {}

    def getPosterURL(self):
        """ Generiamo la URL della cover generata dal servizio di multipler.

        Nel caso in cui ci sia impostata una lead image sull'oggetto, quella
        ha la precedenza su quella generata automaticamente dal servizio di
        streaming multipler. Questo per evitare che se un video ha una cover
        che è stata generata come un fotogramma nero, si può impostare una
        grafica più sensata...
        """

        if self.context.image:
            return (
                self.context.absolute_url()
                + "/@@download/image/"
                + urllib.quote(self.context.image.filename)
            )  # noqa
        video_infos = self.getVideoInfos()
        if not video_infos:
            return ""
        return "https://test-multipler.lepida.it/vod/test/video/{0}/{1}.jpg".format(  # noqa
            video_infos.get("video_id", ""),
            video_infos.get("video_file_id", ""),
        )


class TestMultiplerIframe(BrowserView):
    regexp_search = r"https?://test-multipler.lepida.it/[a-zA-Z]*/test/video/"

    def getVideoURL(self):
        return self.context.video_url

    def getVideoInfos(self):
        try:
            string_match = re.search(
                self.regexp_search, self.context.video_url,
            )

            string_match = (
                self.context.video_url[: string_match.start()]
                + self.context.video_url[string_match.end() :]
            )

            if not string_match:
                return {}
            return {
                "video_id": string_match.split("/")[0],
                "video_file_id": string_match.split("/")[1],
            }
        except Exception as e:
            logger.exception(e)
            return {}

    def getPosterURL(self):
        """ Generiamo la URL della cover generata dal servizio di multipler.

        Nel caso in cui ci sia impostata una lead image sull'oggetto, quella
        ha la precedenza su quella generata automaticamente dal servizio di
        streaming multipler. Questo per evitare che se un video ha una cover
        che è stata generata come un fotogramma nero, si può impostare una
        grafica più sensata...
        """

        if self.context.image:
            return (
                self.context.absolute_url()
                + "/@@download/image/"
                + urllib.quote(self.context.image.filename)
            )  # noqa
        video_infos = self.getVideoInfos()
        if not video_infos:
            return ""
        return "https://test-multipler.lepida.it/vod/test/video/{0}/{1}.jpg".format(  # noqa
            video_infos.get("video_id", ""),
            video_infos.get("video_file_id", ""),
        )
