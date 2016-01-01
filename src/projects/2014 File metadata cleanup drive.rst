.. title: File metadata cleanup drive
.. slug: file-metadata-cleanup-drive
.. date: 2014-09-11T00:00:00
.. ongoing: true
.. image: /images/MrMetadata-screenshot.png
.. roles: analyst, project lead
.. tags: Wikimedia, metadata, Wikimedia Commons, licensing, multimedia

.. highlights::

    In 2014 and 2015, I led the File metadata cleanup drive, a community effort to fix file description pages and tweak license templates, to ensure that multimedia files consistently contain machine-readable metadata across Wikimedia wikis.


A short while after Wikipedia was created in 2001, contributors started
to upload pictures to the site to illustrate articles. Over the years,
Wikimedians have accumulated over 22 million files on Wikimedia Commons,
the central media repository that all Wikimedia sites can pull from. In
addition, nearly 2.5 million other files are spread out across hundreds
of individual wikis. MediaWiki, the software platform used for Wikimedia
sites, wasn't originally designed for multimedia content. We've made
good progress with `better upload
tools <https://blog.wikimedia.org/2012/05/29/1-million-media-files-uploaded-using-upload-wizard/>`__,
for example, but the underlying system still very much focuses on text.
On MediaWiki, each file has a file description page that contains all
the information ("metadata") related to the picture: what it depicts,
who the author is, what rights and limitations are associated with it,
etc. Many wikis have developed templates (reusable bits of wikicode) to
organize such file metadata, but a lot of information is still
unstructured in plain wikitext. In October 2014, the Wikimedia
Foundation `launched an
initiative <https://blog.wikimedia.org/2014/10/27/structured-commons-project-launches-in-berlin/>`__
to develop a `new underlying
system <https://commons.wikimedia.org/wiki/Special:MyLanguage/Commons:Structured_data>`__
for file metadata using the same technology powering
`Wikidata <https://www.wikidata.org>`__. This project is still in the
early stages, and even when it becomes available, it will take a long
time to migrate the existing metadata to structured data. The goal of
the `File metadata cleanup
drive <https://meta.wikimedia.org/wiki/Special:MyLanguage/File_metadata_cleanup_drive>`__
is to make the migration process for those 24+ million files less
tedious, by making sure that robots can process most of the files
automatically. Machine-readable data also makes it easier to reuse
Wikimedia content consistently with `best practices for
attribution <http://wiki.creativecommons.org/Best_practices_for_attribution>`__.
Examples of tools that use existing machine-readable data include the
`stockphoto
gadget <https://commons.wikimedia.org/wiki/Help:Gadget-Stockphoto>`__ on
Commons, `WikiWand <http://www.wikiwand.com/>`__ and `Media
Viewer <https://www.mediawiki.org/wiki/Multimedia/About_Media_Viewer>`__.
The PDF generator and offline readers like
`Kiwix <http://www.kiwix.org/>`__ are other tools that will benefit from
this effort.

Evolution of the file description page
======================================

The upcoming Structured data project aims to build a system where you
edit the metadata using a form, you view it in a nice format, and robots
can understand the content and links between items. [caption
id="attachment\_8358" align="aligncenter" width="760"]\ |image0| With
Structured data, robots will know exactly what field refers to what kind
of information. This will make it easier for humans to search and edit
metadata.[/caption] Many files on Wikimedia Commons aren't actually very
far from that model. Many files have an "Information template", a way to
organize the different parts of the metadata on the page. Information
templates were originally created to display metadata in a consistent
manner across files, but they also make it possible to make the
information easier to read for robots. This is achieved by adding
*machine-readable markers* to the HTML code of the templates. Those
markers say things like "this bit of text is the description", and "this
bit of text is the author", etc. and robots can pick these up to
understand what humans have written. This situation is ideal for the
migration, because it tells robots exactly how to handle the bits of
metadata and which field they belong to. [caption id="attachment\_8356"
align="aligncenter" width="760"]\ | Current information and license
templates can be read by machines if they contain special markers.
Robots will be able to migrate many files to structured data
automatically if they use those templates.| Current information and
license templates can be read by machines if they contain special
markers. Robots will be able to migrate many files to structured data
automatically if they use those templates.[/caption] If the
machine-readable markers aren't present, the robots need to guess which
field corresponds to which type of content. This makes it more difficult
to read the metadata, and their parsing of the text is less accurate.
The good news is that by just adding a few markers to the templates, all
the files that use the template will automatically become readable for
robots. [caption id="attachment\_8354" align="aligncenter"
width="760"]\ |légende| If a file contains information and license
templates, but they don't have the special markers, it's difficult for
robots to migrate it. Fortunately, `it's easy to add the special
markers <https://meta.wikimedia.org/wiki/Special:MyLanguage/File_metadata_cleanup_drive/How_to_fix_metadata>`__.[/caption]
Things become fuzzier for robots when the information isn't organized
with templates. In this case, robots just see a blob of text and have no
idea what the metadata is saying. This means that the migration has to
be made entirely by human hands. [caption id="attachment\_8350"
align="aligncenter" width="760"]\ | If the file's metadata only contains
wikitext, we need to organize the content by adding an information and a
license template manually. Those templates need to contain the special
markers.| If the file's metadata only contains wikitext, we need to
organize the content by adding an information and a license template
manually. Those templates need to contain the special markers.[/caption]

Fixing files and templates
==========================

Many files across wikis are in one of the latter states that aren't
readable by robots, and about 700,000 files on Commons are missing an
information template as well. In order to fix them so they can be easily
migrated in the future requires, we need an inventory of files missing
machine-readable metadata. That's where
`MrMetadata <https://tools.wmflabs.org/mrmetadata>`__ comes into play.
MrMetadata (a wordplay on *M*\ achine-\ *R*\ eadable Metadata) is a
dashboard tracking, for each wiki, the proportion of files that are
readable by robots. It also provides an exhaustive list of the "bad"
files, so we know which ones to fix. [caption id="attachment\_8344"
align="aligncenter" width="760"]\ |Screenshot of the MrMetadata
dashboard for the English-language Wikivoyage| Each wiki storing images
has a dedicated dashboard showing the proportion of files with
machine-readable metadata, and providing a list of the files to
fix.[/caption] Once the files have been identified, a `multilingual
how-to <https://meta.wikimedia.org/wiki/Special:MyLanguage/File_metadata_cleanup_drive/How_to_fix_metadata>`__
explains how to fix the files and the templates. Fixing template is
easy: you just add a few machine-readable markers, and you're done. For
example, the `English
Wikivoyage <https://tools.wmflabs.org/mrmetadata/wikivoyage/en/historical_tallies.svg>`__
went from 9% to 70% in just a few weeks. Fixing individual files
requires more manual work, but there are tools that make this less
tedious.

Get involved
============

If you'd like to help with this effort, you can `look for your wiki on
MrMetadata <https://tools.wmflabs.org/mrmetadata>`__, bookmark the link,
and start going through the list. By looking at the files, you'll be
able to determine if if has a template (where you can add markers) or if
you need to add the template as well. [caption id="attachment\_8346"
align="aligncenter" width="760"]\ |Screenshot of the Chinese-language
version of the 'How to fix metadata' page on Meta-Wiki| The multilingual
how-to provides a step-by-step guide to fixing files and templates. It's
currently available in more than a dozen languages.[/caption] If you add
markers to the templates, wait a couple of days for MrMetadata to
update, so you can see the remaining files missing machine-readable
information. The `multilingual
how-to <https://meta.wikimedia.org/wiki/Special:MyLanguage/File_metadata_cleanup_drive/How_to_fix_metadata>`__
provides a step-by-step guide to fixing files and templates. [caption
id="attachment\_8364" align="aligncenter" width="760"]\ |Bar chart
showing the increase in proportion of files with machine-readable
metadata on the English-language Wikivoyage| Adding special markers to
the templates can improve metadata readability very quickly. The English
Wikivoyage went from 9% to 70% of "good" files in just a few
weeks.[/caption]

Impact
======

An assessment of impact conducted in January 2015 showed that, in three
months, the cleanup drive had contributed to eliminating a third of the
files missing machine-readable metadata across all wikis. Most of this
progress was driven by editing file templates on the wikis with the most
files. Over this period we gained 3 percentage points in the total
proportion of files with machine-readable metadata. [caption
id="attachment\_8366" align="aligncenter" width="760"]\ |Chart showing
the impact of the File metadata cleanup drive. The source data comes
from MrMetadata, and more specifically the historical tallies for
Commons and historical tallies for all wikis combined between 2014-10-10
and 2015-01-22. The stacked bar chart (blue & yellow) uses the left-side
axis. The deltas (Δ) represent the absolute difference in files for
Commons (Δ in the blue bars) and for all other wikis (Δ in the yellow
bars) between the start and end dates of the chart. The standalone
Δtotal is the total difference for all wikis combined. The top (green)
line chart uses the right-side axis.| In three months, over a third of
the files missing machine-readable metadata were fixed.[/caption] The
challenge at this point was that most of the low-hanging fruits
(templates that were on lots of pictures) have been exhausted, and most
of the remaining files don't have templates. This means that we need to
add the templates ourselves to structure information that is currently
in raw wikitext, which will take more time. This will be done by running
focused campaigns using bots on large sets of files whenever possible.

.. |image0| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/the-path-5-760x223.png
   :target: https://commons.wikimedia.org/wiki/File:Evolution_of_file_metadata_on_Wikimedia_sites_05.svg
.. | Current information and license templates can be read by machines if they contain special markers. Robots will be able to migrate many files to structured data automatically if they use those templates.| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/the-path-4-760x187.png
   :target: https://commons.wikimedia.org/wiki/File:Evolution_of_file_metadata_on_Wikimedia_sites_04.svg
.. |légende| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/the-path-3-760x186.png
   :target: https://commons.wikimedia.org/wiki/File:Evolution_of_file_metadata_on_Wikimedia_sites_03.svg
.. | If the file's metadata only contains wikitext, we need to organize the content by adding an information and a license template manually. Those templates need to contain the special markers.| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/the-path-1-760x107.png
   :target: https://commons.wikimedia.org/wiki/File:Evolution_of_file_metadata_on_Wikimedia_sites_01.svg
.. |Screenshot of the MrMetadata dashboard for the English-language Wikivoyage| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/en.wikivoyage-dashboard-760x606.png
   :target: https://commons.wikimedia.org/wiki/File:En.wikivoyage_dashboard_on_MrMetadata.png
.. |Screenshot of the Chinese-language version of the 'How to fix metadata' page on Meta-Wiki| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/How-to-fix-metadata-screenshot-760x577.png
   :target: https://commons.wikimedia.org/wiki/File:How_to_fix_metadata_screenshot.png
.. |Bar chart showing the increase in proportion of files with machine-readable metadata on the English-language Wikivoyage| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/historical_tallies-760x570.png
   :target: https://commons.wikimedia.org/wiki/File:Historical_tallies_for_file_metadata_on_the_English_Wikivoyage.png
.. |Chart showing the impact of the File metadata cleanup drive. The source data comes from MrMetadata, and more specifically the historical tallies for Commons and historical tallies for all wikis combined between 2014-10-10 and 2015-01-22. The stacked bar chart (blue & yellow) uses the left-side axis. The deltas (Δ) represent the absolute difference in files for Commons (Δ in the blue bars) and for all other wikis (Δ in the yellow bars) between the start and end dates of the chart. The standalone Δtotal is the total difference for all wikis combined. The top (green) line chart uses the right-side axis.| image:: https://guillaumepaumier.com/wp-content/uploads/2015/02/2015-01-File-metadata-cleanup-drive-impact-chart-760x450.png
   :target: https://commons.wikimedia.org/wiki/File:File_metadata_cleanup_drive_impact_Oct2014-Jan2015.svg
