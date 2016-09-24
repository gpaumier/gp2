module.exports = config:
    files:
        javascripts:
            joinTo:
                'libs.js': /^(bower_components|vendor|node_modules)/
                'fumseck.js': /^bits/
        stylesheets:
            joinTo: 'fumseck.css'
    paths:
        watched: ['bits']
        public: 'themes/fumseck/assets'
    plugins:
        sass:
            options:
                includePaths: ['node_modules/foundation-sites/scss']
        postcss:
            processors: [
                require('autoprefixer')({
                    browsers: ['last 2 versions', 'ie >= 9', 'and_chr >= 2.3']
                }),
                require('csswring')
            ]
