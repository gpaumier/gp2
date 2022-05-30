# -*- coding: utf-8 -*-

# Copyright © 2012-2021 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""reStructuredText compiler for Nikola, with some tweaks"""

import io
import logging
import os

import docutils.core
import docutils.nodes
import docutils.transforms
import docutils.utils
import docutils.io
import docutils.readers.standalone
import docutils.writers.html5_polyglot
import docutils.parsers.rst.directives
from docutils.parsers.rst import roles

from nikola.nikola import LEGAL_VALUES
from nikola.metadata_extractors import MetaCondition
from nikola.plugin_categories import PageCompiler
#from nikola.plugins.compile.rest import CompileRest
from nikola.plugins.compile import rest
from nikola.utils import (
    makedirs,
    write_metadata,
    LocaleBorg,
    map_metadata
)

import doit

from .writer_gp2 import WriterGP2

class CompileRestGP2(rest.CompileRest):
    """Compile reStructuredText into HTML."""

    name = "rest_gp2"
    friendly_name = "reStructuredText_gp2"

    def compile_string(self, data, source_path=None, is_two_file=True, post=None, lang=None):
        """Compile reST into HTML strings."""
        # If errors occur, this will be added to the line number reported by
        # docutils so the line number matches the actual line number (off by
        # 7 with default metadata, could be more or less depending on the post).
        add_ln = 0
        if not is_two_file:
            m_data, data = self.split_metadata(data, post, lang)
            add_ln = len(m_data.splitlines()) + 1

        default_template_path = os.path.join(os.path.dirname(__file__), 'template.txt')
        settings_overrides = {
            'initial_header_level': 1,
            'record_dependencies': True,
            'stylesheet_path': None,
            'link_stylesheet': True,
            'syntax_highlight': 'short',
            # This path is not used by Nikola, but we need something to silence
            # warnings about it from reST.
            'math_output': 'mathjax /assets/js/mathjax.js',
            'template': default_template_path,
            'language_code': LEGAL_VALUES['DOCUTILS_LOCALES'].get(LocaleBorg().current_lang, 'en'),
            'doctitle_xform': self.site.config.get('USE_REST_DOCINFO_METADATA'),
            'file_insertion_enabled': self.site.config.get('REST_FILE_INSERTION_ENABLED'),
        }

        from nikola import shortcodes as sc
        new_data, shortcodes = sc.extract_shortcodes(data)
        if self.site.config.get('HIDE_REST_DOCINFO', False):
            self.site.rst_transforms.append(RemoveDocinfo)

        import doit
        doit.tools.set_trace()
        # Create our custom writer and give it our site object so we can get things like config options for srcset sizes:
        writer_gp2 = WriterGP2(self.site)

        output, error_level, deps, _ = rest.rst2html(
            new_data, settings_overrides=settings_overrides, logger=self.logger, source_path=source_path, l_add_ln=add_ln, transforms=self.site.rst_transforms, writer=writer_gp2,
            writer_name='writer_gp2', )
        if not isinstance(output, str):
            # To prevent some weird bugs here or there.
            # Original issue: empty files.  `output` became a bytestring.
            output = output.decode('utf-8')

        output, shortcode_deps = self.site.apply_shortcodes_uuid(output, shortcodes, filename=source_path, extra_context={'post': post})
        return output, error_level, deps, shortcode_deps
