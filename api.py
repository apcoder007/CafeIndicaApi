from flask import  Flask, request, jsonify,session, redirect, url_for,g,abort, Response
from functools import wraps
from collections import namedtuple
from google.appengine.api import urlfetch
import ast
from time import gmtime, strftime
import cloudDbHandler as dbhelper
import imageHandler as imagehandler
# import storage as storeimage
from sets import  Set
import time
import json
import math
import ast
import unicodedata
from datetime import datetime
import random
from math import radians, cos, sin, asin, sqrt
import re
import urllib
from random import randint
import mailhandler as mailHandler
import os
# from google.cloud import storage


API_KEY = ['NkHb13BxRBiZ0JSyxLbAU','Hx1XU63ZThyFGsqfLeGu7']



app = Flask(__name__)


# Configure this environment variable via app.yaml
# CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']



############################### google login credentials ###########################################

#client ID 218003132719-k3f3fl0kpsfcb313ejh654aj14hb9144.apps.googleusercontent.com
#client secret mBjhDUwTlx4EwK-85qtWC_08



############################## end google login credentials #####################################
############################Normal Function To calculate the Detaisl ###################################################

@app.after_request
def after_request(response):
	response.headers['Access-Control-Allow-Origin']='*'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Headers']='Origin, X-Requested-With, Content-Type, Accept, Authorization'
	response.headers['Access-Control-Allow-Methods']= 'GET, PUT, POST, DELETE'
	return response
#######################################Public Site Panel #####################

# Adding Cnote to Server

@app.route('/api/package', methods=['GET', 'POST'])
def getPackage_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		url = userdata['url']

		json_results1 = []
		result1=dbhelper.GetData().getPackage_Image_Tags(url['name'])
		for data in result1:
			db = {
					'file_name':data[0],
					'xcoord':str(data[1]),
					'ycoord':str(data[2]),
					'item_id':data[3],
					'item_name':data[4],
					'item_sp':data[5],
					'item_description':data[6]
					
				}
			json_results1.append(db)

		json_results2 = []
		result2=dbhelper.GetData().getPackage_Fixed(url['name'])
		for data in result2:
			db = {
					'fxd_name':data[0],
					'price':data[1],
					'fxd_id':data[2]
					
				}
			json_results2.append(db)

		json_results3 = []
		result3=dbhelper.GetData().getPackage_Civil(url['name'])
		for data in result3:
			db = {
					'civil_work_name':data[0],
					'civil_price':data[1],
					'civil_id':data[2]
					
				}
			json_results3.append(db)

		json_results4 = []
		result4=dbhelper.GetData().getPackage_Item(url['name'])
		for data in result4:
			db = {
					'pack_name':data[0],
					'item_name':data[1],
					'mrp':data[2],
					'file_name':data[3],
					'sp':data[4],
					'description':unicode(data[5], errors='ignore')
					
				}
			json_results4.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets1":json_results1, "datasets2":json_results2, "datasets3":json_results3, "datasets4":json_results4}))
		return after_request(resp)


@app.route('/api/postcomments/', methods=['GET', 'POST'])
def postComments_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id'],
		comment = userdata['comment'],
		comment_by = userdata['comment_by']
		
		result=dbhelper.GetData().postComments(id, comment, comment_by)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)


@app.route('/api/getmapdetails/', methods=['GET'])
def map_details_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getMapDetails()
		for data in result:
			db = {
					'id':data[0],
					'lat':data[1],
					'lng':data[2],
					'pro_id':data[3],
					'name':data[4],
					'society':data[5],
					'address':data[6],
					'mobile':data[7],
					'client':data[8],
					'status':data[9],
					'path':data[10],
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/projectpayments/<id>', methods=['GET'])
def project_payments_estimation(id):
	if request.method == 'GET':
		json_results = []
		json_results1 = []
		payments, project_cost=dbhelper.GetData().getProjectPayment(id)
		for data in payments:
			db = {
					'id':data[0],
					'project_id':data[1],
					'invoice_no':data[2],
					'amount':str(data[3]),
					'tax_amount':str(data[4]),
					'due_date':str(data[5]),
					'paid_on':str(data[6]),
					'status':data[7],
					'created_by':data[8],
					'created_at':str(data[9]),
					'mode_of_transaction':data[10]
				}
			json_results.append(db)

		for data in project_cost:
			db = {
					'id':data[0],
					'project_id':data[1],
					'amount':str(data[2]),
					'updated_by':str(data[3]),
					'created_by':str(data[4])
				}
			json_results1.append(db)
	
		resp = Response(json.dumps({"success":1, "payments":json_results, "project_cost": json_results1, "msg":"This is the payment details"}))
		return after_request(resp)

@app.route('/api/getprojectdisplaypic/<id>', methods=['GET'])
def project_display_pic_estimation(id):
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getProjectDisplayPic(id)
		for data in result:
			db = {
					'id':data[0],
					'timeline_attachment_id':data[1],
					'path':data[7],
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/project/payment/checkout', methods=['GET', 'POST'])
def projectpaymentData_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		address = userdata['address']
		city = userdata['city']
		email = userdata['email']
		mobile = userdata['mobile']
		name = userdata['name']
		pin = userdata['pin']
		state = userdata['state']
		amount = userdata['amount']['amount']

		json_results = []
		result=dbhelper.GetData().getPaymentData(address,city,email,mobile,name,pin,state,amount)
		# for data in result:
		# 	db = {
		# 			'id':data[0],
		# 			'timeline_attachment_id':data[1],
		# 			'path':data[7],
		# 		}
		# 	json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getsupersections/', methods=['GET'])
def getSuperSections_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getSuperSections()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1].decode('utf-8'),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getallsections/', methods=['GET'])
def getAllSections_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getSections()
		for data in result:
			db = {
					'id':data[0],
					'name':unicode(data[1], errors='ignore'),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getalltestsections/', methods=['GET'])
def getAllTestSections_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getTestSections()
		print 'result = ',result
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)


@app.route('/api/getallsubsections/', methods=['GET'])
def getAllSubsections_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getSubsections()
		for data in result:
			db = {
					'id':data[0],
					'name':unicode(data[1], errors='ignore'),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getall/sections/categories/', methods=['GET'])
def getAllSectionsCategory_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllSectionCategories()

		sub_setionidList=[]

		#####
		super_section_idlist =[]
		section_idlist =[]
		sub_section_idlist =[]
		####

		super_section_list = []

		for data in result:

			super_section_id = data[0]
			section_id = data[2]
			sub_section_id =data[4]

			if super_section_id not in super_section_idlist and section_id not in section_idlist and sub_section_id not in sub_section_idlist:

				super_section_idlist.append(super_section_id)
				section_idlist.append(section_id)
				sub_section_idlist.append(sub_section_id)
		
			
				###############################
				category_list=[]

				category_id = data[6]
				category_name =data[7]

				pivot={
					'category_id':data[6],
					'subsection_id': data[4]

				}

				category_object={

					'id': category_id,
					'name':category_name.decode('ascii'),
					'pivot':pivot
				}

				category_list.append(category_object)
				##############################

				########Sub Section
				sub_section_object_list=[]
				sub_section_object={} 
				sub_section_object['id']=data[4]
				sub_section_object['name']=data[5].decode('ascii')
				sub_section_object['section_id']=data[2]
				sub_section_object['categories']=category_list

				sub_section_object_list.append(sub_section_object)


				#################################Sections Object ####
				sections_list =[]
				sections_object = {}
				sections_object['id'] = data[2]
				sections_object['name']=data[3]
				sections_object['subsections']= sub_section_object_list
				sections_list.append(sections_object)

				###############SuperSection
				super_section_object={}
				super_section_object['id']= data[0]
				super_section_object['name']=data[1]
				super_section_object['sections']=sections_list


				super_section_list.append(super_section_object)

			elif super_section_id in super_section_idlist and section_id not in section_idlist and sub_section_id not in sub_section_idlist:
				section_idlist.append(section_id)
				sub_section_idlist.append(sub_section_id)
		
			
				###############################
				category_list=[]

				category_id = data[6]
				category_name =data[7]

				pivot={
					'category_id':data[6],
					'subsection_id': data[4]

				}

				category_object={

					'id': category_id,
					'name':category_name.decode('ascii'),
					'pivot':pivot
				}

				category_list.append(category_object)
				##############################

				########Sub Section
				sub_section_object_list=[]
				sub_section_object={} 
				sub_section_object['id']=data[4]
				sub_section_object['name']=data[5].decode('ascii')
				sub_section_object['section_id']=data[2]
				sub_section_object['categories']=category_list

				sub_section_object_list.append(sub_section_object)

				#######################
				#################################Sections Object ####

				sections_object = {}
				sections_object['id'] = data[2]
				sections_object['name']=data[3]
				sections_object['subsections']= sub_section_object_list

				for result_object in super_section_list:
					if result_object['id']==data[0]:
						existing_section_list = result_object['sections']
						existing_section_list.append(sections_object)

			elif super_section_id in super_section_idlist and section_id in section_idlist and sub_section_id not in sub_section_idlist:
				sub_section_idlist.append(sub_section_id)
		
			
				###############################
				category_list=[]

				category_id = data[6]
				category_name =data[7]

				pivot={
					'category_id':data[6],
					'subsection_id': data[4]

				}

				category_object={

					'id': category_id,
					'name':category_name.decode('ascii'),
					'pivot':pivot
				}

				category_list.append(category_object)
				##############################

				########Sub Section
				sub_section_object={} 
				sub_section_object['id']=data[4]
				sub_section_object['name']=data[5].decode('ascii')
				sub_section_object['section_id']=data[2]
				sub_section_object['categories']=category_list

				for result_object in super_section_list:
					if result_object['id']==data[0]:

						existing_section_list = result_object['sections']
						if len(existing_section_list) >0:
							for _sub_section in existing_section_list:
								if _sub_section['id'] == data[2]:
									_sub_section['subsections'].append(sub_section_object)
						else:
							sections_object = {}
							sections_object['id'] = data[2]
							sections_object['name']=data[3]
							sections_object['subsections']= sub_section_object_list
							existing_section_list.append(sections_object)



			else:
				###############################
				category_list=[]

				category_id = data[6]
				category_name =data[7]

				pivot={
					'category_id':data[6],
					'subsection_id': data[4]

				}

				category_object={

					'id': category_id,
					'name':category_name.decode('ascii'),
					'pivot':pivot
				}


				for items in super_section_list:
					if items['id'] == data[0]:
						sections_existing_list = items['sections']
						for sub_sec in sections_existing_list:
							if sub_sec['id']== data[2]:
								_category_section = sub_sec['subsections']
								if len(_category_section)>0:
									for cateog in _category_section:
										if cateog['id'] ==data[4]:
										
											cateog['categories'].append(category_object)
								else:
									category_list.append(category_object)
									sub_section_object={} 
									sub_section_object['id']=data[4]
									sub_section_object['name']=data[5].decode('ascii')
									sub_section_object['section_id']=data[2]
									sub_section_object['categories']=category_list
									_category_section.append(sub_section_object)

	
		resp = Response(json.dumps({"success":1, "datasets":super_section_list}))
		return after_request(resp)



@app.route('/api/getcategoryItem/', methods=['GET', 'POST'])
def getCategoryItem_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		params = userdata['params']
		
		result=dbhelper.GetData().getCategoryItems(params)
		json_results = []
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'brand':data[2],
					'url':data[3],
					'mrp':data[4],
					'sp':data[5],
					'images':data[6]
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



@app.route('/api/getproduct/<url>', methods=['GET'])
def getProduct_estimation(url):
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getProduct(url)
		for data in result:
			db = {
					'id':data[0],
					'type':data[1],
					'name':data[2],
					'style':data[3],
					'section':data[4],
					'code':data[5],
					'price':data[6],
					'availability':data[7],
					'length':data[8],
					'width':data[9],
					'description':unicode(data[10], errors='ignore'),
					'added_by':data[11],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getproductbysection/<type>', methods=['GET'])
def getProductbySection_estimation(type):
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getProductbySection(type)
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'url':data[2],
					'style':data[3],
					'price':data[4],
					'description':unicode(data[5], errors='ignore'),
					'images':data[6],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getproductbytype/<type>', methods=['GET'])
def getProductbyType_estimation(type):
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getProductbyType(type)
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'url':data[2],
					'style':data[3],
					'price':data[4],
					'description':unicode(data[5], errors='ignore'),
					'images':data[6],
					'category':data[7],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getproductbystyle/<style>', methods=['GET'])
def getProductbyStyle_estimation(style):
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getProductbyStyle(style)
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'url':data[2],
					'style':data[3],
					'price':data[4],
					'description':unicode(data[5], errors='ignore'),
					'images':data[6],
					'category':data[7]
					
				}
			json_results.append(db)

		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getpackageurl/', methods=['GET'])
def getUrlview_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getPackageUrl()
		for data in result:
			db = {
					'urlname':data[0],
					'urlview':data[1],
					'type':data[2],
					'keywords':data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/store/ledgers', methods=['GET', 'POST'])
def getUpdateledger_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		userid = str(userdata['userid'])
		proid = str(userdata['proid'])
		payee_name = str(userdata['payee_name'])
		particulars = str(userdata['particulars'])
		amount = float(userdata['amount'])
		tax_amount = float(userdata['tax_amount'])
		bank = str(userdata['bank'])
		check_no = str(userdata['check_no'])
		concern_person = str(userdata['concern_person'])
		date = userdata['date']
		bill_no = str(userdata['bill_no'])
		type_of_transaction = str(userdata['type_of_transaction'])
		mode_of_transaction = str(userdata['mode_of_transaction'])
		remarks = str(userdata['remarks'])
		file_type = userdata['type']
		path = userdata['path']
		file = userdata['file']

		result=dbhelper.GetData().postStoreLedger(userid, proid, payee_name, particulars, amount, tax_amount, bank, check_no, concern_person, bill_no, type_of_transaction, mode_of_transaction, remarks, date, file_type, path)
		storeimage.upload_file(file, path, file_type)
		
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

@app.route('/api/store/installements', methods=['GET', 'POST'])
def getUpdateinstallements_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		userid = userdata['userid']
		proid = userdata['proid']
		amount = userdata['amount']
		due = userdata['due']
		due_date = userdata['due_date']
		paid_date = userdata['paid_date']
		mot = userdata['mot']
		tax = userdata['tax']

		result=dbhelper.GetData().postStoreInstallements(userid, proid, amount, due, due_date, paid_date, mot, tax)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

@app.route('/api/public/register/', methods=['GET', 'POST'])
def getpublicregister_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		name = userdata['name']
		email = userdata['email']
		password = userdata['pass']

		result, success = dbhelper.GetData().PostPublicRegister(name, email, password)

		resp = Response(json.dumps({"success":success, "datasets":result}))
		return after_request(resp)

@app.route('/api/public/google/register/', methods=['GET', 'POST'])
def getpublicgoogleregister_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		name = userdata['name']
		email = userdata['email']
		password = userdata['pass']

		result, success = dbhelper.GetData().PostPublicgoogleRegister(name, email, password)

		resp = Response(json.dumps({"success":success, "datasets":result}))
		return after_request(resp)


@app.route('/api/getpublic/login/', methods=['GET', 'POST'])
def getpubliclogin_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		username = userdata['user']
		password = userdata['pass']

		json_results = []
		json_results1 = []
		project = False

		result=dbhelper.GetData().getPublicLogin(username, password)
		permissionresult = dbhelper.GetData().getLoginCod(result[0][0])
		proresult1 = dbhelper.GetData().getLoginPro_One(result[0][0])
		proresult2 = dbhelper.GetData().getLoginPro_Two(result[0][0])

		if set(proresult1) | set(proresult2):
			project = True
		
		for data1 in permissionresult:
			db1 = data1[0]
			json_results1.append(db1)

		if 'cash_on_delivery' in json_results1:
			for data in result:
				if data[2] != '':
					db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					'name':data[3],
					'verified':data[4],
					'cod':True,
					'state':True
					}
					json_results.append(db)

				else:
					db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					'name':data[3],
					'verified':data[4],
					'cod':True,
					'state':False
					}
					json_results.append(db)


		elif 'cash_on_delivery' not in json_results1:
			for data in result:
				if data[2] != '':
					db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					'name':data[3],
					'verified':data[4],
					'cod':False,
					'state':True
					}
					json_results.append(db)

				elif data[2] == '':
					db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					'name':data[3],
					'verified':data[4],
					'cod':False,
					'state':False
					}
					json_results.append(db)

		
	
		resp = Response(json.dumps({"success":1, "user":json_results, "project":project, "state":json_results}))
		return after_request(resp)




@app.route('/api/getpublic/cart/', methods=['GET', 'POST'])
def postPublicUserCart_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id']
		
		cart_result=dbhelper.GetData().getCart(id)
		package_result=dbhelper.GetData().getpublicPackages(id)
		items_price =0
		count_sum =0

		packages_price =0
		for data in cart_result:
			items_price = items_price +float(data[6]) * int(data[3])
			count_sum += int(data[3])
			packages_price += float(mrp)

		package_countsum =0
		pckage_pricesum =0
		for elem in package_result:
			package_countsum += elem[3]
			pckage_pricesum+= elem[4]



		total_price = items_price + pckage_pricesum
		total_itemno = count_sum + package_countsum
		db = {
				'items':cart_result,
				'packages':package_result,
				'items_price':items_price,
				'noitem':count_sum,
				'packages_price': pckage_pricesum,
				'nopack': package_countsum,
				'total_price': total_price,
				'total_itemo':total_itemno
				
				
			}
		json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/project/userdata', methods=['GET', 'POST'])
def getProjectUserData_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		pro_id = userdata['id']

		json_results = []
		new_timelineList,timeline_comment=dbhelper.GetData().getUserProject(pro_id)



		protimecomment = {}
		commenet_timeline =[]
		for data in timeline_comment:
			db = {
						'timelineid':data[0],
						'comment':data[1],
						'comment_id':data[2],
						'time':str(data[3]),
						'name':data[4]
				}
			if str(data[0]) not in commenet_timeline:
				commenet_timeline.append(str(data[0]))

				
				blnkLst=[]
				blnkLst.append(db)
				protimecomment[str(data[0])] = blnkLst

			else:
				protimecomment[str(data[0])].append(db)


################################### group by time in object form ##################################### 
		final_output={}
		timeLineDate_List= []
		final_new_timeline ={}

		for data in new_timelineList:
			db = {
						'projectid':data[0],
						'message':unicode(data[1], errors='ignore'),
						'timeline_id':data[2],
						'attach_id':data[3],
						'path':data[4],
						'type':data[5],
						'time':str(data[6]),
						'day':data[7],
						'dayofmonth':data[8],
						'month':data[9]
						
					}

			if str(data[6]) not in timeLineDate_List:
				timeLineDate_List.append(str(data[6]))

				
				blnkLst =[]
				blnkLst.append(db)

				final_new_timeline[str(data[6])] = {}
				final_new_timeline[str(data[6])][str(data[2])] = blnkLst
			else:
				if str(data[2]) in final_new_timeline[str(data[6])]:
					final_new_timeline[str(data[6])][str(data[2])].append(db)
				else:
					blnkLst =[]
					blnkLst.append(db)
					final_new_timeline[str(data[6])][str(data[2])] = blnkLst

		final_output['new_timeline'] = final_new_timeline

################################## group by timeline_id ##############################
		
		timeline_id_List = []
		timeline_time_List = []
		final_new_timeline_id = {}
		final_new_timeline_time = {}

		for data in new_timelineList:
			db = {
						'projectid':data[0],
						'message':unicode(data[1], errors='ignore'),
						'timeline_id':data[2],
						'attach_id':data[3],
						'path':data[4],
						'type':data[5],
						'time':str(data[6]),
						'day':data[7],
						'dayofmonth':data[8],
						'month':data[9]
			}

			blnklst = []
			blnklst.append(db)

			if data[2] not in timeline_id_List:
				timeline_id_List.append(data[2])

				final_new_timeline_id[data[2]] = blnklst

			else:
				final_new_timeline_id[data[2]].append(db)


			if str(data[6]) not in timeline_time_List:
				timeline_time_List.append(str(data[6]))

				final_new_timeline_time[str(data[6])] = blnklst
			else:
				final_new_timeline_time[str(data[6])].append(db)

			
	
		resp = Response(json.dumps({"success":1, "timeline_time":final_new_timeline_time, "new_timeline":final_output, "protimecomment":protimecomment, 'timeline_id': final_new_timeline_id}))
		return after_request(resp)


@app.route('/api/getpublic/projects/', methods=['GET', 'POST'])
def postPublicUserProjects_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		user_id = userdata['id']
		
		project_timeline,project_user,pro_timeline,proticomment, project_status =dbhelper.GetData().getpublicProjectData(user_id)
		
		pro_comment_obj_final= {}
		pro_comment_list = []
		pro_timeline_id =[]
		for data in proticomment:
			
			if str(data[0]) not in pro_timeline_id:
				timeLineComment = []
				pro_timeline_id.append(str(data[0]))
				dataObj = {

					'timelineid':data[0],
					'comment':data[1],
					'commented_id':data[2],
					'time':str(data[3]),
					'name':data[4]

				}
				timeLineComment.append(dataObj)

				pro_comment_obj_final[str(data[0])] = timeLineComment
			else:
				dataObj = {

					'timelineid':data[0],
					'comment':data[1],
					'commented_id':data[2],
					'time':str(data[3]),
					'name':data[4]

				}

				print "inside"

				dataLst = pro_comment_obj_final[str(data[0])]
				dataLst.append(dataObj)
				print dataLst

				pro_comment_obj_final[str(data[0])] = dataLst


		
		
		date_timeline_list = []
		timeline_dict = {}

		newTimeline_dict={}

		for data in pro_timeline:
			if str(data[6]) not in date_timeline_list:
				json_dataList=[]
				date_timeline_list.append(str(data[6]))
				db = {
						'projectid':data[0],
						'message':unicode(data[1], errors='ignore'),
						'timeline_id':data[2],
						'attach_id':data[3],
						'path':data[4],
						'type':data[5],
						'time':str(data[6]),
						'day':data[7],
						'dayofmonth':data[8],
						'month':data[9]
					}
				json_dataList.append(db)



				timeline_dict[str(data[6])] = json_dataList
				blList=[]
				blList.append(db)
				newTimeline_dict[str(data[6])]={}
				newTimeline_dict[str(data[6])][str(data[2])]= blList 

			else:
				db = {
						'projectid':data[0],
						'message':unicode(data[1], errors='ignore'),
						'timeline_id':data[2],
						'attach_id':data[3],
						'path':data[4],
						'type':data[5],
						'time':str(data[6]),
						'day':data[7],
						'dayofmonth':data[8],
						'month':data[9]
					}
				if str(data[6]) in timeline_dict:
					timeline_dict[str(data[6])].append(db)


				if str(data[6]) in newTimeline_dict:
					blankList=[]
					blankList.append(db)
					newTimeline_dict[str(data[6])][str(data[2])]= blankList 


		user_projects = []
		for data in project_user:
			db = {
					'code':data[0],
					'name':data[1],
					'id':data[2],
					
				}
			user_projects.append(db)

		pro_status = []
		
		pro_status_dict = {}
		project_codeStatusList =[]
		final_pro_json= {}



		for data in project_status:
			pro_status_small_list=[]
			if data[2] not in project_codeStatusList:
				project_codeStatusList.append(data[2])
				db = {
					'project_id':data[0],
					'status':data[1],
					'code':data[2]
				}
				pro_status_small_list.append(db)

				final_pro_json[str(data[2])] = pro_status_small_list
			elif data[2] in final_pro_json:
				db = {
					'project_id':data[0],
					'status':data[1],
					'code':data[2]
				}

				final_pro_json[data[2]].append(db)
	

		json_results1=[]
		listresult1 = []
		result1 = []
		timelinedist1 = {}

		project_codeList=[]
		project_date=[]

		final_result ={}


		for data in project_timeline:
			if data[1] not in project_codeList:
				project_codeList.append(data[1])
				final_result[str(data[1])] = {
					str(data[7]):{
						str(data[3]):[{
							'projectid':data[0],
							'code':data[1],
							'message':unicode(data[2], errors='ignore'),
							'timeline_id':data[3],
							'attach_id':data[4],
							'path':data[5],
							'type':data[6],
							'time':str(data[7]),
							'day':data[8]

						}]
					}
				}
			else:
				if str(data[7]) in final_result[str(data[1])]:
					dbData= {
							'projectid':data[0],
							'code':data[1],
							'message':unicode(data[2], errors='ignore'),
							'timeline_id':data[3],
							'attach_id':data[4],
							'path':data[5],
							'type':data[6],
							'time':str(data[7]),
							'day':data[8]

						}
					if str(data[3]) in final_result[str(data[1])][str(data[7])]:

						final_result[str(data[1])][str(data[7])][str(data[3])].append(dbData)

					else:
						blankLst= []
						blankLst.append(dbData)
						final_result[str(data[1])][str(data[7])][str(data[3])] = blankLst
				else:

					dbDict = {
						str(data[3]):[{
							'projectid':data[0],
							'code':data[1],
							'message':unicode(data[2], errors='ignore'),
							'timeline_id':data[3],
							'attach_id':data[4],
							'path':data[5],
							'type':data[6],
							'time':str(data[7]),
							'day':data[8]

						}]
					}

					final_result[str(data[1])][str(data[7])] = dbDict			


	
		resp = Response(json.dumps({"success":1, "timeline":final_result, "msg":'Timeline list', "project_user": user_projects, "project_status":final_pro_json, "project_timeline_time":timeline_dict, "new_timeline":newTimeline_dict, "protimecomment":pro_comment_obj_final}))
		return after_request(resp)


#################################### Android public projects #########################################

# @app.route('/api/android/getproductbystyle', methods=['GET', 'POST'])
# def getProductbyStyle_estimation():
# 	if request.method == 'POST':
# 		userdata = js
# 		json_results = []
# 		result=dbhelper.GetData().getProductbyStyle(style)
# 		for data in result:
# 			db = {
# 					'id':data[0],
# 					'name':data[1],
# 					'url':data[2],
# 					'style':data[3],
# 					'price':data[4],
# 					'description':unicode(data[5], errors='ignore'),
# 					'images':data[6],
# 					'category':data[7]
					
# 				}
# 			json_results.append(db)

# 		resp = Response(json.dumps({"success":1, "datasets":json_results}))
# 		return after_request(resp)

@app.route('/api/android/getdesign', methods=['GET', 'POST'])
def getandroidProductbyStyle_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		style = userdata['style']
		section = userdata['section']

		json_results = []
		result=dbhelper.GetData().getAndroidProductbyStyle(style, section)
		for data in result:
			db = {
					'id':data[0],
					'name':str(data[1]),
					'url':data[2],
					'style':data[3],
					'price':data[4],
					'description':unicode(data[5], errors='ignore'),
					'images':data[6],
					'category':data[7]
					
				}
			json_results.append(db)

		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/android/getstylelist', methods=['GET'])
def getandroidstylelist_estimation():

	result=dbhelper.GetData().getAndroidStylelist()
	json_results = []
	for data in result:
		db = {
			'style':data[0]
		}
		json_results.append(db)

	resp = Response(json.dumps({"success":1, "list":json_results}))
	return after_request(resp)

@app.route('/api/android/getsectionlist', methods=['GET'])
def getandroidsectionlist_estimation():

	result=dbhelper.GetData().getAndroidSectionlist()
	json_results = []
	for data in result:
		db = {
			'style':data[0]
		}
		json_results.append(db)

	resp = Response(json.dumps({"success":1, "list":json_results}))
	return after_request(resp)



@app.route('/api/android/store/bookservices', methods=['GET', 'POST'])
def postandroidbookservices_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		servicename = str(userdata['servicename'])
		name = str(userdata['name'])
		contactnumber = str(userdata['contactnumber'])
		address = str(userdata['address'])
		city = str(userdata['city'])
		state = str(userdata['state'])

		result=dbhelper.GetData().postAndroidbookServices(servicename,name,contactnumber,address,city,state)
	
		resp = Response(json.dumps({"success":result}))
		return after_request(resp)



@app.route('/api/android/public/projects/timeline', methods=['GET', 'POST'])
def postAndroidPublicUserProjectsTimeline_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		user_id = userdata['user_id']
		
		project_timeline,project_user,pro_timeline,proticomment, project_status =dbhelper.GetData().getpublicProjectData(user_id)
		
		json_results = []
		for data in project_timeline:
			db = {
					'project_id':data[0],
					'project_code':data[1],
					'message':unicode(data[2], errors='ignore'),
					'timeline_id':data[3],
					'attach_id':data[4],
					'path':data[5],
					'type':data[6],
					'time':str(data[7]),
					'dayname':data[8]
			}
			json_results.append(db)
		resp = Response(json.dumps({"project_timeline":json_results}))
		return after_request(resp)

@app.route('/api/android/public/projects/gettimeline/byprojectcode', methods=['GET', 'POST'])
def postAndroidPublicUserProjectsTimelineByprojectcode_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		project_code = userdata['project_code']
		
		project_timeline = dbhelper.GetData().getpublicProjectDataByprojectCode(project_code)
		
		json_results = []
		for data in project_timeline:
			db = {
					'project_id':data[0],
					'project_code':data[1],
					'message':unicode(data[2], errors='ignore'),
					'timeline_id':data[3],
					'attach_id':data[4],
					'path':data[5],
					'type':data[6],
					'time':str(data[7]),
					'dayname':data[8]
			}
			json_results.append(db)
		resp = Response(json.dumps({"project_timeline":json_results}))
		return after_request(resp)


@app.route('/api/android/public/projects/comments', methods=['GET', 'POST'])
def postAndroidPublicUserProjectsComments_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		user_id = userdata['timeline_id']
		
		android_comments =dbhelper.GetData().getPublicUserComments(user_id)
		
		json_results = []
		for data in android_comments:
			db = {
					'timeline_id':data[0],
					'comments':data[1],
					'commented_by':data[2],
					'created_at':str(data[3]),
					'username':data[4],
			}
			json_results.append(db)
		resp = Response(json.dumps({"comments":json_results}))
		return after_request(resp)


@app.route('/api/android/public/projects/status', methods=['GET', 'POST'])
def postAndroidPublicUserProjectsStatus_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		pro_code = userdata['pro_code']
		
		android_comments =dbhelper.GetData().getPublicUserProjectStatus(pro_code)
		
		json_results = []
		for data in android_comments:
			db = {
					'project_id':data[0],
					'status':data[1],
					'code':data[2]
			}
			json_results.append(db)
		resp = Response(json.dumps({"status":json_results}))
		return after_request(resp)


@app.route('/api/android/getprojectlist/<id>', methods=['GET'])
def getprojectlists(id):
	if request.method == 'GET':
		json_results = []
		result = dbhelper.GetData().getProjectLists(id)
		for data in result:
			db = {
					'id':data[0],
					'code':data[1],
					'name':data[2],
					'client_user_id':data[3],
					'society':data[4],
					'contact_person':data[5],
					'mobile':data[6],
					'address':data[7],
					'pin':data[8],
					'created_by':data[9],
					'created_at':str(data[10]),
					'city':data[11],
					'state':data[12]
			}
			json_results.append(db)
		resp = Response(json.dumps({"success":1, "projectlist":json_results}))
		return after_request(resp)



########################### Admin Site Panel########################################################
#Admin Site url

@app.route('/api/getusers/', methods=['GET'])
def getAdminUser_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAdminUser()
		for data in result:
			db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getlogin/', methods=['GET', 'POST'])
def postAdminUser_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		username = userdata['username']
		password = userdata['password']
		
		result=dbhelper.GetData().getLoginData(username, password)
		json_results = []
		for data in result:
			db = {
					'id':data[0],
					'email':data[1],
					'password':data[2],
					'name':data[3]
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getusersdetails/', methods=['GET', 'POST'])
def getAdminUserDetails_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id']

		json_results = []
		result=dbhelper.GetData().getAdminUserDetails(id)
		for data in result:
			db = {
					'name':data[0],
					'role':data[1],
					'permissions':data[2],
					'id': data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

##########################################Bulk Orders######################################
@app.route('/api/getbulkorderdetails', methods=['GET'])
def getBulkOrder_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getBulkOrderDetails()
		for data in result:
			db = {
					'name':data[0],
					'email':data[1],
					'mobile':data[2],
					'company': data[3],
					'description': data[4],
					'file': data[5],
					'created_at': str(data[6]),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

############################################Callback Request#################################

@app.route('/api/getcallbackrequestdetails', methods=['GET'])
def getCalbackRequest_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getCallbackRequest()
		for data in result:
			db = {
					'name':data[0],
					'mobile':data[1],
					'created_at':str(data[2]),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

##########################################Designer Request####################################


@app.route('/api/getdesignerrequestdetails', methods=['GET'])
def getDesignerRequest_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getDesignerRequest()
		for data in result:
			db = {
					'name':data[0],
					'email':data[1],
					'mobile':data[2],
					'created_at':str(data[3]),
					'description':data[4],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



##########################################Item Request############################################

@app.route('/api/getitemrequestdetails', methods=['GET'])
def getItemRequest_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getItemRequest()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'mobile':data[2],
					'email':data[3],
					'created_at':str(data[4]),
					'description':data[5],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

##########################################Package Request#######################################


@app.route('/api/getpackagerequestdetails', methods=['GET'])
def getPackageRequest_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getPackageRequest()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'mobile':data[2],
					'email':data[3],
					'created_at':str(data[4]),
					'description':data[5],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


############################################Item Order###########################################


@app.route('/api/getitemorderdetails', methods=['GET'])
def getItemOrderRequest_estimation():
	if request.method == 'GET':

		listresult = []
		listdist = {}
		result = []

		json_results = []
		dbresult=dbhelper.GetData().getItemOrderRequest()
		for data in dbresult:
			db = {
					'order_id':data[0],
					'cart_id':data[1],
					'amount':data[2],
					'transaction_status':data[3],
					'bank_ref_no':data[4],
					'payment_mode':data[5],
					'status_message':data[6],
					'card_name':data[7],
					'created_at':str(data[8]),
					'item_id':data[9],
					'item_name':data[10],
					'item_brand':data[11],
					'item_code':data[12],
					'item_price':data[13],
					'package_id':data[14],
					'package_name':data[15],
					'package_code':data[16],
					'package_price':data[17],
					'billing_name':data[18],
					'billing_mobile':data[19],
					'billing_email':data[20],
					'billing_address':data[21],
					'billing_city':data[22],
					'billing_state':data[23],
					'billing_pin':data[24],
					'shipping_name':data[25],
					'shipping_mobile':data[26],
					'shipping_email':data[27],
					'shipping_addresss':data[28],
					'shipping_city':data[29],
					'shipping_state':data[30],
					'shipping_pin':data[31],
					
				}
			result.append(db)

		for atom in range(0, len(result)):
			if result[atom]['order_id'] not in listresult:
				listresult.append(result[atom]['order_id'])

		for atomlist in range(0, len(listresult)):
			listdist[listresult[atomlist]] = []
			for x in range(0, len(result)):
				if listresult[atomlist] == result[x]['order_id']:
					listdist[listresult[atomlist]].append(result[x])

		json_results.append(listdist)

		resp = Response(json.dumps({"success":1, "datasets":listdist}))
		return after_request(resp)


#################################Employees All####################################################


@app.route('/api/getemployeesalldetails', methods=['GET'])
def getEmployeesAll_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getEmployeeAllDetails()
		for data in result:
			db = {
					'name':data[0],
					'mobile':data[1],
					'email':data[2],
					'dob':str(data[3]),
					'alt_email':data[4],
					'addressline1':data[5],
					'addressline2':data[6],
					'id':data[7],
					'pin':data[8],
					'doj':str(data[9]),

					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



@app.route('/api/getemployeesallmanagedetails', methods=['GET', 'POST'])
def getEmployeesAllmanageDetails_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id']

		json_results = []
		result=dbhelper.GetData().getEmployeeAllmanageDetails(id)
		for data in result:
			db = {
					'name':data[0],
					'mobile':data[1],
					'email':data[2],
					'dob':str(data[3]),
					'alt_email':data[4],
					'addressline1':data[5],
					'addressline2':data[6],
					'id':data[7],
					'pin':data[8],
					'doj':str(data[9]),

					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getemployeesallpermissionsroles', methods=['GET', 'POST'])
def getEmployeesAllPermissionsRoles_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id']

		json_results = []
		result=dbhelper.GetData().getEmployeeAllPermissionsroles(id)
		for data in result:
			db = {
					'display_name':data[0],
						
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/change/employeespassword', methods=['GET', 'POST'])
def getEmployeesPassword_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		id = userdata['id']
		password = userdata['pass']
		 

		result=dbhelper.GetData().postEmployeesPassword(password, id)
		
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

##################################   Packages          ##############################################

@app.route('/api/getadminpackagedetails', methods=['GET'])
def getAdminPackage_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAdminPackageDetails()
		for data in result:
			db = {
					'id':data[0],
					'type':data[1],
					'name':data[2],
					'style':data[3],
					'section':data[4],
					'code':data[5],
					'price':data[6],
					'availability':data[7],
					'length':data[8],
					'width':data[9],
					'description':unicode(data[10], errors='ignore'),
					'designers':data[11],
					'added_by':data[12],
					'created_at':str(data[13]),
					'updated_at':str(data[14]),
					'panorama_image_id':data[15],
					'url':str(data[16]),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

############################# Package Ordering packagegold ####################################


@app.route('/api/getpackagegold', methods=['GET'])
def getPackageGold_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getPackageGoldDetails()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'style':data[2],
					'price':data[3],
					'images':data[4],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

######################### Package Ordering packageplatinum   ###################################


@app.route('/api/getpackageplatinum', methods=['GET'])
def getPackagePlatinum_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getPackagePlatinumDetails()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'style':data[2],
					'price':data[3],
					'images':data[4],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

######################### Package Ordering packagesilver   ###################################


@app.route('/api/getpackagesilver', methods=['GET'])
def getPackageSilver_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getPackageSilver()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'style':data[2],
					'price':data[3],
					'images':data[4],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

############################## Vendor selected vendors #########################################

@app.route('/api/getselectvendor', methods=['GET'])
def getSelectVendor_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getSelectedVendor()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'address':data[2],
					'city':data[3],
					'pin':data[4],
					'phone':data[5],
					'website':data[6],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

############################### All Projects ##############################################


@app.route('/api/creteproject', methods=['GET', 'POST'])
def createProject_estimation():
	if request.method == 'POST':
		userdata = json.loads(request.data)
		client_email = userdata['client_email']
		society = userdata['society']
		name = userdata['name']
		contact_person = userdata['contact_person']
		mobile = userdata['mobile']
		pin = userdata['pin']
		address = userdata['address']
		city = userdata['city']
		state = userdata['state']
		user_id = userdata['user_id']

		json_results = []
		result=dbhelper.GetData().CreateProject(client_email, society, name, contact_person, mobile, pin, address, city, state, user_id)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)



@app.route('/api/getallprojects', methods=['GET'])
def getAllProjects_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllProjects()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'society':data[2],
					'code':data[3],
					'client':data[4],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/postprojectteam', methods=['GET','POST'])
def postProjectTeam_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		projectid = userdata['proid']
		uid = userdata['uid']
		proteamdata = userdata['data']

		result=dbhelper.GetData().postProjectTeam(projectid, uid, proteamdata)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

@app.route('/api/postclients', methods=['GET','POST'])
def postClients_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		projectid = userdata['proid']
		uid = userdata['uid']
		proteamdata = userdata['data']

		json_results = []
		result=dbhelper.GetData().postClients(projectid, uid, proteamdata)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

@app.route('/api/removeTeam', methods=['GET','POST'])
def removeTeam_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		ppid = userdata['ppid']

		result=dbhelper.GetData().removeTeams(ppid)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)


@app.route('/api/getallprojectdetails', methods=['GET', 'POST'])
def gettAllprojectDetails_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		projectid = userdata['id']

		json_results1 = []
		result=dbhelper.GetData().getAllProjectDetailsById(projectid)
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'society':data[2],
					'code':data[3],
					'contact_person':data[4],
					'mobile':data[5],
					'pin':data[6],
					'address':data[7],
					'client':data[8],
					'email':data[9],
							
				}
			json_results1.append(db)

		json_results2 = []
		result1=dbhelper.GetData().getAllProjectTeamsById(projectid)
		for data in result1:
			db = {
					'uid':data[0],
					'name':data[1],
					'email':data[2],
					'role':data[3],
					'ppid':data[4],
							
				}
			json_results2.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results1, "datasets2":json_results2}))
		return after_request(resp)

@app.route('/api/getallprojecttimelins', methods=['GET', 'POST'])
def gettAllprojectTimelines_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		projectid = userdata['id']

		json_results = []
		listresult = []
		listdist = {}
		result = []
		dbresult=dbhelper.GetData().getAllProjectTimelines(projectid)
		for data in dbresult:
			db = {
					'projectid':data[0],
					'message':unicode(data[1], errors='ignore'),
					'timeline_id':data[2],
					'time_id':data[3],
					'path':data[4],
					'type':data[5],
					'time':str(data[6]).split(" ")[0]			
				}
			result.append(db)


		for atom in range(0, len(result)):
		    if result[atom]['time'] not in listresult:
		        listresult.append(result[atom]['time'])


		final_list = []
		for atomlist in range(0, len(listresult)):
		    listdist[listresult[atomlist]] = []
		    for x in range(0, len(result)):
		        if listresult[atomlist] == result[x]['time']:
		            listdist[listresult[atomlist]].append(result[x])
			# final_list.append(listdist)

		json_results.append(listdist)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/get/all/timeline/comments', methods=['GET', 'POST'])
def getAllTimelineComment_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		projectid = userdata['id']

		json_results = []
		listresult = []
		listdist = {}
		result = []
		dbresult=dbhelper.GetData().getAllTimelineComment(projectid)
		for data in dbresult:
			db = {
					'timelineid':data[0],
					'comment':data[1],
					'comment_id':data[2],
					'time':str(data[3]),
					'name':data[4],	
				}

			result.append(db)

		for atom in range(0, len(result)):
		    if result[atom]['timelineid'] not in listresult:
		        listresult.append(result[atom]['timelineid'])

		for atomlist in range(0, len(listresult)):
		    listdist[listresult[atomlist]] = []
		    for x in range(0, len(result)):
		        if listresult[atomlist] == result[x]['timelineid']:
		            listdist[listresult[atomlist]].append(result[x])
		            
		json_results.append(listdist)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/get/all/empteam', methods=['GET'])
def getAllProjectTeam_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllProjectEmployees()
		for data in result:
			db = {
					'id':data[0],
					'emp_name':data[1],
					'emp_email':data[2]
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/get/all/clients', methods=['GET'])
def getAllProjectClients_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllProjectCleints()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'email':data[2]
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



@app.route('/api/get/all/pi/data', methods=['GET'])
def getAllProjectpidata_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllProjectpidata()
		for data in result:
			db = {
					'timeline_attachment_id':data[1],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getprojectstatus', methods=['GET', 'POST'])
def getAllprojectstatus_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		userid = userdata['uid']
		projectid = userdata['pid']

		json_results = []
		result=dbhelper.GetData().getAllProjectStatus(userid, projectid)
		for data in result:
			db = {
					'status':data[0],
					'project_id':data[1],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/basic/edit', methods=['GET', 'POST'])
def getUpdateBasicInfo_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		proid = userdata['id']
		society = userdata['society']
		projectname = userdata['projectname']
		contact_person = userdata['contact_person']
		mobile = userdata['mobile']
		address = userdata['address']

		result=dbhelper.GetData().getUpdateBasic(proid, society, projectname, contact_person, mobile, address)
	
		resp = Response(json.dumps({"success":1, "datasets":result}))
		return after_request(resp)

@app.route('/api/getledgerclient', methods=['GET', 'POST'])
def getAllLedgerClients_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		proid = userdata['proid']

		json_results = []
		result = dbhelper.GetData().getAllLedgerClients(proid)
		for data in result:
			db = {
					'id':data[0],
					'client':data[1],
					'project_name':data[2]
				}
			json_results.append(db)


		json_results1 = []
		result1 = dbhelper.GetData().getAllProjectInstallement(proid)
		for data in result1:
			db = {
					'id':data[0],
					'project_id':data[1],
					'invoice_no':data[2],
					'amount':str(data[3]),
					'tax_amount':str(data[4]),
					'due_date':str(data[5]),
					'paid_on':str(data[6]),
					'status':data[7],
					'created_by':data[8],
					'created_at':str(data[9]),
					'mode_of_transaction':data[10]
				}
			json_results1.append(db)

		json_results2 = []
		result2 = dbhelper.GetData().getAllProjectPayments(proid)
		for data in result2:
			db = {
					'id':data[0],
					'tarnsaction_status':data[1],
					'duepayment':data[2],
					'bank_ref_no':str(data[3]),
					'payment_mode':data[4],
					'card_name':str(data[5]),
					'created_at':str(data[6]),
					
				}
			json_results2.append(db)

		json_results3 = []
		result3 = dbhelper.GetData().getAllProjectExpenses(proid)
		for data in result3:
			db = {
					'id':data[0],
					'project_id':data[1],
					'name':data[2],
					'amount':str(data[3]),
					'particulars':data[4],
					'mode_of_transaction':str(data[5]),
					'type_of_transaction':str(data[6]),
					'bill_no':data[7],
					'tax_amount':str(data[8]),
					'remarks':data[9],
					'created_by':data[10],
					'created_at':str(data[11]),
					'bank':data[12],
					'cheque_number':data[13],
					'concern_person':data[14],
					'date':str(data[15]),
					'path':data[16],
					'type':data[17]
					
				}
			json_results3.append(db)


		resp = Response(json.dumps({"success":1, "datasets":json_results, "datasets1":json_results1, "datasets2":json_results2, "datasets3":json_results3}))
		return after_request(resp)

##################################  Campaign Module  #####################################

@app.route('/api/getcampaign', methods=['GET'])
def getAllCampaign_estimation():
	if request.method == 'GET':

		json_results = []
		result=dbhelper.GetData().getAllCampaign()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'subject':unicode(data[2], errors='ignore'),
					'message':unicode(data[3], errors='ignore'),
					'description':unicode(data[4], errors='ignore'),
					
				}
			json_results.append(db)

		json_results1 = []
		result1=dbhelper.GetData().getAllMailinglist()
		for data in result1:
			db = {
					'id':data[0],
					'name':data[1],
					'email':data[2],
					'mobile':data[3],
					'society_name':data[4],
					'city':data[5],
					'response':data[6],
					'remarks':data[7],
					'added_by':data[8],
					'created_at':str(data[9])
					
				}
			json_results1.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results, "datasets1":json_results1}))
		return after_request(resp)



################################### Panorama Module  ######################################


@app.route('/api/getallpanorama', methods=['GET'])
def getAllPanorama_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllPanorama()
		for data in result:
			db = {
					'id':data[0],
					'file_name':data[1],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



################################### ITEMS Module  ######################################


@app.route('/api/getallsearchitems', methods=['GET'])
def getAllSearchItems_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getAllSearchingItems()
		for data in result:
			db = {
					'id':data[0],
					'name':unicode(data[1], errors='ignore'),
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



################################### Coupon Module  ######################################


@app.route('/api/getallcoupon', methods=['GET'])
def getAllCoupon_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getCreateCoupan()
		for data in result:
			db = {
					'id':data[0],
					'code':data[1],
					'discount_percent':data[2],
					'discount_amount':data[3],
					'valid_from':str(data[4]),
					'valid_to':str(data[5]),
					'description':data[6],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


################################### package url customization  ######################################


@app.route('/api/getpackagesectionurlcustom', methods=['GET'])
def getAllpackagesectionCutomization_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getpackageUrlCustomization1()
		for data in result:
			db = {
					'section':data[0],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getpackageurlcustom', methods=['GET'])
def getAllpackageurl_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getpackageUrlCustomization2()
		for data in result:
			db = {
					'id':data[0],
					'urlname':data[1],
					'urlview':data[2],
					'type':data[3],
					'keywords':data[6],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



@app.route('/api/getpackagestyleurlcustom', methods=['GET'])
def getAllpackagestyleCutomization_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getpackageUrlCustomization3()
		for data in result:
			db = {
					'style':data[0],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getpackagesdetailsbyID', methods=['GET', 'POST'])
def getAllpackagesDetailsByID_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getpackagedetailsby(packageid)
		for data in result:
			db = {
					'id':data[0],
					'type':data[1],
					'name':data[2],
					'style':data[3],
					'section':data[4],
					'code':data[5],
					'price':data[6],
					'availability':data[7],
					'length':data[8],
					'width':data[9],
					'description':unicode(data[10], errors='ignore'),
					'designers':data[11],
					'panorama_image_id':data[15],
					'url':data[16],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


@app.route('/api/getpackagescivilworks', methods=['GET', 'POST'])
def getAllpackagesCivilWorks_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getpackagesdetailscivilworks(packageid)
		for data in result:
			db = {
					'id':data[0],
					'package_id':data[1],
					'civil_work_name':data[2],
					'price':data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getpackagesfurnitures', methods=['GET', 'POST'])
def getAllpackagesFurnitures_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getpackagesfurnitures(packageid)
		for data in result:
			db = {
					'id':data[0],
					'package_id':data[1],
					'fixed_furniture_name':data[2],
					'price':data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getpackageimagesbyid', methods=['GET', 'POST'])
def getAllpackageImagesByID_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getpackageimagesByID(packageid)
		for data in result:
			db = {
					'id':data[0],
					'file_name':data[1],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getpackageimagestagsbyid', methods=['GET', 'POST'])
def getAllpackageImagesTagsByID_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getpackageimagestgsByID(packageid)
		for data in result:
			db = {
					'id':data[0],
					'file_name':data[1],	
					
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/getallpackagesimagesbyid', methods=['GET', 'POST'])
def getSupportAllpackageImagesByID_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		packageid = userdata['id']

		json_results = []
		result=dbhelper.GetData().getAllpackagesimagesByID(packageid)
		for data in result:
			db = {
					'id':data[0],
					'file_name':data[1],
							
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)



################################### Manage Roles and Permissions #################################


@app.route('/api/allemployerroles', methods=['GET'])
def getAllRolesDetails_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getallRoles()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'display_name':data[2],
					'description':data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/allroleNpermissions', methods=['GET'])
def getAllRolesNPermissionsDetails_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getallrolePermissions()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'display_name':data[2],
					'description':data[3],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


############################## Employee Registration ############################################

# @app.route('/api/empregitration/', methods=['GET', 'POST'])
# def postEmployeeRegistration_estimation():
# 	if request.method == 'POST':
# 		userdata = json.loads(request.data)
# 		username = userdata['username']
# 		dob = userdata['dob'],
# 		addressline1 = userdata['addressline1'],
# 		addressline2 = userdata['addressline2'],
# 		pin = userdata['pin'],
# 		joiningdate = userdata['joiningdate'],
# 		alt_email = userdata['alt_email'],
# 		mobile = userdata['mobile']
# 		print(username);
		
# 		result=dbhelper.GetData().postEmployeeRegistration(username, dob, addressline1, addressline2, pin, joiningdate, alt_email, mobile)
# 		json_results = []
# 		for data in result:
# 			db = {
# 					'id':data[0],
# 					'email':data[1],
# 					'password':data[2]
					
# 				}
# 			json_results.append(db)
	
# 		resp = Response(json.dumps({"success":1, "datasets":json_results}))
# 		return after_request(resp)


@app.route('/api/empregitration', methods=['GET', 'POST'])
def postEmployeeRegistration_estimation():
	if request.method == 'POST':

		userdata = json.loads(request.data)
		username = userdata['username'],
		dob = userdata['dob'],
		addressline1 = userdata['addressline1'],
		addressline2 = userdata['addressline2'],
		pin = userdata['pin'],
		joiningdate = userdata['joiningdate'],
		alt_email = userdata['alt_email'],
		mobile = userdata['mobile'],
		added_by = userdata['added_by']

		
		result=dbhelper.GetData().postEmployeeRegistration(username, dob, addressline1, addressline2, pin, joiningdate, alt_email, mobile, added_by)
		json_results = []
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'email':data[2],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


################################ Cash On Delivery module ######################################

@app.route('/api/allcodusers', methods=['GET'])
def getAllcodUsers_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getCashonDeliveryUsers()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1],
					'email':data[2],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/allcodroles', methods=['GET'])
def getAllcodUsersRoles_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getCashonDeliveryroles()
		for data in result:
			db = {
					'id':data[0],
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)


################################### Manage Categories module ###############################

@app.route('/api/allcategories', methods=['GET'])
def getAllCategories_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getallCategories()
		for data in result:
			db = {
					'id':data[0],
					'name':data[1]
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)

@app.route('/api/allcoupons', methods=['GET'])
def getAllCoupons_estimation():
	if request.method == 'GET':
		json_results = []
		result=dbhelper.GetData().getallCoupons()
		for data in result:
			db = {
					'id':data[0],
					'code':data[1],
					'discount_percent':data[2],
					'discount_amount':data[3],
					'valid_from':str(data[4]),
					'valid_to':str(data[5]),
					'description':data[6],
					'created_by':data[7],
					'created_at':str(data[8])
					
				}
			json_results.append(db)
	
		resp = Response(json.dumps({"success":1, "datasets":json_results}))
		return after_request(resp)









app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
		  
if __name__ == "__main__":
	app.run()