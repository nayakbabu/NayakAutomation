# Docker Desktop Installation Guide for Windows 11

Simple and Complete Step by Step Guide

---

## 1. Enable WSL (Windows Subsystem for Linux)

1. Right-click on the **Start** button → select **Terminal (Admin)**  
   (or **Windows PowerShell (Admin)**)

2. Copy and paste the following command, then press **Enter**:

   ```powershell
   wsl --install

   
3-:Wait for the process to complete (it will download and install Ubuntu by default).

4-: Restart your laptop when prompted.

5-: After restart, open Terminal (Admin) again and run
#wsl --set-default-version 2 (In your powershell terminal )

next action Download & Install Docker Desktop

1-Open your browser (Edge or Chrome).
2-Go to the official Docker website:
3-https://www.docker.com/products/docker-desktop/
4- Click Download for Windows and run the installer.
5-Follow the on-screen instructions (accept defaults is fine).
6-Restart your computer if prompted.

Next action Verify Docker Installation.

Press Windows key, type Terminal, and open Windows Terminal (or PowerShell).


Run these commands one by one


#docker --version
docker run hello-world

 If you see the "Hello from Docker!" message, installation is successful!


Next step of action Set CPU, Memory & Swap Limits (Recommended)


1-Press Windows key + R, type the following and press Enter

notepad %USERPROFILE%\.wslconfig

2- Paste the following content into Notepad:


[wsl2]
memory=8GB
processors=4
swap=2GB

Adjust values based on your system (e.g., 4GB/2 processors for lower RAM laptops).


3-Click File → Save (or press Ctrl + S).

4-Close Notepad.

5-Restart Docker Desktop(Right-click the Docker whale icon in the system tray → Restart)


Done! 
You now have Docker Desktop fully installed and optimized on Windows 11.










