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
from datetime import datetime, date
from typing import Union, Optional
from uuid import UUID

from pydantic import Field, BaseModel, validator

from schemas import ORMBaseModel


class Location(ORMBaseModel):
    LocationId: UUID
    PointID: str
    PublicRelease: bool
    AlternateSiteID: Union[str, None]  # = Field(..., alias="alternate_site_id")
    elevation_method: Union[str, None]  # = Field(..., alias="elevation_method")
    Elevation: Union[float, None]
    SiteNames: Union[str, None]  # = Field(..., alias="site_names")
    SiteID: Union[str, None]  # = Field(..., alias="site_id")
    Easting: Union[float, None]
    Northing: Union[float, None]
    geometry: Optional[dict] = None

    @validator("Elevation")
    @classmethod
    def elevation_check(cls, v):
        if v is not None:
            return round(v, 2)
        else:
            return 0


class LocationGeoJSON(ORMBaseModel):
    type: str = "Feature"
    properties: dict = Field(default={}, alias="properties")
    geometry: dict = Field(..., alias="geometry")


class LocationFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: list = Field(..., alias="features")
# ============= EOF =============================================
