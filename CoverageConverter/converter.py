import json

class CoverageConverter:
    def __init__(self):
        pass

    def convert_deployment_json(self, deployment_json):
        with open(deployment_json) as f:
            data = json.load(f)

        pdv_coverage_json = data['result']['details']['runTestResult']['codeCoverage']
        coverage_list = []

        for i in pdv_coverage_json:
            coverage_dict = {}
            coverage_dict["id"] = i.get("id")
            coverage_dict["name"] = i.get("name")
            coverage_dict["totalLines"] = i.get("numLocations")

            if i.get("locationsNotCovered"):
                temp_list = {}
                for items in i.get("locationsNotCovered"):
                    temp_list[items.get("line")] = items.get("column")
                    coverage_dict["lines"] = temp_list

            coverage_dict["totalCovered"] = int(i.get("numLocations")) - int(i.get("numLocationsNotCovered"))
            coverage_dict["coveredPercent"] = round((float(i.get("numLocations")) - float(i.get("numLocationsNotCovered"))) / float(i.get("numLocations")) * 100.0)
            coverage_list.append(coverage_dict)

        with open('sonar_coverage.json', 'w') as outjson:
            json.dump(coverage_list, outjson, indent=2)
