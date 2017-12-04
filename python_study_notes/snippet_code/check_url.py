import http.client


##PythonVersion: python3.5
##Useage: check if the url is healthy

def checkweb(url):
    conn=http.client.HTTPSConnection(url)
    conn.request("GET","/")
    r1=conn.getresponse()
    #print(r1.status, r1.reason)
    if r1.status == 200:
        return 1
    else:
        return 0

if __name__=='__main__':
    assert checkweb("www.example.com")
