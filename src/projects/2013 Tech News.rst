.. title: Tech news
.. category: projects-en
.. subtitle: the Wikimedia technical newsletter
.. slug: wikimedia-tech-news
.. date: 2013-05-16T00:00:00
.. end: 2015-08-17T00:00:00
.. image: /images/2013-12-16_Tech_news_process_-_Overview.svg
.. roles: writer, project lead
.. keywords: Wikimedia, Engineering, Wikipedia, writing, translation, technology, technical communication

.. highlights::

    Every week, tech ambassadors assemble, simplify and translate “Tech News”, a curated newsletter then delivered to hundreds of subscribers across wikis. But how exactly did this start, how does it work behind the scenes, and how does it fit within our efforts to bring developers and users closer together?


Wikimedians, the tens of thousands of volunteers [#]_ who write and improve articles on Wikipedia and its sister sites, do not like to encounter software bugs and other changes that prevent them from curating the sum of all human knowledge. Quite understandably, they regularly complain that they were not notified of a specific change or new feature that `broke their workflow <http://www.xkcd.com/1172/>`__. It's a perennial topic, and it's generally brought up independently every few months; the latest occurrence happened in December [#]_.

And yet, in a movement as transparent as Wikimedia, where almost every document, code change and mailing list is public, the problem is rarely the lack of information. Anyone can look at the more than 5,000 `code changes <https://gerrit.wikimedia.org>`__ made on average by developers every month [#]_; anyone can also contribute to the more than 1,200 `issues <https://bugzilla.wikimedia.org>`__ opened every month [#]_, or read (and reply to) the more than 1,500 mailing list messages that they exchange [#]_. I'm not even mentioning `code reviews <https://www.mediawiki.org/wiki/Git/Tutorial#How_we_review_code>`__, real-time `IRC chat <https://meta.wikimedia.org/wiki/IRC/Channels#MediaWiki_and_technical>`__ or edits to the documentation on `mediawiki.org <https://www.mediawiki.org/wiki/>`__, all of which are also public.

No, the problem is rarely that information is kept private; in a situation quite representative of our time, Wikimedians who want to follow technical changes are faced with `information overload <https://en.wikipedia.org/wiki/Information_overload>`__. We know the information we're looking for is out there; the problem is how to find it without being overwhelmed, and how to find it before it has consequences for us.


Technical ambassadors: The first attempt at a 2-way communication line between developers and editors
=====================================================================================================

As I mentioned, the problem isn't new. I'll assume that it's been here all along, since Wikipedia was created in 2001, and continued as the site underwent major rewrites of its software [#]_ and frequent outages that only the most long-term editors still recall. That said, the problem became more apparent when the Wikimedia Foundation really started to have the resources to make major software changes. This was in 2008, when the Foundation was awarded a grant by the Stanton Foundation to finance the "Wikipedia Usability Initiative," with the goal of improving the software to make it easier to contribute to the encyclopedia [#]_.

The Wikipedia Usability Project is what brought the now familiar `"Vector" look <https://blog.wikimedia.org/2010/05/13/a-new-look-for-wikipedia/>`__ to Wikipedia, as well as the then-new `editing toolbar <https://blog.wikimedia.org/2010/03/25/wikimedia-gets-ready-for-some-big-changes/>`__. These were the biggest changes to Wikipedia's interface in a long time, and the Usability team knew that they needed to find a way to communicate with editors across wikis. Besides direct on-wiki discussions and blog posts, they created a new mailing list in August 2010, called "`wikitech-ambassadors <https://lists.wikimedia.org/mailman/listinfo/wikitech-ambassadors>`__"; its purpose was to allow interested Wikimedians to be notified of major technical changes, act as an ambassador to their home wiki (initially the long-tail wikis), and report back issues and concerns to the list. The ambassadors list was low-traffic: subscribers wouldn't get as many e-mails as on the general technical list, `wikitech-l <https://lists.wikimedia.org/mailman/listinfo/wikitech-l>`__. The list also had an explicit focus on users, meaning it wasn't necessary to have specialized technical knowledge to participate.

Deputizing volunteer ambassadors was a great way to scale two-way communication to hundreds of wikis. But while a noble effort, the mailing list wasn't as successful as hoped. Few editors joined the list, and much of the communication still had to be done by the Usability team through blog posts (which were unidirectional and didn't reach as many Wikimedians) or directly on the wikis.

.. figure:: /images/2014-01-02_Wikitech-ambassadors_stats.svg

    The wikitech-ambassadors mailing list was used episodically in 2010−2011; its usage started to increase in 2012.


The wikitech-ambassadors list continued to be used very episodically throughout 2010 and 2011 for one-off announcements [#]_. Around Summer 2012, I started experimenting with ways to improve the 2-way communication between users and developers. At the time, there wasn't a lot of dialogue on the ambassadors list; it was a low-traffic, mostly-announce list for developers talking to Wikimedia users [#]_. Since then, we've partly managed to turn it into a medium-traffic list for discussion between developers and Wikimedia users, to report issues, share ideas and provide feedback.


Beyond ambassadors: The genesis of the technical newsletter
===========================================================

The membership and activity of the ambassadors list started to increase in 2012, and continued in 2013, to reach about 200 members (as of December 11, 2013), among which roughly 15% are Wikimedia Foundation employees [#]_. This is a level that is honorable, but still far from ideal, especially when considering that many subscribers, I reckon, are interested in getting the news, but not necessarily in acting as an ambassador to their wiki. Moreover, it requires extra effort for developers to explicitly advertise a technical change on the list. Even if they remember and are willing to do it, the ambassadors list (unlike wikitech-l) isn't part of their usual workflow.

Then, there is also the "`Not my wiki <https://meta.wikimedia.org/wiki/Not_my_wiki>`__" problem, summarized as: "People prefer to work on their home wiki. Other wikis seem much further than just a single click away." For users, subscribing to the ambassadors mailing list requires a much bigger perceived effort than just getting the information on their wiki. We needed to find a way to reach editors in their own environment.

In Fall 2012, I started a set of `on-wiki consultations <https://www.mediawiki.org/wiki/Technical_communications/Fall_2012_consultation>`__ to ask editors how they thought we could collectively improve the dialogue between users and developers. One of the major proposed solutions was to "communicate more widely, but on less stuff. Only select activities and changes likely to interest the audience. For example, select deployment changes likely to impact editors, and have them translated and delivered across all wikis. Augment with specific notices for particularly important/urgent/attention-worthy messages." [#2012consult]_

There were already some local initiatives doing this on a couple of wikis: the `English Wikipedia Signpost <https://en.wikipedia.org/wiki/en:Wikipedia:Wikipedia_Signpost>`__'s Technology report, and the German Wikipedia's |Projektneuheiten|_ had both been keeping an eye on technical changes, and notifying their readers of what could impact them. However, those community newspapers were specific to their local wiki; there was also a lot of scattered and duplicated effort between their writers. In March 2013, I started a discussion to gauge interest in pooling resources [#]_, which led to the creation of the tech newsletter.

.. |Projektneuheiten| replace:: *Projektneuheiten*

.. _Projektneuheiten: https://en.wikipedia.org/wiki/de:Wikipedia:Projektneuheiten


Setting up Tech News
====================

I created the `Tech/News <https://meta.wikimedia.org/wiki/Tech/News>`__ page in May 2013, with the explicit goal of inviting contribution and making it easy to participate, even in a come-and-go fashion. The `first newsletter <https://meta.wikimedia.org/wiki/Tech/News/2013/21>`__ was ready a few days later. Because it was the first issue, I advertised it to all Wikimedia wikis by globally distributing it to their local discussion page. Readers were invited to subscribe individually to receive the next issues; it was also possible to subscribe a community discussion page where the newsletter would be posted for editors to read every week. There was a surge of subscriptions following that announcement; readership has been steadily increasing since then, in a process that (I suppose) involves editors discovering the tech newsletter when it's posted on other people's talk page.


.. figure:: /images/2014-01-02_Technews_screen.png
    :class: framed

    The Tech/News page provides clear calls to action and pointers on how to subscribe and participate.


I wasn't alone in this initiative. From the beginning, `Tomasz W. Kozlowski <https://meta.wikimedia.org/wiki/User:Odder>`__ participated in writing the newsletter, and he would go on to become the primary writer until August. He's also the one who originally consolidated our habits and experience into the `Tech news manual <https://meta.wikimedia.org/wiki/Tech/News/Manual>`__, which has served as a checklist for writing and publishing the newsletter every week. In fact, I came to rely so much on his work that, when Tomasz decided to take a well-deserved wikibreak, the newsletter went on a hiatus, then returned to its regular publication schedule.

In June, when we officially announced the tech newsletter, only a few issues had been published, but readers were already showing their appreciation, and its content was already being used by the Signpost writers to put together their own Tech report. [#]_


.. figure:: /images/2013-12-16_Tech_news_subscribers_2013-W21_to_2013-W51.svg

    The number of subscribers surged when the newsletter was announced, showing that it was meeting a real need from Wikimedians. It has been steadily increasing since then.


Keeping it simple
=================

One of the things we realized while writing the first issues of the newsletter was that we needed to translate a lot of the technical jargon into plain English. Our audience is primarily composed of Wikimedia editors who, even if they have encyclopedic knowledge of copyright law and can build wiki templates that make coffee, aren't necessarily familiar with the terminology and concepts used in software development or system administration of web servers. Therefore, we have to stay clear of specialized technical vocabulary, use paraphrases where needed and explain complex concepts.

.. figure:: /images/2013-12-16_Tech_news_process_1_-_Monitoring_and_writing.svg

    Tech ambassadors monitor technical activity across many channels, select noteworthy information and simplify it to make it accessible to readers who don’t have specialized technical expertise.


Using simple language is also a requirement as we cater to a multilingual audience. Many Wikimedians who read the newsletter aren't native English speakers, so it's easier for them if we keep the text simple and avoid colloquialisms.

There is of course a balance to strike between understandability in layman's terms and technical accuracy, but I think we've managed to accomplish one without sacrificing the other. I've recently compiled some `readability metrics <https://meta.wikimedia.org/wiki/Tech/News/Readability>`__ to help assess how we were doing in a slightly more rigorous manner than gut feeling. The mean `Flesch-Kincaid reading ease <https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests>`__ score for all past issues of the tech newsletter is about 56, which apparently isn't too bad for a technical publication, even if we're not yet at the `Up-Goer Five <http://blogs.scientificamerican.com/guest-blog/2013/01/27/science-in-ten-hundred-words-the-up-goer-five-challenge/>`__ level. It translates to an approximate grade level of 8.5, i.e. what a US student finishing junior high school can understand. More information is available in the `raw data <https://meta.wikimedia.org/wiki/Tech/News/Readability>`__ for people interested in diving deeper into this topic.


The other part of the puzzle: languages
=======================================

Keeping the text simple is one way to make the newsletter accessible to Wikimedians who aren't native English speakers, but it's only our fallback strategy. Our primary goal is to have the newsletter translated into as many languages as possible every week, so that subscribers can read it in their own language. It's an ambitious goal considering the weekly publication schedule but, using a trial-and-error approach, we've managed to reach a respectable amount of translations available every week.

Translation of the newsletter is done through the `Translate extension <https://www.mediawiki.org/wiki/Extension:Translate>`__ for MediaWiki, which provides a lot of neat features that save the translator's time, like easily accessible translation memory for similar sentences. Another neat feature of that extension is translation variables, which allow us to insert immutable parameters inside a translated sentence. In the tech newsletter, we mostly use this feature to hide long links, since they're the same regardless of the language; this removes complexity for the translators by letting them focus on the rest of the sentence. We also use it to make translations more reusable from one issue to the next (using translation memory), when only a few predictable numbers change.

.. figure:: /images/2013-12-16_Tech_news_process_2_-_Translation.svg

    The newsletter is routinely translated by volunteers to about a dozen languages every week-end.


Thanks to these features, and more importantly to the restless work of the volunteer translators, who donate their time every week-end, the tech newsletter is routinely available in about a dozen languages every week, which I believe makes it the most translated weekly publication across the Wikimedia movement.


Robots and mailpersons of Wikimedia
===================================

Once the newsletter is written and translated, it needs to be delivered to its hundreds of subscribers. We've been using `MZMcBride <https://meta.wikimedia.org/wiki/User:MZMcBride>`__'s `EdwardsBot <https://meta.wikimedia.org/wiki/User:EdwardsBot>`__ for that task, a "`bot <https://en.wikipedia.org/wiki/Wikipedia:Bots>`__" (automated program) written in Python that goes though the `list of subscribers <https://meta.wikimedia.org/wiki/Global_message_delivery/Targets/Tech_ambassadors>`__ and delivers the newsletter every Monday.

Global delivery of a monolingual text using EdwardsBot is relatively straightforward: give the bot a list of subscribers, set up the text to be posted, and it merrily goes to deliver it across wikis. The process is a bit more complex when the text is available in multiple languages: ideally, you'd want readers on the French Wikipedia to get the newsletter in French, and so on for all languages for which a translation is available. The first problem is that it wouldn't be convenient to maintain separate lists of subscribers broken down by language, and ask EdwardsBot to go through each list with a different translation. Furthermore, the languages vary from week to week, depending on the availability of translators. Dealing with all those special cases manually every week would be very inefficient.

Ideally, we should be able to give EdwardsBot all available translations of a weekly issue of the newsletter, and trust that it'll deliver the appropriate translation (if available) depending on the language used where it's posting. This would be similar to a European mailman being entrusted with copies of the same letter in different languages, and asking him to deliver the French translation to subscribers living in France, the Finnish translation to subscribers living in Finland, etc. The way we're doing this for the tech newsletter is by telling EdwardsBot to look up the language of the wiki it's posting on, and check if a translation is available in its mail bag. If it is, it posts that one; otherwise, it posts the original version in English. For people familiar with MediaWiki's "parser functions," this is done with a ``#switch`` condition.

Adding that language check isn't actually very complicated once you've done it once. What really takes time is assembling the catalog of multilingual texts that EdwardsBot will be picking from. Originally, we did this by hand, by manually copy/pasting the content of the available translations and assembling them into the ``#switch``. After a few unfortunate copy/paste errors that required us to clean up after the bot, I decided to automate that part as well, both to save time and to remove that potential source of human error. And, to be honest, I also thought this would be a cool project and an opportunity to play with the Lua programming language, which had been introduced on Wikimedia sites a few months earlier [#]_.

I had never worked with Lua before, but it turned out to be fairly intuitive; I was able to write a `short module <https://meta.wikimedia.org/wiki/Module:Tech_news>`__ that we're now using every week to assemble the available translations into the multilingual newsletter. What previously required manual (and human error-prone) copy/pasting is now handled by simply `calling the module <https://meta.wikimedia.org/wiki/Tech/News/Sandbox>`__'s ``assembleNewsletter`` function, and providing the list of languages. The module then directly outputs the multilingual text, ready for delivery.

.. figure:: /images/2013-12-16_Tech_news_process_3_-_Assembly.svg

    We use a custom Lua script to pull all translations together to assemble the multilingual newsletter, ready for delivery.


A few weeks later, another delivery tool was enabled on Wikimedia sites: `MassMessage <https://meta.wikimedia.org/wiki/MassMessage>`__. Written by then-volunteer developer `Kunal Mehta <https://meta.wikimedia.org/wiki/User:Legoktm>`__, MassMessage is a `MediaWiki extension <https://www.mediawiki.org/wiki/Extension:MassMessage>`__, meaning it's more closely integrated with MediaWiki than the external Python bot. It provides a user interface on the wiki and can use internal MediaWiki features like the "job queue," which queues tasks and processes them when resources are available.

.. figure:: /images/2013-12-16_Tech_news_process_4_-_Language_selection_and_delivery.svg

    Finally, the multilingual newsletter is delivered to subscribers across wikis by MassMessage, a broadcasting extension for MediaWiki.


After a few successful tests, we switched to MassMessage to deliver the weekly newsletter. Both community discussion pages and all individual subscribers are now getting the newsletter on their talk page through MassMessage.

In the future, it will probably be possible to hook into a system like `MediaWiki's notifications <https://www.mediawiki.org/wiki/Extension:Notifications>`__ and allow users to subscribe to thematic newsletters directly from their user preferences, making the subscription and cross-wiki delivery process even easier. There are still improvements to be made, but the process is now reasonably straightforward considering the tools at our disposal.


Looking to the future with Liaisons and Ambassadors
===================================================

The Tech newsletter is now on relatively stable tracks: we have the experience, routine and tools to ensure its publication every week, and `you're welcome to join the team <https://meta.wikimedia.org/wiki/Tech/News#contribute>`__. However, the newsletter is still mostly unidirectional; it's a channel designed for broadcast, not dialogue.

Another suggestion that came up during the Fall 2012 consultation was to hire more Community Liaisons for Engineering[#2012consult]_. Being able to predict what feature or technical change will or will not cause issues is dependent on having the institutional knowledge to do so, regardless of whether those issues are related to policy, product or simple resistance to change. At the time, `Oliver Keyes <https://meta.wikimedia.org/wiki/User:Okeyes_(WMF)>`__ was the only Community Liaison on the Product team's staff, and a popular request during the consultation was to "clone Oliver;" since then, several other Product Liaisons have been hired, initially to help with the activation of VisualEditor across Wikimedia wikis. I had the opportunity to work closely with them during that period, and their work has been splendid, earning them the rare common appreciation and respect of both users and engineering staff.

I believe Tech ambassadors and Community Liaisons have similar roles and will work more closely together in the future. They have the same goal of acting as facilitators between users and developers, and in the end it doesn't really matter who's a volunteer and who's an employee. The Tech newsletter is useful to support the work of ambassadors and liaisons, who in return make the interaction more bidirectional.

We've used the tech newsletter successfully in the Wikimedia movement to inform users without overwhelming them, and ambassadors and liaisons have complemented it by providing more details as needed, and relaying the user's questions, comments and concerns to the engineers. Even if this process is still young and imperfect, I believe it is a worthy goal to work towards a virtuous cycle that will benefit users and developers alike, and by extension the whole Wikimedia community.


.. [#] `Active Wikimedia Editors <http://reportcard.wmflabs.org/graphs/active_editors>`__ for All Wikimedia Projects (5+ edits per month). Wikimedia Report Card. Retrieved November 11, 2013.

.. [#] Alex Brollo. `Please use sitenotice when a new    version of software is deployed <http://thread.gmane.org/gmane.science.linguistics.wikipedia.technical/74186/>`__. wikitech-l. December 5, 2013.

.. [#] `Source code <http://korma.wmflabs.org/browser/scm.html>`__. Wikimedia Community Metrics. Retrieved November 11, 2013.

.. [#] `Issues <http://korma.wmflabs.org/browser/its.html>`__. Wikimedia    Community Metrics. Retrieved November 11, 2013.

.. [#] `Mailing lists <http://korma.wmflabs.org/browser/mls.html>`__. Wikimedia Community Metrics. Retrieved November 11, 2013.

.. [#] Guillaume Paumier, Sumana Harihareswara and MediaWiki developers. `The Architecture of Open Source Applications: MediaWiki <http://aosabook.org/en/mediawiki.html>`__. `ISBN 978-1105571817 <https://meta.wikimedia.org/wiki/Special:BookSources/9781105571817>`__

.. [#] `Wikipedia to become more user-friendly for new volunteer writers <https://wikimediafoundation.org/wiki/Press_releases/Wikipedia_to_become_more_user-friendly_for_new_volunteer_writers>`__. Wikimedia Foundation. December 3, 2008.

.. [#] `The Wikitech-ambassadors archives <http://lists.wikimedia.org/pipermail/wikitech-ambassadors/>`__. Retrieved December 11, 2013.

.. [#] Guillaume Paumier. `New, lower traffic, announcements only email list for Wikimedia developers <http://lists.wikimedia.org/pipermail/wikitech-l/2012-July/061621.html>`__. wikitech-l. July 10, 2012.

.. [#] `Wikitech-ambassadors subscribers <https://lists.wikimedia.org/mailman/roster/wikitech-ambassadors>`__ (Requires login). Retrieved December 11, 2013.

.. [#2012consult] `Technical communications/Fall 2012 consultation: Summary <https://www.mediawiki.org/w/index.php?title=Technical_communications/Fall_2012_consultation&oldid=845003>`__. mediawiki.org. Retrieved December 18, 2013.

.. [#] `Talk:Tech/Ambassadors: Noteworthy changes <https://meta.wikimedia.org/w/index.php?title=Talk:Tech/Ambassadors&oldid=5546521#Noteworthy_changes>`__. Meta-Wiki. Retrieved December 19, 2013.

.. [#] Tomasz W. Kozlowski and Guillaume Paumier. `Subscribe to Tech News to stay informed of upcoming technical changes <https://blog.wikimedia.org/2013/06/12/subscribe-to-tech-news-to-stay-informed-of-upcoming-technical-changes/>`__. Wikimedia Blog. June 12, 2013.

.. [#] Sumana Harihareswara. `New Lua templates bring faster, more flexible pages to your wiki <https://blog.wikimedia.org/2013/03/11/lua-templates-faster-more-flexible-pages/>`__. Wikimedia blog. March 11, 2013.

.. |The wikitech-ambassadors mailing list was used episodically in 2010−2011; its usage started to increase in 2012.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Wikitech-ambassadors_stats.svg_-760x524.png
   :target: https://commons.wikimedia.org/wiki/File:Wikitech-ambassadors_stats.svg
.. |The Tech/News page provides clear calls to action and pointers on how to subscribe and participate.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Technews_screen-760x513.png
   :target: https://meta.wikimedia.org/wiki/Special:MyLanguage/Tech/News
.. |The number of subscribers surged when the newsletter was announced, showing that it was meeting a real need from Wikimedians. It has been steadily increasing since then.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Tech_news_subscribers_2013-W21_to_2013-W51.svg_-760x349.png
   :target: https://commons.wikimedia.org/wiki/File:Tech_news_subscribers_2013-W21_to_2013-W51.svg
.. |Tech ambassadors monitor technical activity across many channels, select noteworthy information and simplify it to make it accessible to readers who don’t have specialized technical expertise.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Tech_news_process_1_-_Monitoring_and_writing.svg_-760x427.png
   :target: https://commons.wikimedia.org/wiki/File:Tech_news_process_1_-_Monitoring_and_writing.svg
.. |The newsletter is routinely translated by volunteers to about a dozen languages every week-end.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Tech_news_process_2_-_Translation.svg_-760x534.png
   :target: https://commons.wikimedia.org/wiki/File:Tech_news_process_2_-_Translation.svg
.. |We use a custom Lua script to pull all translations together to assemble the multilingual newsletter, ready for delivery.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Tech_news_process_3_-_Assembly.svg_-760x529.png
   :target: https://commons.wikimedia.org/wiki/File:Tech_news_process_3_-_Assembly.svg
.. |Finally, the multilingual newsletter is delivered to subscribers across wikis by MassMessage, a broadcasting extension for MediaWiki.| image:: https://guillaumepaumier.com/wp-content/uploads/2014/01/Tech_news_process_4_-_Language_selection_and_delivery.svg_-584x760.png
   :target: https://commons.wikimedia.org/wiki/File:Tech_news_process_4_-_Language_selection_and_delivery.svg
