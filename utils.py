# -*- coding: utf-8 -*-
"""Created on Tue Jan  9 15:58:51 2018
@author: marnold

Helper functions for use by genquake.  Includes 
functions for converting data and creating obspy 
objects.
"""

import obspy
from time import gmtime, strftime

def lowercaseInput(dct):# convert source input information to lowercase
    dct['datasource']= str(dct['datasource']).lower()
    dct['eventsource']= str(dct['eventsource']).lower()
    dct['magSource']= str(dct['magSource']).lower()
    dct['locationSource']= str(dct['locationSource']).lower()   
    
def updateDictionary(dct):# add calculated values to dictionary
    dct['dataid'] = dct['eventsource'] + dct['eventid']
    dct['eventPid'] = 'quakeml:' + dct['datasource'] + '.anss.org/event/'+ dct['dataid']
    dct['epPid'] = 'quakeml:' + dct['datasource'] + '.anss.org/eventParameters/'+ dct['eventid']
    dct['magPid'] = 'quakeml:' + dct['datasource'] + '.anss.org/magnitude/'+ dct['dataid'] + '/' + dct['type']
    dct['oPid'] = 'quakeml:' + dct['datasource'] + '.anss.org/origin/'+ dct['dataid']
    
def generateCreationInfo(dct): # create, fill and return obspy creation_info object 
    creation_info = obspy.core.event.base.CreationInfo(
        agency_id = dct['eventsource'],
        creation_time = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    )
    return creation_info
    
def depthToMeters(dct):
    depth = float(dct['depth'])
    depth = depth * 1000
    dct ['depth'] = str(depth)
    horizontal_uncertainty = float(dct['horizontalUncertainty'])
    horizontal_uncertainty = horizontal_uncertainty * 1000
    dct['horizontalUncertainty'] = str(horizontal_uncertainty)
    uncertainty = float(dct['uncertainty'])
    uncertainty = uncertainty * 1000
    dct ['uncertainty'] = str(uncertainty)

def generateOrigin(dct, ci):
    """ Create an origin object, fill it with items,
    set public id and add creation info. Then return
    origin object
    """
    new_origin = obspy.core.event.origin.Origin(
        resource_id = dct['oPid'],
        time = dct['time'],
        longitude = dct['longitude'], 
        latitude = dct['latitude'], 
        depth = dct['depth'],
        depth_errors = dct['uncertainty'],
        depth_type = dct['depthType'],
        evaluation_mode = dct['evaluationModeOrg'], 
        evaluation_status = dct['evaluationStatusOrg'],
        creation_info = ci,
        origin_uncertainty = dct['horizontalUncertainty'])
    return new_origin
    
def generateMagnitude(dct, ci, origin):
    """ Create a magnitude object, fill it with items,
    set public id and origin id pointing to origin
    and add creation info. Then return magnitde object
    """
    new_magnitude = obspy.core.event.magnitude.Magnitude(
        resource_id = obspy.core.event.base.ResourceIdentifier(
            id= dct['magPid']
        ),
        mag = dct['mag'],
        magnitude_type = dct['type'],
        evaluation_mode = dct['evaluationModeMag'], 
        evaluation_status = dct['evaluationStatusMag'],
        origin_id = dct['oPid'],
        # following block is equivalent to origin_id = dct['oPid'],
        #    origin_id = obspy.core.event.base.ResourceIdentifier(
        #       referred_object = origin
        #    ),
        creation_info = ci
    )
    return new_magnitude

def generateEvent(dct, ci, orgs, mags):# create fill and return obspy event object
    """ Create an event object and fill it with items
    including magnitudes, origins, creation info and
    event descriptions
    """
    eventDescriptions = []
    if dct['title'] != "": # check for title, if title not null add to quakeml
        event_title = obspy.core.event.event.EventDescription(text = dct['title'], type = "earthquake name" ) 
        eventDescriptions.append(event_title)
    new_event = obspy.core.event.event.Event(
        resource_id = dct['eventPid'],
        origins = orgs,
        magnitudes = mags,
        creation_info = ci,
        comments = [
            obspy.core.event.base.Comment(
                text = dct['comment'],
                force_resource_id = False
            )
        ],
        event_descriptions = eventDescriptions,
        event_type = dct['eventType'],
        preferred_magnitude_id = dct['magPid'],
        preferred_origin_id = dct['oPid']
    )
    return new_event
