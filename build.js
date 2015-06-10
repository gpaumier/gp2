var metalsmith = require('metalsmith');
var markdown   = require('metalsmith-pandoc');
var templates  = require('metalsmith-templates');

metalsmith(__dirname)
    .source('src')
    .use(markdown())
    .use(templates({
        engine: 'jade'
    }))
    .destination('build')
    .build(function (err) {
        if (err) {
            throw err;
        }
    });
