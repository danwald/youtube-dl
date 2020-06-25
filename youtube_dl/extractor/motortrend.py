# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class MotorTrendIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?motortrendondemand\.com/(?:detail/)?(?:[\w-]+/)?(?P<id>[^/]+)/?(?:$|[?#])'
    _TEST = {
        #'url': 'https://www.motortrendondemand.com/detail/the-story-of-ford-vs-ferrari/0_1j1evbz7/',
        'info_dict': {
            'id': '0_1j1evbz7',
            'ext': 'unknown_video',
            'title': 'The Story of Ford vs Ferrari',
            'description': 'md5:8c26e5433046a58967ed7e4ea2e6f484',
        },
        'params': {
            'skip_download': True,
        },
        'expected_warnings': ['Failed to download m3u8 information'],
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
