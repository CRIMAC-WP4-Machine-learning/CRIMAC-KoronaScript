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

In parallel with the development and new and more advanced instruments, there has risen a need for new algorithms and tools to effectively process the often large amounts of data produced.  Software analytics are important for tasks like noise detection and removal, data compression, bottom detection, species identification and other acoustic target classification, and integrating with related data.  Several popular software packages exist, often combining a variety of analytics with an easy to use graphical interface, including LSSS [@korneliussen2006large] and EchoView (Echoview Software Pty Ltd., 2025).

(more?)

<!-- PyEchoLab [@wall2018pyecholab], and EchoPype [@lee2024interoperable]. -->

While interactive scrutiny by expert users remains an important method to interpret acoustic data, it is often convenient or even necessary to automate the processing.  As data collection volumes increase, labor costs and expert availabilty becomes major obstacles to effective data use.  Having a programmatic interface that can be scripted is quickly becoming a necessity.

Furthermore,  many important algorithms and processing modules have many tunable parameters, and a scriptable API allows these parameters to be optimized by an automated (or semi-automated) process using grid search or other schemes.  The other user can perform sensitivity analysis to evaluate the importance of each parameter, and can compare the results from different configurations to find the process that best fits a particular challenge.

Finally, by embedding the analysis in a program, it can be shared, copied, and versioned (e.g.\ in GitHub), which supports reproducibility and verifiability, and is particularly useful for scientific work. The process can also be  intermixed with other processing operations, like AI-based classification models [e.g., @brautaset2020acoustic], or functionality offered by other analysis toolkits like pyEchoView [@wall2018pyecholab] or EchoPype [@lee2024interoperable].

_KoronaScript_ is a Python application programming interface (API) that interfaces with KORONA, the processing components of the popular acoustic analysis package, LSSS.  This gives the user full programmatic access to all the processing modules and algorithms offered by KORONA through a convenient Python interface.

## LSSS

The Large Scale Survey System (LSSS) [@korneliussen2006large] has been a popular platform for analyzing acoustics data for two decades.

 (todo: who uses it - examples)

 (figure)

## The KORONA processing library

LSSS integrates with a data processing library called KORONA [@korona].  This library is comprised of a number individual modules, offering access to a wide range of functionality and algorithms, including noise removal, broadband pulse compression, automated target classification, format conversions.
In addition to the integration with the LSSS platform, KORONA also provides its own graphical user interface for configuring and orchestrating them. \ref{fig:korona}

(Figure)

List of modules, documentation, etc

## The KoronaScript programmatic interface

(How it is implemented)

Code generation from self-documented KORONA modules

Generated XML and JSON specifications

Calling out to the Java subsystem for execution.

# Availability

PYPI
GitHub
LSSS and KORONA

# Acknowledgments


# References
