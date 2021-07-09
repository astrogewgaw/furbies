from json import dump
from requests import get
from csv import DictReader


with open("furbies.json", "w+") as fobj:
    dump(
        obj=dict(
            data={
                str(i + 1): {
                    key: (
                        None
                        if value == "-"
                        else {
                            "frb": str,
                            "utc": str,
                            "mjd": float,
                            "telescope": str,
                            "ra": str,
                            "dec": str,
                            "l": float,
                            "b": float,
                            "frequency": float,
                            "dm": float,
                            "flux": float,
                            "width": float,
                            "fluence": float,
                            "snr": float,
                            "reference": str,
                            "redshift": float,
                        }[key](value)
                    )
                    for key, value in row.items()
                }
                for i, row in enumerate(
                    DictReader(
                        get(
                            "https://raw.githubusercontent.com/HeRTA/FRBSTATS/main/catalogue.csv"
                        )
                        .content.decode()
                        .splitlines()
                    )
                )
            }
        ),
        fp=fobj,
        indent=4,
    )
