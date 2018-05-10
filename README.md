# Quakeml Generator (Using Obspy)

# Table of Contents

1. [Introduction](#1-introduction)
2. [Dependencies](#2-dependencies)
3. [Run Instructions](#3-run-instructions)
4. [Files Description](#4-files-description)
5. [Input File Instructions](#5-input-file-instructions)
1. [Format Example](#51-format-example)
2. [Descriptions for Input File Keys](#52-descriptions-for-input-file-keys)
6. [Contact Information](#6-contact-information)

_________________

# 1. Introduction
Quakeml Generator uses the Obspy framework to create, fill and write a new event to a quakeml file.  Data to be written to a quakeml file is passed to the program as a .txt file. Instructions and examples for formatting the .txt file for proper parsing are described below.  This program is written for quakeml version 1.2 documentation may be found here: [https://quake.ethz.ch/quakeml/Documents]

# 2. Dependencies
- python 3 (should include 'time' and 'argparse')
- obspy

# 3. Run Instructions
- Execute from command line followed by input file
- ./genquake input.txt -o output.xml
- for help: ./genquake -h 

# 4. Files Description
- genquake - main python executable (from command line with filein as arg)
- utils.py - header file contains functions to generate quakeml 
- TextAsInput.py - functions to handle filein as arg, and parse text file in. 
- input.txt - example input file
- output.txt - example output file


# 5. Input File Instructions

1. Must be a text file ending in .txt
2. Must contain all keys from example file (eventid, datasource…etc)
3. Keys and values are separated by triple colon, ex. ::: 
4. Values may be left blank, but keys and separators are required
- uncertainty:::7     // ok
- uncertainty:::      // ok, will create empty node    
- uncertainty         // wrong, no separator
- newkey:::value      // wrong, only predefined keys are accepted in this version
5) One entry per line

## 5.1 Format Example:  
eventid:::us1000ex1     <br>
datasource:::US         <br>
eventsource:::US        <br>
mag:::0.1               <br>
type:::Mw               <br>
.
.
.

Full example file: [input.text](input.txt)


## 5.2 Descriptions for Input File Keys
### Event Keys
- eventid [string]: Unique identifier for the event, not including event source. Ex: for us10008mgu enter 10008mgu
- datasource [string]: Code for the agency that submitted the data to the catalog
- eventsource [string]: Code for the agency that collected the data
- magSource [string]: Network that originally authored the reported magnitude for this event. Typical values include AK, AT, CI, HV, LD, MB, NC, NM, NN, PR, PT, SE, US, UU, UW
- locationSource [string]: The network that originally authored the reported location of this event.  Typical values include AK, AT, CI, HV, LD, MB, NC, NM, NN, PR, PT, SE, US, UU, UW
- eventType [enumeration] Must match one of the following: 
"not existing", 
"not reported", 
"earthquake", 
"anthropogenic event", 
"collapse", 
"cavity collapse", 
"mine collapse", 
"building collapse", 
"explosion", 
"accidental explosion", 
"chemical explosion", 
"controlled explosion", 
"experimental explosion", 
"industrial explosion", 
"mining explosion", 
"quarry blast", 
"road cut", 
"blasting levee", 
"nuclear explosion", 
"induced or triggered event", 
"rock burst", 
"reservoir loading", 
"fluid injection", 
"fluid extraction", 
"crash", 
"plane crash", 
"train crash", 
"boat crash", 
"other event", 
"atmospheric event", 
"sonic boom", 
"sonic blast", 
"acoustic noise", 
"thunder", 
"avalanche", 
"snow avalanche", 
"debris avalanche", 
"hydroacoustic event", 
"ice quake", 
"slide", 
"landslide", 
"rockslide", 
"meteorite", 
"volcanic eruption"
- comment [string]: Additional information such as references...etc
- title [string]: Title to be displayed on ComCat

### Magnitude Keys
- mag [string]: Magnitude of event (will be preferred magnitude value)
- type [string]: The method or algorithm used to calculate the preferred magnitude for the event.  Typical values include Md, Ml, Ms, Mw, Me, Mi, Mb, MLg
- evaluationModeMag [enumeration] Must be one of the following: manual: automatic
- evaluationStatusMag [enumeration] Must be one of the following: reviewed, preliminary, confirmed, final, rejected, reported


### Origin Keys
- time [string]: Time in UTC, Ex: 1970-01-01T00:00:00.000Z, pattern = YYYY-MM-DDTHH:MM:SS.000Z
- longitude [string]: Decimal degrees longitude. Negative values for western longitudes(-180:180)
- latitude [string]: Decimal degrees latitude. Negative values for southern latitudes(-90:90)
- horizontalUncertainty [string]: Horizontal uncertainty of reported location of the event in kilometers.
- depth [string]: Depth of the event in kilometers (program converts this to meters for quakeml)
- depthType [string]: Type of origin depth determination. Allowed values are, "from location", "from moment tensor inversion", "from modeling of broad-band P waveforms", "constrained by depth phases", "constrained by direct phases", "constrained by depth and direct phases", "operator assigned", "other"
- uncertainty [string]: Vertical uncertainty of reported location of the event in kilometers.
- evaluationModeOrg [enumeration] Must be one of the following: manual: automatic
- evaluationStatusOrg [enumeration] Must be one of the following: reviewed, preliminary, confirmed, final, rejected, reported

# 6. Contact Information

For questions please contact:
- Paul Earle - pearle@usgs.gov 
- Michael Arnold - marnold@usgs.gov 

