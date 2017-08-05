import webapp2
import jinja2
import cgi
import os
import jinja2
import smtplib
import json
import StringIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mailTemplate


import base64
# import leads_mail
# import data_warrior_confirmationMail
from google.appengine.api import mail

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class sendMail():
    
#     def sendLeadsDetails(self,to_id,name,mailid,phone,subject,content):
#         message = mail.EmailMessage(sender = "Homezpot Leads Management <team.homezpot@gmail.com>",
#                                         subject = "New Request: "+subject)
#         message.to = to_id
#         message.html = leads_mail.mail_content%(name,mailid,phone,subject,content)
#         message.send()

    def sendAdminAccountDetails(self, orderId,dateTime,pickUp,dropOff,startLatitude,startLongitude,endLatitude,endLongitude,vehicleType,finalDistance,finalFare,loadingTime,unLoadingTime,completeTime,waitingTime,email,contact,driverName,name, extra,baseFare,trafficSurcharge,waitCharge,tollTax,discount,payable,licenseNo):
        message = mail.EmailMessage(sender = "Moovo Team <tech.moovo@gmail.com>",
                                        subject = "Your Trip Invoice with Moovo")
        if not mail.is_email_valid(email):
            return "Wrong email! Check again!"

        message.to = email
        home = jinja_environment.get_template('moovoinvoice.html')
        message.html = home.render(orderId=orderId, dateTime=dateTime, pickUp=pickUp, dropOff=dropOff, startLatitude=startLatitude, startLongitude=startLongitude, endLatitude=endLatitude, endLongitude=endLongitude, vehicleType=vehicleType, finalDistance=finalDistance, finalFare=finalFare, loadingTime=loadingTime,unLoadingTime=unLoadingTime,completeTime=completeTime,waitingTime=waitingTime,email=email,contact=contact,driverName=driverName,name=name, extra=extra,baseFare=baseFare,trafficSurcharge=trafficSurcharge,waitCharge=waitCharge,tollTax=tollTax,discount=discount,payable=payable,licenseNo=licenseNo)
        message.send()
        return "Mail Send"

    def sendAdminBusinessAccountDetails(self, orderId,dateTime,pickUp,dropOff,startLatitude,startLongitude,endLatitude,endLongitude,vehicleType,finalDistance,finalFare,loadingTime,unLoadingTime,completeTime,waitingTime,email,contact,driverName,name, extra,baseFare,trafficSurcharge,waitCharge,tollTax,discount,payable,licenseNo,address,advance,pending):
        message = mail.EmailMessage(sender = "Moovo Team <tech.moovo@gmail.com>",
                                        subject = "Your Trip Invoice with Moovo")
        if not mail.is_email_valid(email):
            return "Wrong email! Check again!"

        message.to = email
        home = jinja_environment.get_template('moovoinvoiceV02.html')
        message.html = home.render(orderId=orderId, dateTime=dateTime, pickUp=pickUp, dropOff=dropOff, startLatitude=startLatitude, startLongitude=startLongitude, endLatitude=endLatitude, endLongitude=endLongitude, vehicleType=vehicleType, finalDistance=finalDistance, finalFare=finalFare, loadingTime=loadingTime,unLoadingTime=unLoadingTime,completeTime=completeTime,waitingTime=waitingTime,email=email,contact=contact,driverName=driverName,name=name, extra=extra,baseFare=baseFare,trafficSurcharge=trafficSurcharge,waitCharge=waitCharge,tollTax=tollTax,discount=discount,payable=payable,licenseNo=licenseNo,address=address,advance=advance,pending=pending)
        message.send()
        return "Mail Send"

#     def sendConfirmationMailDataWarriosHackathon(self, to_id):
#         message = mail.EmailMessage(sender = "Data Warriors <anshuman.mishra@innovaccer.com>",
#                                         subject = "InnovAccer-Data Warriors Confirmation")
#         if not mail.is_email_valid(to_id):
#             return "Wrong email! Check again!"
# 
#         message.to = to_id
#         message.html = data_warrior_confirmationMail.mail_content
#         message.send()
#         return "Mail Send"

#     def sendInviteRequestFollowup(self,to,clientName, reportingDate, reportingAddress, destination, driverRate, vehicleNo, vehicleDes, driverContact, driverName, companyRate, biltyNo, freightType, freightQuantity, freightWeight):
#         message = mail.EmailMessage(sender = "Team Moovo <tech.moovo@gmail.com>",
#                                         subject = "Your Trip Details With Moovo")
#         message.to = to
#         #message.html = email_html.html_body%( user, recruiter,test_id,to,test_id,encoded_to,test_id,encoded_to)
#         # print clientName, reportingDate, reportingAddress, destination, driverRate, vehicleNo, vehicleDes, driverContact, driverName, companyRate, biltyNo, freightType, freightWeight, Mango
#         message.html = invite_received_email.html_body%("There",clientName, reportingDate, reportingAddress, destination, driverRate, vehicleNo, vehicleDes, driverContact, driverName, companyRate, biltyNo, freightType, freightQuantity, freightWeight)
#         message.send()

    def sendClientTripDetails(self,to):
        message = mail.EmailMessage(sender = "Team Gtrans <tech.moovo@gmail.com>",
                                        subject = "Gtrans News Letter April Edition")
        message.to = to
        #message.html = email_html.html_body%( user, recruiter,test_id,to,test_id,encoded_to,test_id,encoded_to)
        # print clientName, reportingDate, reportingAddress, destination, driverRate, vehicleNo, vehicleDes, driverContact, driverName, companyRate, biltyNo, freightType, freightWeight, Mango
        message.html = mailTemplate.html_body%()
        message.send()

#     def sendInvite(self,to,uid,user):
#         message = mail.EmailMessage(sender = "Team Moovo <tech.moovo@gmail.com>",
#                                         subject = "Your Trip Details")
#         message.to = to
#         
#         #message.html = email_html.html_body%( user, recruiter,test_id,to,test_id,encoded_to,test_id,encoded_to)
#         message.html = validation_email.html_body%(user, uid)
#         message.send()