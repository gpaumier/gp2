.. title: Ten features that would dramatically improve Wikimedia Commons
.. category: articles-en
.. slug: ten-features-that-would-dramatically-improve-wikimedia-commons
.. date: 2009-06-30 12:22:30
.. tags: Wikimedia
.. keywords: MediaWiki, metadata, UX, Wikimedia Commons, Design


.. highlights::

    Where our hero makes an early Christmas wishlist and implores the developer fairies to give Wikimedia Commons some much-needed love.


MIT's *Technology Review* recently published an article about `improvements to come regarding the management of video content <http://www.technologyreview.com/web/22900/page1/>`__ on Wikipedia and Wikimedia websites. I heard a lot of people say: "Good, but what about pictures?" Some technical improvements described by the *Technology Review* will be useful for both images and videos, such as the `media and upload wizard <http://techblog.wikimedia.org/2009/03/add-media-wizard-and-firefogg-on-testwikipediaorg/>`__ currently developed by Michael Dale. However, Wikimedia Commons still needs many little (or big) features that would dramatically improve its user-friendliness.

Browsing & reusing
==================

#. **Automatic localization**: Websites such as Wikimedia Commons and meta-wiki host content in various languages and have a multilingual audience. These multilingual wikis should automagically `detect the locale of the user's browser <http://blog.notanendive.org/post/2008/09/25/I-don-t-spreche-Deutsch-merci-beaucoup>`__ and use it as language of the interface, especially for unregistered users. As for users with an account, their browser's locale should be set as the default language in their preferences.
#. **Usage-centric page layout**: It's all very nice to know that such image is a "retouched picture" or that such diagram was "made using Inkscape." But I think what most of the users want to know is: how to use the picture (in Wikimedia projects or elsewhere) and how to download it (using the best resolution available). Many people use the right-click-save-as method to save pictures from the Internet. If they do that on Commons, they will only save the low-resolution preview. There should be a big button « Download high-res », as well as snippets of code to embed a file with proper attribution.

Metadata
========

Full metadata support is the cornerstone of many other features. EXIF is probably the most known type of metadata, but there are also others such as IPTC or XMP.

3. **Pull metadata from files on upload**: this idea is not a new one, yet it hasn't been implemented. A fair amount of photographers add a lot of metadata to their files: author, description, copyright information, geotags, keywords, etc. and it is extremely cumbersome to have to redo all the work by hand during the upload.
4. **Store metadata in a database** to make search and attribution easier, especially: description, license, media type (photo, diagram, map, etc.). It should be connected to the MediaWiki API to allow for easy extraction of these data.
5. **Push metadata to files on download**: In the field of publishing, storing credit information directly into the file's metadata is strongly recommended and is a standard practice to avoid losing track of it.

.. sidebar::
   Related open bugs:

   -  `bugzilla:6672 <https://bugzilla.wikimedia.org/show_bug.cgi?id=6672>`__: EXIF orientation not used (rotation from digital cameras)
   -  `bugzilla:3361 <https://bugzilla.wikimedia.org/show_bug.cgi?id=3361>`__: Image author, description, and copyright data saved in EXIF fields
   -  `bugzilla:16956 <https://bugzilla.wikimedia.org/show_bug.cgi?id=16956>`__: Show IPTC metadata on image description page
   -  `bugzilla:657 <https://bugzilla.wikimedia.org/show_bug.cgi?id=657>`__: Pull copyright metadata from files on upload
   -  |11484|_: Include ISO rating in abbreviated exif metadata.

.. role:: strike
    :class: strike

.. |11484| replace:: :strike:`bugzilla:11484`
.. _11484: https://bugzilla.wikimedia.org/show_bug.cgi?id=11484

Editing
=======

6. Built-in **basic editing features** (lossless rotate, crop) and ability to save under another name (i.e. for crops). Similarly, a built-in **geocoding feature** using OpenStreetMap. `Geocoding <http://commons.wikimedia.org/wiki/Commons:Geocoding>`__ images means attaching geographic information about the place where the work was made. This may be made easier by the `current initiative to integrate OpenStreetMap <http://techblog.wikimedia.org/2009/04/openstreetmap-maps-will-be-added-to-wikimedia-projects/>`__ with Wikimedia projects. And of course it should save the coordinates as metadata.

Rating
======

7. Some sort of community-managed **rating feature**; as someone said elsewhere, "Commons is a depository, and depositories are expected to host lots of junk." A rating feature would allow the best of Commons to be presented first during the search, and junk to be presented last.

Searching
=========

With currently more than 4.6 million files (and counting), it is becoming increasingly important to improve the search features of Wikimedia Commons.

8.  **An "advanced search" feature** similar to `flickr's <http://www.flickr.com/search/advanced/?>`__. It should be possible to search by media type, by license, and to add toggles such as "safe mode" (explicit content) or "personality rights."
9.  **Multilingual search**: Files on Commons are ordered in hierarchical categories, using English as *lingua franca*. If you want to find a file, you have to search in English. I imagine it is possible to use some dictionary (coupled to the language detection) to give good results for a search in any language.
10. **Google-Images-friendliness**. A lot of people use Google Images to find pictures, but images from Wikimedia Commons rarely appear in these results (unless they are used on a Wikipedia page).
