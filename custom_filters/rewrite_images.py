# -*- coding: utf-8 -*-
import lxml
import lxml.etree as le
import os
import mimetypes

from nikola.filters import _ConfigurableFilter, apply_to_text_file
from PIL import Image
from copy import deepcopy

import doit

################################################################
################################################################

# walk the document and find all the <img>

@_ConfigurableFilter(image_srcset_sizes='IMAGE_SRCSET_SIZES',
image_srcset_format='IMAGE_SRCSET_FORMAT', extra_image_extensions='EXTRA_IMAGE_EXTENSIONS', output_folder='OUTPUT_FOLDER')
@apply_to_text_file
def rewrite_images (data, image_srcset_sizes=[], image_srcset_format='', extra_image_extensions=[], output_folder='output'):
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

            node.getparent().replace(node, rewrite_raster(doc, node, image_srcset_format, extra_image_extensions, output_folder, image_srcset_sizes))

    # The doctype disappears so we have to re-add it manually
    # https://lxml.de/api/lxml.etree-module.html#tostring
    page = lxml.html.tostring(doc, encoding='unicode', doctype='<!DOCTYPE html>')
    # remove stray closing source tags:
    return page.replace('</source>', '')

################################################################
################################################################

# if this is an SVG file, only add png fallback

def rewrite_svg(node):
    # TODO
    return node

################################################################
################################################################

# if this is jpg, jpeg, or png,
# * add srcset and sizes attributes
# * add webp (and later avif) alternatives

def rewrite_raster(doc, node, image_srcset_format, extra_image_extensions, output_folder, srcset_sizes_all):
    """Given an image HTML node, returns a modified image node that now includes srcset and sizes attributes for that image (but only if we actually have srcset images)
    """

    # Find the available sizes for the image:
    src = node.get('src')
    srcset_list = get_srcset_list(output_folder, src, srcset_sizes_all)

    # if we have srcset images images to add to the img element, do it here:
    if srcset_list:

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

    if extra_image_extensions:
        # We have extra image output formats to add to the page. In this case, we need to replace the <img> tag by a <picture> tag, add our extra formats with their MIME `type` and own set of `srcset` values, and make the <img> tag a child of the new <picture> element. Values for the `sizes` are the same as for the <img>. We don't have any art direction in here, just resolution switching for different file types.

        # We might not have extra sizes, but we still might have an extra format.

        img_node = deepcopy(node)
        picture_node = doc.makeelement('picture')

        for extension in extra_image_extensions:
            source_node = doc.makeelement('source')

            # Add the alternative srcset with extra extension:
            src_name, src_ext = os.path.splitext(src)
            source_src = src_name + extension
            source_node.set('type', mimetypes.guess_type(source_src)[0])
            srcset = source_src

            # If we have srcset candidates, add them now:
            if srcset_list:
                srcsets = [srcset]
                full_srcset_fmt = image_srcset_format + " {size}w"

                for src_size in srcset_list:
                    srcsets.extend([full_srcset_fmt.format(
                        name = src_name,
                        size = src_size,
                        ext = extension)]
                    )

                srcset = ', '.join(srcsets)
                source_node.set('sizes', sizes)

            source_node.set('srcset', srcset)
            picture_node.append(source_node)

        picture_node.append(img_node)
        
        return picture_node

    return node

def get_srcset_list(output_folder, src, srcset_sizes_all):
    """
    Given a path to an image, returns a list of integers representing the other sizes available for that image.
    """

    src_dir = os.path.basename(os.path.dirname(src))
    src_name = os.path.basename(src)
    src_file = os.path.abspath(os.path.join(output_folder, src_dir, src_name))

    try:
        src_width = Image.open(src_file).size[0]
    except FileNotFoundError:
        # This shouldn't happen, but it might during testing when we don't have all our images
        src_width = 1000    

    return [ size for size in srcset_sizes_all if (size < src_width) ]

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
    #golden2 = 1 / phi ** 2
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
