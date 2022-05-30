# -*- coding: utf-8 -*-
from lxml import html
import lxml.etree as le

################################################################
################################################################

# walk the document and find all the <img>

def rewrite_images (html):
    #import doit
    #doit.tools.set_trace()
    return html

################################################################
################################################################

# if this is an SVG file, only add png fallback


################################################################
################################################################

# if this is jpg, jpeg, or png,
# * add srcset and sizes attributes
# * add webp (and later avif) alternatives

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
