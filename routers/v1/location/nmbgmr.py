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
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK

from dependencies import get_db
from routers.v1 import locations_feature_collection
from routers.v1.crud import db_get_locations, db_get_location
from auth import auth

router = APIRouter(prefix="/api/v1/locations", tags=["locations"],

                   dependencies=[Depends(auth.authenticated())])


@router.get("")
def get_locations(db: Session = Depends(get_db)):
    locations = db_get_locations(db, only_public=False)
    return locations_feature_collection(locations)


@router.get("/notes")
def location_notes(pointid: str, db: Session = Depends(get_db)):
    loc = db_get_location(db, pointid, only_public=False)
    if loc is None:
        loc = Response(status_code=HTTP_200_OK)
    return loc.LocationNotes or ""

#
# @router.get("/{pointid}/projects", response_model=List[schemas.ProjectLocations])
# def location_projects(pointid: str, db: Session = Depends(get_db)):
#     q = db.query(models.ProjectLocations)
#     q = q.filter(models.ProjectLocations.PointID == pointid)
#     return q.all()
#
#
# @router.get("/{pointid}/owners", response_model=schemas.OwnersData)
# def location_detail_owners(pointid: str, db: Session = Depends(get_db)):
#     q = db.query(models.Location, models.Well, models.OwnersData)
#     q = q.join(models.Well)
#     q = q.join(models.OwnerLink)
#     q = q.join(models.OwnersData)
#
#     q = q.filter(models.Location.PointID == pointid)
#     try:
#         loc, well, ownersdata = q.first()
#         return ownersdata
#     except TypeError as e:
#         return {}
# ============= EOF =============================================
