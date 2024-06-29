import pandas as pd
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


f=open("data/my_api_key.txt","r")

lines=f.readlines()
my_key=lines[0]
f.close()

base_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"

def find_lawd_cd(in_text):
    lawd_cd = pd.read_csv("data/법정동코드 전체자료.txt", sep='\t', encoding ='cp949') #'euc-kr', 'utf-8'
    lawd_cd.columns = ["code", "name", "check"]
    result = lawd_cd[(lawd_cd['name'].str.contains(in_text)) & (lawd_cd['check'] == "존재")].head(1).iloc[0,0].astype(str)[0:5]    
    return result


in_lawd = input("검색지역 입력 : ")
in_deal_ymd = input("계약월 입력(예: 201912) : ")

in_lawd_cd = find_lawd_cd(in_lawd)
in_lawd_cd

in_svckey = my_key
area_cd = "LAWD_CD=" + in_lawd_cd
deal_dt = "DEAL_YMD=" + in_deal_ymd
svc_key = "serviceKey=" + in_svckey

url = base_url + "?" + area_cd + "&" + deal_dt + "&" + svc_key
url


response = requests.get(url)
response


def find_xml_items(response):
    # print(response)
    root = ET.fromstring(response.content)
    # xml_content = ET.tostring(root, encoding="unicode")
    # print(xml_content)
    
    item_list = []
    for child in root.find('body').find('items'):
        elements = child.findall('*')
        data = {}
        for element in elements:
            tag = element.tag.strip()
            # print(tag)
            text = element.text.strip()
            # print(text)

            data[tag] = text
        item_list.append(data)  
    return item_list

items_list = find_xml_items(response)
result = pd.DataFrame(items_list)
name_info = in_lawd + "_" + in_deal_ymd
file_name = f"data/result_{name_info}.csv"
result.to_csv(file_name, index=False, encoding='utf-8')

