import dagster as dg


daily_partitions = dg.DailyPartitionsDefinition(
    start_date="2024-12-15"
)


@dg.asset(
    partitions_def=daily_partitions,
    metadata={"partition_expr": "created_at"},
    backfill_policy=dg.BackfillPolicy.single_run(),
)
def users(context) -> None:
    """A table containing all users data"""
    # during a backfill the partition range will span multiple hours
    # during a single run the partition range will be for a single hour
    first_partition, last_partition = context.asset_partitions_time_window_for_output()
    context.log.info(f"Processing users data from {first_partition} to {last_partition}")
