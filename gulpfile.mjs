'use strict';

// TODO clean up some more using https://github.com/gulpjs/gulp#use-latest-javascript-version-in-your-gulpfile

import gulp from 'gulp';
import dartSass from 'sass-embedded';
import gulpSass from 'gulp-sass';
const sass = gulpSass(dartSass);
import sourcemaps from 'gulp-sourcemaps';
import { deleteAsync } from 'del';
import cleanCSS from 'gulp-clean-css';
import concat from 'gulp-concat';

// Future: gulp-imagemin, gulp-copy

// General

var assetDest = "themes/phenix/assets";

function clean() {
  return deleteAsync([
    assetDest + '/styles/*',
    assetDest + '/js/*',
    ]);
};

// Styles

var sassSrc = "./bits/styles/**/*.scss";
var assetDest = "themes/phenix/assets";
var cssDest = assetDest + "/styles";

export function buildStyles() {
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

// JavaScript

var jsSrc = "./bits/**/*.js";
var jsDest = assetDest + "/js";

export function buildScripts() {
  return gulp.src(jsSrc)
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest(jsDest));
};

// Main

function watchFiles() {
  gulp.watch(sassSrc, buildStyles);
  gulp.watch(jsSrc, buildScripts);
};

export { watchFiles as watch };

const build = gulp.series(clean, gulp.parallel(buildStyles, buildScripts));
/*
 * Export a default task
 */

export default build;
