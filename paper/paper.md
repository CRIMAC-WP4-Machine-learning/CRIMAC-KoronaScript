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

KoronaScript is a Python library that provides a programmatic interface to KORONA, a wide collection of algorithms and processing modules for acoustic data processing.  KORONA is integrated with the Large Scale Survey System (LSSS), a popular package for scientific analysis of data from acoustic equiment, including echo sounders, sonars, and hydrophones.

# Statement of need

Acoustic instruments have become essential tools for marine science, and a variety of echo sounders and sonars are routinely used to explore the world below the ocean surface.  Multi-beam echo sounders map the sea floor in high detail, split beam and multi frequency echo sounders measure the abundance of fish for stock assessments, side-scan and synthtetic aperture sonars can resolve objects in minute detail, ACDP measures deep sea currents.

In parallel with the development and new and more advanced instruments, there has risen a need for new algorithms and tools to effectively process the often large amounts of data produced.  Software analytics are important for tasks like noise detection and removal, data compression, bottom detection, species identification and other acoustic target classification, and integrating with related data.  Several popular software packages exist, often combining a variety of analytics with an easy to use graphical interface, including LSSS [@korneliussen2006large], HERMES and Movies3d [@trenkel2009overview], and EchoView (Echoview Software Pty Ltd., 2025) (or [@EchoviewSoftware]?).

<!-- @Rolf: more? -->

While interactive scrutiny by expert users remains an important method to interpret acoustic data, it is often convenient or even necessary to automate the processing.  As data collection volumes increase, labor costs and expert availabilty becomes major obstacles to effective data use.  Having a programmatic interface that can be scripted is quickly becoming a necessity.

Furthermore,  many important algorithms and processing modules have many tunable parameters, and a scriptable API allows these parameters to be optimized by an automated (or semi-automated) process using grid search or other schemes.  The other user can perform sensitivity analysis to evaluate the importance of each parameter, and can compare the results from different configurations to find the process that best fits a particular challenge.

Finally, by embedding the analysis in a program, it can be shared, copied, and versioned (e.g.\ in GitHub), which supports reproducibility and verifiability, and is particularly useful for scientific work. The process can also be  intermixed with other processing operations, like AI-based classification models [e.g., @brautaset2020acoustic], or functionality offered by other analysis toolkits like pyEchoView [@wall2018pyecholab] or EchoPype [@lee2024interoperable].

_KoronaScript_ is a Python application programming interface (API) that interfaces with KORONA, the processing components of the popular acoustic analysis package, LSSS.  This gives the user full programmatic access to all the processing modules and 
algorithms offered by KORONA through a convenient Python interface.

# State of the field

Traditionally, interpreting marine acoustic data for scientific or resource management purposes have been performed by manual scrutiny by experts using interactive tools. <!-- [@korneliussen2006large, @trenkel2009overview] -->
This approach has been a cornerstone for important long running survey series performed by research insitutes, including the Institute of Marine Research in Norway using LSSS, IFREMER in France using Movies3d, and NOAAA in the US using EchoView.  <!-- @Rolf -->

To support postprocessing of data and scientific information extraction, some programmatic packages exist, including
EchoeViewR [@harrison2015r], which provides an R interface to the EchoView system, and Matecho [@perrot2018matecho], a tool for data analysis implemented in Matlab, and linked to Movies3d [@trenkel2009overview].

With the advent of uncrewed platforms for data collection [@examples of this], the need to build automated workflows automatically has increased.
Increased data complexity and volumes, e.g. from broadband echo sounders, exacerbates this [@guidi2020big;@malde2020machine].
To automate data processing, there exist packages like PyEchoLab [@wall2018pyecholab] and EchoPype [@lee2024interoperable] which offer algorithms and tools with a programmatic interface.

<!-- However... -->

Simultaneously, the advent of deep learning in marine science [@malde2020machine;@beyan2020setting;@rubbens2023machine] has increased the importance of integrating traditional or existing methods with new, data driven approaches.
Although support for machine learning can be found in many programming languages (including Matlab and R), Python is overwhelmingly the most popular choice.  We foresee that the field will increasingly move towards automation that integrates traditional and new methods using Python as the primary glue.

# Software design

## LSSS and KORONA

The Large Scale Survey System (LSSS) [@korneliussen2006large] has been a popular platform for analyzing acoustics data for two decades.

 (todo: who uses it - examples)

 (figure)

LSSS integrates with a data processing library called KORONA [@korona].  This library is comprised of a number individual modules, offering access to a wide range of functionality and algorithms, including noise removal, broadband pulse compression, automated target classification, format conversions.
In addition to the integration with the LSSS platform, KORONA also provides its own graphical user interface for configuring and orchestrating them. \ref{fig:korona}

(Figure)

List of modules, documentation, etc

## The KoronaScript programmatic interface

KoronaScript is implemented as a set of Python classes that each encapsulates a KORONA procssing module.  These classes leverage two core features offered by KORONA.
First, KORONA can generate a description of its modules and their parameters in the form of a JSON file.  KoronaScript parses this, and generates the corresponding Python classes.  This ensures that the KoronaScript will automatically incorporate new features provided by new releases of KORONA.

Second, the KORONA user interface writes configured pipelines to XML files, which are then processed by the corresponding processing modules.  KoronaScript leverages this interface by having the classes generate the same XML ouptput as the KORONA GUI would produce.  A `KoronaScript` class lets the user organize class instances in a sequence, and calling the KORONA processing infrastructure on the generated XML specification.

## Availability

PYPI
GitHub
LSSS and KORONA

# Research impact statement

(Overview/list of papers using korona and LSSS)


# AI usage disclosure

A large language model was used to review drafts and offer suggestions for improvement. All suggestions were manually reviewed.  AI has not been used for direct generation of code or text.

# Acknowledgments

# References
