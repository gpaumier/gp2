module.exports = config:
    files:
        javascripts:
            joinTo:
                'libs.js': /^(bower_components|vendor)/
                'fumseck.js': /^bits/
        stylesheets:
            joinTo: 'fumseck.css'
    paths:
        watched: ['bits']
        public: 'src/bits'
    plugins:
        sass:
            options:
                includePaths: ['bower_components/foundation/scss']
