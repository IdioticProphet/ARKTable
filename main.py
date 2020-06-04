import utils, math, logging, os
from constants import *


class ItemTable:
    def __init__(self, file_path, owned_dlc):
        self.all_items = utils.load_data(file_path)
        self.owned_dlc = owned_dlc
        self.available_items = utils.get_item_by_dlc(self.all_items, owned_dlc)


class ARKTableEntry:
    def __init__(self, item_object):
        self.item_name = item_object["name"]
        self.item_experience = item_object["craftingXp"]
        if self.item_experience <= 0: 
            raise NoExperience
        self.item_components = self.get_components(item_object)
        self.effort_value = self.get_effort_value(item_object)
        
    def get_components(self, item_object) -> dict:
        components = {}
        for item in item_object["resources"]:
            components[item["itemName"]] = item["amount"]
        return components

    def get_effort_value(self, item_object):
        total_item_effort = 0
        logging.debug(item_object["name"])
        for entry in item_object["resources"]:
            itemName = entry["itemName"]
            amount = entry["amount"]
            
            if itemName in mats.keys():
                total_item_effort += (mats[itemName] * amount)
            else:
                raise BaseItemNotFound(f"Base Item Not found {itemName}")
        
        return self.item_experience/total_item_effort
            

class ARKTable(ItemTable):
    def __init__(self, file_path, owned_dlc=[""]):
        super().__init__(file_path, owned_dlc)
        self.table = self.make_table()

    def make_table(self):
        table = []
        for name, data in self.all_items.items():
            if name in self.available_items:
                try:
                    entry = ARKTableEntry(data)
                    if entry.effort_value > -1000:
                        table.append(entry)
                except BaseItemNotFound:
                    continue
                except NoExperience:
                    continue
        return table

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    data_dir = os.path.join(os.getcwd()+"/data/")
    main_table = ARKTable(file_path=os.path.join(data_dir+"craftable-items.json"), owned_dlc=[""])
    main_table.table.sort(key=lambda x: x.effort_value, reverse=True)
    logging.info(f"Your Best item is: {main_table.table[0].item_name}")
