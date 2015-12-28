.. title: Temporal evolution of the content & participants of Wikimedia Commons
.. slug: evolution-content-participants-wikimedia-commons-wikipedia
.. date: 2010-03-28 23:57:27
.. tags: Wikimedia
.. keywords: Multimedia usability, Research, Wikimedia Commons
.. image: /images/2010-03-28_content_vs_participants_chart_solarized.png
.. image-caption: Fig. 1: Temporal evolution of the ratio of media files on Wikimedia Commons per active participant (orange squares) and evolution of the ratio of articles on the English-language Wikipedia per active participant (blue triangles).
.. todo: find original SVG files


.. highlights::

    As part of the Multimedia Usability project, I have been doing a lot of research to better understand how Wikimedia Commons is functioning, and particularly to understand its users & participants. One side I am particularly interested in is the demographics and the content dynamics of Commons.


In June last year, I summarized my view with the following comment:

    The main issue of Commons is that it is growing way too fast. This issue is quite unique in Wikimedia projects: when a wiki is growing, it is usually growing because its community is growing. The issue with Commons is that it is a central repository used by almost all the other wikis; many users on Commons are not regular participants there, they only use it to upload pictures for their wiki and they don't involve themselves in the local Commons community, which remains limited. As a consequence, this Commons community doesn't have the human resources to face the workload induced by the growth of the wiki.

    In a nutshell, **Commons' issue is that the wiki is growing faster than its community**.

And apparently, `I wasn't the only one to think so <http://guillaumepaumier.com/2009/06/30/ten-features-that-would-dramatically-improve-wikimedia-commons/comment-page-1/#comment-10>`__. Yet, this statement was only an opinion, and was not based on actual research. My opinion hasn't changed much since then, but now I actually have some data to support this conclusion.


Content and community growth
============================

There has been much interest in the academic world about "Who writes Wikipedia?'' and whether most of the content is contributed by an elite group of participants or by occasional visitors [#]_ [#]_. Roth *et al.* studied the factors influencing wiki viability and noted a "dynamical intertwinement of population and content growth'' [#]_; they had earlier suggested that a wiki's success was linked to "a virtuous demographic path with content and contributors co-evolving" [#]_.

In a media repository like Wikimedia Commons, however, the focus of activity is on contributing new media files, rather than improving the existing ones. Once a file has been uploaded, improvements are mostly limited to metadata and peripheral information (description of the media file, copyright information, general topics, location, etc.); the files themselves are rarely edited. As a consequence, it is particularly interesting to study the dynamics of population & content in this special case. For this purpose, I studied the temporal evolution of the Files-to-active Participants ratio (F:P) and compared it to the Articles-to-active Participants (A:P) ratio on the English Wikipedia (Fig. 1, above). All the data come from `stats.wikimedia.org <http://stats.wikimedia.org>`__.

While the articles-to-participants ratio has remained stable on Wikipedia after the first few years of existence, the files-to-participants ratio has been steadily increasing since the creation of Wikimedia Commons. F\:P has exceeded A\:P since then and is now ten times higher than A:P. This demonstrates that Wikimedia Commons, despite being successful in terms of content, does not follow the usual model of "viable'' or "successful'' wikis, and requires new metrics and new models.

Content inflow management
=========================

Because of the fundamental difference between a text-based encyclopedia and a media repository, a more interesting approach is to compare the capacity of the community of participants to "absorb'' the inflow of new content contributed to the platform. Thus, I studied the temporal evolution of the ratio of persistent new media files uploaded each month, per very active participants on Wikimedia Commons (Fig. 2).

I compared it to the ratio of persistent new articles per very active participants on the English-language Wikipedia. "Persistent'' means that I only counted media files and articles that were not deleted during the patrolling process; the actual number of files uploaded and articles created is higher. I chose to consider only very active participants (more than 100 edits per month) since they are the more likely participants to engage into patrolling activities, such as checking newly uploaded files or newly created pages.

.. figure:: /images/2010-03-28_content_inflow_commons_enwp.png

    Fig. 2: Temporal evolution of the ratio of persistent new media files on Wikimedia Commons per very active participant (orange squares) and evolution of the ratio of persistent new articles on the English-language Wikipedia per very active participant (blue triangles).

The ratio of persistent new media files per very active participants has doubled since the creation of Wikimedia Commons and still continues to increase. This ratio is now more than ten times higher than the one for articles on the English-language Wikipedia. **Because of this imbalance between the growth of the content and the growth of the community, Wikimedia Commons faces a peculiar challenge.**


Using appropriate tools
=======================

Some may argue that comparing uploads and the creation of new pages is like comparing apples and oranges; I agree to some extent. For this reason, I have also studied the evolution of the number of edits on the English Wikipedia, which may be a better indicator of the inflow the community has to absorb. This will be the subject of an upcoming article.

The MediaWiki software provides various maintenance and patrolling tools that allow participants to check newly contributed content; one of these tools is the "watchlist'', a personal page listing the recent changes made to pages of interest selected by each participant. Watchlists are appropriate for text-based wikis like Wikipedia where participants want to check new edits to existing pages, rather than new pages.

However, maintenance activities on Wikimedia Commons mainly consist of checking new files (especially their copyright status) and classifying them appropriately. For this purpose, the usefulness of the watchlist is limited. Some ad-hoc tools have been developed by power participants, but **MediaWiki does not provide dedicated features to help the limited community of participants absorb the inflow of new media files**. This is where the `Multimedia Usability project <https://guillaumepaumier.com/tag/multimedia-usability/>`__ can step in.

.. [#] \E. H. Chi, N. Kittur, B. Pendleton, and B. Suh. `Long tail of user participation in Wikipedia <http://asc-parc.blogspot.com/2007/05/long-tail-and-power-law-graphs-of-user.html>`__.

.. [#] \R. Priedhorsky, J. Chen, S. T. K. Lam, K. Panciera, L. Terveen, and J. Riedl. Creating, destroying, and restoring value in Wikipedia. In *GROUP’07: Proceedings of the 2007 international ACM conference on Supporting group work*, pages 259–268, New York, NY, USA, 2007. ACM. (`PDF <http://www-users.cs.umn.edu/~reid/papers/group282-priedhorsky.pdf>`__, 250KB)

.. [#] \C. Roth, D. Taraborelli, and N. Gilbert. Measuring wiki viability. An empirical assessment of the social dynamics of a large sample of wikis. In *Proceedings of the 4th International Symposium on Wikis - WikiSym2008*, New York, NY, USA, 2008. ACM. (`PDF <http://epubs.surrey.ac.uk/cgi/viewcontent.cgi?article=1021&context=cress>`__, 311KB)

.. [#] \C. Roth. Viable wikis: Struggle for life in the wikisphere. In *WikiSym’07: Proceedings of the 2007 international symposium on Wikis*, pages 119–124, New York, NY, USA, 2007. ACM. (`PDF <http://www.patres-project.eu/images/4/47/ViableWikis.pdf>`__, 334KB)
