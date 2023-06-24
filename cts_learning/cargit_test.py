import json
import requests
class GetEntityid():
    '''
    This class is to get entity IP from entity name
    '''
    def get_entityid(self, aedatastore, hostname):

        '''
        This method will will write ip address as additional attribbute with ciname as input
        '''
        url= aedatastore['HC_URL']+'/api/v1/viewentities?where={"entityname":"'+hostname+ '"}'
        print(url)
        headers = {}
        data = []
        headers['Content-Type'] = 'application/json'
        token = aedatastore['UPDATE_TOKEN']
        headers['Authorization'] = 'Bearer '+token
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, headers=headers, verify=False)
        status = response.status_code
        if status == 200:
            queryresult = json.loads(response.text)
                   
        if (queryresult["_items"] != []):
            queryresult = queryresult["_items"][0]['entityid']
            return queryresult
        else:
            message = response.text
            raise Exception(message)