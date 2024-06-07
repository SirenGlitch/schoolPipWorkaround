import os

base_command = 'py -m pip install \
--trusted-host pypi.org \
--trusted-host pypi.python.org \
--trusted-host files.pythonhosted.org '

package = input("What package would you like to install? (Just press Enter for pygame) ")

if package:
    install_command = base_command + package
else:
    install_command = base_command + 'pygame'

os.system(install_command)
