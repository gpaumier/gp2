var cheerio = require('cheerio');

/**
 * Walk through the HTML of each file and prepend '/files/' to the img srcs since that's where they live after the build.
 *
 * TODO:
 * - add multiple sizes for responsive images
 * - add PNG fallback for SVG if it's not supported by the browser
 */

function img() {
    return function (files, metalsmith, done) {
        for (var file in files) {
            var $ = cheerio.load(files[file].contents);
            $('img').each(function (index, element) {
                $(this).attr('src', '/files/' + $(this).attr('src'));
            });
            files[file].contents = $.html();
        }
        done();
    };
};

module.exports.img = img;
