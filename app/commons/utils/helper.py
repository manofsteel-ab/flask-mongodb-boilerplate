def convert_iso_to_utc(iso_datetime_obj):
    """Convert ISO datetime object to UTC datetime object without the
    microsecond part & utc offset
    """
    return iso_datetime_obj.replace(microsecond=0, tzinfo=None)
