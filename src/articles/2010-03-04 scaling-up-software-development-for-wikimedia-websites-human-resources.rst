.. title: Scaling up Software development for Wikimedia websites
.. subtitle: Part I: Human resources
.. category: articles-en
.. slug: scaling-up-software-development-for-wikimedia-websites-human-resources
.. date: 2010-03-04 20:57:44
.. tags: Wikimedia,
.. keywords: MediaWiki, Engineering, Wikimedia
.. image: /images/2010-03-04_Brighton_University_usability_lab_by_Danny_Hope.jpg


.. highlights::

   Our human resources are currently focusing on what happens after the code has been written: we review it, we try to ensure quality, we try to automate testing, we file bugs, etc. However, there is little preparation before the development is actually done. This has led to a developer-driven design, resulting in an interface based on the implementation model. We need a more systematic approach to User experience and development management if we want to scale up properly.

.. class:: rowspan-2
.. sidebar::

   Over the past few weeks, I have been thinking about a more structured way to manage software and product development within the Wikimedia community. The result is a list of ideas and recommendations I have compiled and submitted to the relevant staff members at the Wikimedia Foundation. I am also publishing them here in order to allow for wider feedback.

   The content of this article reflects only my personal opinion and is not an official plan or communication of the Wikimedia Foundation. Read also in this series:

   -  :doc:`Wikimedia and MediaWiki bugs, issues, and requests <wikimedia-mediawiki-bugs-issues-and-requests>`
   -  :doc:`Wikimedia User experience programs: a systematic approach <wikimedia-user-experience-programs>`
   -  :doc:`Scaling up Software development for Wikimedia websites (Part II: Tools) <scaling-up-software-development-for-wikimedia-websites-tools>`

.. class:: rowspan-2
.. figure:: /images/2010-03-04_Brighton_University_usability_lab_by_Danny_Hope.jpg

   |usability lab|_ by `Danny Hope`_, under `CC-By`_, from Wikimedia Commons.

.. |usability lab| replace:: *Brighton Uni Usability Lab*

.. _usability lab: https://commons.wikimedia.org/wiki/File:Japanese_Tea_pot_by_Denis_Savard.jpg

.. _Danny Hope: https://secure.flickr.com/photos/yandle/

.. _CC-By: https://creativecommons.org/licenses/by/2.0/legalcode


Product management & Design
===========================

In the Software development world, Product managers and Designers are the most common bridges between users and engineers. Product managers identify the needs of users and prioritize features & improvements; their goal is to translate the users' experience and feedback into explicit requirements to meet the users' expectations. It is then the role of the designers to create innovative, well-thought solutions to address these issues and meet the requirements. Finally, developers provide feedback about the technical feasibility of these solutions, and implement them the best way possible. This is of course a simplistic summary, but it helps get the point across.

"Designer" can have a lot of different meanings. A lot of people think that "design" is just making things pretty. When I talk about designers, I think mainly of |interaction designers|_, i.e. people who design solutions to improve the user experience and the way the product interacts with the user.

.. |interaction designers| replace:: *Interaction* Designers

.. _interaction designers: http://en.wikipedia.org/wiki/Interaction_design

The community of MediaWiki users is amazingly large, partly because they include participants from all Wikimedia Websites. Similarly, MediaWiki also benefits from a large base of volunteer developers. Product managers and designers have been the missing piece in this picture; their bridging role is critical, simply because there aren't any volunteers to take up this task. Admittedly, some users are also developers, and some developers keep themselves informed of the users' wishes. But **without product managers, clear requirements & prioritization are missing**. And **without designers, the technical solutions created by the developers don't meet the users' expectations** and mental model.

In my experience, developers prefer to focus on the actual development and rarely enjoy meta-activities related to it. They usually dislike project management and writing product specifications, and rightly so: it is not their job. However, **a successful software product strategy cannot rely only on development**.

We benefit from a large community of volunteer developers, but we lack management & design resources; it is the role of the Foundation to supplement this lack. It doesn't mean we shouldn't expand our development team: our number of paid core developers is ridiculously small. It only means we should also invest where the weakness lies.

**Recommendation: Recruit Product managers and Designers to strengthen the development cycle of our technological platform**

Research team
=============

The `Multimedia usability project <http://usability.wikimedia.org/wiki/Multimedia:Hub>`__ has relied heavily on initial research in order to gather as much information as possible about users and their goals. A lot of useful information was already available, but a lot of specific metrics were also missing; collecting and analyzing them took a lot of time and it will still take months to get all the metrics we need.

Research is critical in order to make the right decisions, especially about design. **Research is the only way know our users in order to make the best design & management decisions.** Good research is the best basis on which product managers, designers and developers can then respectively specify, design and build awesome solutions.

Right now the only researcher we have is Erik Zachte as Data analyst, but his job seems to essentially focus on providing operational metrics. While this work is much needed, we also need some more specific data on a case by case basis. I see at least three other positions needed:

-  A **UX research specialist**, who would conduct regular in-house low-cost usability testing, and generally manage UX studies
-  A **Metrics engineer**, who would develop integrated metrics in the software and be able to extract specific information from the database on a case by case basis.
-  A **Community specialist**, with a good knowledge of social psychology and online interaction, who would especially focus on improving the interaction between participants by identifying the community issues and proposing ways to fix them.

**Recommendation: Build a Research team to guide design & strategic decisions about our technological platform**

Volunteer developers
====================

We benefit from a fantastic community of volunteer developers, but we underestimate their potential; I think we are not doing enough to support their work and engage them into our activities. In 2007, the Foundation hired Cary Bass to try and coordinate the large pool of volunteers willing to help us with meta activities.

Similarly, **we need a Developer community manager to care for our volunteer developers**. We need someone who knows the developer community very well, and knows their strengths and weaknesses in order to find the right person for each job. We need someone who can help orient new volunteers, organize real-life meet-ups and manage projects such as the Google Summer of Code.

**Recommendation: Recruit a Community manager to coordinate the efforts of volunteer developers.**
