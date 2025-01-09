import pandas as pd
import numpy as np

# This python mode is equivalent of dim_listing_w_host.sql sql model
def model(dbt, session):
    # Load the input datasets as pandas DataFrames
    dim_listings_cleansed = dbt.ref("dim_listings_cleansed").to_pandas()
    dim_hosts_cleansed = dbt.ref("dim_hosts_cleansed").to_pandas()

    # Perform a LEFT JOIN on the host_id column
    merged_df = dim_listings_cleansed.merge(
        dim_hosts_cleansed,
        how="left",
        left_on="HOST_ID",
        right_on="HOST_ID",
        suffixes=("", "_HOST")
    )

    # Select and compute the necessary columns
    result_df = pd.DataFrame({
        "listing_id": merged_df["LISTING_ID"],
        "listing_name": merged_df["LISTING_NAME"],
        "room_type": merged_df["ROOM_TYPE"],
        "minimum_nights": merged_df["MINIMUM_NIGHTS"],
        "price": merged_df["PRICE"],
        "host_id": merged_df["HOST_ID"],
        "host_name": merged_df["HOST_NAME"],
        "host_is_superhost": merged_df["IS_SUPERHOST"],
        "created_at": merged_df["CREATED_AT"],
        "updated_at": merged_df[["UPDATED_AT", "UPDATED_AT_HOST"]].max(axis=1)
    })

    return result_df
