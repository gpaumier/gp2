# -*- coding: utf-8 -*-

# Copyright © 2014-2021 Pelle Nilsson and others.

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

"""Resize images and create thumbnails and different sizes for them."""

import os

from nikola.plugin_categories import Task
from nikola.image_processing import ImageProcessor
from nikola import utils


class ScaleImageMultiple(Task, ImageProcessor):
    """Resize images and create thumbnails for them."""

    name = "scale_images_multiple"

    def process_tree(self, src, dst):
        """Process all images in a src tree and put the (possibly) rescaled images in the dst folder."""
        srcset_fmt = self.kw['image_srcset_format']
        srcset_sizes_all = self.kw['image_srcset_sizes']
        base_len = len(src.split(os.sep))
        for root, dirs, files in os.walk(src, followlinks=True):
            root_parts = root.split(os.sep)
            dst_dir = os.path.join(dst, *root_parts[base_len:])
            utils.makedirs(dst_dir)
            for src_name in files:
                if (not src_name.lower().endswith(tuple(self.image_ext_list)) and not src_name.upper().endswith(tuple(self.image_ext_list))):
                    continue
                dst_file = os.path.join(dst_dir, src_name)
                src_file = os.path.join(root, src_name)
                srcset_name, srcset_ext = os.path.splitext(src_name)

                # Find out the width of the image so we only resize up to that size
                src_width = get_image_width(src_file)
                srcset_sizes = [ size for size in srcset_sizes_all if (size < src_width) ]
                
                # Create the list of filenames, starting with the "max_sized" version that bears the same name as the original file:
                dsts = [dst_file]
                # Now add all the other filenames, based on their size:
                for srcset_size in srcset_sizes:
                    srcset_size_file = os.path.join(dst_dir, srcset_fmt.format(
                        name = srcset_name,
                        size = srcset_size,
                        ext = srcset_ext,
                        #ext = '.webp',
                    ))
                    dsts.append(srcset_size_file)
                yield {
                    'name': dst_file,
                    'file_dep': [src_file],
                    'targets': dsts,
                    'actions': [(self.process_image, (src_file, dsts, srcset_sizes))],
                    'clean': True,
                }

    def process_image(self, src, dsts, srcset_sizes):
        """Resize an image."""

        # Make sure the order here is the same as the order of the list of filenames
        sizes = [self.kw['max_image_size']]
        sizes.extend(srcset_sizes)

        self.resize_image(
            src,
            dst_paths=dsts,
            max_sizes=sizes,
            bigger_panoramas=True,
            preserve_exif_data=self.kw['preserve_exif_data'],
            exif_whitelist=self.kw['exif_whitelist'],
            preserve_icc_profiles=self.kw['preserve_icc_profiles']
        )

    def gen_tasks(self):
        """Copy static files into the output folder."""
        self.kw = {
            'image_srcset_sizes': self.site.config['IMAGE_SRCSET_SIZES'],
            'image_srcset_format': self.site.config['IMAGE_SRCSET_FORMAT'],
            'max_image_size': self.site.config['MAX_IMAGE_SIZE'],
            'image_folders': self.site.config['IMAGE_FOLDERS'],
            'output_folder': self.site.config['OUTPUT_FOLDER'],
            'filters': self.site.config['FILTERS'],
            'preserve_exif_data': self.site.config['PRESERVE_EXIF_DATA'],
            'exif_whitelist': self.site.config['EXIF_WHITELIST'],
            'preserve_icc_profiles': self.site.config['PRESERVE_ICC_PROFILES'],
        }

        self.image_ext_list = self.image_ext_list_builtin
        self.image_ext_list.extend(self.site.config.get('EXTRA_IMAGE_EXTENSIONS', []))

        yield self.group_task()
        for src in self.kw['image_folders']:
            dst = self.kw['output_folder']
            filters = self.kw['filters']
            real_dst = os.path.join(dst, self.kw['image_folders'][src])
            for task in self.process_tree(src, real_dst):
                task['basename'] = self.name
                task['uptodate'] = [utils.config_changed(self.kw)]
                yield utils.apply_filters(task, filters)

def get_image_width(path):
        """Look up the width of an image so we only resize up to that width."""

        return 1500