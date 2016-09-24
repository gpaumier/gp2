.. title: Wikimedia and MediaWiki bugs, issues, and requests
.. category: articles-en
.. slug: wikimedia-mediawiki-bugs-issues-and-requests
.. date: 2010-03-04 02:26:46
.. tags: Wikimedia
.. keywords: MediaWiki, Engineering, Wikimedia
.. image: /images/2010-03-04_Bug_on_Sunflower_Petal.jpg
.. image-caption: A bug on a sunflower.
.. todo: format URLs and IRC channels


.. highlights::

    Over the past few weeks, I have been thinking about how to improve (or rather, kick off) a more structured way to manage software and product development within the Wikimedia community. The result is a list of ideas and recommendations I have compiled and submitted to the relevant staff members at the Wikimedia Foundation. I am also publishing them here in order to allow for a wider feedback. This article is the first of a series dedicated to this topic.


.. warning::

    The content of this article reflects only my personal opinion and is not an official plan or communication of the Wikimedia Foundation.


Right now, the bug tracker we use is based on Bugzilla and located at `bugzilla.wikimedia.org <http://bugzilla.wikimedia.org>`__. Many major free projects use a generic "bugs" or "issues" prefix or suffix in their URL: `bugs.kde.org <http://bugs.kde.org>`__, `bugs.gentoo.org <http://bugs.gentoo.org>`__, `issues.apache.org <http://issues.apache.org>`__, `www.debian.org/Bugs <http://www.debian.org/Bugs>`__. Some projects use the "bugzilla" prefix like we currently do, like `bugzilla.gnome.org <http://bugzilla.gnome.org>`__. The latter is an example of a choice based on the implementation model: the name reflects the technical implementation of the bug tracker, not its actual purpose. A better name would be closer to the user model and describe the actual goal of the platform: to report and manage bugs and issues related to a specific project. If we do change our tracker, the current name will have to change too, because it is specific to a given tool.

**Recommendation: Use a generic descriptive prefix rather than one based on the tool we use.**


Wikimedia & MediaWiki
=====================

Another current issue is the confusion caused by the similar names used for the organization (Wikimedia) and the software (MediaWiki). A good example of this confusion is the number of MediaWiki users who join the `#wikimedia <irc://irc.freenode.net/wikimedia>`__ IRC channel instead of `#mediawiki <irc://irc.freenode.net/mediawiki>`__ to ask for software support. The confusion is even worsened by the fact that we have a unique bug tracker located at `bugzilla.wikimedia.org <http://bugzilla.wikimedia.org>`__, dealing with issues related to both Wikimedia websites *and* the MediaWiki software.

There are obviously strong ties between Wikimedia projects and MediaWiki: all Wikimedia projects use the MediaWiki software, and the MediaWiki software is primarily developed with Wikimedia projects in mind. However, there is also a growing community of MediaWiki users who are not Wikimedia users and we should provide them with tools relevant to them. This might be for instance a support forum dedicated to MediaWiki users.

Wikimedia projects and MediaWiki are separate products and they should be acknowledged as such: as a consequence, **the separation between bugs in the MediaWiki software, and Wikimedia-specific operations & configuration requests should be made more explicit**. Obviously, we would prefer to have a unique back-end to support both sites, particularly to be able to move bugs and requests from one platform to another, but this is easily configurable. Possible names could be `dev.mediawiki.org <http://dev.mediawiki.org>`__ and `tech.wikimedia.org <http://tech.wikimedia.org>`__; both are currently unused. They are pretty wide prefixes, because we may host a real project management platform there, rather than just bug trackers.

**Recommendation: Offer two different public-facing platforms for MediaWiki- and Wikimedia-related issue tracking.**


Read also in this series
========================

-  `Wikimedia User experience programs: a systematic approach <http://guillaumepaumier.com/2010/03/04/wikimedia-user-experience-programs/>`__
-  `Scaling up Software development for Wikimedia websites (Part I: Human resources) <http://guillaumepaumier.com/2010/03/04/scaling-up-software-development-for-wikimedia-websites-human-resources/>`__
-  `Scaling up Software development for Wikimedia websites (Part II: Tools) <http://guillaumepaumier.com/2010/03/05/scaling-up-software-development-for-wikimedia-websites-tools/>`__


.. class:: copyright-notes

    |bug|_ by `Ryan Poplin`_, under `CC-By-SA`_, from flickr.

.. |bug| replace:: *Bug on Sunflower Petal #1*
.. _bug: https://commons.wikimedia.org/wiki/File:Bug_on_Sunflower_Petal_-1_%282725390020%29.jpg

.. _Ryan Poplin: https://www.flickr.com/people/27446776@N00

.. _CC-By-SA: https://creativecommons.org/licenses/by-sa/2.0/legalcode
