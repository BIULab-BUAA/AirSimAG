#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AirSim camera record example
"""

import airsim
import numpy as np
import cv2
import os
import time

# =============================
# Specify parameters: vehicle names, ports, camera name, save path, FPS
# =============================

UAV_NAME = "UAV"
UGV_NAME = "Car"

UAV_PORT = 41471
UGV_PORT = 41461

CAMERA_NAME = "front_center_scene"

SAVE_ROOT = "planning"

FPS = 10

# =============================
# Get image
# =============================

def get_image(client, vehicle_name):

    response = client.simGetImages(
        [
            airsim.ImageRequest(
                CAMERA_NAME,
                airsim.ImageType.Scene,
                False,
                False,
            )
        ],
        vehicle_name=vehicle_name,
    )[0]

    if response.width == 0:
        return None

    img1d = np.frombuffer(response.image_data_uint8, dtype=np.uint8)

    img_rgb = img1d.reshape(response.height, response.width, 3)

    return img_rgb


def main():

    print("Connecting UAV...")
    uav_client = airsim.MultirotorClient(port=UAV_PORT)
    uav_client.confirmConnection()

    print("Connecting UGV...")
    try:
        ugv_client = airsim.CarClient(port=UGV_PORT)
        ugv_client.confirmConnection()
    except:
        ugv_client = airsim.MultirotorClient(port=UGV_PORT)
        ugv_client.confirmConnection()

    uav_dir = os.path.join(SAVE_ROOT, "UAV")
    ugv_dir = os.path.join(SAVE_ROOT, "UGV")

    os.makedirs(uav_dir, exist_ok=True)
    os.makedirs(ugv_dir, exist_ok=True)

    timestamp_file = open(os.path.join(SAVE_ROOT, "timestamps.txt"), "w")

    frame_id = 0

    dt = 1.0 / FPS

    print("Start recording camera...")
    print("Press Ctrl+C to stop")

    try:

        while True:

            start = time.time()
            timestamp = int(time.time() * 1000)
            uav_img = get_image(uav_client, UAV_NAME)

            if uav_img is not None:

                filename = os.path.join(
                    uav_dir,
                    f"{frame_id:06d}_{timestamp}.jpg"
                )

                cv2.imwrite(filename, uav_img)

                print("UAV saved", filename)

            ugv_img = get_image(ugv_client, UGV_NAME)

            if ugv_img is not None:

                filename = os.path.join(
                    ugv_dir,
                    f"{frame_id:06d}_{timestamp}.jpg"
                )

                cv2.imwrite(filename, ugv_img)

                print("UGV saved", filename)

            timestamp_file.write(f"{frame_id} {timestamp}\n")

            frame_id += 1

            elapsed = time.time() - start

            if elapsed < dt:
                time.sleep(dt - elapsed)


    except KeyboardInterrupt:

        print("\nRecording stopped")

    timestamp_file.close()


if __name__ == "__main__":
    main()