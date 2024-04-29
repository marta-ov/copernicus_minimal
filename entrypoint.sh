#!/bin/bash

cd /home/copernicus_minimal_user/copernicus_minimal
source $(poetry env info --path)/bin/activate

python /home/copernicus_minimal_user/copernicus_minimal/run_copernicus_weather_downloader_minimal.py

