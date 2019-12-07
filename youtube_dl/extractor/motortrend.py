# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class MotorTrendIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?motortrendondemand\.com/(?:detail/)?(?:[\w-]+/)?(?P<id>[^/]+)/?(?:$|[?#])'
    _TEST = {
        'url': 'https://www.motortrendondemand.com/detail/the-story-of-ford-vs-ferrari/0_1j1evbz7/',
        'info_dict': {
            'id': '0_1j1evbz7',
            'ext': 'unknown_video',
            'title': 'The Story of Ford vs Ferrari',
            #'thumbnail': 'https://cdnsecakmi.kaltura.com/p/2093031/sp/209303100/thumbnail/entry_id/0_1j1evbz7/def_height/480/def_width/640/'
        },
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'url': url,
            #'thumbnail': '',
        }
