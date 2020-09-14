import requests;


class CovidData:

    __instances = []

    def __new__(cls, *args, **kwargs):
        if len(CovidData.__instances) == 0:
            return super(CovidData,cls).__new__(cls)
        else:
            return CovidData.__instances[0]

    def __init__(self,os):
        self.os = os
        self.__nation = requests.get(os.environ.get("NATION")).json()
        self.__regions = self.__getRegionDict()
        CovidData.__instances.append(self);

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
