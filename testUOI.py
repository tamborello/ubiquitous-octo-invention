# test Ubiquitous Octo Invention

import json, requests, time

def test_ubiquitous_octo_invention (doc) :

    req = dict({"QueryDoc":doc, "N":10})


    localURL = "http://localhost:7071/api/UOI"

    containerURL = "http://localhost:8080/api/UOI"

    deployedURL = "https://uoi.azurewebsites.net/api/L?code="


    URL = deployedURL

    t0 = time.time()

    init_msg = f"Request,\n{req}\nposted to URL, {URL}."
    response = requests.post(URL, json.dumps(req))
    status = response.status_code
    result = response.text
    t1 = time.time()
    end_msg = f"Status: {status}\nResult: {result}\nExecution time: {t1 - t0} s."

    # return init_msg + " " + end_msg
    # I like it, but maybe later
    return result


# with open("UOITestResult.json", "w") as f:
#     f.write(result)