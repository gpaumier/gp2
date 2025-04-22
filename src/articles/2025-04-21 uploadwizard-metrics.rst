.. title: Wizards, Metadata, and Memory
.. subtitle: Unearthing and Reconstructing UploadWizard's Lost History
.. category: articles-en-featured
.. slug: uploadwizard-metrics
.. date: 2025-04-21
.. template: post_hero.j2
.. image: /images/Goldmark_-_Merlin_-_Zaubergarten_-_Hermann_Burghart_1886.png
.. image_alt: Stage design of the Enchanted Garden by Hermann Burghart for the opera Merlin, featuring dramatic arches, misty foliage, and magical lighting in a painterly, theatrical style.


.. figure:: /images/Goldmark_-_Merlin_-_Zaubergarten_-_Hermann_Burghart_1886.png
   :figclass: lead-figure
   :alt: Stage design of the Enchanted Garden by Hermann Burghart for the opera Merlin, featuring dramatic arches, misty foliage, and magical lighting in a painterly, theatrical style.

   Stage design of the Enchanted Garden by Hermann Burghart for the 1886 premiere of Karl Goldmark's opera *Merlin*. (Herman Burghart on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Goldmark_-_Merlin_-_Zaubergarten_-_Hermann_Burghart_1886.png>`__ // Public domain)


.. highlights::

   One in three pictures you see on Wikipedia was added through UploadWizard, a tool I designed in 2009. Over the past 15 years, **1.8 million unique volunteers** have uploaded over **42 million files** with UploadWizard to Commons, Wikipedia's media library. But unearthing those metrics turned out to be more complicated than I expected. What began as a straightforward question became a journey through over a decade of evolving logging practices, overwritten traces, and quietly deleted markers. The road of metadata archaeology is wild and wicked, winding through the wood. Follow me, my friend, to glory at the end.


The Tower, Reversed
===================

UploadWizard has been used to upload tens of millions of files to Wikimedia Commons. It was designed to simplify the contribution process, especially for newcomers. I was both the designer and product manager of UploadWizard, and it was the first project I worked on after joining the Wikimedia Foundation in 2009. At the time, I was also a very active volunteer contributor on Commons, which made the project feel deeply personal. In many ways, UploadWizard felt like my "baby."

And yet, more than a decade after its introduction, one simple question turned out to be surprisingly hard to answer: **how many files have been uploaded with UploadWizard?**

.. class:: rowstart-2 rowspan-5
.. sidebar::

   .. figure:: /images/tarot_tower_reversed_rider_waite.jpg
         :alt: Reversed illustration of The Tower card from the Rider–Waite tarot deck. Two figures, one crowned, fall from a tall stone tower struck by lightning and engulfed in flames. The card is upside down, with the word "TOWER" and Roman numeral "XVI" appearing inverted. The background shows dark clouds and yellow flames or sparks scattering across the sky.

         In tarot, *The Tower* upright signals sudden upheaval, collapse, or destruction. Reversed, it can represent a crisis narrowly averted, a chance to rebuild, or a transformation still unfolding. The foundations may be shaky, but the collapse is not inevitable. An apt metaphor for UploadWizard's fragmented metadata: though its historical record has eroded over time, the story may still be pieced back together, restoring memory before it's lost entirely. (`Pamela Colman Smith <https://en.wikipedia.org/wiki/Pamela_Colman_Smith>`__ on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:RWS_Tarot_16_Tower.jpg>`__ // Public domain)

In any corporate tech environment, this basic key performance indicator (KPI) would be displayed on an easily accessible metrics dashboard. But Wikimedia isn't a typical tech company. It started as a small, scrappy nonprofit, and it's always kept as little user data as possible to protect the privacy of its readers and contributors. And sometimes, the volunteer nature of Wikipedia and its sister sites makes it even more difficult to follow basic practices to measure a product's impact.

For you see, when it comes to UploadWizard, there is no central log, no consistent tag, no definitive metric. The metadata is incomplete and inconsistent. In a movement devoted to free knowledge and historical preservation, the impact of one of its most important tools has been left largely undocumented.

During the initial development of UploadWizard, we had included a tracking category called ``[[Category:Uploaded with UploadWizard]]`` as a basic product KPI. And for a while, it worked: this maintenance category, hidden from view, populated steadily with uploads from the new tool.

But years later, **the volunteer community decided that the tracking category was unnecessary**. I had managed to save it in 2012,\ [#CfD_uploadwizard_2012]_ but in 2016 it was deleted,\ [#CfD_uploadwizard_2016]_ and the software changed to no longer add it automatically (`gerrit:315121 <https://gerrit.wikimedia.org/r/c/operations/mediawiki-config/+/315121>`__), thus leaving no structured marker. UploadWizard was victim of its own success: volunteers deemed the category purposeless, because "UploadWizard is the default mode of upload." One volunteer likened the UploadWizard tracking category to "having an 'Articles created using the Edit Button' category on Wikipedia."

.. [#CfD_uploadwizard_2012] Wikimedia Commons contributors. "`Commons:Categories for discussion/2012/12/Category:Uploaded with UploadWizard <https://commons.wikimedia.org/wiki/Commons:Categories_for_discussion/2012/12/Category:Uploaded_with_UploadWizard>`__," *Wikimedia Commons*, December 2012.

.. [#CfD_uploadwizard_2016] Wikimedia Commons contributors. "`Commons:Categories for discussion/2016/08/Category:Uploaded with UploadWizard <https://commons.wikimedia.org/wiki/Commons:Categories_for_discussion/2016/08/Category:Uploaded_with_UploadWizard>`__," *Wikimedia Commons*, August 2016.

Recently, I set out to find other ways to measure the uploads. It wasn't just a matter of Wikimedian curiosity; it was about acknowledging an accomplishment and tracing the impact of work I had poured so much of myself into.

The metadata hadn't crumbled all at once. It had eroded quietly, over years of changes, edits, and well-meaning decisions. And yet, the traces were still there, winding out of time, if you knew how to look for them. This is the archaeological story of how I tried to reconstruct that lost history; not just by counting files, but by piecing together evidence across shifting metadata, deleted categories, forgotten patches, and overlapping logging mechanisms.


We're Off to See the Wizard
===========================

The question seemed deceptively simple: how many files had been uploaded using UploadWizard? At least 9 million as of August 2016, according to one comment in the community discussion that had led to the deletion of the category.\ [#CfD_uploadwizard_2016b]_ That was a start.

.. [#CfD_uploadwizard_2016b] "Categories for discussion/2016/08."

The tracking category had given us a built-in count, accessible to anyone and displayed prominently on the category's page. It was no longer available, but I knew of another way to identify the wizard's uploads: **the files would all have the same "logging comment"** for the upload, recorded as "User created page with UploadWizard." It would take a few database queries, but it was still easy enough. Or so I thought.

.. figure:: /images/uploadwizard_log_comment.png
   :figclass: light-img framed-img
   :alt: Screenshot of the file history section on Wikimedia Commons for the image “Tour Hertzienne de Mesnil-Esnard,” showing that the file was uploaded by user Guillom on 10 February 2014 with the comment “User created page with UploadWizard.”

   Screenshot of the file history for `one of my uploads <https://commons.wikimedia.org/wiki/File:Tour_Hertzienne_de_Mesnil-Esnard_(Seine-Maritime)_001.jpg#filehistory>`__ to Wikimedia Commons. The log entry shows the automated comment "User created page with UploadWizard."

The `Quarry <https://meta.wikimedia.org/wiki/Research:Quarry>`__ tool makes it possible to run queries on a copy of Common's database. In October 2016, `Steinsplitter <https://commons.wikimedia.org/wiki/User:Steinsplitter>`__ used the log comment method on Quarry and counted 10,228,537 uploads (`query/13031 <https://quarry.wmcloud.org/query/13031>`__).

.. figure:: /images/uploadwizard_log_comment_query_2016.png
   :figclass: light-img framed-img
   :alt: Screenshot of an SQL query run on the Wikimedia Quarry platform on October 10, 2016. The query counts the number of upload log entries with the comment "User created page with UploadWizard" and returns a result of 10,228,537.

   Screenshot of `query/13031 <https://quarry.wmcloud.org/query/13031>`__ run by Steinsplitter in October 2016 to count UploadWizard uploads using the log comment "User created page with UploadWizard." At the time, this query returned just over 10 million files. However, as I later discovered, this method excluded early uploads (before structured logging began in 2012).


This was a replicable, simple enough method. In October 2020, I used a similar approach to count UploadWizard files, although I had to adapt it due to changes in the structure of the database. My friend `Reedy <https://en.wikipedia.org/wiki/User:Reedy>`__ double-checked with his own query, and **we counted 20,231,414 files**. The number was growing over the years, which made sense.

.. .. class:: rowstart-5 rowspan-2
.. class:: rowspan-2

.. sidebar::
   
   Since 2016, the ``log_comment`` field had been deprecated and replaced by a ``log_comment_id`` (in the |mw_logging_table|_ ) pointing to an associated ``comment_id`` and ``comment_text`` (in the |mw_comment_table|_ ). A quick lookup showed that ``comment_text = "User created page with UploadWizard"`` was ``comment_id = 44`` (`query/41469 <https://quarry.wmcloud.org/query/41469>`__). From there, I could query the ``logging`` table using ``log_comment_id = 44``.

.. |mw_logging_table| replace:: ``logging`` table

.. _mw_logging_table: https://www.mediawiki.org/wiki/Manual:Logging_table

.. |mw_comment_table| replace:: ``comment`` table

.. _mw_comment_table: https://www.mediawiki.org/wiki/Manual:Comment_table

But when I ran the same query again in March 2025, the result was almost exactly the same as in 2020: 20,231,573 files, so I knew **something was wrong** (`query/42024 <https://quarry.wmcloud.org/query/42024>`__).


Down, Down, Down the Road, Down the Wizard's Road
=================================================

After some digging, I found out that Wikimedia's Multimedia team had **changed the log comment in 2020** and replaced it with two possible patterns: "Uploaded own work with UploadWizard" for volunteers uploading their own pictures, and a more complex one for for uploads of works by others: "Uploaded a work by $1 from $2 with UploadWizard" where ``$1`` is the copyright holder, and ``$2`` the source.\ [#translatewiki_uploadwizard2020]_ The former used a fixed format and could be queried easily. The latter, though, would vary from upload to upload.

.. [#translatewiki_uploadwizard2020] `MediaWiki message documentation <https://translatewiki.net/wiki/MediaWiki:Mwe-upwiz-upload-comment-third-party/qqq>`__ for "Mwe-upwiz-upload-comment-third-party," *TranslateWiki.net*, last modified October 21, 2020.

I looked up the identifier of the own-work pattern (`query/91991 <https://quarry.wmcloud.org/query/91991>`__) and queried the database, which returned 14,118,636 files (`query/42025 <https://quarry.wmcloud.org/query/42025>`__).

.. class:: rowspan-3
.. sidebar::

   Because Commons is the central media library for all 300+ language editions of Wikipedia, much of its software is translated in many languages, and I was worried I would have to repeat the queries in hundreds of languages.
   
   Spanish-language contributors often prefer to localize their interface, so it was a good language to test if the translations were being used. The `Spanish translation <https://translatewiki.net/wiki/MediaWiki:Mwe-upwiz-upload-comment-own-work/es>`__ returned no result (`query/91992 <https://quarry.wmcloud.org/query/91992>`__), nor did the `French translation <https://translatewiki.net/wiki/MediaWiki:Mwe-upwiz-upload-comment-own-work/fr>`__ (`query/91993 <https://quarry.wmcloud.org/query/91993>`__).
   
   On further inspection, the original code commit for the message change confirmed that "These messages are localized server-side in order to use the wiki's language, not the user's language," which meant only the English message was used on Commons (`gerrit:625864 <https://gerrit.wikimedia.org/r/c/mediawiki/extensions/UploadWizard/+/625864>`__). Pfeww.

To look into the second pattern for uploads of third-party works, I had to use a regular expression: a pattern of text that matched comment uploads independently of each upload's details (`query/92166 <https://quarry.wmcloud.org/query/92166>`__). The query yielded 4,436,472 results, bringing the total to **a minimum of 38,836,118 files** uploaded with UploadWizard.

I was pretty happy with myself by that point, and decided to tabulate the results by year and month to visualize the growth over time. That's when I realized that the story was more complex, but it led me to eventually discover change tags.


Through Many Miles of Tricks and Trials
=======================================

When I broke down the uploads by year for the original log comment (`query/92164 <https://quarry.wmcloud.org/query/92164>`__), I noticed that **no files were listed for 2010 or 2011**. (There were also some anomalies uploaded after 2020, which I investigated later.) Further research indicated that the original log comment replaced in 2020 had only been introduced in 2012 (`gerrit:9714 <https://gerrit.wikimedia.org/r/c/mediawiki/extensions/UploadWizard/+/9714>`__), leaving out two years of uploads.

.. class:: rowstart-1 rowspan-3
.. sidebar::

   .. figure:: /images/The_Wonderful_Wizard_of_Oz_Book_-_p174_flipped.png
      :alt: Vintage ink illustration of the Cowardly Lion as illustrated by William Wallace Denslow in Lyman Frank Baum's 1900 edition of "The Wonderful Wizard of Oz." The lion is rearing back in alarm, with exaggerated wide eyes, flared mane, and open mouth showing sharp white teeth. The lion's beige body contrasts with its black outlines, and the background is fully transparent except for white details in the eyes and teeth.

      My reaction when I realized that the first two years of uploads didn't have the UploadWizard logging comment I could query. (William Wallace Denslow on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:The_Wonderful_Wizard_of_Oz_Book_-_p174.jpg>`__ // Public domain)

Checking some of my own uploads from that period (`December 2010 <https://commons.wikimedia.org/wiki/File:Fortaleza_do_Pico_Funchal_Madeira_-_076_-_Feb_2008.jpg#filehistory>`__, `March 2012 <https://commons.wikimedia.org/wiki/File:Jonah_Hill_and_Channing_Tatum_-_21_Jump_Street_027_-_WonderCon_2012.jpg#filehistory>`__), I confirmed that they had no log comment or initial edit summary. Their page history did reassure me that I had uploaded them with UploadWizard, since the tracking category had been removed in 2016 (`permalink/222387780 <https://commons.wikimedia.org/w/index.php?oldid=222387780>`__), when the community had decided to get rid of it (that same unfortunate decision that had started me on this whole wikiarchaeology expedition in the first place).

I realized that **the category removal might give me an indirect way to identify early uploads** between 2010 and 2012: they would contain an entry in their edit history with the mention "Category:Uploaded with UploadWizard removed per community decision." I just needed to make sure I excluded files already counted using the log comment method.

I got the associated identifier (`query/92177 <https://quarry.wmcloud.org/query/92177>`__, `query/92193 <https://quarry.wmcloud.org/query/92193>`__) and counted an **additional 529,936 files** uploaded with UploadWizard in 2010−2012, including some false positives that I ruled out later (`query/92202 <https://quarry.wmcloud.org/query/92202>`__).

.. class:: rowstart-4 rowspan-2
.. sidebar::

   Prior to August 2012, the upload message read "User created page with UploadWizard (alpha)", which might have given me a fourth message pattern to find files uploaded with UploadWizard between 2010 and 2012. Unfortunately, the same code commit (`gerrit:9714 <https://gerrit.wikimedia.org/r/c/mediawiki/extensions/UploadWizard/+/9714>`__) showed that the early "alpha" message wasn't recorded as a comment during the upload (confirmed by `query/92174 <https://quarry.wmcloud.org/query/92174>`__).


Winding Out of Time
===================

Through my digging, I came across a few related tickets in Phabricator, Wikimedia's platform for tracking feature requests and bugs. One of them was a request to "Use an informative, custom edit summary for every file uploaded with UploadWizard" (`T142687 <https://phabricator.wikimedia.org/T142687>`__), which gave me a scare because it would have made it impossible to do any sort of counting in the future. But I also found a request to "Mark UploadWizard uploads with a change tag" (`T121872 <https://phabricator.wikimedia.org/T121872>`__).

In MediaWiki, change tags are annotations for certain types of edits, for example if it was made with the visual editor, or if it reverted the content to a previous version.\ [#mw_tags]_ Matthias Mullie had added an ``uploadwizard`` tag to the software in May 2017 (`gerrit:337566 <https://gerrit.wikimedia.org/r/c/mediawiki/extensions/UploadWizard/+/337566>`__), as well as an ``uploadwizard-flickr`` tag for files from flickr. Unfortunately, the tags would only be applied to future uploads. Still, **the tags provided a new, easy, and reliable method** for counting post-2017 uploads, especially those after 2020 when the log message was split into two patterns.

.. [#mw_tags] "`Manual:Tags <https://www.mediawiki.org/wiki/Manual:Tags>`__," *MediaWiki*, last modified April 12, 2024.

In the end, I had identified five methods for counting uploads: 1. the removal of the original category, 2. the original log comment, 3. the two change tags, 4. the log comment for own works, and 5. the log comment for third-party works. I could safely ignore the latter two, but the remaining **three methods still overlapped** over many years, so I needed to figure out exact timestamps and boundaries to avoid double-counting.

.. figure:: /images/uploadwizard_markers.svg
   :figclass: light-img framed-img full-content
   :alt: A timeline diagram showing horizontal bands with the different detection methods, including the now-undeeded split log comment starting in 2020. The three other metadata markers overlap by several years.

   Timeline of the five distinct detection methods used to identify uploads made with UploadWizard over its lifetime, illustrating the fragmented nature of its historical metadata. Each method corresponds to a different metadata marker introduced at different stages: removal of the original category (2010−2016), original log comment (2012−2020), the uploadwizard change tag (2017 onward), and the now-undeeded log comments introduced in 2020.


A few more queries later, I had identified the timestamps for the first upload to use the log comment in 2012 (2012-08-23T20:33:03Z, `query/92207 <https://quarry.wmcloud.org/query/92207>`__), and for the first one to use the change tag (2017-05-10T19:47:57Z, `query/92206 <https://quarry.wmcloud.org/query/92206>`__). The early uploads from 2010−2012 were trickier because the removal of the category was a more fragile detection method.

I went looking through the archives of the Server admin log, which documents software deployments and other system operations in the Wikimedia infrastructure. An entry by Roan Kattouw indicated that UploadWizard had been deployed to Commons on November 30, 2010 at 11:29.\ [#catrope_SAL]_

.. [#catrope_SAL] `Server Admin Log/Archive 17: November 30 <https://wikitech.wikimedia.org/wiki/Server_Admin_Log/Archive_17#November_30>`__, *Wikitech*: ``11:29 logmsgbot: catrope synchronized php-1.5/wmf-config/InitialiseSettings.php 'Enable UploadWizard on commonswiki'``. 

This gave me a strict boundary and it narrowed down the search for the first file uploaded with UploadWizard. I  looked for pages created that day that were later edited to remove the UploadWizard category (`query/92267 <https://quarry.wmcloud.org/query/92267>`__), and found a photo of the `TV Tower of East Berlin <https://commons.wikimedia.org/wiki/File:TV_Tower_of_East_Berlin.jpg>`__ uploaded shortly after deployment by `Neil Kandalgaonkar <https://commons.wikimedia.org/wiki/User:NeilK>`__, the lead developer of UploadWizard. It is likely that Neil uploaded this file both as an initial test to verify that the tool had been successfully enabled on Commons, and as a fitting inauguration, making it a historically significant first use of the feature.

.. sidebar::

   When I investigated false positives from the category removal method, I found examples where volunteers had accidentally added the category manually even though they hadn't used UploadWizard (`permalink/190105979 <https://commons.wikimedia.org/w/index.php?diff=190105979>`__). I considered looking for pages whose *first revision* included the category (meaning it would have been added by the software itself), but revision text unfortunately can't be queried on Quarry.


Pulling back the curtain
========================

And so, at last, I had all the ingredients for my spell: I had three detection methods, each clearly bounded to avoid false positives and double-counting.

.. figure:: /images/uploadwizard_markers_boundaries.svg
   :figclass: light-img framed-img full-content
   :alt: A stylized timeline showing three colored segments representing different metadata markers used to identify UploadWizard uploads, with vertical lines marking the exact timestamp boundaries between each period.

   This timeline shows the precise the start and end dates for each metadata marker used to detect UploadWizard uploads, making it possible to measure  usage across its full history without overlap.


Once I had assembled a methodology and carved out clean timestamp boundaries for each detection method, I was finally able to begin extracting numbers, and the stories they told.

As of April 21, 2025, **1,820,907 unique volunteers** have uploaded a total of **42,596,080 media files** to Commons with UploadWizard (`query/92995 <https://quarry.wmcloud.org/query/92995>`__, `query/92994 <https://quarry.wmcloud.org/query/92994>`__). The monthly breakdown in the following chart shows the growth rate over the past 15 years, as well as the yearly spikes corresponding to contribution campaigns and global contests like Wiki Loves Monuments (in September−October each year).

.. sidebar::

   It seems somehow fitting that the final tally is 42 million and change, as if representing the answer to Life, Commons, and Everything.

.. figure:: /images/uploadwizard_uploads_by_month.svg
   :figclass: light-img framed-img full-content
   :alt: A vertical bar chart titled “Monthly UploadWizard Uploads (2010–2025)” showing total uploads per month. The x-axis labels show only January of each year from 2011 to 2025. The y-axis ranges from 0 to 600,000 uploads. Notable annual spikes appear around September each year, reflecting seasonal campaign activity.

   Monthly uploads to Wikimedia Commons using UploadWizard, from its launch in November 2010 through April 2025. The chart shows strong annual cycles, with peaks around September, coinciding with Wiki Loves Monuments. The gradual growth over time reflects UploadWizard's role as the primary contribution tool for media files.


To better understand contributor behavior, I ran a query to group UploadWizard users into buckets based on how many files they had uploaded over time (`query/92997 <https://quarry.wmcloud.org/query/92997>`__). The engagement distribution reveals a classic long-tail pattern: of the 1.8 million volunteers who used UploadWizard, nearly half uploaded only a single file, and another 40% contributed fewer than ten. These numbers are consistent with Commons’ role as an open platform, where many users participate sporadically, often to share a single image of personal or local relevance. These numbers were evidence of a tool doing the work it was designed to do: helping people contribute freely licensed media to the world.

.. figure:: /images/uploadwizard_contributors_buckets.svg
   :figclass: light-img framed-img
   :alt: The horizontal bar chart titled "UploadWizard Contributors by Number of Uploads" visualizes the distribution of users based on how many files they uploaded using the tool. It shows that 891,614 users uploaded just one file, while 736,928 users uploaded between 2 and 10 files. Another 165,996 users uploaded between 11 and 100 files, and 22,068 users uploaded between 101 and 1,000 files. At the highest end of the spectrum, 4,302 users uploaded over a thousand files each.

   Distribution of UploadWizard contributors by number of uploads. While the tool lowers barriers for newcomers (over half the users uploaded only once), it's also used by dedicated contributors: more than 4,300 users have uploaded over a thousand files each, highlighting the tool’s long-term utility and wide adoption.


But another story also lies in the deeper tiers: over 22,000 contributors uploaded between 101 and 1,000 files, and more than 4,300 users crossed the 1,000-file threshold. These power contributors (just 0.2% of all uploaders) account for a disproportionate share of Commons' visual knowledge. Their sustained participation underscores that **UploadWizard isn't just a tool for newcomers**. This highlights the importance of balancing ease of use with the advanced needs of experienced users. Designing for both ends of that spectrum is key to growing and sustaining Commons' media ecosystem. 


No One Mourns the Wizard's metadata
===================================

Looking back, the amount of effort it took to reconstruct the history of UploadWizard's usage is perhaps the most ironic aspect of this excavation. Wikimedia is a movement obsessed with preservation: we document every edit, every template, every discussion. We track every page's revision history in minute detail. And yet, the historical record of one of the most significant tools used to contribute content to Commons was never formally maintained.

That's not to say it was malicious, or even careless. It was simply a mismatch of priorities. The category was seen by volunteers as clutter and removed, a reasonable decision made in good faith. But from a product perspective, such decisions can carry unintended consequences, like the **loss of institutional memory**.

.. class:: rowstart-1 rowspan-4
.. sidebar::

   .. figure:: /images/tarot_queen_of_cups_rider_waite.jpg
         :alt: The Queen of Cups card from the Rider–Waite tarot deck. A crowned woman in flowing robes sits on a stone throne by the sea, gazing thoughtfully into an ornate, lidded chalice. The throne is adorned with carvings of sea nymphs, and her feet rest lightly on colorful stones at the water’s edge.

         The *Queen of Cups* holds space for memory and meaning, and evokes the quiet, determined act of care, tending to what might otherwise be lost. (`Pamela Colman Smith <https://en.wikipedia.org/wiki/Pamela_Colman_Smith>`__ on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Cups13.jpg>`__ // Public domain)

Today, measuring the impact of a new tool is much more straightforward: improvements to the platform, like change tags, make measurement easier, and Wikimedia now has full-time product analytics staff involved at every step of the development process. A decade ago, categories and log comments were all we had. Tools like UploadWizard are still in use and central to the contributing experience, but measuring their impact takes more determination. Or, as a mustached orange fluffball would say, someone who cares a whole awful lot.

Like Merlin in *The Once and Future King*, I found myself living backwards in time,\ [#White2011_27]_ remembering what the system once knew, even as its present structure forgot. Querying the past through metadata felt less like analysis and more like reconstruction: following traces not because they were meant to be followed, but because they hadn't yet disappeared.

.. [#White2011_27] T. H. White, *The Once and Future King* (Ace Books, 2011), 27. "It takes practice to see things from the future. But I can tell you one thing. When you are living backwards like me, you learn things in the wrong order."

This fragility, the slow disappearance of signals, is why this work felt more like archaeology than analysis. I wasn't pulling data from a dashboard; I was excavating buried layers, hoping that enough of the traces remained to reconstruct a timeline.


The Wizard and I
================

The last time I tried to count UploadWizard uploads was in 2020. Back then, I used the log comment method and came up with about 20 million files, which already felt staggering. What I didn't realize at the time was that this method missed the first two years of uploads entirely, and that the logging pattern was just about to change.

This time, I discovered twice that amount: **a full third of all files on Commons**. When I first moved to San Francisco and began working on UploadWizard, I couldn't have imagined that the tool would still be in use 15 years later, largely unchanged, and that the numbers would be so vast. It's humbling, a little surreal, and deeply gratifying.


.. class:: rowspan-3
.. sidebar::

   .. figure:: /images/The_Wonderful_Wizard_of_Oz_Book_-_p151.jpg
      :alt: Vintage illustration of the Wizard and Dorothy as illustrated by William Wallace Denslow in Lyman Frank Baum's 1900 edition of "The Wonderful Wizard of Oz." The Wizard's large disembodied head floats above a jeweled throne with a stern expression. A small girl (Dorothy) stands in the foreground, facing the head with her back to the viewer. The scene is bathed in green hues and a dramatic spotlight.

      "The Eyes looked at her thoughtfully." (William Wallace Denslow on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:The_Wonderful_Wizard_of_Oz_Book_-_p151.jpg>`__ // Public domain)


What stayed with me most throughout this archaeological expedition wasn't just the technical puzzle; it was the reassembly, the emotional arc of uncovering it. The joy of finding Neil's first test upload. The frustration of queries that almost worked. The satisfaction of unlocking the Grimmerie and watching the story piece itself back together, one log comment and patch note at a time.

I didn't initially set out to revisit the most important project of my early career; I just wanted to answer a simple question. But as I sifted through missing metadata and fading fragments, I found myself face-to-face with something much more personal: the enduring presence of a tool I helped bring into the world.

This exploration wasn't merely about product analytics and KPIs. It was an act of stitching Commons' memory back together (and in the process, restitching my own) through the quiet, persistent work of following traces others had left behind. It was about memory, continuity, and the fragile threads that hold institutional knowledge together. I set out to measure a tool's impact; through some magic, I ended up unearthing my own legacy.

