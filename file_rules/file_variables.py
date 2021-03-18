from business_rules.business_rules.variables import BaseVariables
from business_rules.business_rules.variables import *

class FileVariables(BaseVariables):

    def __init__(self, file_object):
        #input meta data
        self.meta_data = file_object['metaData']
        self.source_dir = file_object['sourceDir']
        self.file_name = file_object['fileName']

    @numeric_rule_variable(label='Recent Access')
    def recent_access(self):
        return self.meta_data.st_atime

    @numeric_rule_variable(label='Recent Modification')
    def recent_modification(self):
        return self.meta_data.st_mtime

    @string_rule_variable(label='File Name')
    def target_file_name(self):
        return self.file_name
