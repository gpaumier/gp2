.. title: Faire des frises chronologiques vectorielles dans Wikipedia
.. slug: faire-des-frises-chronologiques-vectorielles-dans-wikipedia
.. date: 2009-05-11 16:06:56
.. tags: SVG,Ingénierie,Wikimedia,Wikipedia
.. description: 
.. excerpt: Dans la rubrique « les astuces techniques dont vous vous demandez comment vous avez fait pour vous en passer », je vous présente : la création de frises chronologiques dans Wikipedia qui génère automatiquement une image vectorielle (donc redimensionnable et modifiable à volonté sans perte de qualité).


Dans la rubrique « les astuces techniques dont vous vous demandez comment vous avez fait pour vous en passer[1. « Trop mega super cool », comme dirait `Thomas <http://thomas.holba.ch>`__.] » voici la création de frises chronologiques dans Wikipedia qui génère automatiquement une image vectorielle (donc redimensionnable et modifiable à volonté sans perte de qualité).

L'extension EasyTimeline
========================

Un bref rappel technique : `Wikipedia <http://www.wikipedia.org>`__ repose sur le logiciel `MediaWiki <http://www.mediawiki.org>`__ et un certain nombre d'\ `extensions <http://www.mediawiki.org/wiki/Extension_Matrix>`__ qui *étendent* les fonctionnalités du logiciel de base. L'une de ces extensions, *`EasyTimeline <http://www.mediawiki.org/wiki/Extension:EasyTimeline>`__* (« chronologie facile[2. J'avoue, j'ai hésité à traduire ça par « frise facile », mais j'ai déjà dépassé mon quota de jeux de mots de la journée.] »), permet de construire des frises chronologiques. Son auteur est `Erik Zachte <http://en.wikipedia.org/w/index.php?title=User:Erik_Zachte&oldid=264663975>`__, qui entre temps a été recruté par la Wikimedia Foundation pour maintenir à jour un système de statistiques sur les sites Wikimedia.

Comment ça fonctionne
=====================

En résumé, pour ajouter une frise chronologique dans Wikipedia, il faut entrer les données dans un code spécifique qu'Erik juge « raisonnablement intuitif ». Il ajoute cependant que « pour les débutants, « Chronologie Facile » peut ne pas être facile du tout ». Il recommande donc de s'inspirer du code de frises déjà existantes et de les adapter en fonction de ses besoins. Le code devient rapidement complexe et imposant, à tel point qu'il est souvent exilé dans des pages spécifiques (« `modèles <http://en.wikipedia.org/wiki/Category:Graphical_timeline_templates>`__ ») dont uniquement le résultat est affiché dans l'article de Wikipedia. Il est ainsi possible de créer des frises chronologiques sur l'\ `histoire de l'Empire Ottoman <http://en.wikipedia.org/w/index.php?title=Template:Timeline_of_the_Ottoman_Empire&oldid=213868355>`__ ou les `modèles successifs d'iPod <http://en.wikipedia.org/w/index.php?title=Template:Timeline_of_iPod_models&oldid=284533582>`__.

Réutiliser une frise générée avec EasyTimeline
==============================================

Tout cela est bien sympathique, mais comment réutiliser une telle frise ? Le contenu de Wikipedia est sous licence libre, ce qui autorise quiconque à le réutiliser pour tout usage. Imaginons que je souhaite réaliser un poster sur l'histoire de l'iPod[3. Non, ça ne m'arrive pas tous les jours. Soyez coopératifs, c''est pour les besoins de l'expérience. ]. Je peux reprendre le contenu de l'article de Wikipedia, sous réserve que je crédite les auteurs de façon appropriée. Mais comment afficher la frise chronologique sur le poster ? Dans la plupart des navigateurs, un clic droit sur la frise permet d'afficher uniquement l'image. On peut alors sauvegarder le `résultat de la frise au format PNG <https://upload.wikimedia.org/wikipedia/en/timeline/12b44a41e0bacff3b31736eca3700d72.png>`__. Cette image peut ensuite être réutilisée ailleurs, par exemple dans le présent article : |Frise chronologique des modèles d'iPod| Frise chronologique des modèles d'iPod Le contenu est sous `licence GFDL <http://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License>`__ et la liste des auteurs accessible depuis l'\ `historique des modifications <http://en.wikipedia.org/w/index.php?title=Template:Timeline_of_iPod_models&oldid=284533582>`__ de la frise.

Où est l'image vectorielle ?
============================

Le souci avec cette image PNG est qu'elle est `matricielle <http://fr.wikipedia.org/wiki/Image_matricielle>`__ (*bitmap*) : si on l'agrandit, elle va devenir pixelisée. Idem si l'on souhaite modifier l'image ou le texte : il faut soit modifier le fichier image (ce qui est peu pratique), soit modifier directement la frise sur Wikipedia (ce qui n'est pas nécessairement souhaitable). C'est là qu'est l'astuce : lorsqu'on affiche l'image seule dans le navigateur, il suffit de remplacer l'extension du fichier XXX\ **.png** par `XXX\ **.svg** <http://upload.wikimedia.org/wikipedia/en/timeline/12b44a41e0bacff3b31736eca3700d72.svg>`__. Automatiquement, une version `vectorielle <http://fr.wikipedia.org/wiki/Image_vectorielle>`__ générée par le logiciel s'affiche dans le navigateur[4. Si vous utilisez un navigateur non conforme aux standards du web, par exemple Internet Explorer, il est possible que l'image ne s'affiche pas, mais qu'elle soit proposée au téléchargement.]. On peut alors sauvegarder ce fichier SVG et le modifier dans un logiciel tel qu'Inkscape ; dans le cas de mon poster, je peux l'intégrer directement dans Scribus et l'agrandir à volonté. Certes, je n'ai jamais été un expert en frises chronologiques sur Wikipedia, mais il m'aura fallu presque quatre ans pour découvrir cette fonctionnalité.

Notes et références
===================

.. |Frise chronologique des modèles d'iPod| image:: //guillaumepaumier.com/wp-content/uploads/2009/05/ipod-timeline.png
   :target: http://en.wikipedia.org/w/index.php?title=Template:Timeline_of_iPod_models&oldid=284533582
