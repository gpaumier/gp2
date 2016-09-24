.. title: Wikimedia Commons gets user galleries
.. category: articles-en
.. slug: wikimedia-commons-user-galleries
.. date: 2011-03-16 11:54:49
.. tags: Multimedia usability, UX, Commons, Engineering, Wikimedia
.. image: /images/2011-03-16_myuploads.png

.. highlights::

    A long-awaited feature has just been added to Wikimedia Commons by volunteer developer Bryan Tong Minh.

I just found out that a long-awaited feature for Wikimedia Commons had been enabled a few weeks ago. I'm talking about user galleries, i.e. the ability to list recent uploads by a user to a MediaWiki-powered wiki.

As if often happens, such a tool has been `available on the toolserver <http://toolserver.org/~daniel/WikiSense/Gallery.php>`__ for years (`see an example <http://toolserver.org/~daniel/WikiSense/Gallery.php?wikifam=commons.wikimedia.org&img_user_text=Guillom>`__), and a link to this tool was added to the default Commons interface for user pages.

Nonetheless, a "user gallery" feature built in MediaWiki, similar to `the list of one's edits <http://commons.wikimedia.org/wiki/Special:Contributions/Guillom>`__, was still missing. We `touched the subject <http://usability.wikimedia.org/wiki/Multimedia:User_gallery>`__ during the `Multimedia usability project <http://meta.wikimedia.org/wiki/Multimedia_usability_project_report>`__, but we had to focus on the uploader.

A `feature request <https://bugzilla.wikimedia.org/show_bug.cgi?id=3341>`__ was opened in our bug tracker back in 2005. This morning, while reading my `bugmail <http://en.wiktionary.org/wiki/bugmail>`__, I saw a notification about this bug, saying the feature had been added in 2010 and deployed recently.

It turns out it was added by `Bryan Tong Minh <http://www.mediawiki.org/wiki/User:Bryan>`__, a MediaWiki developer particularly active in multimedia features; he's also the one who wrote the `GlobalUsage extension <http://www.mediawiki.org/wiki/Extension:GlobalUsage>`__ a few years ago, which provides a list of all the pages around Wikimedia sites where a file is included.

It was already possible, in MediaWiki, to list files (in reverse-chronological order) through the `Special:ListFiles <http://commons.wikimedia.org/wiki/Special:ListFiles>`__ special page. Bryan added the ability to filter this list by user, effectively creating a user gallery (`r65013 <http://www.mediawiki.org/wiki/Special:Code/MediaWiki/65013>`__). He then added thumbnails to the page (`r75582 <http://www.mediawiki.org/wiki/Special:Code/MediaWiki/75582>`__). The feature was enabled on Wikimedia sites (including Commons) as part of the `deployment of MediaWiki 1.17 <http://techblog.wikimedia.org/2011/02/main-deployment-of-mediawiki-1-17-to-wikimedia-sites-complete/>`__.

So, it is now possible to see the gallery of uploads by a certain user (`see an example <http://commons.wikimedia.org/wiki/Special:ListFiles/Guillom>`__). Want to see your gallery? Go to `Special:MyUploads <http://commons.wikimedia.org/wiki/Special:MyUploads>`__. Neat, heh?

The gallery is also accessible through the small "uploads" link at the top of `your contributions list <http://commons.wikimedia.org/wiki/Special:MyContributions>`__.

This feature is a *huge* step forward in terms of usability. During our interviews & testing, most people were wondering where their uploads had gone once the upload was completed. I'd like to thank Bryan, and all our awesome volunteers, for their work in making MediaWiki better.

The next step will probably be to add a shortcut to the gallery in the user's top-right menu, as well as in the "Toolbox" menu in the sidebar. Maybe not on all wikis, but it would definitely be useful on Commons.

Further improvement could include the prettification of the page, `perhaps similarly to Flickr <http://www.flickr.com/photos/gpaumier/page2/>`__, and the possibility to get the code to insert the image in a wiki page, as we do at the last step of the `Upload wizard <http://blog.wikimedia.org/blog/2010/11/30/upload-wizard-launches-beta-wikimedia-commons/>`__.

Actually, once that is done, we could pretty much replace the last step of the upload wizard by the gallery page, only with a thank-you message at the top. What do you think?
