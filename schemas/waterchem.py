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
import uuid
from datetime import datetime
from typing import Union

from schemas import ORMBaseModel


class AnalyteMeasurements(ORMBaseModel):
    # OBJECTID: int
    # GlobalID: str

    WCLab_ID: Union[str, None]

    SamplePtID: Union[uuid.UUID, None]
    SamplePointID: Union[str, None]

    AnalysesAgency: Union[str, None]

    Analyte: Union[str, None]
    Symbol: Union[str, None]
    SampleValue: Union[float, None]
    Units: Union[str, None]
    Uncertainty: Union[float, None]
    AnalysisMethod: Union[str, None]
    AnalysisDate: Union[datetime, None]
    Notes: Union[str, None]
    Volume: Union[int, None]
    VolumeUnit: Union[str, None]


# ============= EOF =============================================
