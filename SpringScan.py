import argparse
import sys
import requests
import os
import urllib3
urllib3.disable_warnings()



payload =["/v2/api-docs","/swagger-ui.html","/swagger","/api-docs","/api.html","/swagger-ui","/swagger/codes","/api/index.html","/api/v2/api-docs","/v2/swagger.json","/swagger-ui/html","/distv2/index.html","/swagger/index.html","/sw/swagger-ui.html","/api/swagger-ui.html","/static/swagger.json","/user/swagger-ui.html","/swagger-ui/index.html","/swagger-dubbo/api-docs","/template/swagger-ui.html","/swagger/static/index.html","/dubbo-provider/distv2/index.html","/spring-security-rest/api/swagger-ui.html","/spring-security-oauth-resource/swagger-ui.html","/mappings","/metrics","/beans","/configprops","/actuator/metrics","/actuator/mappings","/actuator/beans","/actuator/configprops","/actuator","/auditevents","/autoconfig","/beans","/caches","/conditions","/configprops","/docs","/dump","/env","/jolokia/list","/flyway","/health","/heapdump","/httptrace","/info","/intergrationgraph","/jolokia","/logfile","/loggers","/liquibase","/metrics","/mappings","/prometheus","/refresh","/scheduledtasks","/sessions","/shutdown","/trace","/threaddump","/actuator/auditevents","/actuator/beans","/actuator/health","/actuator/conditions","/actuator/configprops","/actuator/env","/actuator/info","/actuator/loggers","/actuator/heapdump","/actuator/threaddump","/actuator/metrics","/actuator/scheduledtasks","/actuator/httptrace","/actuator/mappings","/actuator/jolokia","/actuator/hystrix.stream","/actuator/env","/refresh","/actuator/refresh","/restart","/actuator/restart","/jolokia","/actuator/jolokia","/trace","/actuator/httptrace","/article?id=${7*7}","/article?id=66","/h2-console"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
def titleInfo():
    print("""
 ____             _             ____                  
/ ___| _ __  _ __(_)_ __   __ _/ ___|  ___ __ _ _ __  
\___ \| '_ \| '__| | '_ \ / _` \___ \ / __/ _` | '_ \ 
 ___) | |_) | |  | | | | | (_| |___) | (_| (_| | | | |
|____/| .__/|_|  |_|_| |_|\__, |____/ \___\__,_|_| |_|
      |_|                 |___/                       

     	               Author:N1ce
                       Github:https://github.com/N1ce759 
                       
Useage: python3 Spring_Scan.pu -u htpp://example.com                            
        	""")


def getApi(url):
    url =url
    for i in range(90):
        api = payload[i]
        target = url + api
        try:
            res = requests.get(url=target,headers=headers,verify=False,timeout=1)
            status = res.status_code
            if status == 200 and len(res.text) > 0:
                print("\033[1;31;40m%s \t------------>200\033[0m" %target)
                f1.writelines(target + '\n')
            else:
                print("%s \t------------>%s" %(target,status))
        except Exception as e:
            print("%s \t------------>Error" %(target))


def main():
    parser = argparse.ArgumentParser(description='Tool Test')
    parser.add_argument('-u', '--url', type=str, help=' Target ')
    args = parser.parse_args()
    url = args.url
    if url != None:
        if url[-1] =="/":
            url = url[:-1]
        if testStatus(url):
            print("Start..." + '\n')
            getApi(url)
        else:
            print("\033[1;31;40m无法建立到[%s]的连接\033[0m" %url)
            sys.exit(0)
    else:
        sys.exit(0)

def resultInfo():
    print("-----------------------------------------------------------------")
    if os.path.getsize('result.txt'):
        print("检查完成,结果如下：")
        for i in open('result.txt', 'r'):
            print("\033[1;31;40m%s\033[0m" % (i.strip()))
    else:
        print("未获取到相关结果！")

def testStatus(url):
    try:
        status = requests.get(url=url,headers=headers,verify=False,timeout=2).status_code
        if status != None:
            return True
    except:
        return False

if __name__ == '__main__':
    titleInfo()
    f1 = open('result.txt','wt')
    main()
    f1.close()
    resultInfo()



