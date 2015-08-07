module.exports = config:
    files:
        javascripts:
            joinTo: 'fumseck.js'
        stylesheets:
            joinTo: 'fumseck.css'
    paths:
        watched: ['bits']
        public: 'src/bits'
    plugins:
        sass:
            options:
                includePaths: ['bower_components/foundation/scss']
