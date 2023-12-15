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
from routers import locations_feature_collection, usgs_util
from routers.crud import db_get_locations, db_get_location
from schemas import location

router = APIRouter(prefix="/public/locations", tags=["public/locations"])


@router.get("",
            description='Get all publicly available locations',
            response_model=location.LocationFeatureCollection)
def get_locations(limit: int = 10, db: Session = Depends(get_db)):
    locations = db_get_locations(db, limit=limit)
    return locations_feature_collection(locations)


@router.get('/collaborative_network',
            summary='Get Collaborative Network Locations',
            description='Get locations that are part of the collaborative network',
            response_model=location.LocationFeatureCollection)
def get_collaborative_network(active: bool = True, db: Session = Depends(get_db)):
    locations = db_get_locations(db, collaborative_network=True,
                                 only_active=active,
                                 )
    return locations_feature_collection(locations)


@router.get('/usgs/sitemetadata',
            summary='Get USGS Site Metadata',
            description='Get USGS site metadata from the NWIS service <a '
                        'href="https://waterservices.usgs.gov/rest/Site-Service.html">https://waterservices.usgs.gov'
                        '/rest/Site-Service.html</a>')
def get_usgs_sitemetadata(pointid: str, db: Session = Depends(get_db)):
    loc = db_get_location(db, pointid)
    return usgs_util.get_site_metadata(loc)

# helpers =======================================================================

# ============= EOF =============================================
