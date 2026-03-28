# Network Congestion Control Simulation (OpenGL + Pygame)

This project is a simple graphical simulation of **network congestion control** built using **Python, Pygame, and OpenGL**.  
It visually demonstrates how packets travel through a network and how congestion affects packet transmission speed.

The simulation displays packets moving through a network path connected to a router. When too many packets accumulate, the network becomes congested and packet movement slows down.

--------------------------------------------------

## Features

• Visual simulation of packet transmission  
• Router representation using a 3D sphere  
• Dynamic packet generation  
• Congestion detection based on packet count  
• Reduced packet speed when congestion occurs  
• Real-time animation using Pygame and OpenGL  

--------------------------------------------------

## Technologies Used

Python  
Pygame  
PyOpenGL (OpenGL, GLUT, GLU)  
Random module  

--------------------------------------------------

## Project Concept

The program simulates a network where packets are generated randomly and travel across a communication line.

Key behaviors:

1. Packets are generated randomly from the left side of the screen.
2. Packets move across the network line toward the router.
3. When the number of packets exceeds a certain threshold, congestion occurs.
4. During congestion, packet movement speed decreases.
5. Once packets leave the network path, they are removed from the simulation.

This helps visualize the basic concept of **network congestion control in computer networks**.

--------------------------------------------------

## Installation

1. Install Python (3.x recommended)

2. Install required libraries

pip install pygame
pip install PyOpenGL
pip install PyOpenGL_accelerate

--------------------------------------------------

## How to Run the Program

Run the Python script:

python congestion_simulation.py

A window will open displaying the network simulation.

--------------------------------------------------

## Controls

ESC key → Exit the simulation

--------------------------------------------------

## Visualization Elements

Router  
Represented by a blue 3D sphere.

Packets  
Displayed as small red squares moving along the network path.

Network Path  
A white line representing the communication channel.

Congestion State  
When packet count exceeds 10, the system enters a congested state and packet speed decreases.

