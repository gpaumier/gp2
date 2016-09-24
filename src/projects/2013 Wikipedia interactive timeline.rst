.. title: Wikipedia 2013 timeline
.. category: projects-en-featured
.. slug: wikipedia-2013-timeline
.. date: 2013-12-20T00:00:00
.. end: 2014-01-10T00:00:00
.. image: /images/2014-01-10_Wikipedia-timeline-2013-screenshot.png
.. roles: researcher, writer
.. keywords: Wikimedia, Wikipedia, timeline

.. highlights::

    An illustrated interactive timeline that highlights the main and coolest stories about what happened on Wikipedia and across the Wikimedia movement in 2013.


`Open the timeline » <http://guillaumepaumier.com/timelines/wikipedia-in-2013/>`__
==================================================================================

I love timelines. They present facts in a logical, natural way and are a great tool for looking at the past and understanding how it has brought us to where we are now.

It's difficult to look back at recent events with enough hindsight; however, documenting what is happening is something that ought to be done while it's still fresh in the collective memory. It's also nice to look back at what we've recently accomplished once in a while.

Some time in 2013, I stumbled upon the `TimelineJS <https://github.com/NUKnightLab/TimelineJS>`__ tool, a JavaScript library that generates interactive timelines. I liked it, but didn't immediately think of using it. In December, as I was looking back at what had happened in Wikimedia engineering during the year, I thought this tool could be a great way to showcase what had happened throughout the Wikimedia movement in 2013.

The easiest way to create a timeline with TimelineJS is to prepare a spreadsheet containing all the data in Google docs, generate the timeline `on the Knightlab site <http://timeline.knightlab.com/#make>`__ and embed it from there into your web page. This approach is straightforward and allows people without too much technical knowledge to use the tool, but it also has a number of drawbacks, notably its reliance on multiple third-party tools, and the possible leakage of personal visitor information to those sites.

I chose instead to host the timeline myself, including all the images, and to prepare the data in a local JSON file. Getting started was easy; I set up the `repository on GitHub <https://github.com/gpaumier/timelines>`__, and soon faced the real challenge, which wasn't technical: selecting the stories to feature in the timeline.


Editorial selection
===================

I started from the postulate that most of the newsworthy and cool stories would have been featured on the `Wikimedia blog <https://blog.wikimedia.org>`__, and started going through the archives for 2013. It was neither possible nor desirable to include them all, so I made a pre-selection that I then refined little by little until there were about 30 items.

I had to leave out many stories, and not all stories were featured on the blog either. But I was happy with the selection, that I felt provided a good overview of the activities of the Wikimedia movement.

Then, I started adding them to the JSON file. Each entry required:

-  the date(s) of the story;
-  a headline;
-  a short summary;
-  a picture to illustrate the story;
-  the caption and credit line for the picture;
-  a thumbnail for the bottom slider (32 × 32 pixels).

I tried to sort the items by tag, but eventually decided against it. You can use up to six tags, and for them to make sense in the timeline I would have needed all six, but that resulted in truncated headlines in the bottom slider. Additionally, that slider was more readable when the stories weren't grouped by tags.

It took a fair amount of time and imagination to craft the headlines, so that they would still make sense in the space-constrained bottom slider. That bit was even more challenging when I translated the timeline to French, which is a more
verbose language than English.

Most of the stories were easy to illustrate, even though I had to recreate or edit many of the screenshots, either to ensure proper quality or to visibly highlight a specific part of the interface. The thumbnails were another challenge, because it's difficult to create a recognizable 32 × 32 image. But I carefully crafted thumbnails for each picture, and I was happy with the results.

Last, I wrote `detailed credits <https://github.com/gpaumier/timelines/blob/gh-pages/wikipedia2013/CREDITS.md>`__ for the media assets included in the timeline, in order to complement the basic credit line present near each media file.


Integrating the timeline
========================

All this work was initially done in a simple standalone HTML page that displayed the timeline in the full viewport. It was fine, but if possible I wanted to integrate it properly into the structure and appearance of the rest of the site.

TimelineJS uses LESS to write and compile CSS files, so I started looking at the source files. I had learned to write in LESS a couple of weeks before when I had built the `Fumseck theme <//guillaumepaumier.com/project/fumseck/>`__, so it felt familiar. I edited the files to use the Solarized color scheme, Latin Modern typefaces and a larger font size, to be consistent with that theme. I tried to change the original files as little as possible, and refer to the unmodified sources when possible while compiling, in order to lower the maintenance costs if the library needs to be upgraded in the future.

Finally, I created a custom page template for the WordPress theme that would allow me to embed the timeline using the full width of the viewport.

The final extra step was the translation and localization of the timeline to French. Even if the links to the full stories were in English, I thought French readers might still appreciate viewing the timeline itself. I translated the headlines, summaries, captions and credit lines, and created `a French copy of the timeline <//guillaumepaumier.com/fr/frises/wikipedia-en-2013/>`__ in WordPress.

I'm really quite happy with the result, and the feedback has been overwhelmingly positive. I'm glad people have enjoyed navigating the timeline as much as I did building it.

A few colleagues have asked if the TimelineJS could be used to replace or complement the `aging timeline tool <https://www.mediawiki.org/wiki/Extension:EasyTimeline>`__ currently in use on Wikipedia. I'm not sure it's robust enough to survive Wikipedians, but I do hope that we'll eventually find a nice way to present chronologies within Wikipedia pages, perhaps using dates from Wikidata entries. It will make Wikipedia entries more interactive, and will also make it easier to document our own shared history.

.. class:: copyright-notes

    Photo shown in the screenshot of the timeline: |Pumpkipedia|_ by `Ed Sanders`_, under `CC-BY-SA 3.0`_. Wikipedia logo: ™ Wikimedia Foundation.

.. |Pumpkipedia| replace:: *Pumpkipedia*

.. _Pumpkipedia: https://commons.wikimedia.org/wiki/User:ESanders_%28WMF%29/Pumpkipedia

.. _Ed Sanders: https://commons.wikimedia.org/wiki/User:ESanders_%28WMF%29

.. _CC-BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/legalcode
