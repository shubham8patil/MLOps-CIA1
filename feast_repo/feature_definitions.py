
from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64


# --------------------------------------------------
# ENTITY
# --------------------------------------------------

visitor = Entity(
    name="visitor",
    join_keys=["visitor_id"],
    description="Online shopping visitor/session"
)


# --------------------------------------------------
# DATA SOURCE
# --------------------------------------------------

online_shopper_source = FileSource(
    name="online_shopper_features_source",
    path="/content/feast_repo/data/online_shoppers_features.parquet",
    timestamp_field="event_timestamp"
)


# --------------------------------------------------
# FEATURE VIEW
# --------------------------------------------------

online_shopper_features = FeatureView(
    name="online_shopper_features",

    entities=[visitor],

    ttl=timedelta(days=365),

    schema=[
        Field(name="Administrative", dtype=Int64),
        Field(name="Administrative_Duration", dtype=Float32),
        Field(name="Informational", dtype=Int64),
        Field(name="Informational_Duration", dtype=Float32),
        Field(name="ProductRelated", dtype=Int64),
        Field(name="ProductRelated_Duration", dtype=Float32),
        Field(name="BounceRates", dtype=Float32),
        Field(name="ExitRates", dtype=Float32),
        Field(name="PageValues", dtype=Float32),
        Field(name="SpecialDay", dtype=Float32),
        Field(name="OperatingSystems", dtype=Int64),
        Field(name="Browser", dtype=Int64),
        Field(name="Region", dtype=Int64),
        Field(name="TrafficType", dtype=Int64),
        Field(name="Revenue", dtype=Int64),
    ],

    source=online_shopper_source,

    online=True
)
