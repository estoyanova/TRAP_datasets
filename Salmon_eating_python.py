# Salmon_eating_python v0.1
# Running Salmon on Heintz FASTQ Files

import os
import subprocess
#import re

def SE_Salmon(TRAP_id, t_index):
    
    # Will run Salmon on single end data
    
    try:
        return(subprocess.call(['salmon', 'quant', '-i', t_index, '-l', 'A',
                        '-r', TRAP_id, '-o', 'transcripts_quant/' + TRAP_id[:10]]))
    except:
        return('There was an error with file ' + TRAP_id + '\nCheck that files are not corrupted')

def PE_Salmon(TRAP_ids, t_index):
    
    # Will run Salmon on paired end data
    
    try:
        First, Second = TRAP_ids
        
        return(subprocess.call(['salmon', 'quant', '-i', t_index, '-l', 'A',
                        '-1', First, '-2', Second, '-p', '32',
                        '-o', 'transcripts_quant/' + First[:10]]))
    except:
        return('There was an error with finding paired end files.\nCheck that both files are in database')
    
# read a list of id for salmon quantification

TRAP_id_list = ['666', '667', '668']

# loop and see if they are paired end or single end, e.g. R1 only or R1 & R2

fastq_path = "/Volumes/heintz-bambi1/FastQ/" # all fastq's are in here
file_list = os.listdir(fastq_path)

associated_files = []

for item in TRAP_id_list:
    
    files = [file_name for file_name in file_list if item in file_name]
    associated_files.append(files)

analysis_info = {TRAP_id_list[i]: associated_files[i] for i in range(len(TRAP_id_list))}


# run SE salmon code on R1

t_index = '/mnt/heintz-bambi3/WORK/eli/TRAP_datasets/mm10Trans_Exome_index/'

for key in analysis_info.keys():
    
    if len(analysis_info[key]) == 2:        
        output = PE_Salmon(analysis_info[key], t_index)
        if output == 0:
            print('Files for sample ' + analysis_info[key] + ' run successfully')
        else:
            print('There was an error running salmon on sample '+ key)
        
    else:
        output = SE_Salmon(analysis_info[key], t_index)
        if output == 0:
            print('Files for sample ' + analysis_info[key] + ' run successfully')
        else:
            print('There was an error running salmon on sample '+ key)