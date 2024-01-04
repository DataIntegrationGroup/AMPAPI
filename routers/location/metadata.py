class NMBGMRSummary():

    def __init__(self):
        self.all = "Get all NMBGMR and public well locations and associated data as a list of dictionaries formatted geojsons"
        self.equipment = "Get information on equipment used at an NMBGMR location."
        self.notes = "Get the notes from an NMBGMR location."
        self.projects = "Get the project location for an NMBGMR."
        self.owners = "Get the owners of an NMBGMR well location."
        self.photos = "Get the photos associated with an NMBGMR well location."
        self.photo_photoid = "Get a specific photo from an NMBGMR well location."

class NMBGMRDescription(object):

    def __init__(self):
        self.all = """
        Returns a list of dictionaries that contain information about NMBGMR
        well locations and associated data. Each location must contain a 
        northing and an easting. 

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
        
        self.owners = ""
        self.photos = ""
        self.photo_photoid = ""