from business_rules.business_rules import run_all
from file_rules.file_actions import FileActions
from file_rules.file_variables import FileVariables
from config import configs

def target_files(path):
    import os, sys

    # Open a file
    dirs = os.listdir( path )

    # This would print all the files and directories
    files = []

    for file in dirs:
        files.append({
            "fileName": file,
            "metaData": os.stat(path + file),
            "sourceDir": path + file
        })


    return files


def run_organizer():
    print("Running File Organizer")
    for config in configs:
        file_objects = [files 
                for dir in config["start_dir"]
                for files in target_files(dir)
            ]

        for file_object in file_objects:
          run_all(rule_list=config['rules'],
                defined_variables=FileVariables(file_object),
                defined_actions=FileActions(file_object),
               )

if __name__ == '__main__':
    run_organizer()
    
