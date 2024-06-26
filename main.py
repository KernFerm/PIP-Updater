# MIT License
#
# Copyright (c) 2024
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pkg_resources
from subprocess import check_call, CalledProcessError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='update_packages.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def update_packages():
    packages = [dist.project_name for dist in pkg_resources.working_set]
    updated_packages = []

    for package in packages:
        try:
            result = check_call(f"pip install --upgrade {package}", shell=True)
            if result == 0:
                updated_packages.append(package)
                logging.info(f"Successfully updated {package}")
        except CalledProcessError as e:
            logging.error(f"Failed to update {package}: {e}")

    return updated_packages

def log_updates(run_number, updated_packages):
    logging.info(f"\nRun {run_number} completed. Updated packages:")
    if updated_packages:
        for package in updated_packages:
            logging.info(f" - {package}")
    else:
        logging.info("No packages were updated.")

# Run the updates twice
for run in range(1, 3):
    updated_packages = update_packages()
    log_updates(run, updated_packages)

# Print the log file content to the console
with open('update_packages.log', 'r') as log_file:
    print(log_file.read())
