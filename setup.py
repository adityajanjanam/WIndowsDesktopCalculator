from cx_Freeze import setup, Executable

# Define the executable and its settings
executables = [Executable("calculator.py", base="Win32GUI", target_name="CalculatorApp.exe")]

# Setup cx_Freeze with the information about your application
setup(
    name="CalculatorApp",
    version="1.0",
    description="A simple calculator app",
    executables=executables,
    options={
        'build_exe': {
            'packages': [],
            'include_files': []
        },
        'bdist_msi': {
            'add_to_path': True,
            'initial_target_dir': r'[ProgramFilesFolder]\CalculatorApp',
	       'summary_data': {
                'author': "Aditya Janjanam",  # This is where you set the publisher name
            }

        }
    }
)
         