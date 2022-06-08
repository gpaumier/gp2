# -*- coding: utf-8 -*-
import lxml
import lxml.etree as le
import os

from nikola.filters import _ConfigurableFilter, apply_to_text_file
import doit

################################################################
################################################################

# walk the document and find all the <img>

@_ConfigurableFilter(image_srcset_sizes='IMAGE_SRCSET_SIZES',
image_srcset_format='IMAGE_SRCSET_FORMAT')
@apply_to_text_file
def rewrite_images (data, image_srcset_sizes=[], image_srcset_format=''):
    if not image_srcset_sizes and image_srcset_format:
        return data

    raster_exts = ['jpg', 'png', 'jpeg']

    doc = lxml.html.document_fromstring(data)
    images = doc.xpath('//img')

    #doit.tools.set_trace()

    for node in images:
        src = node.get('src')
        if src.lower().endswith('svg'):
            node = rewrite_svg(node)

        if src.lower().endswith(tuple(raster_exts)):
            node = rewrite_raster(node)

    return lxml.html.tostring(doc, encoding='unicode')

################################################################
################################################################

# if this is an SVG file, only add png fallback

def rewrite_svg(node):
    return node

################################################################
################################################################

# if this is jpg, jpeg, or png,
# * add srcset and sizes attributes
# * add webp (and later avif) alternatives

def rewrite_raster(node):
    placeholder = '../../images/2010-07-03_Qt_duck.jpg'
    node.set('src', placeholder)
    return node

def find_srcset_img(uri):
    pass

# To figure out what's available for srcset, look into the nikola cache to see if we have that information recorded there

# If not, take the image URI and look for other sizes in the image output folder


################################################################

# Figure out the sizes depending on golden layout breakpoint
# * 100vw for all on small viewports: past the breakpoint:
# * is the image in a sidebar? (aka <aside>) if so we know its max size
# * is the image in .full-content?
# * is the image a .section-figure? (aka full-golden-large)
# * is the image a page/post hero spread?
# * if none of this, we're probably in main-content
# * Maybe later: add honeycomb


################################################################
