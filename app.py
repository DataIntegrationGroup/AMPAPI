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
from fastapi import FastAPI, Query
from fastapi_pagination import add_pagination, Page
from starlette.middleware.cors import CORSMiddleware

from settings import settings


app = FastAPI(
    title="New Mexico Bureau of Geology and Mineral Resources Aquifer Mapping Program API",
    version=settings.VERSION,
    docs_url="/",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    description=settings.DESCRIPTION,
    contact={
        "name": "Stacy Timmons",
        "url": "https://geoinfo.nmt.edu/staff/detail.cfml?name=stimmons",
        "email": "stacy.timmons@nmt.edu",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=settings.TAGS,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Page = Page.with_custom_options(
    size=Query(100, ge=1, le=1000),
)

add_pagination(app)


# ============= EOF =============================================
