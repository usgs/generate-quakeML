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
- eventid: Unique identifier for the event, not including event source. Ex: for us10008mgu enter 10008mgu
- datasource: Code for the agency that submitted the data to the catalog
- eventsource: Code for the agency that collected the data
- magSource: Network that originally authored the reported magnitude for this event. Typical values include AK, AT, CI, HV, LD, MB, NC, NM, NN, PR, PT, SE, US, UU, UW
- locationSource: The network that originally authored the reported location of this event.  Typical values include AK, AT, CI, HV, LD, MB, NC, NM, NN, PR, PT, SE, US, UU, UW
- eventType: typical values include, earthquake, mining explosion, mine collapse, rock burst, volcanic eruption, nuclear explosion…etc


### Magnitude Keys
- mag: Magnitude of event (will be preferred magnitude value)
- type: The method or algorithm used to calculate the preferred magnitude for the event.  Typical values include Md, Ml, Ms, Mw, Me, Mi, Mb, MLg
- evaluationMode: manual or automatic
- evaluationStatus: values include reviewed, preliminary, confirmed, final, rejected


### Origin Keys
- time: Time in UTC, Ex: 1970-01-01T00:00:00.000Z, pattern = YYYY-MM-DDTHH:MM:SS.000Z
- longitude: Decimal degrees longitude. Negative values for western longitudes(-180:180)
- latitude: Decimal degrees latitude. Negative values for southern latitudes(-90:90)
- horizontalUncertainty: Horizontal uncertainty of reported location of the event in kilometers.
- depth: Depth of the event in kilometers (program converts this to meters for quakeml)
- depthType: Type of origin depth determination. Allowed values are, "from location", "from moment tensor inversion", "from modeling of broad-band P waveforms", "constrained by depth phases", "constrained by direct phases", "constrained by depth and direct phases", "operator assigned", "other"
- uncertainty: Vertical uncertainty of reported location of the event in kilometers.
- evaluationMode: manual or automatic
- evaluationStatus: values include reviewed, preliminary, confirmed, final, rejected

# 6. Contact Information

For questions please contact:
- Paul Earle - pearle@usgs.gov 
- Michael Arnold - marnold@usgs.gov 

