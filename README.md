# AirSimAG 🚀

<p align="center"><strong>Air–Ground Cooperative Simulation Platform</strong></p>

<p align="center">
  <a href="https://www.unrealengine.com/"><img src="https://img.shields.io/badge/Unreal%20Engine-4.27-0E1128?style=flat-square&logo=unrealengine" alt="Unreal Engine 4.27"/></a>
  <a href="https://github.com/microsoft/AirSim"><img src="https://img.shields.io/badge/Microsoft-AirSim-0078D4?style=flat-square&logo=microsoft" alt="AirSim"/></a>
  <a href="https://www.ros.org/"><img src="https://img.shields.io/badge/ROS-optional-22314E?style=flat-square&logo=ros" alt="ROS"/></a>
  <a href="https://arxiv.org/abs/2603.23079"><img src="https://img.shields.io/badge/arXiv-2603.23079-b31b1b?style=flat-square&logo=arxiv&logoColor=white" alt="arXiv paper"/></a>
</p>

<p align="center">
  <img src="top.png" alt="AirSimAG overview" width="820"/>
</p>

**AirSimAG** is a **high-fidelity simulator** for cooperative air–ground robotics. It lets you simulate **UAVs (drones) + UGVs (ground vehicles)** together, with:

- 🌍 Shared environments & globally consistent states  
- 🛰️ Multi-modal sensors (RGB, depth, segmentation, LiDAR, IMU…)  
- 🤖 Unified ROS & RPC APIs  
- ⚙️ Pipelines for mapping, planning, tracking, and multi-agent formations  

Perfect for **RL, vision-based planning, and cooperative control experiments**!

---

## 📑 Contents

| § | |
|:-:|---|
| 1 | [✨ Key Features](#key-features) |
| 2 | [🎮 Simulation Capabilities](#simulation-capabilities) |
| 3 | [🎬 Task Demos](#task-demos) |
| 4 | [🧰 Getting Started](#getting-started) |
| 5 | [🚀 Quick Start](#quick-start) |
| 6 | [📖 Citation](#citation) |
| 7 | [📜 License](#license) |

---

## ✨ Key Features

| | |
|:---|:---|
| 🤖 **Air–ground coordination** | Tight coupling between UAVs & UGVs with shared state & coordinated control |
| 🧩 **Unified ROS interface** | RPC + ROS wrapper; synchronized topics & services for multi-agent experiments |
| 🛰️ **Sensors** | RGB, depth, segmentation, LiDAR, IMU; multi-camera & multi-vehicle support |
| 🌍 **Space–time consistency** | Globally aligned coordinates + synchronized timestamps for multi-agent fusion |
| ⚙️ **Task-oriented workflows** | Pipelines & hooks for mapping, planning, tracking, formation control |

---

## 🎮 Simulation Capabilities

AirSimAG inherits AirSim features:

- **Vehicles:** Multirotor (UAV), Car (UGV)  
- **Sensors:** Configurable in `settings.json`  
- **ROS Wrapper:** Optional, fully integrated  

### 📷 Vision & images

| Modality | Description |
|:---------|:------------|
| **RGB / Scene** | Color cameras for learning & perception |
| **Depth** | Planar / perspective depth |
| **Segmentation** | Semantic / instance masks |
| **Extras** | Optical flow, surface normals, IR-style view (optional) |

### 📡 Sensors

| Sensor | Description |
|:-------|:-----------|
| **LiDAR** | 3D point cloud scans |
| **IMU** | Linear acceleration + angular velocity |
| **GPS / GNSS** | Global positioning & navigation |
| **Other** | Barometer, magnetometer, distance sensors |

### 🌍 Environment & State

| | |
|:---|:---|
| **Odometry / Kinematics** | Pose, velocity, acceleration; ROS-friendly |
| **Clock / Time stepping** | Simulation time, pause/step for repeatable experiments |
| **Weather** | Rain, snow, dust, wind |
| **Collision & World** | Meshes, ray casts, collision detection |

---

## 🎬 Task Demos

🎥 **Demo video:** `fig_airsimag/AirSimAG.mp4`

### 🗺️ Mapping

Cooperative mapping with UAV + UGV, synchronized scene & point clouds.

<p align="center">
  <img src="fig_airsimag/task_mapping.png" alt="Mapping task" width="900"/>
</p>

(a) Mapping scene. (b) Fused point cloud map: UAV points in blue, UGV
points in green. (c) UAV and UGV trajectories during the mapping task.


### 🛤️ Path Planning

Multi-level path planning: overpasses, tunnels, obstacles.

<p align="center">
  <img src="fig_airsimag/task_planning.png" alt="Planning task" width="900"/>
</p>
(a) UGV planned path from UAV’s first-person view. (b) UGV
first-person view during planning. (c) Executed UGV trajectory.


### 🎯 Target Tracking

UAV: aerial global view  
UGV: local ground view

<p align="center">
  <img src="fig_airsimag/task_tracking0.png" alt="Tracking task" width="900"/>
</p>

(a) Unreal Engine scene showing the third-person view, UAV first-person
view, and UGV first-person view. (b) Tracking map.

### 🛸 Multi-agent Formation

4 UAVs (square) + 3 UGVs (circle)

<p align="center">
  <img src="fig_airsimag/task_multi.png" alt="Formation task" width="500"/>
</p>

**Hardware:** RTX 4090 + Intel i7-14700KF + 62GB RAM  

| Metric | Value |
|:-------|:-----:|
| **Num. UAV** | 4 |
| **Num. UGV** | 3 |
| **Odometry ROS Topic (Hz)** | >25 |
| **Image ROS Topic (Hz)** | >5 |
| **UE4 FPS** | 45–60 |
| **Memory Usage (MB)** | ~14,852 |

> 💾 **Download pre-recorded rosbags:** [Baidu Netdisk](https://pan.baidu.com/s/1k7ELMYJ1HHQqjnw8iYFZTg?pwd=e7jx) (password: `e7jx`)

---

## 🧰 Getting Started

**Dependencies:**

- 🎮 Unreal Engine 4.27  
- 🧩 AirSim plugin  
- 🤖 ROS (optional)

**Documentation & Build:**

- [AirSim Docs](https://microsoft.github.io/AirSim/)  
- Build instructions: [Windows](https://microsoft.github.io/AirSim/build_windows) · [Linux](https://microsoft.github.io/AirSim/build_linux)  

**APIs:** Python / C++ for images, LiDAR, IMU, vehicle control, ROS integration.

---

## 🚀 Quick Start

### 1️⃣ Clone repo

```bash
git clone [https://github.com/air-sim/airsimag.git](https://github.com/BIULab-BUAA/AirSimAG)
cd AirSimAG
```

### 2️⃣ Build the Unreal Engine project

```bash
# Linux
./build.sh
```

Copy compiled Plugins to your environment project (e.g., CityParkEnvironmentCollection 4.27).

### 3️⃣ Run the simulation

```bash
# Linux
cd ~/UnrealEngine-4.27.0-files
./Engine/Binaries/Linux/UE4Editor
```

Set **GameMode** to **AirSimGameMode**.

### 4️⃣ Play the simulation

Copy `fig_airsimag/settings.json` to your AirSim `settings.json` (Documents on Windows, `~/Documents/AirSim` on Linux). This example configures an air–ground setup with LiDAR and cameras; sensor options are described in the [AirSim documentation](https://microsoft.github.io/AirSim/).

Click **Play** in the Unreal Editor.

### 5️⃣ Control the vehicle

#### 📷 5.1 AirSim Python API — camera recording

```bash
cd AirSimAG/ros
python src/example/camera_record_ag.py
```

#### 📡 5.2 AirSim Python API — LiDAR recording

```bash
cd AirSimAG/ros
python src/example/lidar_record_ag.py
```

#### 🛰️ 5.3 ROS Wrapper

```bash
cd AirSimAG/ros
catkin_make
source devel/setup.bash
roslaunch airsim_ros_pkgs airsim_all.launch
```

Use `rostopic list` to inspect odometry, images, and control topics.

#### ⌨️ 5.4 Keyboard control example

```bash
cd AirSimAG/ros
source devel/setup.bash
python src/example/keyboard_ctrl.py
```

This node publishes body-frame velocity commands for the UAV and car control commands for the UGV. If no key is pressed in the polling window, both vehicles are commanded to **stop** (UAV zero velocity, UGV brake applied). Key bindings for `ros/src/example/keyboard_ctrl.py`:

**🚁 UAV (multirotor)**

| Key | Action |
|:---:|:---|
| **W** | Move forward (positive body-frame forward velocity) |
| **S** | Move backward |
| **A** | Strafe left |
| **D** | Strafe right |
| **F** | Ascend (negative vertical velocity in NED; “up” in world frame) |
| **B** | Descend (positive vertical velocity in NED; “down” in world frame) |
| **Y** | Yaw (positive angular rate about the body vertical axis) |

**🚗 UGV (ground vehicle)**

Keys **8**, **2**, **4**, **6**, and **5** follow a **numeric keypad layout** (8 = up, 2 = down, 4 = left, 6 = right, 5 = center).

| Key | Action |
|:---:|:---|
| **8** | Drive forward (throttle, straight) |
| **2** | Drive backward (reverse throttle, straight) |
| **4** | Forward motion with steering to the **left** |
| **6** | Forward motion with steering to the **right** |
| **5** | Release throttle and steering (coast / stop maneuver; brake command cleared in this example) |

**🔑 Common**

| Key | Action |
|:---:|:---|
| **Q** | Quit the keyboard control node |

> 💡 **Note:** Ensure **Num Lock** is on if you use a keyboard where the number keys share the numpad; otherwise use the dedicated digit keys that produce `8`, `2`, `4`, `6`, `5` in the terminal.

---

## 📖 Citation

If you use this platform in academic work, please cite AirSim and AirSimAG:

```bibtex
@inproceedings{airsim2017fsr,
  author = {Shital Shah and Debadeepta Dey and Chris Lovett and Ashish Kapoor},
  title = {AirSim: High-Fidelity Visual and Physical Simulation for Autonomous Vehicles},
  year = {2017},
  booktitle = {Field and Service Robotics},
  eprint = {arXiv:1705.05065},
  url = {https://arxiv.org/abs/1705.05065}
}

@misc{airsimag2026cui,
      title={AirSimAG: A High-Fidelity Simulation Platform for Air-Ground Collaborative Robotics}, 
      author={Yangjie Cui and Xin Dong and Boyang Gao and Jinwu Xiang and Daochun Li and Zhan Tu},
      year={2026},
      eprint={2603.23079},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2603.23079}, 
}
```

---

## 📜 License

All rights reserved.
