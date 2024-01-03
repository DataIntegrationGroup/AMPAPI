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
from database import Base
from models import MeasurementMixin


class WaterLevel(Base, MeasurementMixin):
    __tablename__ = "WaterLevels"
    OBJECTID = Column(Integer, primary_key=True)
    WellID = Column(
        GUID, ForeignKey("WellData.WellID"), primary_key=True, cache_ok=True
    )
    DepthToWaterBGS = Column(Numeric)
    DateMeasured = Column(Date)
    TimeMeasured = Column(Time)
    PublicRelease = Column(Boolean)

    MeasuringAgency = Column(String(50))

    @declared_attr
    def DataSource(self):
        return Column(String(5), ForeignKey("LU_DataSource.Code"))

    @declared_attr
    def LevelStatus(self):
        return Column(String(2), ForeignKey("LU_LevelStatus.Code"))

    @declared_attr
    def DataQuality(self):
        return Column(String(2), ForeignKey("LU_DataQuality.Code"))

    @declared_attr
    def lu_level_status(cls):
        return relationship("LU_LevelStatus", uselist=False, lazy="joined")

    @declared_attr
    def lu_data_quality(cls):
        return relationship("LU_DataQuality", uselist=False, lazy="joined")

    @property
    def level_status(self):
        try:
            return self.lu_level_status.Meaning
        except AttributeError:
            return ""

    @property
    def data_quality(self):
        try:
            return self.lu_data_quality.Meaning
        except AttributeError:
            return ""
# ============= EOF =============================================
