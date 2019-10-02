import json
import re
from urllib.request import urlopen

'''
The use of objects has various benefits.
1. Better control of context
2. State that can be evaluated
3. Data can be created and then processing can be added
4. Clean interface 
'''


class TopicSummarizer():
    """TopicSummarizer - Summarizes a wikipedia entry 

    Returns:
        str: [Summary of entry]
    """

    TEXT_URL_TMP = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=2&titles={title}&format=json'
    THUMB_URL_TMP = 'https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles={title}&format=json'

    def __init__(self, topic):
        self.topic = str(topic)

    def process(self):
        self._fetch_text()
        self._fetch_thumbnail()
        return self

    def get_results(self, as_text=False):
        if as_text:
            return self.topic + ' summary: ' + self._text
        return TopicSummary(self.topic, self._thumb_url, self._text)

    def _fetch_text(self):
        self._text_api_url = self.TEXT_URL_TMP.format(title=self.topic)
        self._text_resp = self._get_url_json(self._text_api_url)
        self._text = list(self._text_resp['query']['pages'].values())[
            0]['extract']

    def _fetch_thumbnail(self):
        self._thumb_api_url = self.THUMB_URL_TMP.format(title=self.topic)
        self._thumb_resp = self._get_url_json(self._thumb_api_url)
        self._thumb_url = list(self._thumb_resp['query']['pages'].values())[0][
            'thumbnail']['source']

    def _get_url_json(self, url):
        resp = urlopen(url)
        resp_body = resp.read()
        return json.loads(resp_body)


class TopicSummary():
    def __init__(self, topic, thumb_url, text):
        self.topic = topic
        self.thumb_url = thumb_url
        self.text = re.sub(r'</*.>', '', text)

    def __repr__(self):
        cn = self.__class__.__name__
        return '%s(%r, %r, %r)' % (cn, self.topic, self.thumb_url, self.text)


def main():
    from argparse import ArgumentParser
    prs = ArgumentParser(description='summarize topics from Wikipedia')
    prs.add_argument('-t', '--topic', help='the target topic', required='True')
    args = prs.parse_args()

    print(TopicSummarizer(args.topic).process().get_results(as_text=True))

    return


if __name__ == '__main__':
    main()
