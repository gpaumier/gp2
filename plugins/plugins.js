var cheerio = require('cheerio');

/**
 * Walk through the HTML of each file and prepend '/files/' to the img srcs since that's where they live after the build.
 *
 * TODO:
 * - add multiple sizes for responsive images
 * - add PNG fallback for SVG if it's not supported by the browser
 */

function rewriteImages() {
    return function (files, metalsmith, done) {
        for (var file in files) {

            var $ = cheerio.load(files[file].contents);

            $('img').each(function (index, element) {

                // Rewrite the path to the files directory

                $(this).attr('src', '/files/' + $(this).attr('src'));

                // Mark SVG, JPG and PNG files

                var extension = $(this).attr('src').slice(-3);

                if (['svg', 'jpg', 'png'].indexOf(extension)) {
                    $(this).addClass('img-' + extension);
                }

            });

            addSVGFallback($, 'png');
            addWebP($, 'jpg');
            addWebP($, 'png');

            files[file].contents = $.html();
        }
        done();
    };
};

module.exports.rewriteImages = rewriteImages;

/**
 * Rewrite SVG src attributes to use a PNG bitmap image by default for older browsers, and let newer browsers pick the SVG from <picture>.
 */

function addSVGFallback($, fallbackExtension) {

    $('.img-svg').each(function (index, element) {

        // cheerio doesn't yet implement .wrap(), so we need to work around it. This will be much simpler with .wrap().

        $(this).replaceWith(
            '<picture><source type="image/svg+xml" srcset="'
            + $(this).attr('src')
            + '" />'
            + '<img src="'
            + $(this).attr('src').slice(0,-3) + fallbackExtension
            + '" alt="'
            + $(this).attr('alt')
            + '" class="'
            + $(this).attr('class')
            + '"></picture>'
        );
    });

    return $;
}

/**
 * Add WebP sources for JPG and PNG images in <picture>, for browsers that support it.
 */

function addWebP($, srcExtension) {

    $('.img-' + srcExtension).each(function (index, element) {

        $(this).replaceWith(
            '<picture><source type="image/webp" srcset="'
            + $(this).attr('src').slice(0,-srcExtension.length) + 'webp'
            + '" />'
            + '<img src="'
            + $(this).attr('src')
            + '" alt="'
            + $(this).attr('alt')
            + '" class="'
            + $(this).attr('class')
            + '"></picture>'
        );
    });

    return $;
}
