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
from sqlalchemy import func

from models import location, waterlevel, waterchem
from models.location import ProjectLocations


def geometry_filter(q):
    return q.filter(location.Location.Easting is not None).filter(
        location.Location.Northing is not None
    )


def public_release_filter(q):
    return q.filter(location.Location.PublicRelease == True)


def active_monitoring_filter(q):
    q = q.filter(location.Well.MonitoringStatus.notlike("%I%"))
    q = q.filter(location.Well.MonitoringStatus.notlike("%C%"))
    q = q.filter(location.Well.MonitoringStatus.notlike("%X%"))
    return q


def pointid_filter(q, pointid):
    if pointid:
        q = q.filter(location.Location.PointID == pointid)
    return q


def collabnet_filter(q):
    return q.filter(ProjectLocations.ProjectName == "Water Level Network")


def db_get_equipment(db, pointid):
    q = db.query(location.Equipment)
    q = q.join(location.Location)
    q = pointid_filter(q, pointid)
    q = q.order_by(location.Equipment.DateInstalled.desc())
    return q.all()


def db_get_locations(db, limit=10,
                     collaborative_network=False,
                     only_active=False,
                     only_public=True):
    q = db.query(location.Location, location.Well)
    q = q.join(location.Well)
    if collaborative_network:
        q = q.join(ProjectLocations)

    q = geometry_filter(q)
    if collaborative_network:
        q = collabnet_filter(q)
    if only_public:
        q = public_release_filter(q)
    if only_active:
        q = active_monitoring_filter(q)

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


def db_get_well(db, pointid, only_public=True):
    q = db.query(location.Well)
    q = q.join(location.Location)
    q = q.filter(location.Location.PointID == pointid)
    if only_public:
        q = public_release_filter(q)
    return q.first()


def db_get_photos(db, pointid):
    q = db.query(location.WellPhotos)
    q = q.filter(location.WellPhotos.PointID == pointid)
    return q.all()


# waterchem =======================================================================
MAJOR_CHEM_ANALYTES = ['Na', 'K', 'Ca']

def db_get_analyte_measurements(db, pointid, analyte, only_public=True, minorandtrace=False):
    if analyte is None:
        table = waterchem.MajorChemistry if not minorandtrace else waterchem.MinorandTraceChemistry
    else:
        if analyte in MAJOR_CHEM_ANALYTES:
            table = waterchem.MajorChemistry
        else:
            table = waterchem.TraceChemistry

    q = db.query(table)

    if only_public or pointid:
        q = q.join(location.Location, func.substring(table.SamplePointID, 0, func.len(table.SamplePointID)) ==
                   location.Location.PointID)

    if only_public:
        q = public_release_filter(q)

    if pointid:
        q = q.filter(location.Location.PointID == pointid)

    if analyte:
        q = q.filter(table.Analyte == analyte)

    q = q.limit(10)
    return q.all()


# =================================================================================

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
