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
import requests


def get_site_metadata(location):
    """
    get site metadata from USGS
    :param location:
    :return:
    """

    siteid = location.SiteID
    url = f"https://waterservices.usgs.gov/nwis/site/?format=rdb&sites={siteid}&siteStatus=all&siteOutput=expanded"
    resp = requests.get(url)
    if resp.status_code == 200:
        return make_site_record(resp.text), url


def make_site_record(txt):
    header = ''
    for line in txt.split("\n"):
        if line.startswith("#"):
            continue

        if line.startswith("agency_cd"):
            header = [h.strip() for h in line.split("\t")]
            continue

        if line.startswith("5s"):
            continue

        return dict(zip(header, [l.strip() for l in line.split("\t")]))
# ============= EOF =============================================
