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

from datetime import date, time, datetime
from typing import Union

from pydantic import Field, validator

from schemas import ORMBaseModel


class WaterLevels(ORMBaseModel):
    DepthToWaterBGS: Union[float, None] = None
    DepthToWaterBGSUnits = "feet"
    DateMeasured: Union[date, None] = None
    TimeMeasured: Union[time, None] = None
    LevelStatus: Union[str, None] = None
    DataQuality: Union[str, None] = None
    MeasuringAgency: Union[str, None] = None
    DataSource: Union[str, None] = None
    MeasurementMethod: Union[str, None] = None

    @validator("DepthToWaterBGS")
    def validate_depth_to_water(cls, v):
        return round(v, 2)


# ============= EOF =============================================
