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

    for node in images:
        src = node.get('src')
        if src.lower().endswith('svg'):
            node = rewrite_svg(node)

        if src.lower().endswith(tuple(raster_exts)):
            node = rewrite_raster(node, image_srcset_format)

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

def rewrite_raster(node, image_srcset_format):
    """Given an image HTML node, returns a modified image node that now includes srcset and sizes attributes for that image.
    """

    #doit.tools.set_trace()

    # Find the available sizes for the image:
    src = node.get('src')
    srcset_list = get_srcset_list(src)

    # Build our srcset attribute:
    srcsets = []
    src_name, src_ext = os.path.splitext(src)
    full_srcset_fmt = image_srcset_format + " {size}w"

    for src_size in srcset_list:
        srcsets.extend([full_srcset_fmt.format(
            name = src_name,
            size = src_size,
            ext = src_ext)]
        )

    srcset = ', '.join(srcsets)

    # Determine the relevant sizes for the image in the page context:
    sizes = get_sizes(node)

    # Update attributes of our node with srcset and sizes values and return it:
    node.set('srcset', srcset)
    node.set('sizes', sizes)
    return node

def get_srcset_list(src):
    """
    Given a path to an image, returns a list of integers representing the other sizes available for that image.
    """

    return [400, 800, 1200, 1600, 2400, 3200]

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

def get_sizes(node):

    # Is one of the node's parents an <aside> element? (meaning we're in the sidebar aka smaller golden content side)
    #doit.tools.set_trace()
    #path = node.getroottree().getpath(node)

    # CSS settings from bits/styles/_settings.scss
    breakpoint_large = '1024px'
    breakpoint_medium = '750px'

    phi = (1 + 5 ** 0.5) / 2
    golden1 = 1 / phi
    golden2 = 1 / phi ** 2
    main_content_max_width = 65 #units: ch

    # Container sizes reflect layouts from the golden grids in
    # bits/styles/common/_layout.scss

    sizes = {
        # The default size is always 100vw on narrow viewports.
        # The sizes on wider viewports are based on the golden grid and golden ratio.

        # The sidebar is in a golden relationship with main-content:
        'aside': '(max-width: {}) 100vw, {}ch'.format(breakpoint_medium, main_content_max_width * golden1),

        # Full-content is the sum of default and aside (a.k.a. default * phi), plus the separating gutter, ignored on first approximation:
        'full-content': '(max-width: {}) 100vw, {}ch'.format(breakpoint_medium, main_content_max_width * phi),

        # Hero h2 spreads are trivial to calculare from the viewport width:
        'hero-h2-golden': '(max-width: {}) 100vw, {}vw'.format(breakpoint_medium, golden1 * 100),

        # The article header hero always takes up the full width of the viewport:
        'article-header-hero': '100vw',

        # The default size is main-content above the breakpoint, a.k.a. 65ch (main_content_max_width) at most. We can probably make this more efficient by calculating the width when it's fewer than 65ch, but this works for now.
        'default': '(max-width: {}) 100vw, {}ch'.format(breakpoint_medium, main_content_max_width)
    }

    asides = node.iterancestors('aside')
    for aside in asides:
        return sizes['aside']

    ancestors = node.iterancestors()
    for a in ancestors:

        # Do we have classes in the hierarchy that are meaningful for image sizes?
        if a.get('class'):

            classes = a.get('class').split(' ')

            if 'sidebar' in classes:
                return sizes['aside']

            if 'full-content' in classes:
                return sizes['full-content']

            if 'hero-h2-golden' in classes:
                # is this the first image in the h2?
                # Parent = figure, previous = h2
                if node.getparent().getprevious() is not None and node.getparent().getprevious().tag == 'h2':
                    return sizes['hero-h2-golden']

        if a.get('id') == 'article-header-hero':
            return sizes['article-header-hero']

    return sizes['default']

################################################################
