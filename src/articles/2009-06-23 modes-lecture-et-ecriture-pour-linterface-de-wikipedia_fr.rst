.. title: Modes « lecture » et « écriture » pour l'interface de Wikipedia
.. slug: modes-lecture-et-ecriture-pour-linterface-de-wikipedia
.. date: 2009-06-23 12:16:08
.. tags: Wikipedia
.. description: 
.. excerpt: Le dernier article de Pierrot le Chroniqueur est dédié au mini « flash actu » publié par le Figaro à propos d'un vandalisme tout à fait banal commis sur Wikipedia. J'ai rapidement évoqué cet entrefilet hier soir par l'intermédiaire d'un microblog. Je n'ai pas grand chose à dire de plus, si ce n'est qu'avec ce genre de stratégie, le Figaro est sûr d'avoir de la matière pour rédiger des « flash actu » pour longtemps. Je souhaite cependant revenir sur une idée soulevée par Pierrot dans le même billet. Pierrot propose de rendre le bouton « modifier » plus visible, peut-être dans le cadre de la nouvelle apparence de Wikipedia. Je pense qu'une piste plus prometteuse serait de proposer deux modes alternatifs de l'interface, l'un pour les lecteurs et l'autre pour les participants réguliers.


Le dernier article de Pierrot le Chroniqueur est dédié au mini « flash actu » publié par le Figaro à propos d'un vandalisme tout à fait banal commis sur Wikipedia: `*Le Figaro relève une "erreur" dans Wikipédia : remarques et idées* <http://wikirigoler.over-blog.com/article-32990612.html>`__. J'ai `rapidement évoqué cet entrefilet <http://identi.ca/notice/5629124>`__ hier soir par l'intermédiaire d'un microblog. Je n'ai pas grand chose à dire de plus, si ce n'est qu'avec ce genre de stratégie, le Figaro est sûr d'avoir de la matière pour rédiger des « flash actu » pour longtemps. Je souhaite cependant revenir sur une idée soulevée par Pierrot dans le même billet. Pierrot propose de rendre le bouton *modifier* plus visible, peut-être dans le cadre de la nouvelle apparence de Wikipedia. Je pense qu'une piste plus prometteuse serait de proposer deux modes alternatifs de l'interface, l'un pour les lecteurs et l'autre pour les participants réguliers.

Avoir un bouton « modifier » plus visible
=========================================

Pierrot écrit :

    Les gens qui surveillent (ou sont au courant de l'information) ne se sentent pas obligés de corriger l'erreur manifeste : Plastic Bertrand n'est pas un chanteur des années 30. Blague à part, le bouton modifier n'est pas un réflexe pour l'internaute. C'est parfois heureux, parfois moins comme ici. `Une remarque à creuser peut-être pour une nouvelle apparence de Wikipédia ? <http://guillaumepaumier.com/fr/2009/06/20/testez-le-prototype-de-la-nouvelle-apparence-de-wikipedia/>`__

Le bouton *modifier*, qui permet à tout internaute de modifier la page de Wikipedia qu'il est en train de lire (et donc de corriger une erreur) n'est en effet pas très visible. Il n'est pas rare, lorsque je présente Wikipedia lors d'une conférence, que certaines personnes de l'assistance soient surprises quand je leur apprends que tout le monde (eux compris) peuvent modifier un article. Un premier pas a été fait il y a quelques mois, quand un contributeur (connu sous son pseudonyme Kropotkine\_113) a proposé de changer l'apparence du bouton *modifier* pour le rendre plus visible. Suite à une `rapide consultation des participants <http://fr.wikipedia.org/w/index.php?title=Wikip%C3%A9dia:Le_Bistro/6_janvier_2009&oldid=41127708#Mettre_l.27onglet_.C2.AB_modifier_.C2.BB_.C3.A9crit_en_blanc_sur_fond_bleu>`__, l'apparence par défaut du site a été `très légèrement altérée <http://fr.wikipedia.org/w/index.php?title=MediaWiki:Monobook.css&diff=prev&oldid=36851095>`__ pour que le bouton *modifier* soit désormais en blanc sur fond bleu, dans l'espoir qu'il attire davantage l'attention des visiteurs. Cependant, une rapide consultation des `statistiques de Wikipedia <http://stats.wikimedia.org/EN/ChartsWikipediaFR.htm>`__ ne fait pas apparaître, à première vue, de changement majeur depuis janvier 2009.

Deux interfaces séparées
========================

Pierrot fait également référence à `mon précédent article <http://guillaumepaumier.com/fr/2009/06/20/testez-le-prototype-de-la-nouvelle-apparence-de-wikipedia/>`__, dédié au prototype de nouvelle apparence préparé par la *Wikipedia usability initiative*. Je ne crois cependant pas que rendre le bouton *modifier* plus visible soit dans les objectifs de l'équipe de Naoko Komura. La tendance actuelle de cette initiative est de simplifier l'interface et de réduire le bruit visuel. Cela dit, lors de ma présentation faite à Taipei pour Wikimania 2007, j'avais notamment évoqué la possibilité d'avoir deux modes d'interface pour Wikipedia : un mode « lecture » et un mode « écriture ». Il y a en effet un sérieux gap entre l'interface idéale du lecteur ou participant occasionnel et celle du rédacteur régulier :

-  Le lecteur s'intéresse essentiellement au contenu ; il a besoin qu'on lui rappelle le principe de Wikipedia (chacun peut modifier une page) et les conséquences qui en découlent (il faut conserver un esprit critique, vérifier les faits et croiser les sources). Il a également besoin d'être invité à participer, au besoin à l'aide d'un gros bouton *modifier* et d'un sympathique message incitatif. Par contre, il n'a pas besoin de liens vers les « modifications récentes », les « pages spéciales » et tout un tas de charabia et espaces techniques.
-  À l'inverse, le participant régulier n'a pas besoin qu'on lui rappelle qu'il peut modifier les pages du site. Il sait comment le schmilblick fonctionne, il cherche l'efficacité et les raccourcis, fussent-ils incompréhensibles.

À mon avis, le problème est précisément que des attentes et des besoins très différents doivent être balancés dans l'interface actuelle, qui ne propose pas les deux modes dont j'ai parlé. J'imagine pourtant qu'il serait assez simple de réaliser ces deux interfaces et de proposer de basculer d'un mode à l'autre en un clic.

Liste de suivi des sujets « sensibles »
=======================================

Pour finir, même si c'est un peu hors-sujet pour cet article, un rapide commentaire sur une autre proposition de Pierrot :

    Concernant les sujets considérés comme sensibles, il serait peut-être utile de pouvoir constituer une liste de suivie spécifique consultable à volonté. C'est faisable, certains projets en avait une, me semble-t-il.

Je ne suis pas persuadé que ce soit réellement nécessaire. Les articles « sensibles » et les plus souvent vandalisés sont déjà suivis par de nombreux participants. Par ailleurs, ces mêmes articles sont, si je me rappelle bien, particulièrement suivis par le programme anti-vandalisme Salebot, qui annule automatiquement la plupart des modifications non pertinentes. De temps en temps, un vandalisme passe au travers des mailles du filet, mais ce risque serait toujours présent si l'on rajoutait un autre outil à l'arsenal anti-vandalisme.
