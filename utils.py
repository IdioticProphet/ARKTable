import json, re
from constants import *
"""
Thanks to Akia Vongdara for providing me with the data that this file uses, the format he uses is core to my program
"""
def load_data(data_path: str) -> dict:
    """
    Loads JSON file
    """
    try:
        all_items = json.load(open(data_path))
    except FileNotFoundError:
         raise Exception("File not found")
    return all_items

def get_item_by_dlc(all_items, owned_dlc: list) -> list:
    """
    Find what resources you can craft based on what DLC's you own
    returns List of itemnames
    """
    item_list = []
    expansion_name = [item.name for item in DLC]
    expansion_parenthesis = [item.value for item in DLC]
    for expansion in owned_dlc:
        if expansion not in expansion_name+expansion_parenthesis:
            raise Exception("Used Invalid DLC")
        
    for item in all_items.keys():
        item_parenthesis = get_parenthesis_in_str(item)
        if item_parenthesis == []:
            item_parenthesis = [""]
        for item_dlc in item_parenthesis:
            """
            The phrase item_dlc is not at all faithful to the data, but it works like it needs to
            this is because the item will always be tagged with its DLC, theres just some additional tags
            """
            if item_dlc in expansion_parenthesis and item_dlc not in owned_dlc:
                continue
            elif "Resource" not in all_items[item]["types"] or all_items[item]["resources"] != []:
                item_list.append(item)
    return item_list
    
def get_all_resources(data_path: str) -> list:
    """
    Digs through data set to find all of the base resources, complex(consisting of other base items) or not
    ex: "Congealed Gas Ball (Aberration)": {"resources": [{"itemName": "Condensed Gas (Extinction)","amount": 1}]}
    ret: ["Condensed Gas (Extinction)"]
    """
    resource_list = []
    all_items = load_data(data_path=data_path)

    for item in all_items.keys():
        item_parenthesis = get_parenthesis_in_str(item)
        if item_parenthesis == []:
            item_parenthesis = [""]
            if "Resource" in all_items[item]["types"] or all_items[item]["resources"] == []:
                resource_list.append(item)
    return resource_list

def get_parenthesis_in_str(item: str) -> list:
    """
    Get all of the items within parenthesis
    ex: "I am a string (Strings!) (Are!) (Cool!)" -> ["(Strings!)", "(Are!)", "(Cool!)"]
    """
    parenthesis = re.findall(r"(\(.*?\))", item)
    return parenthesis
    
    
def get_parenthesis_in_data_set(data_path: str) -> list:
    """
    Gets all of the parenthesis that occur after item names in the dataset
    Originally called mode before I found that that EVERY egg had a parenthesis after it...
    ex keys: ["Ghillie Leggings (P+)", "Leather (Primitive Plus)"] -> ["(P+)", "(Primitive Plus)"]
    """
    mode_list = []
    all_items = load_data(data_path)
    for item in all_items.keys():
        found_modes = get_parenthesis_in_str(item)
        for mode in found_modes:
            if mode not in mode_list:
                mode_list.append(mode) 
    return mode_list

def get_all_types(data_path: str) -> list:
    types = []
    all_items = load_data(data_path)
    for item in all_items.keys():
        for t in all_items[item]["types"]:
            if t not in types: types.append(t)
    return types

def get_lightest_item(data_path):
    weight= 10
    all_items = load_data(data_path)
    for item in all_items.keys():
        if (w := all_items[item]["weight"]) < weight:
            if w != 0 and w!= .005: # .005 and 0 are just way too low lmao
                weight = w 
    return weight


        
    
