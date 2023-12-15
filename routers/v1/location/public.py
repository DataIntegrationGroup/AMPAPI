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
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from routers.v1 import locations_feature_collection
from routers.v1.crud import db_get_locations
from schemas import location

router = APIRouter(prefix="/api/v1/public/locations", tags=["public/locations"])


@router.get("", response_model=location.LocationFeatureCollection)
def get_locations(limit: int = 10, db: Session = Depends(get_db)):
    locations = db_get_locations(db, limit=limit)
    return locations_feature_collection(locations)

# helpers =======================================================================

# ============= EOF =============================================
