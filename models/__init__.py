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
from fastapi_utils.guid_type import GUID
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declared_attr, relationship

from database import Base


class LU_Mixin(object):
    Code = Column(Integer, primary_key=True)
    Meaning = Column(String(50))


class LU_Formations(Base, LU_Mixin):
    __tablename__ = "LU_Formations"


class LU_LevelStatus(Base, LU_Mixin):
    __tablename__ = "LU_LevelStatus"


class LU_DataQuality(Base, LU_Mixin):
    __tablename__ = "LU_DataQuality"


class LU_MeasurementMethod(Base, LU_Mixin):
    __tablename__ = "LU_MeasurementMethod"


class LU_DataSource(Base, LU_Mixin):
    __tablename__ = "LU_DataSource"


class LU_AltitudeMethod(Base, LU_Mixin):
    __tablename__ = "LU_AltitudeMethod"


class MeasurementMixin(object):
    MeasuringAgency = Column(String(50))

    @declared_attr
    def MeasurementMethod(cls):
        return Column(String(50), ForeignKey("LU_MeasurementMethod.Code"))

    @declared_attr
    def DataSource(cls):
        return Column(String(50), ForeignKey("LU_DataSource.Code"))

    @declared_attr
    def lu_measurement_method(cls):
        return relationship("LU_MeasurementMethod", uselist=False, lazy="joined")

    @declared_attr
    def lu_data_source(cls):
        return relationship("LU_DataSource", uselist=False, lazy="joined")

    @property
    def measurement_method(self):
        try:
            return self.lu_measurement_method.Meaning
        except AttributeError:
            return ""

    @property
    def data_source(self):
        try:
            return self.lu_data_source.Meaning
        except AttributeError:
            return ""


class ProjectLocations(Base):
    __tablename__ = "ProjectLocations"
    GlobalID = Column(GUID, primary_key=True)
    LocationId = Column(GUID, ForeignKey("Location.LocationId"))
    PointID = Column(String(10))
    ProjectName = Column(String(250))
# ============= EOF =============================================
