from dagster import Definitions, load_assets_from_modules, define_asset_job

from . import assets  # noqa: TID252

all_assets = load_assets_from_modules([assets])

partitioned_job = define_asset_job("partitioned_job", all_assets)

defs = Definitions(
    assets=all_assets,
    jobs=[partitioned_job],
)
