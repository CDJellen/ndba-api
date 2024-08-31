from typing import List

import netCDF4 as nc


from ndbc_api.api.parsers.opendap._base import BaseParser


class StdmetParser(BaseParser):

    @classmethod
    def nc_from_responses(cls, responses: List[dict], use_timestamp: bool = False) -> 'nc.Dataset':
        return super(StdmetParser,
                     cls).nc_from_responses(responses)
