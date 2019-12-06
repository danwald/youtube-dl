# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class MotorTrendIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?motortrendondemand\.com/(?:detail/)?(?:[\w-]+/)?(?P<id>[^/]+)/?(?:$|[?#])'
    _TEST = {
        'url': 'https://www.motortrendondemand.com/detail/the-story-of-ford-vs-ferrari/',
        'info_dict': {
            'id': '0_1j1evbz7',
            'ext': 'mp4',
            'title': 'AUTOBIOGRAPHY:  Season 1, Episode 9 - The Story of Ford vs Ferrari | MotorTrend',
            'thumbnail': r're:^https?://.*\.jpg$',
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
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
