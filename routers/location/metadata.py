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

        self.photos = """Returns a list of photo information for all photos 
        associated with a location. Each WellPhoto object has the following
        attributes:

        - **GlobalUD**: the primary key
        - **PointID**: 
        - **OLEPath**: the path to photo
        """

        self.photo_photoid = ""