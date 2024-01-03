# ===============================================================================
# Copyright 2023 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Float,
    Numeric,
    Date,
    Time,
    DateTime,
)
from sqlalchemy.orm import relationship, declared_attr
from fastapi_utils.guid_type import GUID
from geo_utils import utm_to_latlon


class Location(Base):
    __tablename__ = "Location"
    LocationId = Column(GUID, primary_key=True)
    PointID = Column(String(50))
    SiteID = Column(String(200))
    AlternateSiteID = Column(String(50))
    SiteNames = Column(String(255))

    PublicRelease = Column(Boolean)
    Easting = Column(Integer)
    Northing = Column(Integer)
    Altitude = Column(Float)

    LocationNotes = Column(String(255))

    AltitudeMethod = Column(String(50), ForeignKey("LU_AltitudeMethod.Code"))
    lu_elevation_method = relationship("LU_AltitudeMethod", uselist=False)

    @property
    def Elevation(self):
        return self.Altitude

    @property
    def elevation_method(self):
        return self.lu_elevation_method.Meaning

    @property
    def geometry(self):
        lon, lat = self.lonlat
        elevation = self.Altitude
        # altitude is in ft above sea level geojson wants meters
        if elevation is not None:
            # convert feet to meters
            elevation *= 0.3048

        return {"coordinates": [lon, lat, elevation or 0], "type": "Point"}

    _lonlat = None

    @property
    def lonlat(self):
        if self._lonlat is None:
            e, n = self.Easting, self.Northing
            lon, lat = utm_to_latlon(e, n)
            self._lonlat = lon, lat
        else:
            lon, lat = self._lonlat

        return lon, lat


class Well(Base):
    __tablename__ = "WellData"
    # LocationId = Column(GUID, ForeignKey("Location.LocationId"))
    LocationId = Column(GUID)
    WellID = Column(GUID, primary_key=True)
    PointID = Column(String(50), ForeignKey("Location.PointID"))
    HoleDepth = Column(Integer)
    WellDepth = Column(Integer)
    OSEWellID = Column(String(50))
    OSEWelltagID = Column(String(50))
    MeasuringPoint = Column(String(50))
    MPHeight = Column(Numeric)
    CasingDiameter = Column(Numeric)
    CasingDepth = Column(Numeric)
    CasingDescription = Column(String(50))
    FormationZone = Column(String(50), ForeignKey("LU_Formations.Code"))
    StaticWater = Column(Numeric)
    DataSource = Column(String(200))
    MonitoringStatus = Column(String(3))

    lu_formation = relationship("LU_Formations", backref="wells", uselist=False)
    location = relationship("Location", backref="well", uselist=False)

    # manual_waterlevels = relationship("WaterLevels", backref="well", uselist=False)

    @property
    def pod_url(self):
        ose_id = self.OSEWellID
        if ose_id:
            url = (
                "https://services2.arcgis.com/qXZbWTdPDbTjl7Dy/arcgis/rest/services/"
                "OSE_PODs/FeatureServer/0/query?"
                f"where=+db_file%3D%27{ose_id}%27&f=pjson&outFields=*"
            )
            return url

    @property
    def formation(self):
        return self.lu_formation.Meaning


class ProjectLocations(Base):
    __tablename__ = "ProjectLocations"
    GlobalID = Column(GUID, primary_key=True)
    LocationId = Column(GUID, ForeignKey("Location.LocationId"))
    PointID = Column(String(10))
    ProjectName = Column(String(250))


class OwnersData(Base):
    __tablename__ = "OwnersData"
    FirstName = Column(String(50))
    LastName = Column(String(50))
    OwnerKey = Column(String(50), primary_key=True)
    Email = Column(String(50))
    CellPhone = Column(String(50))
    Phone = Column(String(50))
    MailingAddress = Column(String(50))
    MailCity = Column(String(50))
    MailState = Column(String(50))
    MailZipCode = Column(String(50))
    PhysicalAddress = Column(String(50))
    PhysicalCity = Column(String(50))
    PhysicalState = Column(String(50))
    PhysicalZipCode = Column(String(50))
    SecondLastName = Column(String(50))
    SecondFirstName = Column(String(50))
    SecondCtctEmail = Column(String(50))
    SecondCtctPhone = Column(String(50))


class OwnerLink(Base):
    __tablename__ = "OwnerLink"
    GlobalID = Column(GUID, primary_key=True)
    LocationId = Column(GUID, ForeignKey("Location.LocationId"))
    OwnerKey = Column(String(50), ForeignKey("OwnersData.OwnerKey"))


class Equipment(Base):
    __tablename__ = "Equipment"
    ID = Column(Integer, primary_key=True)
    PointID = Column(String(50))
    LocationId = Column(GUID, ForeignKey("Location.LocationId"))
    EquipmentType = Column(String(50))
    Model = Column(String(50))
    SerialNo = Column(String(50))
    DateInstalled = Column(DateTime)
    DateRemoved = Column(DateTime)
    RecordingInterval = Column(Integer)
    Equipment_Notes = Column(String(50), name="Equipment Notes")


class WellPhotos(Base):
    __tablename__ = "WellPhotos"
    GlobalID = Column(GUID, primary_key=True)
    PointID = Column(String(50))
    OLEPath = Column(String(255))
# ============= EOF =============================================
