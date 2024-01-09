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

import csv
import io
from datetime import datetime
from fastapi_pagination import Page, LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from dependencies import get_db
from routers import AuthAPIRouter
from routers.crud import waterlevels_manual_query, waterlevels_continuous_query, waterlevels_query
from schemas import waterlevel

router = AuthAPIRouter(prefix="waterlevels")

@router.get("/", response_model=Page[waterlevel.WaterLevels])
@router.get(
    "/limit-offset",
    response_model=LimitOffsetPage[waterlevel.WaterLevels],
    include_in_schema=False,
)
def get_waterlevels(pointid: str = None, db: Session = Depends(get_db)):
    q = waterlevels_query(db, pointid, only_public=False)
    return paginate(q)


@router.get("/manual", response_model=Page[waterlevel.WaterLevels])
@router.get(
    "/manual/limit-offset",
    response_model=LimitOffsetPage[waterlevel.WaterLevels],
    include_in_schema=False,
)
def get_waterlevels_manual(pointid: str = None, db: Session = Depends(get_db)):
    q = waterlevels_manual_query(db, pointid, only_public=False)
    return paginate(q)


@router.get("/continuous", response_model=Page[waterlevel.WaterLevels])
@router.get(
    "/continuous/limit-offset",
    response_model=LimitOffsetPage[waterlevel.WaterLevels],
    include_in_schema=False,
)
def get_waterlevels_continuous(pointid: str = None, db: Session = Depends(get_db)):
    q = waterlevels_continuous_query(db, pointid, only_public=False)
    return paginate(q)


# ============= EOF =============================================
