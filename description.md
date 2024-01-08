This API provides access to the Aquifer Mapping Program's groundwater level and water
chemistry database.

# Data

## General
The data is stored in a MSSQL database. The database is updated on a semi-regular basis
with new manually measured depth to groundwater measurements.

## Groundwater Level Data
There are two "types" of groundwater level data: manual measurements and continuous

### Manual Measurements
Manual measurements are taken by field staff typically using a steel tape.

### Continuous Measurements
Continuous measurements are taken by either a pressure transducer or acoustic transponder.

## Private vs. Public
Some of the data collected by NMBGMR is private and requires appropriate privileges and authentication for access. The following endpoints require such authentication:

- **/locations**
- **/locations/equipment**
- **/locations/notes**
- **/locations/projects**
- **/locations/owners**
- **/locations/photos**
- **/locations/photo/{photoid}**

## IDs & Keys
There are two types of IDs that are commonly used throughout the database that can be used to query objects, as well as to relate data to each other. They are:

### PointID
PointID is the primary ID used to identify a location in NMBGMR's database. The PoindID identifies a location. Equipment, ProjectLocations, Well, and WellPhoto all use PointID to relate to a Location.

It is used by the following classes:
- Location
- Equipment
- ProjectLocations
- Well
- WellPhoto

### LocationId
LocationId is used as the primary key of a Location. It can also be used to relate Equipment and Well to a Location.

### Other IDs
IDs apart from PointID and LocationId exist to query tables. These are as follows:

- Location.**SiteID**: used to associate a Location with USGS data
- Location.**AlternateSideID**
- ProjectLocations.**GlobalID**: the primary key for a ProjectLocations object
- OwnersData.**OwnerKey**: the primary key for an OwnersData object
- Well.**WellID**: the primary key for a Well object
- Well.**OSEWellID**
- Well.**OSEWelLTagID**
- WellPhoto.**GlobalID**: the primary key for a WellPhoto object

