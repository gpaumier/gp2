.. title: MediaWiki 1.19 deployment to Wikimedia sites: Test it before it breaks
.. slug: mediawiki-1-19-deployment
.. date: 2012-02-12 03:46:59
.. tags: MediaWiki,Wikimedia blog,Engineering,Wikimedia
.. description: 


We've recently `set up a Beta cluster <//blog.wikimedia.org/2012/01/28/beta-cluster-test-software-before-deployment/>`__, replicating a selection of Wikimedia wikis, where Wikimedians have tested the new version and checked that it worked reasonably well with their local wiki's specific customizations.

Things are looking good, and the current plan is to run the deployment in five stages **between February 15 and March 1, 2012**. The schedule may change based on unexpected issues, so you should refer to the **`MediaWiki 1.19 roadmap <//www.mediawiki.org/wiki/MediaWiki_1.19/Roadmap>`__** for an up-to-date schedule of when your wiki will be affected.

Many new features and bug fixes brought by MediaWiki 1.19 are back-end, behind-the-scenes changes, for example infrastructure work to support our ongoing `move to Swift <https://blog.wikimedia.org/2012/02/09/scaling-media-storage-at-wikimedia-with-swift/>`__ as our media storage platform.

There are also more visible improvements, like better diff readability for colorblind people, and better support of the user's gender and language in the interface. A list of all changes is available in the `draft release notes <//svn.wikimedia.org/viewvc/mediawiki/branches/REL1_19/phase3/RELEASE-NOTES-1.19?view=markup>`__.

Check JavaScript and Gadgets compatibility with ResourceLoader
==============================================================

A particular area of improvement in MediaWiki 1.19 relates to JavaScript. While most of the legacy site scripts, user scripts and `gadgets <//www.mediawiki.org/wiki/Extension:Gadgets>`__ will continue to work, it's also possible that the new version be less forgiving of assumptions and errors in code. For example, faster load times may uncover errors in scripts that don't explicitly declare the modules they're using.

Furthermore, a new version of `ResourceLoader <//www.mediawiki.org/wiki/ResourceLoader>`__ will be deployed later this year, that will bring improvements specific to gadgets, but *will* require gadgets to be made compatible with ResourceLoader.

Gadgets maintainers are therefore strongly advised to start upgrading their scripts now, to avoid major disruption later. The **`migration guide to ResourceLoader <//www.mediawiki.org/wiki/ResourceLoader/Migration_guide_(users)>`__** is the main document for Gadget developers; a list of `JavaScript deprecations <//www.mediawiki.org/wiki/ResourceLoader/JavaScript_Deprecations>`__ and `default modules <//www.mediawiki.org/wiki/ResourceLoader/Default_modules>`__ are available as well.

You can also join the `2011 Resource Walker <//meta.wikimedia.org/wiki/User:Krinkle/Le_Tour_de_Wik%C3%AD/2011_Resource_Walker>`__, an attempt to go through all Wikimedia wikis and update outdated JavaScript. An `IRC <//www.mediawiki.org/wiki/IRC>`__ workshop is planned to facilitate the process; more information will be posted later on this blog.

Moving towards transparent upgrades
===================================

As we move towards more frequent software upgrades, we expect them to be less and less painful — and ideally, at some point they'll go so smoothly that users won't even notice them, except for the new features that will appear. We're not completely there yet, but we've made progress in the past year or so, and we're committed to continue our efforts, both for the benefits of developers and users.

In the meantime, please bear with us if, despite our efforts, you encounter issues due to the upgrade; we'll try and fix them as soon as we can. It's not too late to `visit the Beta cluster <http://labs.wikimedia.beta.wmflabs.org>`__ and `report issues <http://labs.wikimedia.beta.wmflabs.org/wiki/Problem_reports>`__ there or `in our bug tracker <https://bugzilla.wikimedia.org/enter_bug.cgi?product=MediaWiki&version=1.19-svn>`__. The more people test beforehand, the smoother the deployment should go.

*Originally published on the `Wikimedia Tech blog. <https://blog.wikimedia.org/2012/02/11/mediawiki-1-19-deployment/>`__*
