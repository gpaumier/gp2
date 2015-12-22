.. title: The Universal Language Picker
.. clean: no
.. slug: universal-language-picker
.. date: 2010-09-29 00:13:26
.. tags: language,Multimedia usability,Engineering,Wikimedia
.. description: 
.. excerpt: Have you ever had a hard time finding your language in a web interface? The Universal language picker aims to solve this problem by accepting any valid input from the user and associating it with the language value stored in the software.

*This article is a follow-up to my previous article about the `state of the language selection in MediaWiki and Wikipedia <http://guillaumepaumier.com/2010/06/26/state-of-language-selection-mediawiki-wikipedia/>`__.*

The interface of MediaWiki is available in literally hundreds of languages, where many other major websites only care about English, and maybe a handful of other "major" languages.

The problem is that, with the number of available languages growing, it has become difficult to find the one you're looking for. Especially if you don't know in what language it's displayed, or how the languages are ordered.

Context
=======

The main focus of the Multimedia usability project right now is on developing `a new upload wizard <http://blog.wikimedia.org/blog/2010/08/07/prototype-upload-wizard/>`__, to replace the insanely complicated current upload form on `Wikimedia Commons <http://commons.wikimedia.org>`__. It's not going as fast as I expected, but we've made some great progress recently.

A few months ago, we did some "hallway testing": we asked some of our co-workers (who aren't necessarily wiki-experts) to try out the upload wizard. As they were using it, we watched them and tried to identify what was confusing, in order to improve the interface & interaction with the user.

It was really interesting, as they were all using the upload wizard differently. One was an "explorer", who would expand each and every sub-menu in order to better understand the options offered to her. Another would just try to proceed as fast as possible, get the job done and get it over with. It was a sort of rehearsal for our then-upcoming `User experience (UX) study <http://guillaumepaumier.com/2010/07/23/wikimedia-multimedia-ux-testing-videos/>`__, and we learned a lot.

Where's my Hindi?
=================

|Surjection between all the possible inputs from the user, and the language value stored in the software| Surjection between all the possible inputs from the user, and the language value stored in the software

Now, what kind of interface can we use to implement this model?

A simple input field with `autocomplete <http://en.wikipedia.org/wiki/Autocomplete>`__.

Simple as that. Forget endless drop-down menus with weird sorting orders. All we need is a simple input field with autocomplete containing all existing items in the *n* × *n* languages table. It doesn't matter if it's incomplete: as we get more translations, we'll add them to the table.

Of course, we'll need to use an arbitrary sorting order for autocomplete suggestions anyway. But by using an input field with autocomplete instead of a drop-down, the user can refine their search and dramatically decrease the size of the subset of items they're searching in.

Ideally, the user wouldn't even have to search: in many cases, it's possible to guess a sensible default language, based for example on the browser language. We could pre-populate the input field with a grayed out default text that disappears if the user clicks to edit the field.

Further implications
====================

This design has broader applications: the upload wizard is not the only place where the user might want to select a language. User preferences are an obvious example.

Given the multilingual nature of Commons, it would even make sense to add a language selector for the interface on the sign-up page. Right now, the user has to go change the language in their preferences after they've signed up.

I'd be delighted to hear opinions and comments about this proposed design. Do you think it would work? How technically feasible would it be?

Notes
=====

.. |Surjection between all the possible inputs from the user, and the language value stored in the software| image:: //guillaumepaumier.com/wp-content/uploads/2013/04/languages-surjection.png
   :target: //guillaumepaumier.com/wp-content/uploads/2013/04/languages-surjection.png
