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
from typing import List

from fastapi import APIRouter, Depends
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette.responses import FileResponse
from starlette.status import HTTP_200_OK

from dependencies import get_db
from models.location import ProjectLocations, Location, Well, OwnersData, OwnerLink
from routers import locations_feature_collection
from routers.crud import db_get_locations, db_get_location, db_get_photos, db_get_equipment
from auth import auth
from schemas import location

router = APIRouter(prefix="/authorized/locations", tags=["authorized/locations"],
                   dependencies=[Depends(auth.authenticated())])


@router.get("")
def get_locations(db: Session = Depends(get_db)):
    locations = db_get_locations(db, only_public=False)
    return locations_feature_collection(locations)


@router.get("/equipment", response_model=List[location.Equipment])
def get_location_equipment(pointid: str, db: Session = Depends(get_db)):
    eq = db_get_equipment(db, pointid)
    if eq is None:
        eq = Response(status_code=HTTP_200_OK)
    return eq


@router.get("/notes")
def get_location_notes(pointid: str, db: Session = Depends(get_db)):
    loc = db_get_location(db, pointid, only_public=False)
    if loc is None:
        loc = Response(status_code=HTTP_200_OK)
    return loc.LocationNotes or ""


@router.get("/projects", response_model=List[location.ProjectLocations])
def get_location_projects(pointid: str, db: Session = Depends(get_db)):
    q = db.query(ProjectLocations)
    q = q.filter(ProjectLocations.PointID == pointid)
    return q.all()


@router.get("/owners", response_model=location.OwnersData)
def get_location_owners(pointid: str, db: Session = Depends(get_db)):
    q = db.query(Location, Well, OwnersData)
    q = q.join(Well)
    q = q.join(OwnerLink)
    q = q.join(OwnersData)

    q = q.filter(Location.PointID == pointid)
    try:
        loc, well, ownersdata = q.first()
        return ownersdata
    except TypeError as e:
        return {}


@router.get("/photos", response_model=List[location.WellPhoto])
def get_location_photos(pointid: str, db: Session = Depends(get_db)):
    photo_records = db_get_photos(db, pointid)
    return photo_records


@router.get('/photo/{photoid}')
def get_location_photo(photoid: str):
    if photoid:
        path = f"/mnt/wellphotos/Digital photos_wells/{photoid}"
        return FileResponse(path)
    else:
        return Response(status_code=HTTP_200_OK)
# ============= EOF =============================================
