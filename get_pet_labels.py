#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Akshata Sangam
# DATE CREATED: 06.11.2023                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
  
    pet_label_list = listdir(image_dir)
    for filename in range (0,len(pet_label_list),1):
        pet_label_list[filename] = pet_label_list[filename].lower() 
    pet_name_list = []
    for filename in pet_label_list:
        split = filename.split("_")
        #print(split)
        pet_name = " "
        for name in split:
            if name.isalpha():
                pet_name += name + " "
        print(pet_name)
        pet_name_list.append(pet_name.strip())
    
    results_dic = dict()
    filename_list = listdir(image_dir)
   
    number_in_dict = len(results_dic)
   
   
    for key in range(0, len(filename_list), 1):
        if filename_list[key] not in results_dic:
            label_list = []
            label_list.append(pet_name_list[key])
            results_dic[filename_list[key]] = label_list
        else:
            print("Warning: Key = ", filename_list[key], "already exists in results_dic with value = ", results_dic[filename_list[key]])
        
    for key in results_dic:
        print("Filename = ", key, "Pet Label = ", results_dic[key])
 
    return results_dic

