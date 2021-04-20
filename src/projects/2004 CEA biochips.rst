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
   :alt: ustration of a DNA microarray, showing rows of color dots


.. highlights::

    add abstract here

• Developed a miniaturized fluorescence-based immuno-assay on a microarray.
• Adapted a liquid phase surface chemistry protocol to a vapor phase protocol for microsystems.

Laboratory for Functionalization and Chemistry for Microsystems (LFCM) of the CEA-Léti in Grenoble, France. CEA-Léti is one of the world's largest organizations for applied research in microelectronics and nanotechnology.

Technical abstract
==================

In this study, I adapted a capillary-based immunoassay to a planar fluorescence microarray, and developed a vapor-phase silanization protocol for use in peptide digestion microsystems.

The biological model concerns a neuropeptide known as Substance P (SP), and the anti-SP monoclonal antibody mAb SP31. These molecules are grafted on functionalized glass slides using the CEA-2 liquid-phase silanization protocol, based on 5,6-epoxyhexyltriethoxysilane. The amine functions of the proteins and peptides covalently bind to the silane's aldehyde ending. I developed two tests: immobilization of antibodies revealed with fluorescent antigens, and immobilization of peptides revealed with marked antibodies. The binding of biological probes on the surface was optimized, as well as the revealing steps with the target. I characterized the chemical and biological layers using contact angle measurement, photothermal deflection spectroscopy, and neutron reflectometry.

In order to transfer this protocol to microsystems, I developed a vapor phase adaptation of the CEA-2 silanization protocol, and validated it using fluorescence, contact angle measurement, and atomic force microscopy. After optimizing the protocol on glass slides with the SP/anti-SP model, I applied it to microsystems for proteomics. In particular, I explored the vapor-phase silanization of peptide digestion microreactors developed for the BioChipLab project.

----

Biochips and microarrays
========================

.. figure:: /images/Mouse_cdna_microarray.jpg

   Louis M. Staudt/NIH on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Mouse_cdna_microarray.jpg>`__ // Public domain

Microarrays contain thousands of spots containing biological probes, like DNA or proteins, attached to the surface via a chemical layer. They rely on fluorescence and help scientists test many different samples in parallel.

Mass parallel testing
~~~~~~~~~~~~~~~~~~~~~

Whether it is to find a vaccine, discover new drugs, diagnose patients, or study DNA, the motto is often the same: conduct more tests, more quickly. Mass testing enables biologists to try more molecules and vary experimental conditions, which helps them find the proverbial needle in the haystack of combinations.

The principle of biochips is similar to how progress in microelectronics has led to an increase in computing power, by decreasing the size of transistors and integrating more of them into a single chip. In biochips, laboratory functions and samples are miniaturized and thousands of experiments happen in parallel on a single chip. This kind of *high-throughput testing* enables scientists to conduct experiments and test many molecules at the same time, thus increasing efficiency.

.. figure:: /images/Biochip.jpg
   :figclass: biochip

   DNA microarray on a glass slide. (`Argonne Laboratory <https://www.flickr.com/people/35734278@N05>`__ on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Biochip.jpg>`__ // `CC BY-SA 2.0 <https://creativecommons.org/licenses/by-sa/2.0/legalcode>`__)

In particular, *microarrays* involve printing a large number of biological samples using a technology similar to inkjet printing. Small droplets are deposited on a surface in an regular pattern, leading to a high density of biological probes, and small amounts of biological materials used in each.

A variety of biological molecules can be printed into microarrays, like DNA, proteins, and antibodies. To ensure regularity and consistency, the samples are printed using a machine called a *spotter*, or micro-arrayer. The biological probes are printed as micro-droplets onto a chemical layer on top of substrates like glass slides.

Biological molecules, and antibodies in particular, are fragile. Droplets are printed very gently in order to maintain their cohesion on the surface. Glycerol is often added to the sample solutions to increase their viscosity, help the droplets keep their shape, and limit evaporation. Once printed, the samples must be cleaned softly and kept in an environment that preserves their integrity until the experiment is complete.

.. figure:: /images/Biochips_spotter.jpg
   :figclass: spotter

   At the LFCM lab, microarrays are printed in a clean room environment using a Packard BioChip Arrayer. Its four piezoelectric capillary tips deposit samples on the surface without contact, using technology similar to ink jet printing. Droplets have a volume of around 350 pL and leave the piezo tips with a kinetic energy lower than the substrate's surface energy, so that the droplet stays whole when it makes contact. The average diameter of spots printed on our silane layer is 150 µm.

.. Vidéo : /videos/Biochips_spotting.mov


Fluorescence in biochips
~~~~~~~~~~~~~~~~~~~~~~~~

Microarrays often rely on fluorescence as a detection mechanism. *Fluorophores* are molecules that absorb light at a certain color and re-emit it at another color. They are combined with biological molecules of interest to detect their presence or their interaction. Because fluorophores emit light at a different color (wavelength) than what they receive, scientists can separate the two colors, and measure only the light emitted in return: it indicates how many biological molecules (DNA strands, antibodies, etc.) are in a specific spot.

.. container:: fluorescence-diagrams

   .. figure:: /images/Biochips_Jablonski_diagram.svg

      The Jablonski diagram shows (1) the excitation of the fluorophore to an excited electronic state S':subscript:`1` by absorption of a photon of energy *h ν*:subscript:`ex`, (2) vibrational relaxation to a lower-energy state S\ :subscript:`1`, and (3) the return to the original electronic state S\ :subscript:`0` by emission of a photon of energy *h ν*:subscript:`em` lower than that of the absorbed photon.

   .. figure:: /images/Biochips_Stokes.svg

      The emission of a photon of lower energy than the absorbed photon causes the Stokes shift: a difference between the absorption spectrum and the emission spectrum to a longer wavelength *λ*, which makes measurement possible.

The intensity of fluorescence emitted by the molecules is measured by a scanner or a microscope, leading to grayscale images where brighter zones indicate more fluorescence emitted than darker ones. A palette of false colors is then used to interpret the results.

.. container:: fluorescence-palette

   .. figure:: /images/Biochips_236-32_532_closeup_raw.png
   .. figure:: /images/Biochips_236-32_532_closeup_colors.jpg
   .. figure:: /images/Biochips_palette.jpg
      :figclass: palette

   .. class:: caption

      Fluorescence is measured at the wavelength of the light emitted by the fluorophore, to filter out the light used to excite it. The raw image (left) therefore only measures intensity, from dark (no signal) to bright (fluorescence emitted). The final image (right) shows false colors after applying a palette for visualization (bottom).

Surface functionalization
~~~~~~~~~~~~~~~~~~~~~~~~~

Scientists from the LFCM laboratory have developed a chemical protocol to attach biological molecules to an inorganic surface like glass or metallic oxides.\ [#cea2]_ Known as "CEA-2," the protocol is based on a *silane* (a molecule that contains an atom of silicon) and therefore called *silanization*. The process involves successive steps that progressively modify the molecules on the surface using chemical treatments. In the final step, biological molecules of interest are spotted on the modified surface and bind to the chemical layer.

The CEA-2 protocol is an established way to attach biological molecules to surfaces, and is routinely used in the lab to print DNA microarrays on glass slides (as oligonucleotides). The slides are usually silanized in bulk to increase consistency and reproducibility of results.

.. figure:: /images/Biochips_silane.svg
   :figclass: silane

   Chemical formula of 5,6-epoxyhexyltriethoxysilane (CAS: 86138-01-4), the basis for CEA-2 surface functionalization. EtO represents ethoxy groups CH\ :subscript:`3`\ CH\ :subscript:`2`\ O–.

.. class:: expert

   In technical terms, after a surface activation in a basic environment, the silanization binds 5,6-epoxyhexyltriethoxysilane to the surface and creates Si--O--Si bonds. The silane's epoxide function is then opened into a diol function by acid hydrolysis. The last step, which consists in oxidizing the diol into an aldehyde, is done immediately before grafting biological probes, whose amine functions bind to the silane's aldehyde.

.. container:: cea2-protocol

   .. figure:: /images/Biochips_functionalization_cea2_step1.svg
   .. figure:: /images/Biochips_functionalization_cea2_step2.svg
   .. figure:: /images/Biochips_functionalization_cea2_step3.svg
   .. figure:: /images/Biochips_functionalization_cea2_step4.svg
   .. figure:: /images/Biochips_functionalization_cea2_step5.svg
   .. figure:: /images/Biochips_functionalization_cea2_step6.svg

.. figure:: /images/Biochips_reactor.jpg
   :figclass: reactor

   A large desiccator serves as silanization reactor. Modified to hold up to forty glass slides or twenty-five 100-mm wafers, it improves reproducibility by silanizing  substrates in bulk.

.. [#cea2] Françoise Vinet and Alain Hoang / Commissariat à l'Énergie Atomique. *Method of immobilizing probes, in particular for producing bio chips*. `Patent FR2818662 <https://bases-brevets.inpi.fr/fr/document/FR2818662.html>`__ (2002).

----

Antibody microarray on CEA-2 protocol
=====================================

.. figure:: /images/Biochips_236-30_532.jpg

TODO: add intro

Substance P
~~~~~~~~~~~

Substance P (SP) is a neurotransmitter from the neurokinin family, synthesized by neurons and able to excite nearby neurons. SP is involved in many physiological systems, including  the transmission of pain information into the central nervous system.

Substance P was used as a model molecule in the development of a novel approach to detect biological warfare agents, led by Laure-Marie Neuburger of the *Laboratoire d'Études et de Recherches en Immunoanalyse* (LERI).\ [#neuburger2006]_ Laure-Marie had been developing the immunoassay in capillaries, and produced the antibodies and antigens, conjugated with fluorophores or other molecules. I adapted Laure-Marie's immunoassay to planar microarrays using the CEA-2 protocol, traditionally used for DNA biochips.

.. [#neuburger2006] Laure-Marie Neuburger. *Design of fluorescence immunoassays. Perspectives for continuous monitoring of biological warfare agents.* Ph.D dissertation. Chemical Sciences, AgroParisTech, 2006. `pastel-00004770 <https://hal.archives-ouvertes.fr/pastel-00004770>`__.

.. figure:: /images/Biochips_Substance_P.svg

   Substance P.

Immunoassay protocols
~~~~~~~~~~~~~~~~~~~~~

I conducted several protocols all involving antibody microarrays, or immunoassays. They all involved a preliminary silanization to prepare the glass surface and coat it with a chemical layer. Biological probes (antibodies) are then spotted in droplets on that layer, and left to immobilize overnight in a high-humidity environment to prevent evaporation.

Once the probes are bound to the chemical layer, the surface is rinsed to remove excess molecules, and blocking proteins are attached to saturate free active sites on the surface. Blocking proteins make sure that nothing else can attach in areas that aren't covered with antibodies, including fluorescent markers. Preventing this *non-specific adsorption* limits background noise during detection.

A solution containing the target molecules (antigens/peptides) is then deposited on the spotted surface, and left to incubate under a plastic cover slip. If the peptides are marked with a fluorophore, then detection is direct: after rinsing and drying the surface, the results are obtained directly from the fluorescence scanner.

.. class:: expert

   Some peptides are not directly marked with a fluorophore, but rather with a biotin, a small vitamin. Biotin has an extraordinarily high affinity for streptavidin, a larger protein; their bond is one of the strongest known non-covalent interactions. Such *biotinylated* peptides can be indirectly detected using *streptavidinated fluorophores*, meaning fluorophores attached to a streptavidin. The antibodies themselves can also be marked with a biotin, to check their presence on the surface independent of their interaction with peptides.

.. figure:: /images/Biochips_immunotest_paths.svg

   Stages of the protocol for three possible antibody microarray tests: (a) Direct verification of the immobilization of biotinylated antibodies on the surface, using streptavidinated fluorophores. (b) Direct reading of the binding of fluorescent peptides on immobilized antibodies. (c) Indirect reading of the binding of biotinylated peptides on immobilized antibodies, using streptavidinated fluorophores.

Parameter study & protocol optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Biological tests, and immunoassays in particular, can be difficult to control because they depend on so many different parameters: duration and temperature of the successive steps, humidity, blocking proteins, buffers, etc. In order to increase the reproducibility of our tests, I worked with fellow engineer Isabelle Mingam to study those parameters and optimize them for the most consistent results.

The tests confirmed the need for blocking proteins to limit background noise, and a small amount of glycerol to limit the evaporation of droplets. We also found out that the drying step, done by centrifuge for DNA microarrays in the lab, might be too strong for antibodies: a softer drying method better preserved their integrity, in particular their antigen-binding site (paratope) needed to recognize and attach molecules of interest.

.. TODO: Collapse spotting patterns https://get.foundation/building-blocks/blocks/table-expand.html

Probe attachment
----------------

A first experiment tested the grafting of antibodies and antigens on the CEA-2 chemical layer. Biotinylated antibodies and antigens were spotted, and their presence was directly detected using streptavidinated fluorophores (Cyanine3). As expected, only biotinylated antibodies (rows 3 & 4) and biotinylated peptides (rows 7 & 8) showed significant fluorescence. Neither non-biotinylated nor control probes showed high fluorescence.

.. figure:: /images/Biochips_GP-08_bloc2_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM
   * Antibody mAb SP31 1 μM, 10% glycerol
   * Biotinylated antibody mAb SP31-biot 0.8 μM
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol
   * Control antibody Il2-73 1 μM
   * Control antibody Il2-73 1 μM, 10% glycerol
   * Peptide LMN1 1 μM
   * Peptide LMN1 1 μM, 10% glycerol

Blocking proteins
-----------------

This experiment was similar to the initial grafting of probes, but free actives sites were not blocked: without neutral proteins like bovine serum albumin (BSA), fluorophores adsorbed on the surface and led to high background noise.

.. figure:: /images/Biochips_GP-02_bloc2_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM
   * Antibody mAb SP31 1 μM, 10% glycerol
   * Biotinylated antibody mAb SP31-biot 0.8 μM
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol
   * Control antibody Il2-73 1 μM
   * Control antibody Il2-73 1 μM, 10% glycerol
   * Peptide LMN1 1 μM
   * Peptide LMN1 1 μM, 10% glycerol

Drying steps
------------

Incubating regular antibodies with biotinylated peptides should lead to a significant fluorescence signal, but it originally didn't (rows 1 & 2). This led us to reconsider the drying step by centrifuge after immobilization, which might damage the antibodies. We switched to a softer drying step using an azote stream instead. The final drying step (after incubation and immediately before detection) can still be done using a centrifuge, since fluorophores are more robust than antibodies.

.. figure:: /images/Biochips_GP-10_bloc2_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM
   * Antibody mAb SP31 1 μM, 10% glycerol
   * Biotinylated antibody mAb SP31-biot 0.8 μM
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol
   * Control antibody Il2-73 1 μM
   * Control antibody Il2-73 1 μM, 10% glycerol
   * Peptide LMN1 1 μM
   * Peptide LMN1 1 μM, 10% glycerol

Glycerol content
----------------

We originally used a 10% glycerol concentration for probes to prevent evaporation. However, too high a concentration may decrease fluorescence later. A study of glycerol percentage revealed that 2% glycerol was enough to prevent evaporation.

.. figure:: /images/Biochips_217b-03_bloc1_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM, 0% glycerol
   * Antibody mAb SP31 1 μM, 2% glycerol
   * Antibody mAb SP31 1 μM, 4% glycerol
   * Antibody mAb SP31 1 μM, 6% glycerol
   * Antibody mAb SP31 1 μM, 8% glycerol
   * AntibodymAb SP31 1 μM, 10% glycerol
   * Control antibody Il2-73 1 μM, 10% glycerol
   * Control antibody Il2-73 1 μM, 10% glycerol

Incubation period
-----------------

A higher temperature on incubation leads to a faster reaction, but needs to remain compatible with our biological molecules. Our reaction kinetics study showed that the reaction between antibodies and antigens was very fast, so we tested incubation periods of five minutes (top) and one hour (bottom). Results after one hour showed more consistent fluorescence (indicative of target saturation) and comparable background noise.

.. figure:: /images/Biochips_236-30_532s.jpg
.. figure:: /images/Biochips_236-29_532s.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM, 10% glycerol
   * Antibody mAb SP31 1 μM, 10% glycerol
   * Control antibody Il2-73 1 μM, 10% glycerol


Chemical layer
--------------

In the original microarray protocol, DNA strands (oligonucleotides) were grafted onto the CEA-2 layer at the aldehyde stage via their amine ending (NH\ :subscript:`2`). Our antibodies and antigens also had amine functions, so it made sense to graft them at the aldehyde stage as well. Out of scientific curiosity, we decided to test grafting them on the epoxide (top) and diol (bottom) stages. Both led to less consistent, lower fluorescence, so we stuck to aldehyde.

.. figure:: /images/Biochips_216-31_bloc2_532.jpg
.. figure:: /images/Biochips_216-07_bloc2_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM, 10% glycerol
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol
   * Control antibody Il2-73 1 μM, 10% glycerol
   * Peptide LMN1 1 μM, 10% glycerol


Reducing agent
--------------

The imine chemical function between the biological probe and the silane's aldehyde needs to be reduced to be stable over time. This reduction can be done *in situ*  by adding NaCNBH\ :subscript:`3` directly to the solution of probes (top), or afterwards with a NaBH\ :subscript:`4` bath (bottom). The latter turned out to damage the blocking proteins and increased background noise, so we chose *in situ* reduction.

.. figure:: /images/Biochips_217b-06_bloc2_532.jpg
.. figure:: /images/Biochips_217b-07_bloc2_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 1 μM, 10% glycerol, with NaCNBH\ :subscript:`3`
   * Antibody mAb SP31 1 μM, 10% glycerol, no NaCNBH\ :subscript:`3`
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol, with NaCNBH\ :subscript:`3`
   * Biotinylated antibody mAb SP31-biot 0.8 μM, 10% glycerol, no NaCNBH\ :subscript:`3`
   * Control antibody Il2-73 1 μM, 10% glycerol, with NaCNBH\ :subscript:`3`
   * Control antibody Il2-73 1 μM, 10% glycerol, no NaCNBH\ :subscript:`3`
   * Peptide LMN1 1 μM, 10% glycerol, with NaCNBH\ :subscript:`3`
   * Peptide LMN1 1 μM, 10% glycerol, no NaCNBH\ :subscript:`3`


Reproducibility
---------------

Once the different parameters of the protocol were optimized, we printed biological probes onto an entire glass slide, and measured an interspot variation of 7.7%, which indicates good reproducibility between spots of the same biological test.

.. figure:: /images/Biochips_236-32_532.jpg

.. container:: spotting-pattern

   * Antibody mAb SP31 incubated with peptide LMN1 marked with Alexa-532 (2196 spots: 36 columns by 61 lines; *x* step: 600 μm, *y* step: 800 μm)


Alternative detection methods
=============================

.. figure:: /images/jj-ying-fbKDd7R7_24-unsplash.jpg

   `JJ Ying <https://unsplash.com/@jjying>`__ on `Unsplash <https://unsplash.com/photos/fbKDd7R7_24>`__

TODO: Add intro; chemical characterization

Reaction kinetics
~~~~~~~~~~~~~~~~~

All the fluorescence-based experiments conducted so far were done after a period of incubation between antibodies and peptides. I worked with Rémi Galland, from the CEA's *Laboratoire d'Imagerie des Systèmes d'Acquisition* (LISA), to study the kinetics of that interaction in real time.\ [#galland2008]_ The principle of the experiment was similar to previous immunoassays, except that fluorescence wass measured continuously as the target peptides, marked with fluorophores, were introduced into the system.

.. figure:: /images/Biochips_reaction_kinetics.svg
   :figclass: reaction-kinetics-diagram

   Principle of real-time measurement of the antibody−peptide interaction.

Our exploratory work showed promising results: we were able to observe a rapid increase in signal during the first few minutes of the experiment, showing a plateau (indicating saturation) after about 30 minutes. The signal then decreased over time due to photobleaching (the gradual fading of fluorophores under the exciting light). These results prompted us to experiment with shorter incubation periods (described above).

.. figure:: /images/Biochips_reaction_kinetics_1nM.svg
   :figclass: reaction-kinetics-chart

   Reaction kinetics between mAb SP31 antibodies, grafted on CEA-2 chemistry, and fluorescein-marked LMN1 peptides in solution at 1 nM (P = 500 µW, D = 0.5 mL/min, pH = 7.4).

.. [#galland2008] Rémi Galland. *Mise en œuvre de concepts de détecteurs optiques de fluorescence intégrant la source de lumière au composant pour des immunoanalyses adaptées à des applications hors laboratoires.* Ph.D dissertation. Biophysics, Université Joseph-Fourier -- Grenoble I, 2008. `tel-00332307 <https://tel.archives-ouvertes.fr/tel-00332307>`__.

Photothermal deflection spectroscopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Photothermal deflection spectroscopy (PDS) is a technique used to characterize thin layers by measuring the change in refractive index of a sample due to heating by light. In other words, one laser heats a surface to different degrees depending on what's on it; another laser is shone through the same surface, and the way it's deflected by heat provides information on what's there.

.. figure:: /images/Biochips_Photothermal_deflection_spectroscopy_setup.png
   :figclass: framed apparatus-jackson

   Experimental apparatus for transverse PDS from Jackson *et al.*'s 1981 article "`Photothermal deflection spectroscopy and detection <https://digital.library.unt.edu/ark:/67531/metadc827884/>`__." *Applied Optics.* **20** (8): 1333–1344.

The principle of the immunoassay is the same as in fluorescence experiments, except the final detection step to visualize antibodies and antigens is done indirectly using gold nanoparticles rather than a fluorophore. For this experiment, I partnered with Violaine Vizcaino, from the CEA's *Laboratoire d'Ingénierie des Composants Photoniques* (LICP).\ [#mirage]_

.. class:: expert

   In technical terms, an Argon laser provides the pump beam that heats up the surface. It's focused by mirrors rather than a dioptric system, which could cause chromatic aberrations. The probe beam from a 2 mW He-Ne laser is detected by a quadrant photodiode. The LICP's experiment is set up for Transverse PDS, where the pump beam comes in normal to the surface, and the probe beam passes parallel. The substrate's surface undergoes the usual CEA-2 process, and mAb SP31 antibodies are grafted onto it. A solution of biotinylated antigens is incubated on the surface, followed by streptavidinated gold nanobeads with a 10 nm diameter. The presence of the gold nanobeads is finally detected by PDS.

Although we used a highly concentrated antigen solution for this exploratory experiment, we were able to detect antigens on their specific antibodies, indicating that the interaction had taken place. No signal was detected on the control antibodies, indicating that the interaction was specific to our probe antibodies.

.. container:: figures

   .. figure:: /images/Biochips_billes100.png

      Result of the PDS experiment in false colors for a 100 nM antigen solution. Antigens are detected (via gold nanobeads) on the first two rows containing specific antibodies, but not on the third row containing control antibodies.

   .. container:: spotting-pattern

      * Antibody mAb SP31 1 μM, 2% glycerol
      * Antibody mAb SP31 1 μM, 2% glycerol
      * Control antibody Il2-73 1 μM, 2% glycerol

.. [#mirage] Violaine's technical report isn't available publicly, but `Wikipedia's article on photothermal spectroscopy <https://en.wikipedia.org/wiki/Photothermal_spectroscopy>`__ provides a general overview of the technique, and details about the LICP's experimental setup are available in Appendix B of `my own report </documents/Biochips_report.pdf>`__ (in French), pages 69−72 (PDF, 3.2 MB).


Neutron reflectometry
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/Institut_Laue_Langevin_inside_reactor_hall.jpg

   Inside the hall of the high-flux nuclear reactor at Institut Laue-Langevin in Grenoble, France. (Nerd bzh on `Wikimedia Commons <https://commons.wikimedia.org/wiki/File:Institut_Laue_Langevin_inside_reactor_hall.jpg>`__ // `CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0/legalcode>`__)

one of the most intense neutron sources in the world

Neutron reflectometer with horizontal scattering geometry

Institut Laue-Langevin (ILL) with Giovanna Fragneto
D17 reflectometer

.. [#cubitt2002] \R. Cubitt and G. Fragneto. D17: The new reflectometer at the ILL. *Appl. Phys. A* **74**, s329--s331 (2002). `doi 10.1007/s003390201611 <https://doi.org/10.1007/s003390201611>`__, `full text <https://www.ill.eu/fileadmin/user_upload/ILL/3_Users/Scientific_groups/Large_Scale_Structures/People/Giovanna_FRAGNETO/D17.pdf>`__


----

Vapor-phase silanization for proteomics
=======================================

.. figure:: /images/luke-besley-zAv-nWtQJlc-unsplash.jpg

   `Luke Besley <https://unsplash.com/@besluk>`__ on `Unsplash <https://unsplash.com/photos/zAv-nWtQJlc>`__

TODO: Add intro

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

   Mass spectrum of a sample of Cytochrome C (10 pmol/µL) digested by trypsine immobilized on a vapor-phase CEA-2 chemical layer. (F. Mittler / CEA-Léti)
