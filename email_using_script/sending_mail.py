# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 07:48:21 2020

@author: VenkataDurgaRajesh
"""

# user need to enable less secure apps access on his gmail account from which he is sending the mail
import smtplib
import logging
import os
import datetime
from email.utils import make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
# from configuration import email
import sys
import json
import socket

with open(os.path.join("configuration.json"),"r") as f:
       configuration=json.load(f)
       
       
msg = MIMEMultipart('alternative') 
msg['From'] = configuration['email']
msg['cc'] = configuration['ccreceiver']
msg['To']=configuration['receiver']
msg['Subject'] = "Rajesh sent this mail from python script"
email_address=configuration['email']
password=configuration['password']
    
htmltext="""\
<html>
  <head></head>
  <body>
    <p>Dear Family Members,<br/><br/></p>
    <p>"Please check the below details of Rajesh: "<br/><br/>
    {Error_msg}
    </p>
    <table style=\"width:700px;table-layout:fixed\" border=1>
    <tr>
    <td style=\"width:200px\"><b>Full Name</b></td>
    <td bgcolor="{model_response_bgcolor}" style=\"width:300px\">{Model_Response}</p></td>
    </tr>
    <tr>
    
    <tr>
    <td style=\"width:200px\"><b>Age</b></td>
    <td bgcolor="{feedback_bgcolor}" style=\"word-wrap:break-word;\">{Feedback_Modified_Time}</td>
    </tr>
    <tr>
   <td style=\"width:200px\"><b>Gender</b></td>
    <td bgcolor="{pingservice_bgcolor}" style=\"width:300px\">{Ping_working}</p></td>
    </tr>
    <tr>
   <td style=\"width:200px\"><b>Marital Status</b></td>
    <td style=\"width:300px\">{Last_Ping}</p></td>
    </tr>
    <td style=\"width:200px\"><b>Employed</b></td>
    <td style=\"width:300px\">{Datamart_RowCount}</p></td>
    </tr><tr>
    <td style=\"width:200px\"><b>Company</b></td>
    <td style=\"width:300px\">{DB_RowCount}</p></td>
    </tr>
    <tr>
    <td style=\"width:200px\"><b>Address</b></td>
    <td bgcolor="{ticket_diff_bgcolor}" style=\"width:300px\">{Tickets_diff_msg}</p></td>
    </tr>
    <tr>
   <td style=\"width:200px\"><b>PINCODE</b></td>
    <td bgcolor="{groupuser_bgcolor}" style=\"width:300px\">{Status}</p></td>
    </tr>
    <tr>
   <td style=\"width:200px\"><b>Contact Number</b></td>
    <td style=\"width:300px\">{Records}</p></td>
    </tr>
   </table>
   <br/><br/>Thank you<br/>Rajesh Venkata    
  </body>
</html>
""".format(pingservice_bgcolor='cyan',groupuser_bgcolor='cyan',model_response_bgcolor='cyan',feedback_bgcolor='cyan',ticket_diff_bgcolor='cyan',Error_msg="PFB the Table",Ping_working="Male",Tickets_diff_msg="D.NO:1-285,Kanuru,Vijayawada",Model_Response="Thoomu Venkata Durga Rajesh",Datamart_RowCount="YES",DB_RowCount="TCS",Feedback_Modified_Time="22",Start_Time="start_time",End_Time="end_time",Status="520007",Records="9100262588",Last_Ping="NM",Second_Last_Ping="second_last_update")
msg.attach(MIMEText(htmltext, 'html'))
# Main Code
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_address,password)
    smtp.send_message(msg)
    smtp.close()
    print("Mail sent successfully....!")