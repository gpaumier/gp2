.. title: Frise interactive : Wikipédia en 2013
.. slug: frise-wikipedia-2013

.. highlights::

    Une frise chronologique interactive qui retrace les temps forts de Wikipédia et du mouvement Wikimedia en 2013.

`Voir la frise » <http://guillaumepaumier.com/fr/frises/wikipedia-en-2013/>`__
==============================================================================

J'aime beaucoup les frises chronologiques. Elles permettent de présenter
les faits de façon logique et naturelle, et je trouve qu'elles sont très
utiles pour comprendre comment les évènements passés ont mené au
présent. Il n'est pas toujours facile d'avoir du recul sur les
évènements récents ; d'un autre côté, il faut profiter du fait qu'ils
sont encore frais dans la mémoire collective pour les documenter. Un
jour de 2013, je suis tombé sur l'outil
`TimelineJS <https://github.com/NUKnightLab/TimelineJS>`__, une
bibliothèque JavaScript qui permet de générer des frises interactives.
Je l'ai trouvé sympathique sur le moment, mais sans y penser davantage.
En décembre, alors que j'essayais de récapituler ce qui s'était passé en
2013 au département technique de la Wikimedia Foundation, j'y ai repensé
et je me suis dit qu'une telle frise serait une manière originale de
présenter ce qui s'était passé dans le mouvement Wikimedia en 2013. La
façon la plus simple de créer une frise avec TimelineJS, c'est de
préparer toutes les informations dans un classeur Google Docs, de
générer la frise `sur le site de
Knightlab <http://timeline.knightlab.com/#make>`__ et d'intégrer ensuite
le code dans une page web. Cette approche est assez simple, et permet
aux utilisateurs d'utiliser l'outil même s'ils ne sont pas experts en
technologies web. Par contre, elle a aussi l'inconvénient de reposer sur
des outils externes et de risquer la transmission d'informations
personnelles des visiteurs à ces sites. J'ai donc choisi l'autre
approche, qui consiste à héberger la frise soi-même, ainsi que toutes
les images, et de préparer toutes les informations dans un fichier JSON
local. Après avoir rapidement mis en place le `dépôt sur
GitHub <https://github.com/gpaumier/timelines>`__, je me suis vite rendu
compte que le vrai défi n'était pas technique, mais bien éditorial : il
s'agissait de sélectionner les articles que j'allais inclure dans la
frise.

Sélection éditoriale
====================

Je suis parti du postulat selon lequel la plupart des évènements
remarquables auraient fait l'objet d'un article sur le `blog
Wikimedia <https://blog.wikimedia.org>`__, et je me suis donc plongé
dans les archives du blog. Je ne pouvais pas inclure tous les articles
parus en 2013 (environ 400), et ils ne méritaient pas tous non plus d'y
être ; j'ai donc fait une présélection, que j'ai ensuite affinée petit à
petit, jusqu'à ce qu'il n'en reste qu'une trentaine. J'ai dû laisser de
côté de nombreux articles ; par ailleurs, certains évènements n'ont pas
été mentionnés sur le blog Wikimedia. Mais au final, j'étais satisfait
de la sélection, qui donne à mon avis une bonne vue d'ensemble des
activités de mouvement Wikimedia. Ensuite, j'ai commencé à rédiger et
ajouter les informations dans le fichier JSON. Pour chaque évènement,
j'ai indiqué :

-  la date ;
-  un titre ;
-  un résumé de quelques lignes ;
-  une image d'illustration ;
-  la légende et les informations de droit d'auteur de l'image ;
-  une vignette de 32 pixels de large, utilisée dans la frise de
   navigation.

Avec TimelineJS, on peut également trier les évènements par sujet
(jusqu'à six sujets au total pour la frise) ; j'ai essayé cette
fonctionnalité, mais les titres étaient coupés par manque de place. Par
ailleurs, la frise était plus lisible quand les évènements étaient
arrangés librement. J'ai donc décidé au final de ne pas utiliser ces
tags. Rédiger les titres des diapositives n'a pas été chose facile :
j'ai dû redoubler d'imagination pour qu'ils puissent tenir dans la frise
de navigation, à côté des vignettes. C'était déjà un défi en anglais,
mais c'est devenu encore plus difficile lorsque j'ai traduit la frise en
français, qui est une langue plus bavarde. La plupart des articles
étaient assez faciles à illustrer ; j'ai dû recréer ou modifier la
plupart des captures d'écran, soit pour obtenir une image de meilleure
qualité, soit pour mettre en avant une certaine partie de l'interface.
Les vignettes, par contre, c'était une autre paire de manches : il est
difficile de créer une image reconnaissable quand on est limité à un
carré de 32 pixels de large. Ça m'a pris du temps, mais j'ai réussi à
créer des vignettes assez reconnaissables pour chaque diapositive. Pour
finir, j'ai rédigé des informations détaillées sur `le droit d'auteur et
les
licences <https://github.com/gpaumier/timelines/blob/gh-pages/wikipedia2013/CREDITS.md>`__
des fichiers multimédia inclus dans la frise, en plus des indications
données dans les diapositives.

Intégrer la frise dans le site
==============================

À l'origine, j'ai fait tout ce travail de préparation dans une simple
page HTML indépendante, dans laquelle la frise était affichée en
remplissant toute la fenêtre. Dans l'idéal, je voulais l'intégrer
ensuite dans l'arborescence du site, avec une apparence cohérente, les
menus, etc. TimelineJS utilise `LESS <http://lesscss.org/>`__ pour
écrire et compiler les styles CSS. J'ai appris à écrire du LESS quelques
semaines plus tôt, quand j'ai construit
`Fumseck <//guillaumepaumier.com/project/fumseck/>`__, le thème
WordPress utilisé sur ce site. J'ai donc pu modifier les fichiers pour
remplacer les couleurs de la frise par la palette
`Solarized <http://ethanschoonover.com/solarized>`__, et les polices de
caractère par la famille `Latin
Modern <http://www.gust.org.pl/projects/e-foundry/latin-modern>`__. Dans
la mesure du possible, j'ai conservé les fichiers originaux et compilé
le CSS à partir des fichiers sources s'ils n'avaient pas été modifiés.
Mon objectif était de réduire les conflits potentiels lors des futures
mises à jour de TimelineJS. Pour finir, j'ai créé un modèle de page dans
le thème WordPress pour y intégrer la frise en pleine largeur. Une fois
la frise `terminée en
anglais <//guillaumepaumier.com/timelines/wikipedia-in-2013/>`__, je
suis passé à la traduction en français. Je me suis dit que les
francophones apprécieraient de pouvoir consulter la frise chronologique
dans leur propre langue, même si les articles du blog Wikimedia étaient
en anglais. J'ai donc traduit les titres, les textes, les légendes, les
crédits, et créé `la version française de la
frise <//guillaumepaumier.com/fr/frises/wikipedia-en-2013/>`__ dans
WordPress. Je suis très content du résultat, et les réactions ont été
très positives. Certains de mes collègues m'ont demandé si TimelineJS
pourrait remplacer (ou complémenter) l'\ `outil de
frise <https://www.mediawiki.org/wiki/Extension:EasyTimeline>`__
actuellement utilisé sur Wikipédia, qui commence à dater sérieusement.
Je ne suis pas sûr que TimelineJS soit assez robuste pour survivre aux
hordes de Wikipédiens, mais dans tous les cas, j'espère que nous aurons
un jour à notre disposition un meilleur outil permettant d'afficher des
chronologies dans Wikipedia, peut-être en utilisant Wikidata. Cela
rendrait les articles de Wikipédia plus interactifs et permettrait aussi
de documenter notre propre histoire plus facilement.
