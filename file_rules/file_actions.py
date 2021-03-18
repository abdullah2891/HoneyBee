from business_rules.business_rules.actions import BaseActions, rule_action
from business_rules.business_rules.fields import FIELD_TEXT
from shutil import move
from os import remove

from shutil import move

class FileActions(BaseActions):

    def __init__(self, file_object):
        #input meta data
        self.meta_data = file_object['metaData']
        self.source_dir = file_object['sourceDir']
        self.file_name = file_object['fileName']

    @rule_action(params={"target_dir": FIELD_TEXT})
    def move_to_backup(self, target_dir):
        print("triggered", self.file_name)
        source_filedir = self.source_dir
        target_file_dir = target_dir + '/' + self.file_name

        move(source_filedir , target_file_dir)

    @rule_action(params={})
    def delete_dir(self):
        print("triggered delete", self.file_name)
        source_filedir = self.source_dir

        remove(source_filedir)
