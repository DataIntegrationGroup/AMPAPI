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
import os


class Settings:
    # PROJECT_NAME: str = "Job Board"
    # PROJECT_VERSION: str = "1.0.0"
    #
    # USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")
    # POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    # POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    # POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # POSTGRES_PORT: str = os.getenv(
    #     "POSTGRES_PORT", 5432
    # )  # default postgres port is 5432
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    # DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    DESCRIPTION = ''
    TAGS = None

    """
    Versioning rules. 
    X.Y.Z
    X - major version. incompatible API changes
    Y - minor version. backward compatible API changes. new features
    Z - patch version. backward compatible bug fixes. cosmetic changes
    """

    VERSION = '0.4.0'
    ALLOWED_HOSTS: list = ["*"]

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # in mins
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    SQLALCHEMY_DATABASE_URL: str

    # FIEF ==================================================
    FIEF_URL: str
    FIEF_CLIENT_ID: str
    FIEF_CLIENT_SECRET: str

    def __init__(self):
        self.IS_LOCAL = os.getenv("IS_LOCAL", True)
        self.SECRET_KEY = os.getenv("SECRET_KEY")

        self.FIEF_CLIENT_SECRET = os.getenv("FIEF_CLIENT_SECRET")
        self.FIEF_CLIENT_ID = os.getenv("FIEF_CLIENT_ID")
        self.FIEF_URL = os.getenv("FIEF_URL")
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            self.SQLALCHEMY_DATABASE_URL = database_url
        else:
            # user = os.environ.get("POSTGRES_USER")
            # password = os.environ.get("POSTGRES_PASSWORD")
            # host = os.environ.get("POSTGRES_HOST")
            # database = os.environ.get("POSTGRES_DB")

            user = os.environ.get("DB_USER")
            password = os.environ.get("DB_PASSWORD")
            host = os.environ.get("DB_HOST")
            database = os.environ.get("DB_NAME")

            self.SQLALCHEMY_DATABASE_URL = (
                f"mssql+pymssql://{user}:{password}@{host}/{database}"
            )

        with open('./description.md') as rfile:
            self.DESCRIPTION = rfile.read()

        self.TAGS = [{'name': 'public/locations', 'description': 'Publicly available locations'},
                     {'name': 'public/waterlevels', 'description': 'Publicly available water levels'},
                     {'name': 'public/waterchemistry', 'description': 'Publicly available water chemistry'},

                     {'name': 'authorized/locations', 'description': 'Locations only accessible to NMBGMR Staff; '
                                                                     '<b>authentication required</b>'},
                     {'name': 'authorized/waterlevels', 'description': 'Water levels only accessible to NMBGMR Staff; '
                                                                       '<b>authentication required</b>'},
                     {'name': 'authorized/waterchemistry', 'description': 'Water chemistry only accessible to NMBGMR '
                                                                          'Staff; '
                                                                          '<b>authentication required</b>'},
                     {'name': 'NGWMN', 'description': 'National Ground Water Monitoring Network. These endpoints are '
                                                      'used by the NGWMN to access data from the NMBGMR'},
                     ]


settings = Settings()
# ============= EOF =============================================
