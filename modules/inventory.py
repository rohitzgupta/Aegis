import pandas as pd


def load_inventory(file_path):

    return pd.read_csv(file_path)


def process_inventory_query(query, inventory_df):

    query = query.strip()

    if query.lower().startswith("count by"):

        column = (
            query.lower()
            .replace("count by", "")
            .strip()
        )

        if column in inventory_df.columns:

            return (
                inventory_df
                .groupby(column)
                .size()
                .reset_index(name="count")
                .sort_values(
                    "count",
                    ascending=False
                )
            )

        return f"Column '{column}' not found."

    filters = {}

    for item in query.split(","):

        if "=" not in item:
            continue

        key, value = item.split("=", 1)

        filters[key.strip()] = value.strip()

    result = inventory_df.copy()

    for key, value in filters.items():

        if key not in result.columns:
            continue

        result = result[
            result[key]
            .astype(str)
            .str.lower()
            ==
            value.lower()
        ]

    return result