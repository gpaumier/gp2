.. title: State of the language selection in MediaWiki and Wikipedia
.. clean: no
.. slug: state-of-language-selection-mediawiki-wikipedia
.. date: 2010-06-26 00:15:10
.. tags: language,MediaWiki,Engineering,Wikimedia
.. description: 
.. excerpt: This article is meant as an introduction to my next article, about language selectors, which is the one I originally intended to write. As it was growing longer and longer, I decided to split this review into a dedicated post. There are two main use cases for language selection across Wikimedia projects: the language of the content, and the language of the interface. In this article, I am reviewing a few examples of tools related to language selection on MediaWiki websites, and particularly on Wikimedia wikis.

*This article is meant as an introduction to `my next article, about language selectors <http://guillaumepaumier.com/2010/09/29/universal-language-picker/>`__, which is the one I originally intended to write. As it was growing longer and longer, I decided to split this review into a dedicated post.*

Interface language selection
============================

Language setting in user preferences
------------------------------------

On each MediaWiki website, users who create an account can select the language of the software interface. That means, for example, that you can read Wikipedia articles in Italian, but with the interface in French. This feature is particularly useful for Wikipedia participants who are familiar with the interface in their mother tongue.

|Descriptions in German, English, French and Italian; the language is formatted in bold font.| Description of a Picture of the Day on Commons in various languages

Langswitch & Autotranslation
----------------------------

*Langswitch* and *Autotranslate* are two similar methods used on Commons to show a given text depending on the user's language (as specified in their preferences). They're more elaborate systems than *Language select* and *Language templates*, but they essentially try to address the same issue.

***`Langswitch <http://commons.wikimedia.org/wiki/Template:LangSwitch>`__*** is more lightweight and used for `simple templates <http://commons.wikimedia.org/wiki/Category:Internationalization_templates_using_LangSwitch>`__: all translations are contained in one page. For example, the "`France <http://commons.wikimedia.org/w/index.php?title=Template:France&action=edit>`__\ " template on Commons uses *Langswitch*; it includes the translation of the word "France" in all available languages, and provides a link to the appropriate article in the associated language edition of Wikipedia. If the user's language is German, they will only see "`Frankreich <http://de.wikipedia.org/wiki/Frankreich>`__\ ".

***`Autotranslate <http://commons.wikimedia.org/wiki/Template:Autotranslate>`__*** is used for heavier templates that contain more text; in this case, it is easier to segregate the translations into dedicated subpages. This is how license templates have worked (although they're now being replaced, see below).

A template using *Autotranslate* (called "autotranslated template") typically consists of a subpage defining the template's layout, and a subpage for each translation of the template's messages. The "`PD-self <http://commons.wikimedia.org/wiki/Template:PD-self>`__\ " template is autotranslated, for example; it has a layout `subpage <http://commons.wikimedia.org/wiki/Template:PD-self/layout>`__, and subpages for all available languages, such as `English <http://commons.wikimedia.org/wiki/Template:PD-self/en>`__, `Japanese <http://commons.wikimedia.org/wiki/Template:PD-self/ja>`__ and `Russian <http://commons.wikimedia.org/wiki/Template:PD-self/ru>`__.

The {{int:}} MediaWiki "magic word"
-----------------------------------

**{{int:}}** is a `MediaWiki magic word <http://www.mediawiki.org/wiki/Help:Magic_words#Miscellaneous>`__ used to show a MediaWiki interface message in the user's language (as set in their preferences). Its main limitation is that it only works for MediaWiki interface messages. Yet, I am placing it into the "Content language selection" section, because it has recently been used to replace *Langswitch* and *Autotranslation*.

Using {{int:}} to display something in the user's language is a more robust system; it's also the reason for which license templates were converted to system messages (and bundled into the `WikimediaLicenseTexts <http://www.mediawiki.org/wiki/Extension:WikimediaMessages>`__ extension).

Basically, in the case of Commons, many templates requiring translation rarely change (e.g., the `licensing templates <http://commons.wikimedia.org/wiki/Commons:Copyright_tags>`__). As templates, they belong to the content, not the interface. But licenses are managed with templates *because* the software doesn't provide a built-in interface for them. Ideally, licenses would be managed by MediaWiki itself (or an extension). But we're not there yet.

So, what's currently happening is, these licensing templates are being replaced by alternatives that use custom MediaWiki messages. The content that was once stored in the templates is being moved to dedicated interface messages. That way, they can be automatically displayed in the user's language using {{int:}}. And they can also be translated by the translatewiki.net community.

This system doesn't solve the issue for unregistered users, though.

Conclusion
==========

There is a multitude of cases where a user may want or come to select a language while navigating a Wikimedia site. They may want to choose in what language the website interface will be displayed, or select the language of the content.

For multilingual Wikimedia wikis like Commons and meta, language selection is a regular issue, because they intrinsically target a multilingual audience. Some ad-hoc systems have been developed over time to try and work around the technical limitations of MediaWiki, but they can't replace a built-in language management system.

Current language selection solutions also don't cater for the needs or unregistered readers, who are the majority of the people visiting Wikimedia projects. That issue will have to be addressed at some point if we want to reach a truly global audience.

Another challenge with language selection is the interface you provide the user with to make their choice, i.e. the actual "selector". It is not obvious what design is the best and allows the user to select the language they want in the most efficient manner. This will be the topic of my next article.

Notes
=====

.. |Descriptions in German, English, French and Italian; the language is formatted in bold font.| image:: /wp-content/uploads/2013/04/language-templates.png
   :target: /wp-content/uploads/2013/04/language-templates.png
