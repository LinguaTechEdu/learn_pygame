#!/usr/bin/env bash
# This script will require sudo privileges.
# If using for a workshop:
#   1. Pre install everything if possible. This is the best possible option.
#   2. If no pre-install, then at least pre-install virtualenv and pygame. Then you can allow this script to inherit site-packages which require no permissions.
#pip install virtualenv

virtualenv env -p python2.7 --system-site-packages
source ../env/bin/activate
pip install -U -I -r setup/requirements.txt
