.. title: State of the language selection in MediaWiki and Wikipedia
.. category: articles-en
.. slug: state-of-language-selection-mediawiki-wikipedia
.. date: 2010-06-26 00:15:10
.. tags: Wikimedia
.. keywords: language, MediaWiki, Engineering, Wikimedia
.. todo: add bold-monospace for {{int:}}


.. highlights::

    There are two main use cases for language selection across Wikimedia projects: the language of the content, and the language of the interface. In this article, I am reviewing a few examples of tools related to language selection on MediaWiki websites, and particularly on Wikimedia wikis.


.. sidebar::

    This article is meant as an introduction to :doc:`my next article, about language selectors <universal-language-picker>`, which is the one I originally intended to write. As it was growing longer and longer, I decided to split this review into a dedicated post.


Interface language selection
============================

Language setting in user preferences
------------------------------------

On each MediaWiki website, users who create an account can select the language of the software interface. That means, for example, that you can read Wikipedia articles in Italian, but with the interface in French. This feature is particularly useful for Wikipedia participants who are familiar with the interface in their mother tongue.

.. figure:: /images/2010-06-26_language_selector_prefs.png
   :figclass: framed

   Drop-down menu from MediaWiki's user preferences to select the language of the interface


The default language for MediaWiki messages is English. The localization of MediaWiki has been made possible with the `translatewiki.net <http://www.translatewiki.net>`__ platform (former "betawiki") and the hundreds of volunteer translators who try to keep up with the ever changing MediaWiki messages. And `they're doing a terrific job <http://www.mediawiki.org/wiki/Localisation_statistics>`__.

This language setting, though, only works for registered users. If you're only a reader and you don't have a user account, you're stuck with the default language specified for the website. Usually, the default interface language is the same as the content language, and most readers are content with that.

The problem comes with multilingual wikis, i.e. wikis that contain content in several languages. For example, `Wikimedia Commons <http://commons.wikimedia.org>`__, `Wikimedia Meta-Wiki <http://meta.wikimedia.org>`__ and the `Wikimedia Foundation website <http://wikimediafoundation.org>`__ are multilingual wikis; they are central places for Wikimedians from all projects in all languages. Only one interface language can be used as the default, and it's generally English. If you can't read English and you're looking for media files on Wikimedia Commons, you're going to have a hard time navigating the site.


The *uselang* parameter
=======================

A workaround is to use the |uselang|_ parameter to specifically ask MediaWiki to render the interface in a given language.\ [#]_ An example of its use is the "Commons" template, used on some Wikimedia projects to provide a visible link to the Commons page or category about a specific topic. If you're reading the `Catalonia article on the German-language Wikipedia <http://de.wikipedia.org/wiki/Katalonien>`__, and scroll to the bottom, you'll find a link to Commons directing you to the `Catalonia category on Commons <http://commons.wikimedia.org/wiki/Category:Catalonia?uselang=de>`__, but with the interface in German.

.. |uselang| replace:: **uselang**

.. _uselang: http://www.mediawiki.org/wiki/Manual:Parameters_to_index.php#User_preference_overriding

.. [#] As a sidenote, the *uselang* method has also been `diverted from its original purpose <http://commons.wikimedia.org/wiki/MediaWiki:UploadForm.js/Documentation>`__ to hack a JavaScript-enhanced upload form on Wikimedia Commons.

This method has obvious drawbacks: first, you need to actually know it exists, and how to use it. You also need to know the ISO 639 code of the language, but if you know the *uselang* parameter exists, I'll assume you know that language code as well.

More importantly, the *uselang* parameter isn't persistent, i.e. it will go away as soon as you leave the page you were viewing. There's an open bug to preserve the *uselang* parameter during sessions (`bug 4125 <https://bugzilla.wikimedia.org/show_bug.cgi?id=4125>`__). But for now, if you land on a page rendered in a specific language using *uselang*, it'll revert to the default language as soon as you move away from that page.


*LanguageSelector* extension for MediaWiki
==========================================

Going a bit further, Daniel Kinzler developed an extension for MediaWiki called |language selector|_. The first feature it provides is to automatically detect the browser language\ [#]_ of unregistered readers and defaults the interface to their language.

.. |language selector| replace:: **LanguageSelector**

.. _language selector: http://www.mediawiki.org/wiki/Extension:LanguageSelector

.. [#] For techies: the ``Accept-Language`` header.

Such an automatic system would be desirable for some Wikimedia websites, especially Commons, but it requires scalability improvements: it would fragment the cache, on which we rely heavily for performance. Nonetheless, it's an issue that'll have to be addressed in any case.

The *LanguageSelector* extension also provides a drop-down selector that can be included in pages. This setting seems to follow the user at least during the session. You can see an example of it used on the home page of `translatewiki.net <http://translatewiki.net>`__.

.. figure:: /images/2010-06-26_langselect_mwext.png
   :figclass: framed
   :alt: Drop-down menu showing a list of languages in their language, prefixed by the language code

   Drop-down language selector from the LanguageSelector MediaWiki extension


Content language selection on monolingual wikis
===============================================

Wikipedia.org portal
--------------------

Wikipedia and most other Wikimedia websites are available in many different languages — over 250 at the time of writing. And that's just existing Wikipedia editions; several thousand languages are spoken across the world population.

On monolingual wikis (i.e. wikis whose content is in only one language), there are two occasions where you may want to select a language: the first is when you choose what site you want to visit, e.g. Wikipedia in English *or* Wikipedia in Spanish. The second occasion is when you want to navigate from one language edition to another, e.g. from Wikipedia in English *to* Wikipedia in Spanish.

On Wikipedia, the first choice happens on the multilingual `wikipedia.org <http://www.wikipedia.org>`__ portal, if you ever happen to go there.

.. figure:: /images/2010-06-26_Wikipedia.org_portal.png
   :figclass: framed
   :alt: Screenshot of the wikipedia.org portal; The Wikipedia logo is surrounded by the 10 largest language editions, then languages are listed in size groups

   Screenshot of the Wikipedia.org portal


On this (`manually curated <http://meta.wikimedia.org/wiki/Project_portals>`__) portal, each language is displayed in the language's language:\ [#]_ English is displayed as "English," German as "Deutsch," French as "Français," etc. The sorting order is based on the size of each language edition, measured in number of articles. In a word, the bigger the Wikipedia, the more prominent the place. "Small" Wikipedia editions are at the very end of the list.

.. [#] This is getting confusing, I know. I'm doing my best, believe me.

In most cases, though, you don't have to make this choice; your search engine conveniently directs you to the language edition of Wikipedia in your language. Once you are on a specific language edition of Wikipedia, though, you can still navigate to related articles in other languages, using interlanguage links.


Interlanguage links
-------------------

**Interlanguage links** are a specific subset of `interwiki links <http://en.wikipedia.org/wiki/Interwiki_links>`__; they allow users to navigate between different language versions of the same page. Links and their order are curated by humans or "bots," i.e. external programs that interact with the software as humans would, but are not part of the MediaWiki software

.. figure:: /images/2010-06-26_interlanguage_links_apple.png
   :figclass: framed
   :alt: List of interlanguage links of the Apple article on Wikipedia in English, and the wikitext that generates them

   List of interlanguage links of the Apple article on Wikipedia in English, and the wikitext that generates them


The sorting order differs from a Wikipedia to another; they have `different standards <http://meta.wikimedia.org/wiki/Interwiki_sorting_order>`__. That means interlanguage links will be sorted in a different order, whether you're reading an article on the Polish Wikipedia, the Finnish Wikipedia, or the Serbian Wikipedia. Convenient, eh?

The default behavior for interlanguage links is to display all the available links. For the `most common topics <http://meta.wikimedia.org/wiki/List_of_articles_every_Wikipedia_should_have>`__, the list can grow quite long. The main page, for example, is the page all language editions are sure to have in common. The interlanguage list for the main page is usually truncated by Javascript in order to avoid having 250 links there.


Content language selection on multilingual wikis
================================================

Multilingual wikis
------------------

Wikipedia editions exist in only one language at a time. It's the same for most of the Wikimedia websites, like Wikisource or Wikibooks. Some projects, though, are meant to be a central place for all Wikimedians.

For example, `Wikimedia Commons <http://commons.wikimedia.org>`__ ("Commons") is the central media repository for all Wikimedia projects. Rather than duplicating media files on all of them, they're centralized into one media library.

`Wikimedia Meta-Wiki <http://meta.wikimedia.org>`__ ("Meta") is another multilingual wiki. Its purpose is to serve as a central coordination platform for the Wikimedia community.

Both these wikis are multilingual: they host content in a variety of languages. But MediaWiki wasn't originally designed for such a use; it was designed to host content in only one language. The community has had to work around this limitation by implementing various tricks & hacks.


JavaScript language select tool
-------------------------------

For a few years, meta has been experimenting with the |language select|_ tool. Language select is a JavaScript hack\ [#]_ that basically hides the text that isn't in the language you've selected.

.. |language select| replace:: **Language select**

.. _language select: http://meta.wikimedia.org/wiki/Meta:Language_select

.. [#] See `Meta-Wiki's Commons.js JavaScript file <https://meta.wikimedia.org/wiki/MediaWiki:Common.js>`_, section *Implements language selection for multilingual elements*.

There too, you have to know the ISO language code, and the user interface isn't very intuitive, but it was a start. The newer JavaScript method detects the language of your browser automatically.

.. figure:: /images/2010-06-26_language_select_meta.png
   :figclass: framed
   :alt: Cropped screenshot of a web page showing a small input field with the text 'en' in it, followed by two buttons, saying 'Select' and 'Show'

   Screenshot of the language select JavaScript tool on meta-wiki


A similar system is also available on Commons, through the *`Multilingual description <http://commons.wikimedia.org/wiki/Template:Multilingual_description>`__* template. As far as I know, though, this template is very rarely used; instead, individual language templates are the standard way of labeling (and sometimes, choosing) content in different languages.


Language templates
------------------

|language templates|_ are used to specify the language of a specific part of a content's page, for example descriptions of a picture on Commons. They also allow registered users to hide content they don't understand, by specifying a "blacklist" of languages they don't want to display. It's particularly useful for `Featured pictures <http://commons.wikimedia.org/wiki/Commons:Featured_pictures>`__, or `Pictures of the Day <http://commons.wikimedia.org/wiki/Commons:Picture_of_the_day>`__, that contain many translations for the caption.

.. |language templates| replace:: **Language templates**

.. _language templates: http://commons.wikimedia.org/wiki/Commons:Language_templates

.. figure:: /images/2010-06-26_language_templates.png
   :figclass: framed full-content
   :alt: Descriptions in German, English, French and Italian; the language is formatted in bold font.

   Description of a Picture of the Day on Commons in various languages


Langswitch & Autotranslation
----------------------------

*Langswitch* and *Autotranslate* are two similar methods used on Commons to show a given text depending on the user's language (as specified in their preferences). They're more elaborate systems than *Language select* and *Language templates*, but they essentially try to address the same issue.

|langswitch|_ is more lightweight and used for `simple templates <http://commons.wikimedia.org/wiki/Category:Internationalization_templates_using_LangSwitch>`__: all translations are contained in one page. For example, the "`France <http://commons.wikimedia.org/w/index.php?title=Template:France&action=edit>`__" template on Commons uses *Langswitch*; it includes the translation of the word "France" in all available languages, and provides a link to the appropriate article in the associated language edition of Wikipedia. If the user's language is German, they will only see "`Frankreich <http://de.wikipedia.org/wiki/Frankreich>`__."

.. |langswitch| replace:: **Langswitch**

.. _langswitch: http://commons.wikimedia.org/wiki/Template:LangSwitch

|autotranslate|_ is used for heavier templates that contain more text; in this case, it is easier to segregate the translations into dedicated subpages. This is how license templates have worked (although they're now being replaced, see below).

.. |autotranslate| replace:: **Autotranslate**

.. _autotranslate: http://commons.wikimedia.org/wiki/Template:Autotranslate


A template using *Autotranslate* (called "autotranslated template") typically consists of a subpage defining the template's layout, and a subpage for each translation of the template's messages. The "`PD-self <http://commons.wikimedia.org/wiki/Template:PD-self>`__" template is autotranslated, for example; it has a layout `subpage <http://commons.wikimedia.org/wiki/Template:PD-self/layout>`__, and subpages for all available languages, such as `English <http://commons.wikimedia.org/wiki/Template:PD-self/en>`__, `Japanese <http://commons.wikimedia.org/wiki/Template:PD-self/ja>`__ and `Russian <http://commons.wikimedia.org/wiki/Template:PD-self/ru>`__.

The ``{{int:}}`` MediaWiki "magic word"
---------------------------------------

**{{int:}}** is a `MediaWiki magic word <http://www.mediawiki.org/wiki/Help:Magic_words#Miscellaneous>`__ used to show a MediaWiki interface message in the user's language (as set in their preferences). Its main limitation is that it only works for MediaWiki interface messages. Yet, I am placing it into the "Content language selection" section, because it has recently been used to replace *Langswitch* and *Autotranslation*.

Using ``{{int:}}`` to display something in the user's language is a more robust system; it's also the reason for which license templates were converted to system messages (and bundled into the `WikimediaLicenseTexts <http://www.mediawiki.org/wiki/Extension:WikimediaMessages>`__ extension).

Basically, in the case of Commons, many templates requiring translation rarely change (e.g., the `licensing templates <http://commons.wikimedia.org/wiki/Commons:Copyright_tags>`__). As templates, they belong to the content, not the interface. But licenses are managed with templates *because* the software doesn't provide a built-in interface for them. Ideally, licenses would be managed by MediaWiki itself (or an extension). But we're not there yet.

So, what's currently happening is, these licensing templates are being replaced by alternatives that use custom MediaWiki messages. The content that was once stored in the templates is being moved to dedicated interface messages. That way, they can be automatically displayed in the user's language using ``{{int:}}``. And they can also be translated by the translatewiki.net community.

This system doesn't solve the issue for unregistered users, though.

Conclusion
==========

There is a multitude of cases where a user may want or come to select a language while navigating a Wikimedia site. They may want to choose in what language the website interface will be displayed, or select the language of the content.

For multilingual Wikimedia wikis like Commons and meta, language selection is a regular issue, because they intrinsically target a multilingual audience. Some ad-hoc systems have been developed over time to try and work around the technical limitations of MediaWiki, but they can't replace a built-in language management system.

Current language selection solutions also don't cater for the needs or unregistered readers, who are the majority of the people visiting Wikimedia projects. That issue will have to be addressed at some point if we want to reach a truly global audience.

Another challenge with language selection is the interface you provide the user with to make their choice, i.e. the actual "selector." It is not obvious what design is the best and allows the user to select the language they want in the most efficient manner. This will be the topic of :doc:`my next article, about language selectors <universal-language-picker>`.
