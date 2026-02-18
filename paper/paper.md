---
title: 'KORONA and KoronaScript: a toolbox for acoustic data processing'
tags:
  - Python
  - Java
  - broadband acoustics
  - sonar
  - echo sounder
author: Ketil Malde
authors:
  - name: Ketil Malde
    orcid: 0000-0001-7381-1849
    affiliation: 1
  - name: Inge Eliassen
    orcid: 0009-0005-0400-3342
    affiliation: 2
  - name: Rolf Korneliussen
    affiliation: 1
affiliations:
 - name: Institute of Marine Research, Bergen, Norway
   index: 2
 - name: NORCE, Bergen, Norway
date: 2026
bibliography: references.bib
---

<!-- to build for JOSS:
     % docker run --rm --volume $PWD/docs:/data --user $(id -u):$(id -g) --env JOURNAL=joss openjournals/inara
	   or for Arxiv:
	 pandoc -s --citeproc --bibliography paper.bib paper.md -o paper.tex
-->

# Summary



# Statement of need

Acoustic instruments have become essential tools for marine science, and a variety of echo sounders and sonars are routinely used to explore the world below the ocean surface.  Multi-beam echo sounders map the sea floor in high detail, split beam and multi frequency echo sounders measure the abundance of fish for stock assessments, side-scan and synthtetic aperture sonars can resolve objects in minute detail, ACDP measures deep sea currents.

In parallel with the deveopment and new and more advanced instruments, there has risen a need for new algorithms and tools to effectively process the often large amounts of data produced.  Software analytics are important for tasks like noise detection and removal, data compression, bottom detection, species identification and other acoustic target classification, and integrating with related data.  Several popular software packages exist, often combining a variety of analytics with an easy to use graphical interface.

<!-- [@wall2018pyecholab] or EchoPype [@lee2024interoperable] -->

# LSSS

One popular platform for analyzing acoustics data is the Large Scale Survey System (LSSS) [@korneliussen2006large]. For two decades, this system has been expanded to provide an interactive platform for scrutinizing acoustic survey data.

 (todo: who uses it - examples)

 (figure)

# The KORONA processing library

LSSS integrates with a data processing library called KORONA [@korona].  This library is comprised of a number individual modules, offering access to a wide range of functionality, like noise removal, broadband pulse compression, automated target classification, format conversions, and so on.
In addition to the integration with the LSSS platform, KORONA also provides its own graphical user interface for configuring and orchestrating them. \ref{fig:korona}

(Figure)

List of modules, documentation, etc

# The KoronaScript programmatic interface

The graphical user interfaces provided by LSSS and KORONA make it easy even for relatively untrained users to access the analytics modules and configure and run analysis pipelines.  However, for many use cases, a programmatic approach may be preferable.

For instance, in a scientific setting it may be necessary to experiment systematically with a variety of settings to optimize the processing to a specific task.  In this case, it is convenient to write a loop over the relevant parameter values (different levels of noise reduction, say), and evaluate the results.

Another advantage is that processing pipelines in the form of program text can leverage the host of infrastructure aimed at program development.  Processing can be be shared, copied, and versioned (e.g.\ in GitHub), and intermixed with other processing operations, like AI-based classification systems [@brautaset2020acoustic], or functionality offered by other toolkits like pyEchoView [@wall2018pyecholab] or EchoPype [@lee2024interoperable]. 

# Availability



# Acknowledgments


# References
