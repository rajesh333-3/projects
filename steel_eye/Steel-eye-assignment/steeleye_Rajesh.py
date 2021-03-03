# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 07:57:15 2021

@author: VenkataDurgaRajesh
"""
def zip_to_csv_parser(zip_link):
  try:
      data = requests.get(zip_link,stream=True).content
      with open("temp.zip","wb") as file:   
        file.write(data)
        file.close()
      zi = zipfile.ZipFile('temp.zip')
      zi.extractall()
      os.remove("temp.zip")#to free storage occupied
      logger.debug("successfully deleted zip after extraction")
      f_name=list(zi.NameToInfo.keys())[0]
      print("processing..."+f_name)
      logger.info("successfully extracted {}".format(f_name))
      file = open(f_name,encoding="utf-8")
      data = file.read()
      os.remove(f_name)#to free storage occupied
      print("Removed..."+f_name)
      logger.info("successfully deleted {}".format(f_name))
      soup = bsp(data,"xml")
      atrbt = soup.find_all("FinInstrmGnlAttrbts")
      issr = soup.find_all("Issr")
      lol=[["FinInstrmGnlAttrbts.Id","FinInstrmGnlAttrbts.FullNm","FinInstrmGnlAttrbts.ClssfctnTp","FinInstrmGnlAttrbts.CmmdtyDerivInd","FinInstrmGnlAttrbts.NtnlCcy","Issr"]]
      for i in range(len(atrbt)):
        temp_l=[]
        temp_l.append(atrbt[i].find("Id").text)
        temp_l.append(atrbt[i].find("FullNm").text)
        temp_l.append(atrbt[i].find("ClssfctnTp").text)
        temp_l.append(atrbt[i].find("CmmdtyDerivInd").text)
        temp_l.append(atrbt[i].find("NtnlCcy").text)
        temp_l.append(issr[i].text)
        lol.append(temp_l)
      df=pd.DataFrame(lol)
      df.to_csv(f_name[:-3]+"csv")
      print("Successfully saved {}csv shape={}".format(f_name[:-3],str(df.shape)))
      logger.info("Successfully saved {}csv shape={} ".format(f_name[:-3],str(df.shape)))
      return("{}csv".format(f_name[:-3]))
  except Exception as ex:
      logger.critical("Error on line "+str(sys.exc_info()[-1].tb_lineno)+" exception in method load models "+str(ex))
      raise Exception(str(ex))

def init_logger():
  import logging
  global logflag
  if __name__  not in logging.Logger.manager.loggerDict.keys():
    import logging
    logger = logging.getLogger(__name__)  
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('logfile.log')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logflag=1
    return(logger)
  else:
    logger = logging.getLogger(__name__)
    return(logger)

def aws_uploader(file_name):
  import boto3
  #please provide your Aws Access_id and Acess_key and Bucket_name
  s3 = boto3.resource('s3',aws_access_key_id='Access_id',aws_secret_access_key= 'Acess_key')
  s3.meta.client.upload_file(file_name, 'Bucket_name', file_name)
  logger.info("Successfully Uploaded {} to AWS S3 Bucket".format(file_name))
  print("Successfully Uploaded {} to AWS S3 Bucket".format(file_name))


if __name__ == '__main__':
  from bs4 import BeautifulSoup as bsp
  import requests
  import zipfile
  import os
  import sys
  import pandas as pd
  logger=init_logger()
  data = requests.get("https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100").text
  soup = bsp(data,"xml")
  url = soup.find_all("str",{"name":"download_link"})
  urls=[x.text for x in url][0] #to work on only the first link as given in assignment
  print(urls)
  logger.debug("successfully scraped zip urls")
  #for z_link in urls:
  file_name=zip_to_csv_parser(urls)
  aws_uploader(file_name)