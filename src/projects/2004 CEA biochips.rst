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

Biochips and microarrays
========================

.. figure:: /images/Mouse_cdna_microarray.jpg

   Louis M. Staudt/NIH on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Mouse_cdna_microarray.jpg>`__ // Public domain

Rationale and applications
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Biochip.jpg

   `Argonne Laboratory <https://www.flickr.com/people/35734278@N05>`__ on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Biochip.jpg>`__ // `CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0/legalcode>`__


high throughput testing , sensitivity, large scale

biochips and microarrays: high density of biological probes, and small amounts of biological materials

Printing biological microarrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

variety of biological molecules can be printed, like DNA, proteins, and antibodies

biological probes are printed as micro-droplets onto silanized substrates, usually glass slides


.. figure:: /images/Biochips_spotter.jpg

   Microarrays are printed in a clean room environment using a Packard BioChip Arrayer. Its four piezoelectric capillary tips deposit samples on the surface without contact, using technology similar to ink jet printing. Droplets have a volume of around 350 pL and leave the piezo tips with a kinetic energy lower than the substrate's surface energy, so that the droplet stays whole when it makes contact. The average diameter of spots printed on our silane layer is 150 µm.



.. Vidéo : /videos/Biochips_spotting.mov


Fluorescence in biochips
~~~~~~~~~~~~~~~~~~~~~~~~

Fluorescence, fluorophores


.. figure:: /images/Biochips_Jablonski_diagram.svg

   The Jablonski diagram shows (1) the excitation of the fluorophore to an excited electronic state S':subscript:`1` by absorption of a photon of energy *h ν*:subscript:`ex`, (2) vibrational relaxation to a lower-energy state S\ :subscript:`1`, and (3) the return to the original electronic state S\ :subscript:`0` by emission of a photon of energy *h ν*:subscript:`em` lower than that of the absorbed photon.

fluorescence scanner

.. figure:: /images/Biochips_Stokes.svg

   The emission of a photon of lower energy than the absorbed photon causes the Stokes shift: a difference between the absorption spectrum and the emission spectrum to a longer wavelength *λ*, which makes measurement possible.



Surface functionalization
~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. figure:: /images/Biochips_236-30_532.jpg

Substance P
~~~~~~~~~~~

medical diagnosis, pharmaceutical research

antibody and antigens
antibody are very fragile proteins

substance P (SP): neurotransmitter  from the neurokinin family, synthesized by neurons and able to excite nearby neurons. Involved in many physiological systems, including  the transmission of pain information into the central nervous system

Laure-Marie Neuberger, from the *Laboratoire d'Études et de Recherches en Immunoanalyse* (LERI) of the CEA's Direction of Life Sciences. working on this model in capillaries


.. figure:: /images/Biochips_Substance_P.svg

   Substance P.

immunoassays
~~~~~~~~~~~~

A peptide was synthesized with a sequence similar to SP and an amine function added to its C-terminal ending to bind it to silane.

biotin/streptavidin: biotinylated antibodies and biotinylated antigens. streptavidin-Cyanine3 conjugates to reveal biotin

marked peptides: fluorescein, and later antibodies and peptides with Alexa532

Grafting chemical layer: CEA-2 protocol
Immobilization of biological probes on the chemical layer
rinsing and surface saturation
incubation with biological targets
revealing with fluorophores
fluorescence

.. figure:: /images/Biochips_immunotest_paths.svg

   Stages of the protocol for three possible antibody microarray tests: (a) Direct verification of the immobilization of biotinylated antibodies on the surface, using streptavidinated fluorophores. (b) Direct reading of the binding of fluorescent peptides on immobilized antibodies. (c) Indirect reading of the binding of biotinylated peptides on immobilized antibodies, using streptavidinated fluorophores.

Parameter study & protocol optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Biological parameters
---------------------

parameters studied (in collaboration with Isabelle Mingam)

first, testing the grafting of antibodies and antigens: grafting of biotinylated antibodies and antigens on the chemical layer, and direct verification using fluorescence.

blocking of free active sites: usually with neutral proteins like bovine serum albumin (BSA)

.. figure:: /images/Biochips_GP-08_bloc2_532.jpg

.. figure:: /images/Biochips_GP-02_bloc2_532.jpg

drying stage

.. figure:: /images/Biochips_GP-10_bloc2_532.jpg

glycerol content

.. figure:: /images/Biochips_217b-03_bloc1_532.jpg

Incubation duration and temperature

.. figure:: /images/Biochips_236-30_532.jpg

.. figure:: /images/Biochips_236-29_532.jpg


Chemical parameters
-------------------

grafting biological probes at other stages of the chemical functionalization

.. figure:: /images/Biochips_216-31_bloc2_532.jpg

.. figure:: /images/Biochips_216-07_bloc2_532.jpg

Reducing agent

.. figure:: /images/Biochips_217b-06_bloc2_532.jpg

.. figure:: /images/Biochips_217b-07_bloc2_532.jpg

Conclusion: optimized protocol

Reproducibility test

.. figure:: /images/Biochips_236-32_532.jpg

Chemical characterization
~~~~~~~~~~~~~~~~~~~~~~~~~

Reaction kinetics
-----------------

.. figure:: /images/Biochips_reaction_kinetics.svg

   Reaction kinetics

Photothermal deflection spectroscopy
------------------------------------

Photothermal deflection spectroscopy (PDS), also called "Mirage effect"

gold nanobeads

Violaine Vizcaino from the *Laboratoire d'Ingénierie des Composants Photoniques*

.. figure:: /images/Biochips_billes100.png

Neutron reflectometry
---------------------

Neutron reflectometer with horizontal scattering geometry

Institut Laue-Langevin (ILL) with Giovanna Fragneto
D17 reflectometer

Vapor-phase silanization
========================

.. figure:: /images/luke-besley-zAv-nWtQJlc-unsplash.jpg

   `Luke Besley <https://unsplash.com/@besluk>`__ on `Unsplash <https://unsplash.com/photos/zAv-nWtQJlc>`__

Adapting the protocol
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Biochips_vapor_phase.svg

Analysis of chemical layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Atomic force microscopy
-----------------------

.. figure:: /images/Biochips_244-2A.png

.. figure:: /images/Biochips_244-2B.png

.. figure:: /images/Biochips_239-5A.png

.. figure:: /images/Biochips_239-5B.png


Contact angle measurement
-------------------------

.. chart:: Box
   :title: 'Contact angle comparison between liquid phase and vapor phase silanization'
   :box_mode: extremes
   :legend_at_bottom: True
   :truncate_legend: -1

   'Epoxyde, liquid phase', [66.3, 64.5, 68.1, 68.4, 66.6, 66.4, 67.3, 65.5, 64.2, 62.8]
   'Epoxyde, vapor phase', [65.9, 66.1, 65.9, 66.2, 66.3, 65.8, 65.1, 65.9, 64, 64.7]
   'Diol, liquid phase', [56, 54.8, 54, 54.1, 53.5, 52.6, 53.2, 52, 51.4, 50.9]
   'Diol, vapor phase', [49.7, 51.1, 53.2, 52.9, 50.8, 50, 50, 49.1, 47.8, 50.1]



Fluorescence
------------

.. figure:: /images/Biochips_238a-02_532.jpg

.. figure:: /images/Biochips_236-29_532.jpg

Homogeneity and reproducibility
-------------------------------

.. figure:: /images/Biochips_245-02_532.jpg

BioChipLab
~~~~~~~~~~

intro
-----

.. figure:: /images/Biochips_biochiplab.png

   BioChipLab digestion module with connectors. (F. Mittler / CEA-Léti)

Fluorescence microscopy
-----------------------

.. figure:: /images/Biochips_biochiplab_230904_puce5.png

   Fluorescence microcopy confirmed the successful vapor-phase silanization of a BioChipLab digestion module, by binding  Cyanine3 phosphoramidite on the diol ending. The channel surface inside the assembled chip was activated using plasma before silanization. (F. Mittler / CEA-Léti)

Mass spectrometry
-----------------

.. figure:: /images/Biochips_digestion.png

   Mass spectrum of a sample of Cytochrome C (10 pmol/µL) digested by trypsine immobilized on a vapor-phase CEA-2 chemical layer. (F. Mittler / CEA-Léti)
