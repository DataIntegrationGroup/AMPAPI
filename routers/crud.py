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
from models import location, waterlevel


def geometry_filter(q):
    return q.filter(location.Location.Easting != None).filter(
        location.Location.Northing != None
    )


def public_release_filter(q):
    return q.filter(location.Location.PublicRelease == True)


def pointid_filter(q, pointid):
    if pointid:
        q = q.filter(location.Location.PointID == pointid)
    return q


def db_get_locations(db, limit=10, only_public=True):
    q = db.query(location.Location, location.Well)
    q = q.join(location.Well)
    q = geometry_filter(q)
    if only_public:
        q = public_release_filter(q)
    q = q.order_by(location.Location.PointID)
    if limit > 0:
        q = q.limit(limit)
    return q.all()


def db_get_location(db, pointid, only_public=True):
    q = db.query(location.Location)
    q = q.filter(location.Location.PointID == pointid)
    if only_public:
        q = public_release_filter(q)

    return q.first()


def waterlevels_manual_query(db, pointid, only_public=True):
    q = db.query(waterlevel.WaterLevel)

    if pointid:
        q = q.join(location.Well)
        q = q.join(location.Location)
        q = pointid_filter(q, pointid)

    q = q.order_by(waterlevel.WaterLevel.DateMeasured)
    if only_public:
        q = public_release_filter(q)
    return q
# ============= EOF =============================================
