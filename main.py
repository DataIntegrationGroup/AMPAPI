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
from fastapi_pagination import add_pagination

from app import app
from routers.location.nmbgmr import router as nmbgmr_location_router
from routers.location.public import router as public_location_router
from routers.waterlevel.public import router as public_waterlevel_router
from routers.waterlevel.nmbgmr import router as nmbgmr_waterlevel_router
from routers.ngwmn.public import router as public_ngwmn_router
from routers.waterchem.nmbgmr import router as nmbgmr_waterchemistry_router
from routers.waterchem.public import router as public_waterchemistry_router

# authenicated routers
app.include_router(nmbgmr_location_router)
app.include_router(nmbgmr_waterlevel_router)
app.include_router(nmbgmr_waterchemistry_router)

# public routers
app.include_router(public_location_router)
app.include_router(public_waterlevel_router)
app.include_router(public_ngwmn_router)
app.include_router(public_waterchemistry_router)


add_pagination(app)
# ============= EOF =============================================