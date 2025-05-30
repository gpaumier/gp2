.. title: Retour sur l'incident technique de Wikipedia le 24 mars 2010
.. category: articles-fr
.. slug: incident-technique-wikipedia-24-mars-2010
.. date: 2010-03-25 00:00:00
.. tags: Wikimedia
.. keywords: Ingénierie, Wikimedia

.. highlights::

    Où l'on explique la succession de problèmes qui ont conduit à l'inaccessibilité de Wikipedia pendant plusieurs heures le 24 mars 2010.

Ce mercredi, je participais à une réunion de l'équipe technique de la Wikimedia Foundation quand `Mark Bergsma <http://wikimediafoundation.org/wiki/User:Mark_Bergsma>`__, notre *Networking Coordinator* basé à Amsterdam, a subitement dû s'absenter ; ce n'est que quelques instants plus tard que l'équipe a réalisé la raison de son départ.

Un incident de climatisation dans le `centre de traitement de données <http://fr.wikipedia.org/wiki/Centre_de_traitement_de_donn%C3%A9es>`__ d'Amsterdam a déclenché un mécanisme de protection des serveurs, qui se sont automatiquement arrêtés afin de se protéger de la chaleur. Le centre d'Amsterdam gère généralement le trafic des sites Wikimedia en Europe ; Wikimedia dispose de procédures automatiques afin de pallier rapidement ce type d'incident en redirigeant l'ensemble des requêtes européennes vers les serveurs situés en Floride.

Ce processus de redirection est basé sur le `DNS <http://fr.wikipedia.org/wiki/Domain_Name_System>`__, c'est à dire le système qui fait le lien entre un nom de domaine (par exemple, « wikipedia.org ») et l'adresse IP de la machine qui l'héberge (par exemple, « 208.80.152.2 »). Malheureusement, ce système de redirection était défaillant au moment de l'incident de climatisation. L'équipe a rapidement identifié et corrigé le problème, mais c'était trop tard : l'erreur s'était propagée sur Internet dans les bases de données DNS.

En tout et pour tout, l'incident de climatisation et l'incident de DNS interne n'ont duré que quelques minutes. Mais à cette chaîne d'incidents s'est ajouté un autre problème : les bases de données DNS sur le web ont conservé les valeurs erronées trop longtemps, malgré les consignes des serveurs de Wikimedia, qui indiquaient qu'elles devaient être corrigées rapidement. Ainsi, les utilisateurs ne pouvaient pas accéder à Wikipedia, même si Wikipedia était bien là, en parfaite santé.

Cette série d'incidents est assez semblable aux chaînes d'incidents utilisées dans l'analyse des catastrophes aériennes (modèle de Reason, aussi appelé « effet gruyère ») : pris séparément, ces problèmes ne sont pas graves, ni même visibles, mais leur combinaison a rendu Wikipedia inaccessible pendant plusieurs heures.

Cependant, ce n'est pas la fin de l'histoire.

Aussitôt le problème résolu, Mark a rapidement rédigé et publié `un article sur le blog technique de Wikimedia <https://diff.wikimedia.org/2010/03/global-outage-cooling-failure-and-dns/>`__. L'objectif était d'expliquer la cause du souci et de rassurer les utilisateurs. Mais la twittosphère était déjà en pleine ébullition, et `certains <http://twitter.com/Nishkid64/statuses/10990250168>`__ `utilisateurs <http://twitter.com/birrein/statuses/10990408932>`__ `ont eu <http://twitter.com/erwancario/statuses/10990393392>`__ `la bonne idée <http://twitter.com/kureimoru/statuses/10989893466>`__ d'indiquer que la passerelle sécurisée `secure.wikimedia.org <http://secure.wikimedia.org>`__, elle, fonctionnait toujours.

Cette passerelle, qui habituellement ne doit gérer qu'un faible trafic, a aussitôt été saturée. L'ironie, c'est que secure.wikimedia.org est hébergé sur le même serveur que le blog technique qui, du coup, n'était plus accessible. Et `demander aux internautes <http://twitter.com/arielglenn/statuses/10990794181>`__ de ne pas utiliser la passerelle sécurisée n'a eu aucun effet.

Du coup, l'équipe technique a décidé de désactiver temporairement secure.wikimedia.org, afin de rendre de nouveau accessible le blog technique, et ainsi l'article qui expliquait l'origine du problème.

La situation est revenue à la normale après quelques heures, au fur et à mesure que les bases de données DNS ont mis à jour leurs entrées. secure.wikimedia.org a été réactivé peu de temps après, quand la charge serveur est redevenue raisonnable.

L'un des projets sur lesquels l'équipe technique de Wikimedia a prévu de travailler prochainement est la création d'un « indicateur de statut » *(status board)*, qui indiquera aux utilisateurs la « santé » des sites Wikimedia à un moment donné, un peu à la manière du |apps dashboard|_. Cet indicateur, qui sera hébergé de façon indépendante, permettra de tenir les utilisateurs informés des éventuels soucis et du retour à la normale.

.. |apps dashboard| replace:: *Google apps status dashboard*

.. _apps dashboard: http://www.google.com/appsstatus

D'autres projets sont également en cours de finalisation afin d'améliorer de façon générale les performances et la redondance de l'infrastructure opérationnelle de la Wikimedia Foundation, en accord avec `les recommandations du plan stratégique <http://strategy.wikimedia.org/wiki/Wikimedia_Foundation/Feb_2010_Letter_to_the_Board>`__. J'y reviendrai dans quelques semaines.
