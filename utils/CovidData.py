import requests;


class CovidData:
    def __init__(self,os):
        self.os = os
        self.__nation = requests.get(os.environ.get("NATION")).json()
        self.__regions = self.__getRegionDict()

    def getRegionList(self):
        return list(self.__regions.keys())

    def getNationalStatus(self):
        return self.__nation

    def __getRegionDict(self):
        list = requests.get(self.os.environ.get("REGIONS")).json()
        return {obj["denominazione_regione"]: obj for obj in list}

    def getRegionStatus(self,region):
        if region not in self.getRegionList():
            return {"status": "not found"}
        else:
            return self.__regions[region]
