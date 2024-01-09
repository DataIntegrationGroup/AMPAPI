# ==============================================================================
# BEGIN PUBLIC ENDPOINT METADATA CLASSES
# ==============================================================================

class PublicSummary():

    def __init__(self):
        self.all = "Get all publicly available locations"
        self.collaborative_network = "Get all Healy Collaborative Network locations"
        self.usgs_site_metadata = "Get USGS site metadata for a specific location"
        self.info = "Get information about a specific location"
        self.well = "Get well information for a specific location"

class PublicDescription():

    def __init__(self):
        self.all = """
Returns data on all public locations as a collection of
<a href="https://geojson.org/" target="_blank">GeoJSONs</a> stored in an array: 

```        
{
    "type": "FeatureCollection:
    "features": [<Location GeoJSON>...]
}
```

Each Location GeoJSON is formatted as follows:

```
{
    "type": "Feature",
    "properties": "{
        "name": <PointID>,
        "well_depth": {"value": <well depth>, "units": "ft"}
    },
    "geometry": {
        "coordinates": [<longitude>, <latitude>, <elevation or 0>],
        "type": "Point
    }
}
```
"""

        self.collaborative_network = """
Returns data on locations that are in the Healy Collaboratieve Network as a 
collection of <a href="https://geojson.org/" target="_blank">GeoJSONs</a> 
stored in an array: 

```        
{
    "type": "FeatureCollection:
    "features": [<Location GeoJSON>...]
}
```

Each Location GeoJSON is formatted as follows:

```
{
    "type": "Feature",
    "properties": "{
        "name": <PointID>,
        "well_depth": {"value": <well depth>, "units": "ft"}
    },
    "geometry": {
        "coordinates": [<longitude>, <latitude>, <elevation or 0>],
        "type": "Point
    }
}
```
"""

        self.usgs_site_metadata = """
Returns a JSON of site metadata from a USGS site. The data is retrieved
from the <a href="https://waterservices.usgs.gov/docs/" target="_blank">USGS Water Services</a>.
If the metadata  cannot be retrieved or there is an error code as a 
result of the request to USGS, returns None.

The dictionary has the following keys. See <a href="https://help.waterdata.usgs.gov/codes-and-parameters/codes" target="_blank">documentation</a> from the USGS for
further explanations. 

- **agency_cd**: agency
- **site_no**: site identification number
- **station_nm**: site name
- **site_tp_cd**: site type
- **lat_va**: DMS latitude
- **long_va**: DMS longitude
- **dec_lat_va**: decimal latitude
- **dev_long_va**: decimal longitude
- **coord_meth_cd**: latitude-longitude method
- **coord_acy_cd**: latitude-longitude accuracy
- **coord_datum_cd**: latitude-longitude datum
- **dec_coord_datum_cd**: decomal latitude-longitude datum
- **district_cd**: district code
- **state_cd**: state code
- **county_cd**: county code
- **country_cd**: country code
- **land_net_ds**: land net location description
- **map_nm**: name of location map
- **map_scale_fc**: scale of location map
- **alt_va**: altitude accuracy
- **alt_meth_cd**: method altitude determined
- **alt_acy_va**: altitude accuracy
- **alt_datum_cd**: altitude datum
- **huc_cd**: hydrologic unit code
- **basin_cd**: drainage basin code
- **topo_cd**: topographic setting code
- **instruments_cd**: flags for instruments at site
- **construction_dt**: date of first construction
- **inventory_dt**: date site established or inventoried
- **drain_area_va**: drainage area
- **contrib_drain_area_va**: contributing drainage area
- **tz_cd**: time zon abbreviation
- **local_time_fg**: site honors Daylight Savings Time
- **reliability_cd**: data reliability code
- **gw_file_cd**: data-other GW files
- **nat_aqfr_cd**: national aquifer code
- **aqfr_cd**: local aquifer code
- **aqfr_type_cd**: local aquifer type code
- **well_depth_va**: well depth
- **hole_depth_va**: hole depth
- **depth_src_cd**: source of depth data
- **project_no**: project number
"""

        self.info = """
Returns a JSON containing Location information for a specific **PointID**. See the
Location schema for the keys.
"""

        self.well = """
Returns a JSON containing well information for a specific **PointID**. See the 
Well schema for the keys.
"""

# ==============================================================================
# END PUBLIC ENDPOINT METADATA CLASSES
# ==============================================================================

# ==============================================================================
# BEGIN NMBGMR ENDPOINT METADATA CLASSES
# ==============================================================================

class NMBGMRSummary():
    def __init__(self):
        self.all = "Get all NMBGMR and publicly available locations"
        self.equipment = "Get information on equipment used at an NMBGMR location"
        self.notes = "Get the notes from an NMBGMR location"
        self.projects = "Get the projects associated with an NMBGMR location"
        self.owners = "Get the owners of an NMBGMR well location"
        self.photos = "Get the photos associated with an NMBGMR well location"
        self.photo_photoid = "Get a specific photo from an NMBGMR well location"

class NMBGMRDescription(object):

    def __init__(self):
        self.all = """
Returns data on all NMBGMR and public locations as a collection of
<a href="https://geojson.org/" target="_blank">GeoJSONs</a> stored in an array: 

```        
{
    "type": "FeatureCollection:
    "features": [<Location GeoJSON>...]
}
```

Each Location GeoJSON is formatted as follows:

```
{
    "type": "Feature",
    "properties": "{
        "name": <PointID>,
        "well_depth": {"value": <well depth>, "units": "ft"}
    },
    "geometry": {
        "coordinates": [<longitude>, <latitude>, <elevation or 0>],
        "type": "Point
    }
}
```
"""

        self.equipment = """
Returns a list of JSONs that describe the equipment used at location (as 
specified by its **PointID**). The list of equipment is ordered by the date they
were installed. See the Equipment schema for the keys of the JSONs in the list.
"""

        self.notes = """
Returns the notes taken for a particular location as a string. Returns an empty
string if there are no notes.
"""

        self.projects = """
Returns a list of JSONs that describe the projects for a give location (as
specified by its **PointID**). See the ProjectLocations schema for the keys of
the JSONs in the list. 
"""

        self.owners = """
Returns a JSON that describes the owner of a well (as specified by its
**PointsID**). Returns an empty JSON if the data is not available. See the
OwnersData schema for the keys of the JSON. 
"""

        self.photos = """
Returns a list of JSONs that contain information on all photos taken at and for
a Location (as specified by its **PointsID**). See the WellPhoto schema for the
keys of the JSONs.
"""

        self.photo_photoid = """
Returns the file of a specific photo.
"""


# ==============================================================================
# END NMBGMR ENDPOINT METADATA CLASSES
# ==============================================================================

# ==============================================================================
# BEGIN METADATA CLASS INSTANTIATIONS
# ==============================================================================
public_summary = PublicSummary()
public_description = PublicDescription()

nmbgmrd_summary = NMBGMRSummary()
nmbgmrd_description = NMBGMRDescription()

# ==============================================================================
# END METADATA CLASS INSTANTIATIONS
# ==============================================================================