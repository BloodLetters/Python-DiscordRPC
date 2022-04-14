import json


def getClientId():
    file = open("Config.json")
    data = json.load(file)
    return data['Client_Id']


def getDetails():
    file = open("Config.json")
    data = json.load(file)
    return data['Details']


def getState():
    file = open("Config.json")
    data = json.load(file)
    return data['State']


def getlargeIcon():
    file = open("Config.json")
    data = json.load(file)
    return data['Large_Icon']


def getLargeText():
    file = open("Config.json")
    data = json.load(file)
    return data['Large_Text']


def getSmallIcon():
    file = open("Config.json")
    data = json.load(file)
    return data['Small_Icon']


def getSmallText():
    file = open("Config.json")
    data = json.load(file)
    return data['Small_Text']


def reloadTime():
    file = open("Config.json")
    data = json.load(file)
    return data['ReloadTime']


def getButton(Num, Link):
    if str(Num) == "1":
        if not Link:
            file = open("Config.json")
            data = json.load(file)
            return data['Button_1']
        if Link:
            file = open("Config.json")
            data = json.load(file)
            return data['Button_1_Url']
    elif str(Num) == "2":
        if not Link:
            file = open("Config.json")
            data = json.load(file)
            return data['Button_2']
        if Link:
            file = open("Config.json")
            data = json.load(file)
            return data['Button_2_Url']
    else:
        return False
