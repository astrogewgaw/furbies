import re
import requests
import pandas as pd

from pathlib import Path
from textwrap import dedent
from bs4 import BeautifulSoup

url = """
    https://www.wis-tns.org/
    search?
    &page={}
    &discovered_period_value=
    &discovered_period_units=months
    &unclassified_at=0
    &classified_sne=0
    &include_frb=1
    &name=&
    name_like=0
    &isTNS_AT=yes
    &public=all
    &ra=
    &decl=
    &radius=
    &coords_unit=arcsec
    &reporting_groupid[]=null
    &groupid[]=null
    &classifier_groupid[]=null
    &objtype[]=130
    &at_type[]=5
    &date_start[date]=
    &date_end[date]=
    &discovery_mag_min=
    &discovery_mag_max=
    &internal_name=
    &discoverer=
    &classifier=
    &spectra_count=
    &redshift_min=
    &redshift_max=
    &hostname=
    &ext_catid=
    &ra_range_min=
    &ra_range_max=
    &decl_range_min=
    &decl_range_max=
    &discovery_instrument[]=null
    &classification_instrument[]=null
    &associated_groups[]=null
    &official_discovery=0
    &official_classification=0
    &at_rep_remarks=
    &class_rep_remarks=
    &frb_repeat=all
    &frb_repeater_of_objid=
    &frb_measured_redshift=0
    &frb_dm_range_min=
    &frb_dm_range_max=
    &frb_rm_range_min=
    &frb_rm_range_max=
    &frb_snr_range_min=
    &frb_snr_range_max=
    &frb_flux_range_min=
    &frb_flux_range_max=
    &num_page=50
    &display[redshift]=0
    &display[hostname]=0
    &display[host_redshift]=0
    &display[source_group_name]=1
    &display[classifying_source_group_name]=0
    &display[discovering_instrument_name]=0
    &display[classifing_instrument_name]=0
    &display[programs_name]=0
    &display[internal_name]=1
    &display[isTNS_AT]=0
    &display[public]=1
    &display[end_pop_period]=0
    &display[spectra_count]=0
    &display[discoverymag]=1
    &display[discmagfilter]=1
    &display[discoverydate]=1
    &display[discoverer]=1
    &display[remarks]=0
    &display[sources]=0
    &display[bibcode]=0
    &display[ext_catalogs]=0
    &display[repeater_of_objid]=1
    &display[dm]=1
    &display[galactic_max_dm]=0
    &display[barycentric_event_time]=0
    &display[public_webpage]=0
    &format=csv
    """
url = dedent(url).replace("\n", "")


frbhdr = [
    "ID",
    "NAME",
    "RA",
    "DEC",
    "TYPE",
    "PRIMARY_BURST",
    "DM",
    "DM_ERR",
    "DM_UNITS",
    "GAL_DM_LIMIT",
    "GAL_DM_MODEL",
    "BARY_DATETIME",
    "REDSHIFT",
    "HOSTNAME",
    "HOST_REDSHIFT",
    "REPORTING_GROUP",
    "DISC_DATA_SOURCE",
    "CLASSIFYING_GROUP",
    "ASSOC_GROUP",
    "DISC_INTERNAL_NAME",
    "DISC_INSTRUMENT",
    "CLASS_INSTRUMENT",
    "TNS_AT",
    "PUBLIC",
    "END_PROP_PERIOD",
    "DISC_MAG_FLUX",
    "DISC_FILTER",
    "DISC_DATE_UTC",
    "SENDER",
    "REMARKS",
    "EXT_CATALOG",
]


def numpages() -> int:

    """"""

    return len(
        re.search(
            r"Pages(\d[\n\d]+)",
            BeautifulSoup(
                requests.get(url.replace("&format=csv", "").format("0")).content, "lxml"
            ).text,
        )
        .group()
        .split()
    )


def scrap() -> None:

    """"""

    N = numpages()

    dfs = []
    for i in range(N):
        page = requests.get(url.format(str(i)))
        fname = "".join([str(i), ".csv"])
        with open(fname, "w+") as fobj:
            fobj.write(page.content.decode())
        dfs.append(pd.read_csv(fname))
        Path(fname).unlink()
    frbdf = pd.concat(dfs)
    frbdf.columns = frbhdr
    frbdf.reset_index(
        drop=True,
        inplace=True,
    )
    frbdf.index = frbdf.index + 1  # type: ignore

    with open("furbies.json", "w+") as fobj:
        frbdf.to_json(
            fobj,
            indent=4,
            orient="index",
        )


if __name__ == "__main__":

    scrap()