.. title: Lecture de fichiers PDF sur les projets Wikimedia
.. slug: lecture-de-fichiers-pdf-sur-les-projets-wikimedia
.. date: 2009-09-04 22:03:30
.. tags: Wikimedia


Depuis quelques années, le logiciel MediaWiki (sur lequel reposent `Wikipedia <http://fr.wikipedia.org>`__ et tous les autres sites hébergés par la `Wikimedia Foundation <http://wikimediafoundation.org>`__) permet de visualiser directement le contenu d'un fichier `DjVu <http://fr.wikipedia.org/wiki/DjVu>`__. DjVu est un « format de fichier destiné à l'archivage de documents numériques ».

Cette fonctionnalité de lecture directe est particulièrement utile pour le projet `Wikisource <http://fr.wikisource.org>`__, la bibliothèque numérique construite par Wikimedia. Les participants du projet Wikisource relisent des documents scannés, convertis en format DjVu, et les transcrivent en plein texte.

Il utilisent généralement un programme de reconnaissance automatique de caractères pour effectuer le plus gros du travail, et corrigent ensuite manuellement les erreurs ou les caractères non reconnus. L'affichage direct du contenu des fichiers DjVu (à n'importe quelle page) facilite cette relecture, en `affichant côte à côte  <http://fr.wikisource.org/wiki/Page:Emile_Zola_-_La_B%C3%AAte_humaine.djvu/35>`__ le fichier scanné et le texte reconnu [#]_.

Le support des fichiers DjVu par MediaWiki est vraiment très pratique ; cela dit, ce format est assez peu utilisé. La majorité des documents produits aujourd'hui sont exportés au format PDF, dont l'affichage n'est pas nativement supporté par MediaWiki.

Ainsi, lorsque j'ai téléchargé sur Wikimedia Commons ma thèse de doctorat, j'ai importé le `fichier PDF original <http://commons.wikimedia.org/wiki/File:Guillaume_Paumier_-_Technologies_PNIPAM_pour_les_laboratoires_sur_puces.pdf>`__ , et une `version DjVu du même document <http://commons.wikimedia.org/wiki/File:Guillaume_Paumier_-_Technologies_PNIPAM_pour_les_laboratoires_sur_puces.djvu>`__, afin de permettre la consultation directe du document en ligne (sans avoir besoin de le télécharger).

La bonne nouvelle du jour est que **MediaWiki sait maintenant afficher, de façon analogue aux fichiers DjVu, le contenu d'un fichier PDF**, grâce à une extension de MediaWiki appelée |pdfhandler|_. Il est donc désormais possible de consulter les fichiers PDF directement via MediaWiki, comme par exemple les `présentations effectuées à Wikimania <http://wikimania2007.wikimedia.org/wiki/File:GPaumier-Visualidentity-WM2007.pdf>`__.

.. |pdfhandler| replace:: *PDFHandler*

.. _pdfhandler: http://www.mediawiki.org/wiki/Extension:PdfHandler

Cette nouvelle fonctionnalité sera également particulièrement utile dans le cadre de la |wmdoc|_, car elle permettra de consulter les documents produits, dans leur ensemble, sans avoir besoin de les télécharger préalablement.

.. |wmdoc| replace:: *Wikimedia documents initiative*

.. _wmdoc: http://guillaumepaumier.com/2009/05/20/introducing-the-wikimedia-documents-initiative/



.. [#] Par l'intermédiaire d'une extension de MediaWiki appelée |proofread|_, autrement dit « relecture de page ».

.. |proofread| replace:: *Proofread Page*

.. _proofread: http://www.mediawiki.org/wiki/Extension:Proofread_Page
