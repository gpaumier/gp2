.. title: Scaling up Software development for Wikimedia websites
.. subtitle: Part II: Tools
.. category: articles-en
.. slug: scaling-up-software-development-for-wikimedia-websites-tools
.. date: 2010-03-05 18:05:50
.. tags: Wikimedia
.. keywords: MediaWiki, Engineering, Wikimedia
.. image: /images/2010-03-05_Tooled_Flatty_by_flattop341.jpg
.. image-caption: “Give us the tools, and we will finish the job.”




.. highlights::

    I have previously explained why the current setup of the Wikimedia bug tracker is not ideal. I have also advocated for a more managed & scientific software development strategy. This article aims to discuss an appropriate tool to support this strategy, and at the same time fix what is broken.

.. class:: rowspan-2
.. sidebar::

   Over the past few weeks, I have been thinking about a more structured way to manage software and product development within the Wikimedia community. The result is a list of ideas and recommendations I have compiled and submitted to the relevant staff members at the Wikimedia Foundation. I am also publishing them here in order to allow for wider feedback.

   The content of this article reflects only my personal opinion and is not an official plan or communication of the Wikimedia Foundation. Read also in this series:

   -  :doc:`Wikimedia and MediaWiki bugs, issues, and requests <wikimedia-mediawiki-bugs-issues-and-requests>`
   -  :doc:`Wikimedia User experience programs: a systematic approach <wikimedia-user-experience-programs>`
   -  :doc:`Scaling up Software development for Wikimedia websites (Part I: Human resources) <scaling-up-software-development-for-wikimedia-websites-human-resources>`

.. class:: rowspan-2
.. figure:: /images/2010-03-05_Tooled_Flatty_by_flattop341.jpg

   |tools|_ by `flattop341`_, under `CC-By`_, from Wikimedia Commons.

.. |tools| replace:: *Tooled Flatty*

.. _tools: https://commons.wikimedia.org/wiki/File:Japanese_Tea_pot_by_Denis_Savard.jpg

.. _flattop341: https://secure.flickr.com/people/flattop341/

.. _CC-By: https://creativecommons.org/licenses/by/2.0/legalcode


Software lifecycle & Project management
=======================================

Right now, there is little project management of the technical activities at the Foundation. When someone does manage projects, they often use personal desktop applications that don't allow collaborative work. There isn't any real development roadmap or product requirements. If we want to be serious about structuring our activities, **we need a project management strategy & the appropriate associated tools** that allow us to manage things such as project scope, schedule, budget & financial resources, quality assurance, human resources, communications, risks & opportunities, procurement and coordination.

I asked around to see what the needs of the various members of the team were. Naoko Komura, who has been project-managing the Wikipedia Usability Initiative, and is now overseeing all UX programs, is particularly interested in the integration of the Project management platform with calendars & issue tracking. Operations staff members also said they were interested in Project management features such as time and task tracking.

I think it is way past time to have a more organized development process & software lifecycle management. The recent hiring of a new Chief Technical Officer is a step towards a more structured organization of technological activities. Of course, changing our bug tracker alone won't automatically structure our activities, but it is a step in this direction.

**Recommendation: Use tools that allow a better management of, and integration between, the different stages in our product(s) lifecycle.**


Requirements
============

A few months ago, I asked Priyanka Dhanda (our new Code maintenance engineer) to explore open-source collaborative project management platforms that could be easily integrated with bugzilla (or that included a bug tracking system of their own). The Wikimedia tech community was `invited <http://thread.gmane.org/gmane.science.linguistics.wikipedia.technical/46544>`__ to `list requirements of such a tool <http://www.mediawiki.org/wiki/Tracker/PM_tool>`__, as well as possible solutions.

From the feedback we received, we can summarize what the required features for an issue tracker are: integration with our Version control system, being FLOSS, multiple projects support and ability to separate between "tasks" and other items such as bugs and feature requests. Additional, "nice to have" features include: ability to import data from existing Bugzilla instance and fined-grained e-mail subscription options

Similarly, the required features for a Project management tool are: being web-based to facilitate collaboration, multiple projects support, calendar/scheduling and roadmap, assignments & resource management and time tracking per task/user/project. Additional, "nice to have" features include: Gantt charts, public/private projects, fine-grained access to projects by user, basic accounting & budget management and requirements management.


Redmine
=======

I haven't found many Project management softwares that can be easily integrated with Bugzilla. However, I have discovered alternatives to Bugzilla that include project management features like those we're looking for. `Redmine <http://www.redmine.org/projects/redmine>`__ seems to be a good project management software and provides an advanced issue tracking system as well. It supports multiple projects, public/private projects, calendars & Gantt chart, `and a lot of other neat stuff <http://www.redmine.org/wiki/redmine/Features>`__.

It also offers the ability to distinguish between features/improvements and bugs; this would be particularly useful to prioritize development efforts. We are now considering using Redmine as project management software and taking this opportunity to move our Bugzilla setup to Redmine. Initial research shows that a lot of people seem to praise Redmine compared to Bugzilla; there are migration scripts to import an existing Bugzilla setup into a new Redmine one.

`Major projects <http://www.redmine.org/wiki/redmine/WeAreUsingRedmine>`__ such as `TYPO3 <http://forge.typo3.org>`__ are using Redmine. The software seems to benefit from a dynamic community of developers and it is also possible to sponsor custom development. There are many plug-ins to extend the default core features; popular plug-ins are usually included into the core software at some point.

Priyanka set up a local test instance of Redmine to let us play with it a bit; a `public test platform <http://project2.wikimedia.org:3000/>`__ was later made available for wider testing and the Wikimedia Tech community was invited to pitch in. So far, I personally like it and it fits my needs perfectly. Wider testing is now necessary to see if it fits the needs of the tech community.

Because the time I can devote to this change is limited, I haven't reviewed other alternatives than Redmine, and don't plan to unless another major alternative is suggested.

**Recommendation: Move from Bugzilla to Redmine after careful preparation, especially regarding the organization of the platform.**
