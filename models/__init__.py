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
from sqlalchemy import Column, Integer, String

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
# ============= EOF =============================================
