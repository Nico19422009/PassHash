#!/bin/bash
# filepath: passhash.sh

# PASSHASH ASCII Logo
echo "#############################################"
echo "#                                           #"
echo "#   ██████╗  █████╗ ███████╗███████╗██╗  ██╗ #"
echo "#   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║ #"
echo "#   ██████╔╝███████║███████╗███████╗███████║ #"
echo "#   ██╔═══╝ ██╔══██║╚════██║╚════██║██╔══██║ #"
echo "#   ██║     ██║  ██║███████║███████║██║  ██║ #"
echo "#   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ #"
echo "#                                           #"
echo "#############################################"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 to use PassHash."
    exit 1
fi

# Run the Python script
echo "Starting PassHash..."
python3 generator.py