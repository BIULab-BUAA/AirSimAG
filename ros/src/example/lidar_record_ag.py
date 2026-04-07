#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AirSim lidar record example

"""

import os
import time
import airsim
import numpy as np


# ==========================
# Specify parameters: vehicle names, ports, camera name, save path, FPS
# ==========================

UAV_NAME = "UAV"
UGV_NAME = "Car"

UAV_PORT = 41471
UGV_PORT = 41461

LIDAR_NAME = "Lidar"

SAVE_ROOT = "lidar_dataset"

SAVE_RATE = 10   # Hz 

def save_pcd(points, filename):

    points = np.asarray(points, dtype=np.float32)

    n = points.shape[0]

    header = "\n".join([
        "# .PCD v0.7",
        "VERSION 0.7",
        "FIELDS x y z",
        "SIZE 4 4 4",
        "TYPE F F F",
        "COUNT 1 1 1",
        f"WIDTH {n}",
        "HEIGHT 1",
        "VIEWPOINT 0 0 0 1 0 0 0",
        f"POINTS {n}",
        "DATA ascii"
    ])

    with open(filename, "w") as f:

        f.write(header + "\n")

        for x, y, z in points:
            f.write(f"{x} {y} {z}\n")


def get_lidar_points(client, vehicle_name):

    data = client.getLidarData(
        lidar_name=LIDAR_NAME,
        vehicle_name=vehicle_name
    )

    if len(data.point_cloud) < 3:
        return None

    pts = np.array(data.point_cloud, dtype=np.float32)

    pts = pts.reshape(-1, 3)

    return pts

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


    frame_id = 0

    dt = 1.0 / SAVE_RATE

    print("Start recording LiDAR...")
    print("Press Ctrl+C to stop")

    try:

        while True:

            start = time.time()

            timestamp = int(time.time() * 1000)

            uav_pts = get_lidar_points(uav_client, UAV_NAME)

            if uav_pts is not None:

                filename = os.path.join(
                    uav_dir,
                    f"{frame_id:06d}_{timestamp}.pcd"
                )

                save_pcd(uav_pts, filename)

                print(f"UAV saved {filename} ({uav_pts.shape[0]} pts)")

            ugv_pts = get_lidar_points(ugv_client, UGV_NAME)

            if ugv_pts is not None:

                filename = os.path.join(
                    ugv_dir,
                    f"{frame_id:06d}_{timestamp}.pcd"
                )

                save_pcd(ugv_pts, filename)

                print(f"UGV saved {filename} ({ugv_pts.shape[0]} pts)")


            frame_id += 1

            elapsed = time.time() - start

            if elapsed < dt:
                time.sleep(dt - elapsed)


    except KeyboardInterrupt:

        print("\nRecording stopped by user")


if __name__ == "__main__":
    main()