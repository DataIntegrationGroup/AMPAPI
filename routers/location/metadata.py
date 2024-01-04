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
        Get a list of dictionaries that contain information about NMBGMR well
        locations and associated data. Each location must contain a northing and
        an easting. 

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
        self.equipment = ""
        self.notes = ""
        self.projects = ""
        self.owners = ""
        self.photos = ""
        self.photo_photoid = ""