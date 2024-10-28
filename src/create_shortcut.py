import os
import winshell
from win32com.client import Dispatch

# Get current directory path
current_dir = os.getcwd()

# Define the paths for the executable and MSI file
exe_path = os.path.join(current_dir, "Calculator.exe")
msi_path = os.path.join(current_dir, "Calculator.msi")

# Define the paths for the desktop shortcuts
desktop = winshell.desktop()
exe_shortcut_path = os.path.join(desktop, "CalculatorApp.lnk")
msi_shortcut_path = os.path.join(desktop, "Calculator.lnk")

# Function to create shortcut
def create_shortcut(target_path, shortcut_path, description=""):
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.Description = description
    shortcut.IconLocation = target_path  # Set the icon to the same as the target
    shortcut.save()

# Create a desktop shortcut for the executable file
create_shortcut(
    target_path=exe_path,
    shortcut_path=exe_shortcut_path,
    description="Calculator Application"
)

# Create a desktop shortcut for the MSI installer
create_shortcut(
    target_path=msi_path,
    shortcut_path=msi_shortcut_path,
    description="BMI Calculator Installer"
)

print("Shortcuts created successfully on the desktop.")
