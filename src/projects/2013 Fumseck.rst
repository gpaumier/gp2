.. title: Fumseck
.. category: projects-en
.. subtitle: the Solarized WordPress theme
.. slug: fumseck
.. date: 2013-10-24T00:00:00
.. end: 2014-01-06T00:00:00
.. image: /images/2013-12-24_devices-fumseck.jpg
.. roles: designer, coder
.. tags: PHP, WordPress, Solarized, Latin Modern, coding, design
.. has_math: yes

.. highlights::

    Fumseck was a responsive, mobile-first theme for WordPress that I built specifically for this site. It was based on the Solarized color scheme and the Latin Modern font family.


I've never been entirely satisfied with any of the themes that I've tested and used over the years. At some point, I realized that the only way I was going to be happy with both the design and the features was by coding the theme myself. The problem, of course, was that I had never coded in PHP (the scripting language used by WordPress), and that my knowledge of CSS was very basic, although they were both fields I wanted to dive into eventually.

In Fall of 2013, I decided it was time, and got to work. I did some research and read many web articles I had saved in preparation for this project, notably on web technologies, responsiveness and the latest good practices. In the end, there wasn't much that couldn't be understood with a general knowledge of programming and a good look at the reference documentation.

“Fumseck” is the name of Professor Dumbledore's phoenix Fawkes in the French version of the *Harry Potter* book series. Choosing this name was a tongue-in-cheek reference to the fact that this site had been moribund for a while and that I wanted it to "rise from its ashes".

Fumseck is used in conjunction with "Batbelt", a plugin for WordPress that I've written to bundle together customizations I've made to this site that aren't directly related to its appearance. For example, it's the plugin that implements the `Project <//guillaumepaumier.com/projects/>`__ custom content type (used on this page) and custom taxonomies such as `Locations <//guillaumepaumier.com/locations/usa/california/san-francisco/>`__. The Fumseck theme is then in charge of defining the appearance of those customizations, in addition to the rest of the site.


An identity in colors and typefaces
===================================

I fell in love with |latex|_, the document typesetting system, when I started using it for reports and theses in college. I was immediately attracted by its elegance and simplicity. I also found the idea of `compiling <https://en.wikipedia.org/wiki/Compiler>`__ a document really cool.

.. |latex| replace:: :math:`\LaTeX`

.. _latex: https://en.wikipedia.org/wiki/LaTeX


I wanted this site to reflect who I was, and when I found out that `Computer Modern <https://en.wikipedia.org/wiki/Computer_Modern>`__, the family of typefaces designed by Donald Knuth for :math:`\TeX`, had been ported to other font formats by the `GUST e-foundry <http://www.gust.org.pl/projects/e-foundry/index_html>`__ (under the name "Latin Modern"), I knew those were the Chosen Ones.

I also loved the fact that I could use different typefaces from the same family, meaning I could, for example, mix a Serif and a Sans serif typeface that would nonetheless be consistent with each other. Additionally, Latin Modern fonts come with true variations like bold and italics. And have I mentioned how beautiful they look?

If you're using a reasonably modern browser, you're seeing those typefaces right now, loaded as web fonts if you don't already have them installed on your computer. I've used a large base font size because I dislike having to zoom in on so many web pages, even if I have excellent vision.

The color scheme was the other main choice to make regarding the overall appearance of the site. There wasn't much to think about there, though. I knew from the start that I wanted to use Ethan Schoonover's `Solarized <http://ethanschoonover.com/solarized>`__ palette, which I've been using in a variety of documents since I discovered it in 2011.

Solarized is an awesome color scheme with a lot of `cool features <http://ethanschoonover.com/solarized#features>`__, notably a soft contrast and the ability to switch between a light and a dark background with minimal changes. I have plans to create an alternate style sheet based on the dark version of the color scheme, and perhaps a high-contrast version as well: I like the soft tones of Solarized, but the contrast may be insufficient for some people.

Last, since I post content in both English and French, I wanted the browsing experience to be as enjoyable in either language. Not all the content is available in both languages, but I wanted the interface to be fully localized. The theme is therefore written in English, but fully translated and localized into French.


Discovering and experimenting with SASS
=======================================

One of the first things I did for this project was to learn how to use `Sass <http://sass-lang.com/>`__, the CSS extension language, and its associated framework, `Compass <http://compass-style.org/>`__. I read the book |sasscompass|_ by Ben Frain in two days, and started writing Sass files right away. I loved the concept of a CSS preprocessor, because of the modularity and reusability it provided.

.. |sasscompass| replace:: *Sass and Compass for Designers*

.. _sasscompass: http://sassandcompass.com/


Then, I moved on to coding the PHP templates for the different types of pages. Creating the responsive grids and layout was made easy with the `Susy <http://susy.oddbird.net/>`__ framework.


PHP templates
=============

The layout for image posts was a bit challenging, because I wanted to take advantage of the room available on wide viewports while keeping a logical information hierarchy on smaller screens. I also wanted to extract and display some photo-specific information, like photograph metadata (*f*-number, exposure, etc.).

The layout for image posts was also challenging in that it needed to accommodate both landscape- and portrait-oriented pictures. I experimented a bit with `responsive images <http://responsiveimages.org/>`__ and played around with ``<picture>`` and ``src-N``, until it appeared that there was still `no foreseeable consensus <http://html5doctor.com/responsive-images-end-of-year-report/>`__ regarding their implementation in web browsers.


Bootstrap and the path to LESS CSS
==================================

I had completed much of the PHP templates and a reasonable amount of styling when I started working on the header and menus. I thought at first that I'd use a couple of JavaScript libraries to handle the interactive behavior, but I finally settled on moving to `Bootstrap <http://getbootstrap.com/>`__ because it provided most of what I needed. I was already using the icons from `FontAwesome <http://fontawesome.io/>`__, so it made sense to use tools from the same family.

Bootstrap is written in `LESS CSS <http://lesscss.org/>`__, another CSS extension language. I didn't want to maintain CSS in two different languages, so I converted all my SASS files to LESS. I didn't know the LESS syntax at first, but it turned out to be very similar to that of SASS, so switching to it was relatively painless.

I converted the Susy-based grids to Bootstrap's layout system, at first by adding the relevant CSS classes directly to the HTML. This solution felt messy, though, and after a little investigation, I managed to move the Bootstrap grid elements to the CSS by importing the definitions and compiling the stylesheet.


More PHP templates
==================

Once that conversion was done, I finished the header and continued to add the remaining PHP templates, like archive pages and custom page templates. I did a lot of fixing and tweaking, added navigation links, menus, and a custom language switcher for `WPML <http://wpml.org/>`__, the WordPress plugin I use to provide a proper multilingual site. I also looked into theme localization, ``.mo`` and ``.po`` files, and translated and localized the theme's interface.

I usually use a GPS logger when taking pictures, so that I can then correlate the files and geolocalize the pictures by embedding the GPS geographic coordinates into the photo files. To reuse that data automatically, I implemented a feature in the theme that extracts those coordinates, converts them to a human-readable format and displays them on the photo's page; there is also a link to the location on OpenStreetMap based on another coordinates format.


Going live
==========

After some more tweaking and a lot of testing, I eventually enabled Fumseck on this website in mid-December 2013, and it's been working great since then.

Fumseck was my first WordPress theme written from scratch; I had barely done any PHP coding before, and my CSS skills were very limited. There are still plenty of small things I want to fix or improve (such as a better interface for the comments, instead of the one provided by WordPress) but I'm really happy with the result.

I feel this theme is a genuine reflection of my personality and my tastes, and I really enjoy publishing content and navigating the site. I hope you'll find the browsing and reading experience as enjoyable as I do.
