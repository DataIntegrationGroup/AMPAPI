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

from auth import auth


def locations_feature_collection(locations):
    def togeojson(l, w):
        return {
            "type": "Feature",
            "properties": {
                "name": l.PointID,
                "well_depth": {"value": w.WellDepth, "units": "ft"},
            },
            "geometry": l.geometry,
        }

    content = {
        "features": [togeojson(*l) for l in locations],
    }

    return content


class AuthAPIRouter(APIRouter):
    def __init__(self, prefix=None, tags=None, *args, **kw):
        if prefix is None:
            raise ValueError("prefix required")

        if tags is None:
            tags = [f"authorized/{prefix}"]

        super(AuthAPIRouter, self).__init__(
            prefix=f"/authorized/{prefix}",
            tags=tags,
            dependencies=[Depends(auth.authenticated())],
            *args,
            **kw,
        )


# ============= EOF =============================================
