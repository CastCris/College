from .General_classes import *
from .functions import *
from .config import *
import subprocess

class Notice(Generic_class_info):
    pass
class Notice_Manager(Generic_manager):
    def get_notices(self)->list:
        notices_path=self.get_items_all()
        if not len(notices_path):
            return []
        notices=[]
        for i in notices_path:
            notices.append(Notice(i))
            notices[-1].get_infos()
        return notices
    def get_notices_filter(self,pattern)->list:
        notices=self.get_notices()
        notices_filtered=[]
        for i in notices:
            if not match_item(i.type,pattern):
                continue
            notices_filtered.append(i)
        return notices_filtered
