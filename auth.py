# ===============================================================================
# Copyright 2023 ross
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

from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from settings import settings

scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.FIEF_URL}/authorize",
    tokenUrl=f"{settings.FIEF_URL}/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

fief = FiefAsync(
    settings.FIEF_URL, settings.FIEF_CLIENT_ID, settings.FIEF_CLIENT_SECRET
)
auth = FiefAuth(fief, scheme)

# ============= EOF =============================================
