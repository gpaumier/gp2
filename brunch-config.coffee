module.exports = config:
    optimize: true
    files:
        javascripts:
            joinTo:
                'libs.js': /^node_modules/,
                'fumseck.js': /^bits/
        stylesheets:
            joinTo: 'fumseck.css'
    paths:
        watched: [
            'bits'
        ]
        public: 'themes/fumseck/assets'
    plugins:
        babel:
            presets: ['env']
        sass:
            options:
                includePaths: ['node_modules/foundation-sites/scss']
        postcss:
            processors: [
                require('autoprefixer')({
                    # per https://foundation.zurb.com/sites/docs/sass.html#autoprefixer-required
                    browsers: ['last 2 versions', 'ie >= 9', 'and_chr >= 2.3']
                }),
                require('csswring')
            ]

    npm: # doc: http://brunch.io/docs/config#-npm-
        compilers: ['babel-brunch']
