import copernicusmarine
import os
from datetime import datetime, timezone

todays_date_time = datetime.utcnow().replace(tzinfo=timezone.utc)
output_path = "/home/copernicus_minimal_user/forecasts"


copernicusmarine.login(
    username=os.getenv("COPERNICUS_USERNAME"),
    password=os.getenv("COPERNICUS_PASSWORD"),
    overwrite_configuration_file=True,
)

copernicus_date = todays_date_time.strftime("%Y%m%d")

today_forecasts = copernicusmarine.get(
    dataset_id="cmems_mod_glo_phy_anfc_merged-uv_PT1H-i",
    filter=f"*_R{copernicus_date}.nc",
    no_directories=True,
    output_directory=output_path,
    force_download=True,
)
