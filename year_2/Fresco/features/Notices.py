from .General_classes import *
from .functions import *
from .config import *
import subprocess

class Notice(Generic_class_info):
    pass
class Notice_Manager(Generic_manager):
    def get_notices(self,divisor:str)->list:
        notices_path=self.get_item_all()
        if not len(notices_path):
            return []
        notices=[]
        for i in notices_path:
            notices.append(Notice(i))
            notices[-1].get_infos(divisor)
        return notices
    def get_notices_filter(self,pattern:str,divisor:str)->list:
        notices=self.get_notices(divisor)
        notices_filtered=[]
        pattern=remove_marked_str(pattern)
        for i in notices:
            notice_type=remove_marked_str(i.get_attr("type")[0])
            if not match_item(notice_type.lower(),pattern):
                continue
            notices_filtered.append(i)
        return notices_filtered
