.. title: Surface functionalization for fluorescence immunoassays and microsystems
.. category: projects-en
.. subtitle: Surface functionalization
.. slug: biochips
.. date: 2004-09-01T00:00:00
.. end: 2008-11-06T00:00:00
.. image: /images/DNA_microarray_23.svg
.. tags: biochips, surface functionalization, silane
.. template: page_custom.tmpl
.. has_math: yes

.. TODO: fix dates, fix title & subtitle



.. figure:: /images/DNA_microarray_23.svg
   :figclass: lead-figure
   :alt: Illustration of a DNA microarray, showing rows of color dots


.. highlights::

    add abstract here

• Developed a miniaturized fluorescence-based immuno-assay on a microarray.
• Adapted a liquid phase surface chemistry protocol to a vapor phase protocol for microsystems.

Laboratory for Functionalization and Chemistry for Microsystems (LFCM) of the CEA-Léti in Grenoble, France. CEA-Léti is one of the world's largest organizations for applied research in microelectronics and nanotechnology.

Technical abstract
==================

In this study, I adapted a capillary-based immunoassay to a planar fluorescence microarray, and developed a vapor-phase silanization protocol for use in peptide digestion microsystems.

The biological model concerns a neuropeptide known as Substance P (SP), and the anti-SP monoclonal antibody mAb SP31. These molecules are grafted on functionalized glass slides using the CEA-2 liquid-phase silanization protocol, based on 5,6-epoxyhexyltriethoxysilane. The amine functions of the proteins and peptides covalently bind to the silane's aldehyde ending. I developed two tests: immobilization of antibodies revealed with fluorescent antigens, and immobilization of peptides revealed with marked antibodies. The binding of biological probes on the surface was optimized, as well as the revealing steps with the target.

In order to facilitate the transfer of this protocol to microsystems, I developed a vapor phase adaptation of the CEA-2 silanization protocol, and validated it using contact angle measurement and atomic force microscopy. After optimizing the protocol on glass slides with the SP/anti-SP model, I applied it to microsystems for proteomics. In particular, I explored the vapor-phase silanization of peptide digestion microreactors developed for the BioChipLab project.

Biochips
========

Rationale and applications
~~~~~~~~~~~~~~~~~~~~~~~~~~

high throughput testing , sensitivity, large scale

biochips and microarrays: high density of biological probes, and small amounts of biological materials

Fluorescence in biochips
~~~~~~~~~~~~~~~~~~~~~~~~

Fluorescence, fluorophores


.. figure:: /images/Biochips_Jablonski_diagram.svg

   The Jablonski diagram shows (1) the excitation of the fluorophore to an excited electronic state S'1 by absorption of a photon of energy *h νex*, (2) vibrational relaxation to a lower-energy state S1, and (3) the return to the original electronic state S0 by emission of a photon of energy *h νem* lower than that of the absorbed photon.

fluorescence scanner

.. figure:: /images/Biochips_Stokes.svg

   The emission of a photon of lower energy than the absorbed photon causes the Stokes shift: a difference between the absorption spectrum and the emission spectrum to a longer wavelength *λ*, which makes measurement possible.


Printing biological microarrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

variety of biological molecules can be printed, like DNA, proteins, and antibodies

.. figure:: /images/Biochips_spotter.jpg

   Microarrays are printed in a clean room environment using a Packard BioChip Arrayer. Its four piezoelectric capillary tips deposit samples on the surface without contact, using technology similar to ink jet printing. Droplets have a volume of around 350 pL and leave the piezo tips with a kinetic energy lower than the substrate's surface energy, so that the droplet stays whole when it makes contact. The average diameter of spots printed on our silane layer is 150 µm.



.. Vidéo : /videos/Biochips_spotting.mov

Surface functionalization
=========================

Scientists from the LFCM laboratory developed a chemical protocol to attach biological molecules to an inorganic surface like glass or metallic oxides. Known as "CEA-2," the protocol is based on a *silane* and therefore called *silanization*.

.. figure:: /images/Biochips_silane.svg

   Chemical formula of 5,6-epoxyhexyltriethoxysilane (CAS: 86138-01-4), the basis for CEA-2 surface functionalization.

.. class:: expert

   After a surface activation in a basic environment, the silanization binds 5,6-epoxyhexyltriethoxysilane to the surface and creates Si--O--Si bonds. The silane's epoxide function is then opened into a diol function by acid hydrolysis. The last step, which consists in oxidizing the diol into an aldehyde, is done immediately before grafting biological probes, whose amine functions bind to the silane's aldehyde.

https://bases-brevets.inpi.fr/fr/document/FR2818662.html

Method of immobilizing probes, in particular for producing bio chips

.. container:: cea2-protocol

   .. figure:: /images/Biochips_functionalization_cea2_step1.svg
   .. figure:: /images/Biochips_functionalization_cea2_step2.svg
   .. figure:: /images/Biochips_functionalization_cea2_step3.svg
   .. figure:: /images/Biochips_functionalization_cea2_step4.svg
   .. figure:: /images/Biochips_functionalization_cea2_step5.svg
   .. figure:: /images/Biochips_functionalization_cea2_step6.svg

.. figure:: /images/Biochips_reactor.jpg

   A large desiccator serves as silanization reactor. Modified to hold up to forty glass slides or twenty-five 100-mm wafers, it improves reproducibility by silanizing  substrates in bulk.

Antibody microarray
===================

.. figure:: /images/Biochips_Substance_P.svg

   Substance P.

.. figure:: /images/Biochips_immunotest_paths.svg

   Stages of the protocol for three possible antibody microarray tests: (a) Direct verification of the immobilization of biotinylated antibodies on the surface, using streptavidinated fluorophores. (b) Direct reading of the binding of fluorescent peptides on immobilized antibodies. (c) Indirect reading of the binding of biotinylated peptides on immobilized antibodies, using streptavidinated fluorophores.

.. figure:: /images/Biochips_reaction_kinetics.svg

   Reaction kinetics


Vapor phase silanization
========================

Adapting the protocol
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Biochips_vapor_phase.svg

BioChipLab
~~~~~~~~~~
.. figure:: /images/Biochips_biochiplab.png

   BioChipLab digestion module with connectors. (F. Mittler / CEA-Léti)

.. figure:: /images/Biochips_biochiplab_230904_puce5.png

   Fluorescence microcopy confirmed the successful vapor-phase silanization of a BioChipLab digestion module, by binding  Cyanine3 phosphoramidite on the diol ending. The channel surface inside the assembled chip was activated using plasma before silanization. (F. Mittler / CEA-Léti)

.. figure:: /images/Biochips_digestion.png

   Mass spectrum of a sample of Cytochrome C (10 pmol/µL) digested by trypsine immobilized on a vapor-phase CEA-2 chemical layer. (F. Mittler / CEA-Léti)
