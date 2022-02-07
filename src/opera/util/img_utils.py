#!/usr/bin/env python

#
# Copyright 2021, by the California Institute of Technology.
# ALL RIGHTS RESERVED.
# United States Government sponsorship acknowledged.
# Any commercial use must be negotiated with the Office of Technology Transfer
# at the California Institute of Technology.
# This software may be subject to U.S. export control laws and regulations.
# By accepting this document, the user agrees to comply with all applicable
# U.S. export laws and regulations. User has the responsibility to obtain
# export licenses, or other export authority as may be required, before
# exporting such information to foreign countries or providing access to
# foreign persons.
#

"""
=================
image_utils.py
=================

"""

from collections import namedtuple
from datetime import datetime


def get_hls_filename_fields(file_name):
    """
    Parse the HLS filename into components, change Julian datetime to (YYYYMMDDTHHMMSS)

    Parameters
    ----------
    file_name : str
        Name of the HLS file

    Returns
    -------
    fields : Ordered Dictionary
        Keys are basic descriptions of the value
        Values are the fields parsed from the HLS file_name


    """
    Fields = namedtuple('Fields', ['product', 'short_name', 'MGRS_tile_id', 'time_of_acquisition',
                                   'collection_version', 'sub_version', 'band_or_QA_fmask', 'data_format'])
    fields = Fields._make(file_name.split('.'))._asdict()
    # Convert to 'YYYYMMDDTHHMMSS' format from Julian datetime
    julian_time = fields['time_of_acquisition'].split('T')
    julian_time[0] = str(datetime.strptime(julian_time[0], '%Y%j').date()).replace('-', '')
    fields['time_of_acquisition'] = 'T'.join(julian_time)

    return fields


if __name__ == '__main__':
    x = get_hls_filename_fields("HLS.S30.T53SMS.2020276T013701.v1.5.B01.tif")
    print(x)
