var metalsmith = require('metalsmith');
var markdown   = require('metalsmith-pandoc');
var templates  = require('metalsmith-templates');
var serve      = require('metalsmith-serve');
var watch      = require('metalsmith-watch')

metalsmith(__dirname)
    .source('src')
    .use(markdown())
    .use(templates({
        engine: 'jade'
    }))
    .destination('build')
    .use(serve({
        port: 8081
    }))
    .use(watch({
        paths: {
            "${source}/**/*": true,
            "templates/**/*": "**/*.md",
        }
    }))
    .build(function (err) {
        if (err) {
            throw err;
        }
    });
