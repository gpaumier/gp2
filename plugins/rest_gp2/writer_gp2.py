# .. coding: utf-8

"""
Plain HyperText Markup Language document tree Writer.
"""


import docutils.writers.html5_polyglot

import mimetypes
import os.path

import docutils
from docutils import frontend, nodes, writers, io
from docutils.transforms import writer_aux
from docutils.writers import html5_polyglot

class WriterGP2(html5_polyglot.Writer):

    def __init__(self):
        html5_polyglot.Writer.__init__(self)
        self.translator_class = HTMLTranslatorGP2


class HTMLTranslatorGP2(html5_polyglot.HTMLTranslator):

    # Copied from docutils.writers.html5_polyglot.HTMLTranslator

    videotypes = ('video/mp4', 'video/webm', 'video/ogg')

    def visit_image(self, node):
        atts = {}
        uri = node['uri']
        mimetype = mimetypes.guess_type(uri)[0]
        if mimetype not in self.videotypes:
            # ORIGINAL: return super(HTMLTranslator, self).visit_image(node)
            return self.visit_image_gp2(node, atts)
        # image size
        if 'width' in node:
            atts['width'] = node['width'].replace('px', '')
        if 'height' in node:
            atts['height'] = node['height'].replace('px', '')
        if 'align' in node:
            atts['class'] = 'align-%s' % node['align']
        if 'controls' in node['classes']:
            atts['controls'] = 'controls'
        atts['title'] = node.get('alt', uri)
        if getattr(self.settings, 'image_loading', None) == 'lazy':
            atts['loading'] = 'lazy'
        # No newline in inline context or if surrounded by <a>...</a>.
        if (isinstance(node.parent, nodes.TextElement) or
            (isinstance(node.parent, nodes.reference) and
             not isinstance(node.parent.parent, nodes.TextElement))):
            suffix = ''
        else:
            suffix = '\n'
        self.body.append('%s<a href="%s">%s</a>%s</video>%s'
            % (self.starttag(node, 'video', suffix, src=uri, **atts),
               uri, node.get('alt', uri), suffix, suffix))

    def depart_image(self, node):
        pass

    # Copied from docutils.writers._html_base.HTMLTranslator
    # In order to make this as future-proof as possible, we don't change anything except to make sure that attributes passed to the function are taken into account:

    # ORIGINAL: def visit_image_gp2(self, node):
    def visit_image_gp2(self, node, atts={}):
        # ORIGINAL: atts = {}
        uri = node['uri']
        mimetype = mimetypes.guess_type(uri)[0]
        # image size
        if 'width' in node:
            atts['width'] = node['width']
        if 'height' in node:
            atts['height'] = node['height']
        if 'scale' in node:
            if (PIL and not ('width' in node and 'height' in node)
                and self.settings.file_insertion_enabled):
                imagepath = url2pathname(uri)
                try:
                    img = PIL.Image.open(
                            imagepath.encode(sys.getfilesystemencoding()))
                except (IOError, UnicodeEncodeError):
                    pass # TODO: warn?
                else:
                    self.settings.record_dependencies.add(
                        imagepath.replace('\\', '/'))
                    if 'width' not in atts:
                        atts['width'] = '%dpx' % img.size[0]
                    if 'height' not in atts:
                        atts['height'] = '%dpx' % img.size[1]
                    del img
            for att_name in 'width', 'height':
                if att_name in atts:
                    match = re.match(r'([0-9.]+)(\S*)$', atts[att_name])
                    assert match
                    atts[att_name] = '%s%s' % (
                        float(match.group(1)) * (float(node['scale']) / 100),
                        match.group(2))
        style = []
        for att_name in 'width', 'height':
            if att_name in atts:
                if re.match(r'^[0-9.]+$', atts[att_name]):
                    # Interpret unitless values as pixels.
                    atts[att_name] += 'px'
                style.append('%s: %s;' % (att_name, atts[att_name]))
                del atts[att_name]
        if style:
            atts['style'] = ' '.join(style)
        if (isinstance(node.parent, nodes.TextElement) or
            (isinstance(node.parent, nodes.reference) and
             not isinstance(node.parent.parent, nodes.TextElement))):
            # Inline context or surrounded by <a>...</a>.
            suffix = ''
        else:
            suffix = '\n'
        if 'align' in node:
            atts['class'] = 'align-%s' % node['align']
        # Embed image file (embedded SVG or data URI):
        if self.image_loading == 'embed':
            err_msg = ''
            if not mimetype:
                err_msg = 'unknown MIME type'
            if not self.settings.file_insertion_enabled:
                err_msg = 'file insertion disabled.'
            try:
                with open(url2pathname(uri), 'rb') as imagefile:
                    imagedata = imagefile.read()
            except IOError as err:
                err_msg = err.strerror
            if err_msg:
                self.document.reporter.error('Cannot embed image %r: %s'
                                             %(uri, err_msg))
            else:
                self.settings.record_dependencies.add(
                                            uri.replace('\\', '/'))
                # TODO: insert SVG as-is?
                # if mimetype == 'image/svg+xml':
                  # read/parse, apply arguments,
                  # insert as <svg ....> ... </svg> # (about 1/3 less data)
                data64 = base64.b64encode(imagedata).decode()
                uri = u'data:%s;base64,%s' % (mimetype, data64)
        elif self.image_loading == 'lazy':
            atts['loading'] = 'lazy'
        if mimetype == 'application/x-shockwave-flash':
            atts['type'] = mimetype
            # do NOT use an empty tag: incorrect rendering in browsers
            tag = (self.starttag(node, 'object', '', data=uri, **atts)
                   + node.get('alt', uri) + '</object>' + suffix)
        else:
            atts['alt'] = node.get('alt', node['uri'])
            tag = self.emptytag(node, 'img', suffix, src=uri, **atts)
        self.body.append(tag)
