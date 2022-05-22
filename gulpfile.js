'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass-embedded'));
const sourcemaps = require('gulp-sourcemaps');
const del = require('del');
const cleanCSS = require('gulp-clean-css');

// Future: gulp-imagemin, gulp-copy


var sassSrc = "./bits/styles/**/*.scss";
var assetDest = "themes/phenix/assets";
var cssDest = assetDest + "/styles";

function buildStyles() {
  return gulp.src(sassSrc)
    .pipe(sourcemaps.init())
    .pipe(sass.sync({
      outputStyle: 'compressed',
      includePaths: ['node_modules/normalize.css']
      }).on('error', sass.logError))
    .pipe(cleanCSS())
    .pipe(sourcemaps.write('./maps'))
    .pipe(gulp.dest(cssDest));
};

function clean() {
  return del([
    assetDest + '/styles/*',
    ]);
};

exports.buildStyles = buildStyles;

exports.watch = function () {
  gulp.watch(sassSrc, buildStyles);
};

exports.default = gulp.series(clean, buildStyles);
