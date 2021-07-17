if __name__ == "__main__":

    import json
    import pandas as pd  # type: ignore
    from textwrap import dedent

    with open("furbies.json", "w+") as f:
        json.dump(
            fp=f,
            obj={
                "data": {
                    str(int(key) + 1): value
                    for key, value in json.loads(
                        pd.read_csv(
                            dedent(
                                """
            https://
            docs.google.com/
            spreadsheets/
            d/
            1W27KNa6yJzYA_b8HLSz4hxtWEZQtxUhGTXfQjlXgpzY/
            export?format=csv&
            gid=1560822367
            """
                            )
                            .replace("\n", "")
                            .strip()
                        ).to_json(orient="index")
                    ).items()
                }
            },
            indent=4,
        )
