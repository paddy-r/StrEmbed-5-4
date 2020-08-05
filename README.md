# StrEmbed-5-4

Version 5-4 of Structure Embedding

Part of the Design Configuration Spaces (DCS) project hosted by the University of Leeds

Hugh Rice (HR/HPR), Tom Hazlehurst (TH) and Hau Hing Chau (HHC)

January-August 2020

School of Mechanical Engineering  
University of Leeds  
LS2 9JT

All communication, including bug/issues reports, to: h.p.rice@leeds.ac.uk

<i> StrEmbed-5-4 is a graphical user interface for visualisation and manipulation of part-whole relationships in assemblies of parts. It is written in Python and uses the modules listed in the "requirements" document. Functionality is based on [StrEmbed-4](https://github.com/hhchau/StrEmbed-4) (and earlier versions) by Hau Hing Chau, written in Perl.</i>  

<b>This research is supported by the UK Engineering and Physical Sciences Research Council (EPSRC) under grant number EP/S016406/1.</b>

Three scripts are required:
1. StrEmbed_5_4
2. step_parse_5_4
3. wxDisplay (from Python-OCC here: https://github.com/tpaviot/pythonocc-core)

It is recommended that you download the entire folder, which contains a users' manual. STEP files are a common data exchange format containing both assembly information (i.e. part-whole information) and shape data; several examples are provided. The "Images" folder contains images necessary for the application; temporary images corresponding to the parts in a loaded STEP file are also stored there.

StrEmbed-5-4 was developed in Spyder, an IDE for Python that is packaged with the Anaconda distribution, which can be downloaded [here](https://www.anaconda.com/distribution/).

StrEmbed-5-4 is published under the GNU General Purpose License version 3, which is given in the LICENSE document.
