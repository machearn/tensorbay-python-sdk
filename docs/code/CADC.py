#!/usr/bin/env python3
#
# Copyright 2021 Graviti. Licensed under MIT License.
#

# pylint: disable=wrong-import-position
# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name
# pylint: disable=unsubscriptable-object

"""This file includes the python code of CADC.rst."""

"""Authorize a Client Instance"""
from tensorbay import GAS
from tensorbay.dataset import FusionDataset

gas = GAS("<YOUR_ACCESSKEY>")
""""""

"""Create Fusion Dataset"""
gas.create_dataset("CADC", is_fusion=True)
""""""

"""List Dataset Names"""
gas.list_dataset_names()
""""""

from tensorbay.opendataset import CADC

fusion_dataset = CADC("<path/to/dataset>")


"""Upload Fusion Dataset"""
# fusion_dataset is the one you initialized in "Organize Fusion Dataset" section
fusion_dataset_client = gas.upload_dataset(fusion_dataset, jobs=8)
fusion_dataset_client.commit("initial commit")
""""""

"""Read Fusion Dataset / get fusion dataset"""
fusion_dataset = FusionDataset("CADC", gas)
""""""

"""Read Fusion Dataset / list fusion segment names"""
fusion_dataset.keys()
""""""

"""Read Fusion Dataset / get fusion segment"""
fusion_segment = fusion_dataset["2018_03_06/0001"]
fusion_segment = fusion_dataset[0]
""""""

"""Read Fusion Dataset / get sensors"""
sensors = fusion_segment.sensors
""""""

"""Read Fusion Dataset / get frame"""
frame = fusion_segment[0]
""""""

"""Read Fusion Dataset / get data"""
for sensor_name in sensors.keys():
    data = frame[sensor_name]
""""""

"""Read Fusion Dataset / get label"""
lidar_data = frame["LIDAR"]
label_box3d = lidar_data.label.box3d[0]
category = label_box3d.category
attributes = label_box3d.attributes
""""""

"""Delete Fusion Dataset"""
gas.delete_dataset("CADC")
""""""
