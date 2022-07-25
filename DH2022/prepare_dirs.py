#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil

from prepare_dirs_utils import retrieve_url, unzip_dir, move_files

# --- create libyan_gazetteer/data/ and tmp_urllib_request/ directories
path2data = os.path.join("libyan_gazetteer", "data")
print(f"[INFO] make directory: {path2data}")
os.makedirs(path2data, exist_ok=True)

path2tmp = os.path.join("tmp_urllib_request")
print(f"[INFO] make directory: {path2tmp}")
os.makedirs(path2tmp, exist_ok=True)

# --- download the data
retrieve_url("https://download.geonames.org/export/dump/LY.zip", os.path.join(path2tmp, "LY.zip"))
retrieve_url("https://download.geonames.org/export/dump/alternateNamesV2.zip", os.path.join(path2tmp, "alternateNamesV2.zip"))
retrieve_url("http://slsgazetteer.org/data/downloads/json/dump.json", os.path.join(path2tmp, "hgl_data.json"))

# --- unzip the data
unzip_dir(os.path.join(path2tmp, "LY.zip"), os.path.join(path2tmp, "LY_dir"))
unzip_dir(os.path.join(path2tmp, "alternateNamesV2.zip"), os.path.join(path2tmp, "alternateNamesV2_dir"))

# --- move the data
move_files(os.path.join(path2tmp, "LY_dir", "LY.txt"), os.path.join(path2data, "LY.txt"))
move_files(os.path.join(path2tmp, "alternateNamesV2_dir", "alternateNamesV2.txt"), os.path.join(path2data, "alternateNamesV2.txt"))
move_files(os.path.join(path2tmp, "hgl_data.json"), os.path.join(path2data, "hgl_data.json"))

# --- remove the tmp_urllib_request/ directory
print(f"[INFO] cleaning up; removing {path2tmp}")
shutil.rmtree(path2tmp)