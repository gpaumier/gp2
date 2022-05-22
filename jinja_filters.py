# -*- coding: utf-8 -*-
from lxml import html
import lxml.etree as le

###############################################################################
"""
New filters must be added to TEMPLATE_FILTERS in conf.py
"""
###############################################################################

def get_lead_text (post_text):
    """ Extract the lead text from a post

    The lead text is identified by a <blockquote> with the 'highlights' class"""

    tree = html.fromstring(post_text)

    try:
        # http://stackoverflow.com/questions/29887576/xpath-extract-current-node-content-including-all-child-node
        highlights = tree.xpath('//blockquote[@class="highlights"]')
        lead_text = highlights[0].text + ''.join(le.tostring(node, encoding='unicode') for node in highlights[0])

    except IndexError:
        lead_text = ''

    return lead_text

###############################################################################

def get_lead_figure (post_text):
    """ Extract the lead figure from a post

    This is similar to get_lead_text except for the lead figure.
    The lead figure is identified by a <figure> with the 'lead-figure' class"""

    tree = html.fromstring(post_text)

    try:
        node = tree.xpath('//figure[@class="lead-figure"]')[0]
        lead_fig = node.text + ''.join(le.tostring(e, encoding='unicode') for e in node)

    except IndexError:
        lead_fig = '<p>ERROR</p>'

    return lead_fig

###############################################################################

def remove_lead_figure (post_text):
    """ Remove the lead figure from a post

    This is the opposite of get_lead_figure for when we want to handle them separately.
    The lead figure is identified by a <figure> with the 'lead-figure' class"""

    tree = html.fromstring(post_text)

    try:
        node = tree.xpath('//figure[@class="lead-figure"]')[0]
        node.getparent().remove(node)

    except IndexError:
        return le.tostring(tree, encoding='unicode')

    return le.tostring(tree, encoding='unicode')

###############################################################################
