# -*- coding: utf-8 -*-
from lxml import html
import lxml.etree as le

def get_lead_text (post_text):
    """ Extract the lead text from a post

    The lead text is identified by a <blockquote> with the 'highlights' class"""

    tree = html.fromstring(post_text)
    highlights = tree.xpath('//blockquote[@class="highlights"]')

    try:
        # http://stackoverflow.com/questions/29887576/xpath-extract-current-node-content-including-all-child-node
        lead_text = highlights[0].text + ''.join(le.tostring(node, encoding='unicode') for node in highlights[0])

    except IndexError:
        lead_text = ''

    return lead_text
