import requests
import time

# API DOCUMENTATION: https://help.bitsighttech.com/hc/en-us/articles/360022913734-GET-Finding-Details
api_key = "USER_APIKEY"
# ASSETS AFFECTING THE RATING
url = "https://api.bitsighttech.com/ratings/v1/companies/XXXXXXX/findings?limit=1000000000&grade=WARN&grade=BAD&affects_rating=true"


# API CHECK
response = requests.get(url, auth=(api_key, ""))
print(response.status_code)
if response.status_code == 401 and str(response.json()["detail"]) == "Invalid token":
        print("Invalid Api key. Please Insert Valid Api key:\n\n\n")
        print(response.status_code)
        exit()
else:
        print("Api Key is Valid.\n")




def company1():
# ONLY FOR OBFUSCATED SUBSCRIPTION (xxx.xxx.11.111)
        xxx = "xxx.xxx."
        replace = ""
json = response.json()
#print(json)
#print(json['results'])
for result in json['results']:
    for r in result['assets']:
        company_assets = r['asset']         # .replace(xxx, replace)
        print(company_assets)
company1()
        
print("---FINISH---")
time.sleep(2)

def company2():

        for result in json['results']:
                try:
                        assetsPorts = result['evidence_key']    # ASSET NOT DISCOVERED
                        split_string = assetsPorts.split(":", 1)
                        assetsNOPorts = split_string[0]
                        print(assetsNOPorts)
                        #print(assetsPorts)
                except KeyError:
                        pass

company2()         
