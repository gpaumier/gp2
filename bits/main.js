"use strict";

// Import jQuery, Foundation, and individual Foundation plugins from
// node_modules using Brunch's NPM support
//
// For Foundation and its plugins, see:
// * https://github.com/zurb/foundation-sites/issues/10336#issuecomment-315955426
// * https://github.com/zurb/foundation-zurb-template/blob/master/src/assets/js/lib/foundation-explicit-pieces.js

import $ from 'jquery';
import { Foundation } from 'foundation-sites/js/foundation.core';
import { Dropdown } from 'foundation-sites/js/foundation.dropdown';
import { DropdownMenu } from 'foundation-sites/js/foundation.dropdownMenu';
import { Touch } from 'foundation-sites/js/foundation.util.touch';
import { Triggers } from 'foundation-sites/js/foundation.util.triggers';

var App = {
    init: function init() {

        // Initialize Foundation and its plugins (per the links above)
        Foundation.addToJquery($);
        Touch.init($);
        Triggers.init($, Foundation);
        Foundation.plugin(Dropdown, 'Dropdown');
        Foundation.plugin(DropdownMenu, 'DropdownMenu');
        $(document).foundation();

        $(document).ready(function() {
          console.log('Phenix JavaScript loaded.');
        } );
    }
};

module.exports = App;
