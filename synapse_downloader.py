##
# @brief Script to download data from paper:
#   
#        Intrapapillary Capillary Loop Classification in Magnification Endoscopy: 
#        Open Dataset and Baseline Methodology by Garcia-Peraza Herrera et al. IJCARS 2020
#
# @author Luis Carlos Garcia Peraza Herrera (luiscarlos.gph@gmail.com).
# @date   February, 2020.

import argparse
import os
import synapseclient

def reminder():
    print("\nIf you use this dataset in your research, please cite:\n")
    print("@article{Garcia-Peraza-Herrera2020,\n" \
        + "    author = {Luis C. Garcia Peraza Herrera et al.},\n" \
        + "    title = {Intrapapillary Capillary Loop Classification in Magnification Endoscopy: " \
        + "Open Dataset and Baseline Methodology},\n" \
        + "    journal = {International Journal for Computer Assisted Radiology and Surgery},\n" \
        + "    year = {2020}\n}")

reminder()

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True, help='Your Synapse username.')
parser.add_argument('--password', required=True, help='Your Synapse password.')
parser.add_argument('--output-dir', required=True, help='Path to the output directory.')
args = parser.parse_args()

# Create output directory if it does not exist
if not os.path.isdir(args.output_dir):
    os.makedirs(args.output_dir)

# Connect to Synapse
syn = synapseclient.Synapse()
syn.login(args.username, args.password)

# Download training and validation dataset
syn.get("syn21637122", downloadLocation=args.output_dir) # train
syn.get("syn21636896", downloadLocation=args.output_dir) # val
print('The data has been successfully downloaded into ' + args.output_dir)

reminder()
