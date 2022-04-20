module.exports = {
  optimize: true,
  files: {
    // javascripts: {
    //   joinTo: {
    //     'libs.js': /^node_modules/,
    //     'phenix.js': /^bits/
    //   }
    // },
    stylesheets: {
      joinTo: {
        'phenix.css': 'bits/styles/*.scss',
        'styles/page_biochips.css': 'bits/styles/custom/page_biochips.scss',
        'styles/page_homepage.css': 'bits/styles/custom/page_homepage.scss',
        'styles/page_phd.css': 'bits/styles/custom/page_phd.scss',
        'styles/page_wikimedia.css': 'bits/styles/custom/page_wikimedia.scss',
        'styles/page_wikimedia2030.css': 'bits/styles/custom/page_wikimedia2030.scss',
        'styles/post_2031-scenarios.css': 'bits/styles/custom/post_2031-scenarios.scss',
        'styles/post_stakes-of-knowledge.css': 'bits/styles/custom/post_stakes-of-knowledge.scss'
      }
    }
  },
  paths: {
    watched: ['bits'],
    public: 'themes/phenix/assets'
  },
  plugins: {
    sass: {
      // https://github.com/brunch/sass-brunch
      options: {
        includePaths: ['node_modules/normalize.css'],
        precision: 8,
        allowCache: true,
        sourceMapEmbed: true
      }
    },
    postcss: {
      processors: [
        require('autoprefixer')(
          // per https://get.foundation/sites/docs/sass.html#autoprefixer-required
          ['last 2 versions', 'ie >= 9', 'android >= 4.4', 'ios >= 7']),
        require('cssnano')
      ]
    },
    copycat: {
      //"fonts/fontawesome": ["node_modules/font-awesome/fonts"]
    }
  },
  npm: {
    compilers: ['babel-brunch']
  }
};
