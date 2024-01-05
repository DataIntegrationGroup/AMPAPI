# ---------------
# BEGIN PUBLIC ENDPOINT METADATA CLASSES
# ---------------

class PublicSummary():

    def __init__(self):
        self.all = "Get all publicly available well locations as a list of geojsons-formatted dictionaries"
        self.collaborative_network = "Get collaborative network locations as a list of geojsons-formatted dictionaries"
        self.usgs_site_metadata = "Get USGS site metadata"
        self.info = "Get information about a specific location"
        self.well = "Get well and corresponding location information for a specific well"

class PublicDescription():

    def __init__(self):
        self.all = """
        Returns a list of dictionaries that contain information about publicly
        available well locations and associated data. Each location must contain
        a northing and an easting. 

        Each dictionary is formatted as a geojson as follows:

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
        """

        self.collaborative_network = """
        Returns a list of dictionaries that contain information about
        collaborative network well locations and associated data. Each location
        must contain a northing and an easting. 

        Each dictionary is formatted as a geojson as follows:

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
        """

        self.usgs_site_metadata = """
        Returns a dictionary of metadata from a USGS site. If the metadata 
        cannot be retrieved or there is an error code as a result of the request
        to USGS, returns None.

        The dictionary has the following keys

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
        Returns location information for a specific PointID. The Location object
        being returned has the following attributes:

        - **LocationId**: primary key
        - **PointID**
        - **SiteID**
        - **AlternateSiteID**
        - **SiteNames**
        - **PublicRelease**
        - **Easting**
        - **Northing**
        - **Altitude**
        - **LocationNotes**
        - **AltitudeMethod**
        - **lu_elevation_method**
        - **Elevation**
        - **elevation_method**
        - **geometry**
        - **lonlat**
        """
# ---------------
# END PUBLIC ENDPOINT METADATA CLASSES
# ---------------

# ---------------
# BEGIN NMBGMR ENDPOINT METADATA CLASSES
# ---------------

class NMBGMRSummary():

    def __init__(self):
        self.all = "Get all NMBGMR and publicly available well locations as a list of geojsons-formatted dictionaries"
        self.equipment = "Get information on equipment used at an NMBGMR location as a list of Equipment objects"
        self.notes = "Get the notes from an NMBGMR location"
        self.projects = "Get the projects associated with an NMBGMR location as a list"
        self.owners = "Get the owners of an NMBGMR well location"
        self.photos = "Get the photos associated with an NMBGMR well location as a list of WellPhoto objects"
        self.photo_photoid = "Get a specific photo from an NMBGMR well location"

class NMBGMRDescription(object):

    def __init__(self):
        self.all = """
        Returns a list of dictionaries that contain information about NMBGMR and
        publicly available well locations and associated data. Each location 
        must contain a northing and an easting. 

        Each dictionary is formatted as a geojson as follows:

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
        """

        self.equipment = """
        Returns a list of equipment used at location (specified by its PointID),
        ordered by the date the equipment was installed. Each Equipment object
        has the following attributes:

        - **ID**: the primary key
        - **PointID**:
        - **LocationID**: the foreign key to join with the Location table
        - **EquipmentType**: the type of equipment used
        - **Model**: the model of the equiment used
        - **SerialNo**: the serial number of the equipment used
        - **DateInstalled**: the date the equipment was installed
        - **DateRemoved**: the date the equipment was removed, if it was removed
        """

        self.notes = """
        Returns the notes taken for a particular location. Returns an empty
        string if there are no notes.
        """

        self.projects = """
        Returns a list of projects for a given PointID. Each
        ProjectLocations object has the following attributes:

        - **GlobalID**: the primary key
        - **LocationID**: the foreign key to join with the Location table
        - **PointID**:
        - **ProjectName**: the name of each project
        """

        self.owners = """
        Returns the owner of a well. Returns an empty dictionary if there is no
        owner. Each OwnersData object has the following attributes:

        - **FirstName**: the first name of the owner
        - **LatName**: the last name of the owner
        - **OwnerKey**: the primary key
        - **Email**: the email address of the owner
        - **CellPhone**: the cellphone number of the owner
        - **Phone**: the phone number of the owner
        - **MailAddress**: street number and name for the mailing address of the owner
        - **MailCity**: city for the mailing address of the owner
        - **MailState**: state for the mailing address of the owner
        - **MailZipCode**: zip code for the mailing address of the owner
        - **PhysicalAddress**: street number and name for the physical address of the owner
        - **PhysicalCity**: city for the physical address of the owner
        - **PhysicalState**: state for the physical address of the owner
        - **PhysicalZipCode**: zip code fo the physical address of the owner
        - **SecondLastName**: the second last name of the owner if it exists
        - **SecondFirstName**: the second first name of the owner if it exists
        - **SecondCtctEmail**: the second email address of the owner if it exists
        - **SecondCtctPhone**: the second phone number of the owner if it exists
        """

        self.photos = """
        Returns a list of photo information for all photos 
        associated with a location. Each WellPhoto object has the following
        attributes:

        - **GlobalUD**: the primary key
        - **PointID**: 
        - **OLEPath**: the path to photo
        """

        self.photo_photoid = """
        Returns the file of a specific photo.
        """

# ---------------
# END NMBGMR ENDPOINT METADATA CLASSES
# ---------------