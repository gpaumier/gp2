var metalsmith  = require('metalsmith');
var markdown    = require('metalsmith-pandoc');
var templates   = require('metalsmith-templates');
var serve       = require('metalsmith-serve');
var watch       = require('metalsmith-watch');
var moment      = require('moment');
var headings    = require('metalsmith-headings');
var convert     = require('metalsmith-convert');
var permalinks  = require('metalsmith-permalinks');
var collections = require('metalsmith-collections');
var branch      = require('metalsmith-branch');
var multiLanguage = require('metalsmith-multi-language');
var copy        = require('metalsmith-copy');
var i18n        = require('metalsmith-i18n');

// Image handling: metalsmith-convert config

var convertConfig = {
    src: '**/*.jpg',
    target: 'jpg',
    resize: {
        width: 320,
        height: 320,
        resizeStyle: 'aspectfit'
    }
};


// Template handling: metalsmith-templates config

var templateConfig = {
    engine: 'jade',
    moment: moment
};


// Collections handling: metalsmith-collection config

var collectionsConfig = {
    articlesEN: {
        pattern: 'articles/*/index_en.md',
        sortBy: 'date',
        reverse: true
    },
    articlesFR: {
        pattern: 'articles/*/index_fr.md',
        sortBy: 'date',
        reverse: true
    }
}


// Processing pipeline

metalsmith(__dirname)
    .source('src')
    .use(multiLanguage({ default: 'en', locales: ['en', 'fr'] }))
    .use(i18n({
        default:   'en',
        locales:   ['en', 'fr'],
        directory: 'locales'
    }))
    .use(collections(collectionsConfig))
    .use(markdown())
    .use(headings('h2'))
    .use(convert(convertConfig))
    .use(branch('articles/*/*.html')
        .use(permalinks({
            pattern: ':locale/articles/:slug'
        }))
    )
    .use(branch('pages/**/*.html')
        .use(permalinks({
            pattern: ':locale/:slug'
        }))
    )
    .use(copy({
        pattern: 'articles/*/*.+(svg|png|jpg)',
        directory: 'files',
        move: true
    }))
    .use(templates(templateConfig))
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
