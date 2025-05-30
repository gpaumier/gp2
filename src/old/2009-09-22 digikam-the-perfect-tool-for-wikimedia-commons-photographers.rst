.. title: digiKam, the perfect tool for Wikimedia Commons photographers?
.. category: articles-en
.. slug: digikam-the-perfect-tool-for-wikimedia-commons-photographers
.. date: 2009-09-22 16:32:44
.. tags: Wikimedia
.. keywords: digiKam, KIPI, metadata, Wikimedia Commons, KDE, Photo

.. highlights::

    Because digiKam provides the tools and Commons the problems, the two should enjoy a happy marriage.


For several years now, I have been a photographer for Wikimedia Commons. Commons is actually the reason why I became interested in photography, and why I bought a DSLR camera and various lenses. And I have ended up taking *a lot* of pictures. The problem when you take a lot of pictures is that the time you need then to process and upload them grows exponentially. Besides, if you want to upload your pictures to several platforms (say, Commons, flickr and your blog), you have to deal with the specifics of each website. It would be much simpler and faster to describe, tag, classify, geotag the pictures only once (using an appropriate batch-editing tool) and then to have each website extract the metadata, or to use an upload tool that extracts them automatically.

Wikimedia Commons
=================

So, on the one hand, you have `Wikimedia Commons <http://commons.wikimedia.org>`__, a repository of freely-licensed multimedia files (photos, maps, diagrams, sounds, videos, etc.). It is a project of the Wikimedia Foundation, from which uploaded files can be used across all Wikimedia projects in all languages, including the famous encyclopedia Wikipedia. Wikimedia Commons contains over 5 million files, the overwhelming majority of which have been contributed by volunteers. Such a large amount of files makes it mandatory to properly:

-  describe what each work is about
-  identify the author and the copyright status of each work
-  classify each work in order to be able to find it later and to manage such a large collection.

Besides these requirements, it is also considered a good practice to `geotag your pictures <http://commons.wikimedia.org/wiki/Commons:Geocoding>`__ (if applicable), i.e. to indicate the geographical location of where the picture was taken.

digiKam
=======

On the other hand, there is `digiKam <http://www.digikam.org>`__, a `FLOSS <http://en.wikipedia.org/wiki/Free_and_open_source_software>`__ "`digital asset management <http://en.wikipedia.org/wiki/Digital_asset_management>`__\ " application whose special features allows to annotate, classify and catalogue a large media library, although it provides some very handy editing and post-processing tools as well. digiKam uses the `KIPI plugins <http://www.kipi-plugins.org>`__, which provide handy features such as batch editing or export modules to a variety of websites, including `Flickr, Picasa and Facebook <http://maketecheasier.com/use-digikam-export-photos-flickr-picasaweb-and-facebook/2009/09/14>`__. The 4th beta release of digiKam 1.0 was `recently released <http://www.digikam.org/drupal/node/477>`__ and the official 1.0 release is `planned for late October <http://www.digikam.org/drupal/about/releaseplan>`__ this year. I won't go through `digiKam's impressive list of features <http://www.digikam.org/node/341>`__; instead, I will focus on those that make digiKam a very powerful tool for Wikimedia photographers.

The perfect combination?
========================

So let's take a quick look at the features digiKam offers that would be handy for people who want to contribute their pictures to Wikimedia Commons:

+-------------------------------------+----------------------------------------+
| *Commons requires or recommends...* | *digiKam offers...*                    |
+-------------------------------------+----------------------------------------+
| copyright information (author and   | full metadata read/write support,      |
| license)                            | including Author and Copyright fields  |
+-------------------------------------+----------------------------------------+
| multilingual descriptions for each  | multilingual descriptions since        |
| file                                | digiKam 1.0, with appropriate language |
|                                     | codes                                  |
+-------------------------------------+----------------------------------------+
| classification with hierarchical    | classification with hierarchical tags  |
| categories                          |                                        |
+-------------------------------------+----------------------------------------+
| geotagging [#]_                     | geotagging (automatically using GPS    |
|                                     | data or manually using Google Earth)   |
+-------------------------------------+----------------------------------------+

So, what's missing? Well, you can do a lot of stuff with digiKam to prepare your pictures before they're uploaded to Commons. Yet, you still have to upload them manually, or using an external tool such as Commonist. And even if you have been spending days to annotate your pictures, describe them in several languages, geotag them, etc., well, all this information remains in the image metadata. Neither Commonist nor MediaWiki knows how to extract these metadata meaningfully (yet); as a consequence, you have to redo all the work when uploading each file to Wikimedia Commons. The Ford Foundation recently `awarded a $300,000 grant <http://wikimediafoundation.org/wiki/Press_releases/Wikimedia_Ford_Foundation_Grant_July_2009>`__ to the Wikimedia Foundation in order to improve the usability of the upload process. I expect some work will be done regarding the extraction of metadata from files. Yet, when uploading a large number of files, it would be more convenient to provide a standalone desktop upload tool like Commonist. Or...

What would really be neat is *an integrated export module to Wikimedia Commons in digiKam*; not only would it serve as a batch upload tool, but it would also read all the metadata and create the file description pages accordingly. A few weeks ago, I contacted the main developer of digiKam in order to discuss the possibility of implementing such an export module. He showed interest in this project even if he didn't have the time to code it himself. As a consequence, I have initiated a `roadmap and brainstorming page for the plugin <http://commons.wikimedia.org/wiki/User:Guillom/KIPI>`__. Feel free to contact me if you're interested in helping implement such a plugin.


.. [#] I recently noticed a `JavaScript tool allowing users to geotag themselves <https://commons.wikimedia.org/wiki/Commons:Geocode_Users?withJS=MediaWiki:Geocode_Users.js>`__, using a map from OpenStreetMap. This is exactly the kind of tool I would like to have for pictures; I can't understand why it exists for users, but not for media files.
