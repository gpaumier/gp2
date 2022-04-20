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
        'styles/page_wikimedia2030.css': 'bits/styles/custom/page_wikimedia2030.scss'
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
        //includePaths: ['node_modules/foundation-sites/scss', 'node_modules/font-awesome/scss'],
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
