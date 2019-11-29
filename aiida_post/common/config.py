"""
General variables used by the app
"""

# supported workchain. Will be changed to check the available endpoint in the definitions

# also will be superseded by something better, i.e. how to get

# list of the supported codes to use in the database
# for now, list is given by the nodes that are loaded in the database
# in the future it will probably be given as a list of "suggested to use"
# also, upf co not belong here
AVAILABLE_CODES = {'qe': 667, 'siesta': 668, 'upf': 'efficiency'}

# map of properties to single workchain
# it should be interesting (necessary?) to also map WHERE to
# find this value / object (output name/location)
PROPERTY_MAPPING = {
    'structure.cod': 'post.CODImport',
    'relax.pw': 'quantumespresso.pw.relax',
    'band_structure.pw': 'quantumespresso.pw.band_structure',
    'band_gap.pw': 'post.BandGap',
    'formationenergy.qe': 'defects.formation_energy.qe'
}
#####################################################################
##BELOW COPIED AND SLIGHTLY MODIFIED FROM AIIDA REST API CONFIG FILE
#####################################################################

# AiiDA REST CONFIG file
# made a copy here in case I want to change something (like the prefix, for instance)

# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""
Constants used in rest api
"""

## Pagination defaults
LIMIT_DEFAULT = 400
PERPAGE_DEFAULT = 20

##Version prefix for all the URLs
PREFIX = '/intersect/v4'
VERSION = '4.0.0'
"""
Flask app configs.

DEBUG: True/False. enables debug mode N.B.
!!!For production run use ALWAYS False!!!

PROPAGATE_EXCEPTIONS: True/False serve REST exceptions to the client (and not a
generic 500: Internal Server Error exception)

"""
APP_CONFIG = {
    'DEBUG': False,
    'PROPAGATE_EXCEPTIONS': True,
}
"""
JSON serialization config. Leave this dictionary empty if default Flask
serializer is desired.

Here is a list a all supported fields. If a field is not present in the
dictionary its value is assumed to be 'default'.

DATETIME_FORMAT: allowed values are 'asinput' and 'default'.

"""
SERIALIZER_CONFIG = {'datetime_format': 'default'}
"""
Caching configuration

memcached: backend caching system
"""
CACHE_CONFIG = {'CACHE_TYPE': 'memcached'}
CACHING_TIMEOUTS = { #Caching TIMEOUTS (in seconds)
    'nodes': 10,
    'users': 10,
    'calculations': 10,
    'computers': 10,
    'datas': 10,
    'groups': 10,
    'codes': 10,
}

# IO tree
MAX_TREE_DEPTH = 5
"""
Aiida profile used by the REST api when no profile is specified (ex. by
--aiida-profile flag).
This has to be one of the profiles registered in .aiida/config.json

In case you want to use the default stored in
.aiida/config.json, set this varibale to "default"

"""
DEFAULT_AIIDA_PROFILE = None
