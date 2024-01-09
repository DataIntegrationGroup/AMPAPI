# ===============================================================================
# Copyright 2024 Jake Ross
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
from sqlalchemy import Column, Float, String, DateTime, Integer

from database import Base


class BaseChemistryMixin:
    OBJECTID = Column(Integer, primary_key=True)
    GlobalID = Column(GUID)

    WCLab_ID = Column(String(25))

    SamplePtID = Column(GUID)
    SamplePointID = Column(String(10))

    AnalysesAgency = Column(String(50))

    Analyte = Column(String(50))
    Symbol = Column(String(50))
    SampleValue = Column(Float)
    Units = Column(String(50))
    Uncertainty = Column(Float)
    AnalysisMethod = Column(String(255))
    AnalysisDate = Column(DateTime)
    Notes = Column(String(255))
    Volume = Column(Integer)
    VolumeUnit = Column(String(50))


class MajorChemistry(Base, BaseChemistryMixin):
    __tablename__ = "MajorChemistry"


class MinorandTraceChemistry(Base, BaseChemistryMixin):
    __tablename__ = "MinorandTraceChemistry"


# ============= EOF =============================================
