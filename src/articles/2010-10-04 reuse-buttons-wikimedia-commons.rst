.. title: One-click reuse buttons on Wikimedia Commons
.. category: articles-en
.. slug: reuse-buttons-wikimedia-commons
.. date: 2010-10-04 22:11:42
.. template: post_hero.j2
.. tags: Wikimedia
.. keywords: Multimedia usability, UX, Wikimedia Commons
.. image: /images/2010-10-04_Democracy_Memorial_Hall_Summer_2007_0054.jpg

.. figure:: /images/2010-10-04_Democracy_Memorial_Hall_Summer_2007_0054.jpg
   :figclass: lead-figure

   A `photograph <https://commons.wikimedia.org/wiki/File:Democracy_Memorial_Hall_-_Summer_2007_0054.jpg>`__ of the front gate of `Chiang Kai-shek Memorial Hall <https://en.wikipedia.org/wiki/Chiang_Kai-shek_Memorial_Hall>`__ in Taipei that I took when I attended my first annual Wikimania conference, and which I used in some of my design mockups.

.. highlights::

    Our volunteers are awesome. More specifically, Magnus Manske is awesome. He just made reusing pictures from Wikimedia Commons a hundred times easier.

One-click reuse cases
=====================

About a year ago, I created some mock-ups of what the `ideal file description page <http://usability.wikimedia.org/w/index.php?title=File:GPaumier_multimedia_usability_draft_mock-ups_Oct09.pdf&page=6>`__ should look like on Commons. One of my suggestions was to add a series of buttons for `one-click reuse cases <http://usability.wikimedia.org/w/index.php?title=File:GPaumier_multimedia_usability_draft_mock-ups_Oct09.pdf&page=8>`__, to make it easier for people to reuse the more than 7 million files available on Wikimedia Commons.


.. figure:: /images/2010-10-04_page8_MU_mock_ups_Oct09.jpg
   :figclass: framed-img
   :alt: Mock-ups of one-click reuse buttons next to the example image

   One-click reuse cases from the October 2009 draft mock-ups (`Source <http://usability.wikimedia.org/w/index.php?title=File:GPaumier_multimedia_usability_draft_mock-ups_Oct09.pdf&page=8>`__)

These prominent buttons would help users embed the media files in wiki pages, HTML code or simply download the file. If you wanted to include the file in a Wikipedia article, it would provide you with the wikicode for it, so you would only have to copy/paste the code snippet, without having to be a wiki expert. Same thing if you wanted to include the file in an external web page. The "Download" button was an attempt to make the current (and quite frankly, hidden) download link more obvious.


.. figure:: /images/2010-10-04_page10_MU_mock_ups_Oct09.jpg
   :figclass: framed-img
   :alt: Mock-ups of file description pages on Commons with code snippets in the foreground

   Code snippets from the October 2009 mock-ups (`Source <http://usability.wikimedia.org/w/index.php?title=File:GPaumier_multimedia_usability_draft_mock-ups_Oct09.pdf&page=10>`__)


Magnus Manke's "Stock photo" tool
=================================

Last week, `Magnus Manske <http://commons.wikimedia.org/wiki/User:Magnus_Manske>`__ created a small JavaScript piece of code to add a "Stock photo" feature and mentioned it on the `Commons mailing list <http://lists.wikimedia.org/pipermail/commons-l/2010-September/005649.html>`__. Magnus is one of the original developers of `MediaWiki <http://www.mediawiki.org>`__, but nowadays he mostly works on Toolserver and JavaScript tools, especially for Commons.

The tool he wrote was pretty neat, and `User:TheDJ <http://commons.wikimedia.org/wiki/User:TheDJ>`__ and I briefly talked about it on IRC. I also pointed TheDJ to my earlier mock-ups from last year, explaining how the idea was similar.

Today, as I was visiting Commons, I was stunned to see a new version of Magnus' tool, available on all file description pages, that was clearly inspired by my design. You can see for yourself by visiting `any file description page <https://commons.wikimedia.org/wiki/File:Democracy_Memorial_Hall_-_Summer_2007_0054.jpg>`__ on Commons.

.. figure:: /images/2010-10-04_ShareThisCommons.png
   :figclass: framed-img
   :alt: Cropped screenshot of the new file description page on Commons

   Screenshot of the buttons as now implemented on Wikimedia Commons


Apparently, TheDJ pointed to my design in `the discussion on the Village pump <http://commons.wikimedia.org/w/index.php?oldid=44689314#Share_this>`__, Magnus implemented it and the feature was globally enabled on Commons for all users.

I think this is fantastic.

Magnus not only reused my design, but he even made it better by adding the possibility to select the size of the file you want to download or embed.

As we held the :doc:`user experience study <wikimedia-multimedia-ux-testing-videos>` for the prototype upload wizard, our users were really pleased to see similar code snippets at the last stage of the wizard, but they were wondering how to obtain this information again. Until now, they couldn't. Now, anyone can.

We couldn't implement the improved file description pages as part of the Multimedia Usability grant, because we had to focus on `the new upload system <http://blog.wikimedia.org/blog/2010/08/07/prototype-upload-wizard/>`__. I'm really thrilled to see volunteers taking on such tasks, and I'd like to express my deepest gratitude and thanks to Magnus, TheDJ, and more generally all the awesome volunteers who help make our software platform better.

The tool's code is available at `MediaWiki:Stockphoto.js <http://commons.wikimedia.org/wiki/MediaWiki:Stockphoto.js>`__; comments and bug reports can be left on `the talk page <https://commons.wikimedia.org/wiki/MediaWiki_talk:Stockphoto.js>`__.

In a nutshell, reusing media files from Wikimedia Commons just got *a lot* easier; this is really nifty. I imagine it would be great if this feature, along with a few similar others, could be integrated directly into MediaWiki, or into an extension for media repositories to be enabled on Wikimedia Commons.
