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

    # use new HTML5 <figure> and <figcaption> elements
    def visit_figure(self, node):

        atts = {}
        #import doit
        #doit.tools.set_trace()
        if node.get('width'):
            atts['style'] = 'width: %s' % node['width']
        if node.get('align'):
            atts['class'] = "align-" + node['align'] + ' test'

        self.body.append(self.starttag(node, 'figure', **atts))

    def depart_figure(self, node):
        if len(node) > 1:
            self.body.append('</figcaption>\n')
        self.body.append('</figure>\n')
