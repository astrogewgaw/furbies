if __name__ == "__main__":

    import pandas as pd  # type: ignore
    from textwrap import dedent

    df = pd.read_csv(
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
    ).to_json(
        "furbies.json",
        indent=4,
        orient="index",
    )
