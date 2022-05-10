"use strict";

// Import jQuery from
// node_modules using Brunch's NPM support

import $ from 'jquery';

var App = {
    init: function init() {

        $(document).ready(function() {
          console.log('Phenix JavaScript loaded.');
        } );
    }
};

module.exports = App;
