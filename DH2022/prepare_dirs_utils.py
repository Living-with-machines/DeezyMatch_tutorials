#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import shutil
import urllib.request
import zipfile


# ------------------------
# --- helper functions ---
# ------------------------

def retrieve_url(http_add, local_name):
    """
    Retrieve a file from a URL.
    Args:
        http_add (str): The URL to retrieve the file from.
        local_name (str): The name to save the file as.
    """

    print(f"[INFO] Retrieving {http_add} to {local_name}")

    try:
        urllib.request.urlretrieve(http_add, local_name)
    except Exception as err:
        print(err)
        print(f"[INFO] Could not download {http_add}. Please download this manually.")

def unzip_dir(zip_path, new_path):
    """
    Unzip a directory.
    Args:
        zip_path (str): The path to the zip file.
        new_path (str): The path to extract the zip file to.
    """

    print(f"[INFO] Unzipping {zip_path} to {new_path}")
    
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(new_path)
    except Exception as err:
        print(err)
        print(f"[INFO] Could not unzip {zip_path}. Please unzip this manually.")

def move_files(src_path, dst_path):
    """
    Move files from one directory to another.
    Args:
        src_path (str): The path to the source directory.
        dst_path (str): The path to the destination directory.
    """

    print(f"[INFO] Moving files from {src_path} to {dst_path}")
    
    try:
        shutil.move(src_path, dst_path)
    except Exception as err:
        print(err)
        print(f"[INFO] Could not move files from {src_path} to {dst_path}. Please move them manually.")