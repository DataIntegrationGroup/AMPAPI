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
from models.locations import models


def geometry_filter(q):
    return q.filter(models.Location.Easting != None).filter(
        models.Location.Northing != None
    )


def public_release_filter(q):
    return q.filter(models.Location.PublicRelease == True)


def db_get_locations(db, limit=10, only_public=True):
    q = db.query(models.Location, models.Well)
    q = q.join(models.Well)
    q = geometry_filter(q)
    if only_public:
        q = public_release_filter(q)
    q = q.order_by(models.Location.PointID)
    if limit > 0:
        q = q.limit(limit)
    return q.all()


def db_get_location(db, pointid, only_public=True):
    q = db.query(models.Location)
    q = q.filter(models.Location.PointID == pointid)
    if only_public:
        q = public_release_filter(q)

    return q.first()
# ============= EOF =============================================
