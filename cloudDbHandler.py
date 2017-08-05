import os

from google.appengine.api import memcache

from google.appengine.api import rdbms
from datetime import datetime
import time
import MySQLdb
import string
import random
# ccutil import hgjh

from ccavutil import encrypt,decrypt


_INSTANCE_NAME = 'cafe-indica-163107:us-central1:apidata' 
CLOUDSQL_USER ='indica'
CLOUDSQL_PASSWORD='tech@123'



def connect_to_cloudsql():
	dbname='indica'
	# When deployed to App Engine, the `SERVER_SOFTWARE` environment variable will be set to 'Google App Engine/version'.
	if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
		# Connect using the unix socket located at
		# /cloudsql/cloudsql-connection-name.
		cloudsql_unix_socket = os.path.join('/cloudsql', _INSTANCE_NAME)

		db = MySQLdb.connect( unix_socket=cloudsql_unix_socket, user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, db=dbname)

	# If the unix socket is unavailable, then try to connect using TCP. This will work if you're running a local MySQL server or using the Cloud SQL proxy, for example: cloud_sql_proxy -instances=your-connection-name=tcp:3306
	else:
		db = MySQLdb.connect(
			host='146.148.110.200',  user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, db=dbname)

	return db


class AddData():

	##############################################################
	#public site

########################## Employee Registration ###########################

	def addUser(self,username,dob,phoneNumber,password):
		try:
			dbname='Android'
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			cursor.execute('insert into userInfo(name,emailId,phoneNumber,password) values (%s,%s,%s,%s)',(name,emailId,phoneNumber,password))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)	
			
	
	#add user to database moovo_guest in table login_details
	def addOrder(self,orderId,deliveryName,deliveryPhone,deliveryAddress,deliveryDetails,subtotalValue,promoValue,vatValue,serviceValue,deliveryChargeValue,finalTotalValue,now_date,userEmail):
		try:
			dbname='Android'
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			cursor.execute('insert into orderDetails(orderId,deliveryName,deliveryPhone,deliveryAddress,deliveryDetails,subTotal,promo,vat,serviceTax,deliveryCharge,totalValue,timeStamp,userEmail) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(orderId,deliveryName,deliveryPhone,deliveryAddress,deliveryDetails,subtotalValue,promoValue,vatValue,serviceValue,deliveryChargeValue,finalTotalValue,now_date,userEmail))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)
			
	
	##Add Cnote to Server 
	def addNewCnoteToServer(self,biltyNo,contractParty, origin,destination, consignor, consignorAddress,consignee,consigneeAddress,cnoteDate,cnoteTime,paymentMode,invoiceNo,vehicleNo,ownerName,ownerContact,driverName,driverContact,vehicleType,capacity,gpsEnabled,vehicleRate,advancePayment, advanceDate,paidBy,freightNo, actualWeight,extraCharge,expDateDelivery,supportedDocName,docDownloadUrl,userName,location,userEmail,remarks):
		try:
			dbname='moovo_asap'
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			submissionDateTime = str(datetime.now())
			status= "open"
			cursor.execute('insert into cnoteDetails(biltyNo,contractParty, origin,destination, consignor, consignorAddress,consignee,consigneeAddress,cnoteDate,cnoteTime,paymentMode,invoiceNumber,vehicleNo,ownerName,ownerContact,driverName,driverContact,vehicleType,capacity,gpsEnabled,vehicleRate,advancePayment, advanceDate,paidBy,freightNo, actualWeight,extraCharge,expDateDelivery,supportedDocName,docDownloadUrl,userName,location,userEmail,submissionDateTime,status,remarks) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(biltyNo,contractParty, origin,destination, consignor, consignorAddress,consignee,consigneeAddress,cnoteDate,cnoteTime,paymentMode,invoiceNo,vehicleNo,ownerName,ownerContact,driverName,driverContact,vehicleType,capacity,gpsEnabled,vehicleRate,advancePayment, advanceDate,paidBy,freightNo, actualWeight,extraCharge,expDateDelivery,supportedDocName,docDownloadUrl,userName,location,userEmail,submissionDateTime,status,remarks))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)
			
	###Add New Fleet Details to the Server
	def addNewFleetData(self,vehicleNo, ownerName, ownerContact, driverName, driverContact, vehicleType, gpsEnabled, capacity):
		try:
			dbname='moovo_asap'
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			submissionDateTime = str(datetime.now())
			cursor.execute('insert into fleet_details(vehicleNo, ownerName, ownerContact, driverName, driverContact, vehicleType, gpsEnabled, capacity) values (%s,%s,%s,%s,%s,%s,%s,%s)',(vehicleNo, ownerName, ownerContact, driverName, driverContact, vehicleType, gpsEnabled, capacity))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)
			
	def addPaymentDetails(self, biltyNo, advancePayment,advancePurpose, advanceDate, paidBy):
		try:
			dbname='moovo_asap'
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			cursor.execute('insert into payment_details(biltyNo, advancePayment, purpose, advanceDate, paidBy) values (%s,%s,%s,%s,%s)',(biltyNo, advancePayment,advancePurpose, advanceDate, paidBy))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)
			
	def addCompleteCnoteInfo(self, biltyNo, tripEndDate, tripEndTime, chalanValue, damage,holdingCustomer, holdingDriver, shortageData, tollValue, supportedDocName, docDownloadUrl, userName, userEmail):
		try:
			
			dbname='moovo_asap'
			location=""
			conn = rdbms.connect(instance=_INSTANCE_NAME, database=dbname)
			cursor = conn.cursor() 
			cursor.execute('insert into completeCnote(biltyNo, tripEndDate, tripEndTime, chalanValue, damage,holdingCustomer, holdingDriver, shortageData, tollValue, supportedDocName, docDownloadUrl, userName, userEmail,location) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(biltyNo, tripEndDate, tripEndTime, chalanValue, damage,holdingCustomer, holdingDriver, shortageData, tollValue, supportedDocName, docDownloadUrl, userName, userEmail,location))
			conn.commit()
			testid = cursor.lastrowid
			conn.close()
			return testid
		except Exception,e:
			print str(e)
		
			
	


	#######################################################################################################
					   
class GetData():

	user_login_id = 0;
	###############################
	#Public site getting data

	def getPackage_Image_Tags(self, url):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = 'select id from packages where url = "%s" '%(url)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		id = dbDetails[0]

		sqlquery = "select images.file_name, package_image_tags.xcoord, package_image_tags.ycoord, package_image_tags.item_id, items.name, item_selling_price.value, items.description from package_image join images on images.id = package_image.image_id left join package_image_tags on package_image_tags.image_id = package_image.image_id left join items on items.id = package_image_tags.item_id left join (select max(id) as item_sp_id, item_id from item_selling_price group by item_id)s on s.item_id = package_image_tags.item_id left join item_selling_price on item_selling_price.id = s.item_sp_id where package_image.package_id = '%s'"%(id)
		print sqlquery
		cursor.execute(sqlquery)
		package_image_tags = []
		for row in cursor.fetchall():
			package_image_tags.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails',package_image_tags
		return package_image_tags 


	def getPackage_Fixed(self, url):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = 'select id from packages where url = "%s" '%(url)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		id = dbDetails[0]

		sqlquery = "select package_fixed_furnitures.fixed_furniture_name, package_fixed_furnitures.price, package_fixed_furnitures.id from packages as pack join package_fixed_furnitures on package_fixed_furnitures.package_id = pack.id where pack.id = '%s'"%(id)
		print sqlquery
		cursor.execute(sqlquery)
		package_fixed = []
		for row in cursor.fetchall():
			package_fixed.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails',package_fixed
		return package_fixed


	def getPackage_Civil(self, url):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = 'select id from packages where url = "%s" '%(url)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		id = dbDetails[0]

		sqlquery = "select package_civil_works.civil_work_name, package_civil_works.price, package_civil_works.id from packages as pack join package_civil_works on package_civil_works.package_id = pack.id where pack.id = '%s'"%(id)
		print sqlquery
		cursor.execute(sqlquery)
		package_fixed = []
		for row in cursor.fetchall():
			package_fixed.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails',package_fixed
		return package_fixed

	def getPackage_Item(self, url):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = 'select id from packages where url = "%s" '%(url)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		id = dbDetails[0]

		# sqlquery = "select packages.name, any_value(items.name), any_value(item_mrp.value), any_value(images.file_name), any_value(item_selling_price.value), packages.description from packages join package_item on packages.id = package_item.package_id join items on items.id = package_item.item_id join item_mrp on items.id = item_mrp.item_id join item_image on items.id = item_image.item_id join images on item_image.image_id = images.id join (select max(id) as item_sp_id, item_id from item_selling_price group by item_id)s on s.item_id = items.id left join item_selling_price on item_selling_price.id = s.item_sp_id where packages.id = '%s' group by item_selling_price.value"%(id)
		sqlquery = "select packages.name, items.name, any_value(item_mrp.value), group_concat(images.file_name), any_value(item_selling_price.value), packages.description from packages join package_item on packages.id = package_item.package_id join items on items.id = package_item.item_id join item_mrp on items.id = item_mrp.item_id join item_image on items.id = item_image.item_id join images on item_image.image_id = images.id join (select max(id) as item_sp_id, item_id from item_selling_price group by item_id)s on s.item_id = items.id left join item_selling_price on item_selling_price.id = s.item_sp_id where packages.id = '%s' group by items.name"%(id)
		print sqlquery
		cursor.execute(sqlquery)
		package_fixed = []
		for row in cursor.fetchall():
			package_fixed.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails',package_fixed
		return package_fixed 


	def postComments(self, id, comment, comment_by):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		
		cursor.execute('insert into timeline_comments (timeline_id, comment, commented_by) values (%s,%s,%s)',(id, comment, comment_by))
		
		db.commit()
		db.close()
		
		return 1


	def getMapDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select project_markers.id, lat, lng, projects.id, name, society, address, mobile, contact_person, project_status.status, timeline_attachment.path from projects left join project_markers on project_markers.project_id = projects.id left join project_status on projects.id = project_status.project_id join project_display_pic on project_display_pic.project_id = project_markers.project_id left join timeline_attachment on project_display_pic.timeline_attachment_id = timeline_attachment.id where project_display_pic.display_pic = 1 order By project_markers.id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		return dbDetails 

	def getProjectPayment(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = "select id from projects where code = '%s'"%(id)
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		project_id = dbDetails[0]

		sqlquery1 = "select * from project_payment where project_id = '%s'"%(project_id)
		cursor.execute(sqlquery1)
		dbDetails1 = []
		for row in cursor.fetchall():
			dbDetails1.append(row)

		sqlquery2 = "select * from project_costs where project_id = '%s'"%(project_id)
		cursor.execute(sqlquery2)
		dbDetails2 = []
		for row in cursor.fetchall():
			dbDetails2.append(row)
		print dbDetails2

		db.commit()
		db.close()
		return dbDetails1, dbDetails2

	def getProjectDisplayPic(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from project_display_pic left join timeline_attachment on project_display_pic.timeline_attachment_id = timeline_attachment.id where project_display_pic.project_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		return dbDetails 


	def postEmployeeRegistration(self, username, dob, addressline1, addressline2, pin, joiningdate, alt_email, mobile, added_by):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from users where email = '%s'"%(username)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)

		if(dbDetails):
			cursor.execute('insert into employees(user_id, address_line1, address_line2, pin, mobile, alt_email, dob, doj, added_by) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(dbDetails[0][0], addressline1, addressline2, pin, mobile, alt_email, dob, joiningdate, added_by))
		db.commit()
		db.close()
		print 'dbDetails', dbDetails[0][0]
		return dbDetails

	def getPaymentData(self, address,city,email,mobile,name,pin,state,amount):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		
		merchant_data='merchant_id='+90885+'&'+'order_id='+1+ '&' + "currency=" + INR + '&' + 'amount=' +amount+'&'+'redirect_url='+'http://www.cafeindica.co.in/'+'&'+'cancel_url='+'http://www.cafeindica.co.in/'+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_address='+p_billing_address+'&'+'billing_city='+p_billing_city+'&'+'billing_state='+p_billing_state+'&'+'billing_zip='+p_billing_zip+'&'+'billing_country='+p_billing_country+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'delivery_name='+p_delivery_name+'&'+'delivery_address='+p_delivery_address+'&'+'delivery_city='+p_delivery_city+'&'+'delivery_state='+p_delivery_state+'&'+'delivery_zip='+p_delivery_zip+'&'+'delivery_country='+p_delivery_country+'&'+'delivery_tel='+p_delivery_tel+'&'+'merchant_param1='+p_merchant_param1+'&'+'merchant_param2='+p_merchant_param2+'&'+'merchant_param3='+p_merchant_param3+'&'+'merchant_param4='+p_merchant_param4+'&'+'merchant_param5='+p_merchant_param5+'&'+'integration_type='+p_integration_type+'&'+'promo_code='+p_promo_code+'&'+'customer_identifier='+p_customer_identifier+'&'
	
		encryption = encrypt(merchant_data,workingKey)

		db.commit()
		db.close()
		print 'dbDetails', address+" "+city+" "+email+" "+mobile+" "+name+" "+pin+" "+state+" "+amount
		return 1

	def getSuperSections(self):
		# try:
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name from supersections"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 
		# except Exception,e:
		# 	print str(e)


	def getSections(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name from sections"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 


	def getTestSections(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(supersection_id) from sections"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		dbDetails1=[]
		dict = {}
		for row in cursor.fetchall():
			dbDetails.append(row)
		for i in range(0, len(dbDetails)):
			print 'id = ',dbDetails[i]
			sqlcmd1 = "select id, name from sections where supersection_id = '%s'"%(dbDetails[i])
			print sqlcmd1
			cursor.execute(sqlcmd1)
			for row in cursor.fetchall():
				dbDetails1.append(str(row))
				print 'row',row
			dict[str(dbDetails[i])] = dbDetails1
			dbDetails1 = []
			
		db.commit()
		db.close()
		print 'dbDetails',dict
		return dict

	def getSubsections(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name from subsections"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails	 


	def getAllSectionCategories(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select supersections.id, supersections.name, sections.id, sections.name, subsections.id, subsections.name, categories.id, categories.name from supersections join sections on supersections.id = sections.supersection_id join subsections on sections.id = subsections.section_id join subsection_category on subsections.id = subsection_category.subsection_id join categories on subsection_category.category_id = categories.id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 
		

	def getProduct(self, url):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		if(url):
			sqlcmd = "select id, type, name, style, section, code, price, availability, length, width, description, added_by from packages where url = '%s'"%(url)
			print sqlcmd
			cursor.execute(sqlcmd)
			dbData = []
			for row in cursor.fetchall():
				dbData.append(row)
		db.commit()
		db.close()
		print 'dbData', dbData
		return dbData

	def getProductbySection(self, type):
		# try:
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id WHERE packages.section like '%s' group by packages.id"%(type)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 
		# except Exception,e:
		# 	print str(e)

	def getCategoryItems(self, params):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		print params
		# if params['section']:
		# 	print "Abhay Prakash"
		param = ""
		value = ""
		if params['category']:
			param = 'categories.name'
			value = params['category']
			print value

		elif params['section']:
			param = 'sections.name'
			value = params['section']
			print value

		elif params['subsection']:
			param = 'subsections.name'
			value = params['subsection']
			print value

		elif params['supersection']:
			param = 'supersections.name'
			value = params['supersection']
			print value

		sqlcmd = "select items.id, items.name, items.brand, items.url, group_concat(distinct(item_mrp.value) order by item_mrp.created_at desc) as mrp, group_concat(distinct(item_selling_price.value) order by item_selling_price.created_at desc) as sp, group_concat(distinct(images.file_name) order by images.id) as images from items join item_image on items.id = item_image.item_id join images on item_image.image_id = images.id join item_category on items.id = item_category.item_id join categories on item_category.category_id = categories.id join subsection_category on categories.id = subsection_category.category_id join subsections on subsection_category.subsection_id = subsections.id join sections on subsections.section_id = sections.id join supersections on sections.supersection_id = supersections.id join item_mrp on items.id = item_mrp.item_id join item_selling_price on items.id = item_selling_price.item_id where %s = '%s' group by items.id"%(param, value)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getProductbyType(self, type):
		# try:
		db = connect_to_cloudsql()
		cursor = db.cursor()
		packagesect = "select * from package_url_views where urlview='%s'"%(type)
		cursor.execute(packagesect)
		dbdata = []
		for row in cursor.fetchall():
			dbdata.append(row)
		if dbdata:
			type = dbdata[0][3]
			key = dbdata[0][6]
			dbDetails=[]
			if type=="SECTION":
				sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, any_value(package_category.category) from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on package_category.package_id = packages.id WHERE packages.section like '%s' group by packages.id"%(key)
				print sqlcmd
				cursor.execute(sqlcmd)
				for row in cursor.fetchall():
					dbDetails.append(row)
			elif type=="STYLE":
				sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, any_value(package_category.category) from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on package_category.package_id = packages.id WHERE packages.style like '%s' group by packages.id"%(key)
				print sqlcmd
				cursor.execute(sqlcmd)
				for row in cursor.fetchall():
					dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 
		# except Exception,e:
		# 	print str(e)

	def  getProductbyStyle(self, style):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, package_category.category from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on packages.id = package_category.category where packages.style like '%s' group by packages.id"%(style)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails

	def getPackageUrl(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select urlname, urlview, type, keywords from package_url_views where type='section'"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails=[]
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails 
		

 ################################# Ledger Store ##################################################

 	def postStoreLedger(self, userid, proid, payee_name, particulars, amount, tax_amount, bank, check_no, concern_person, bill_no, type_of_transaction, mode_of_transaction, remarks, date, file_type, path):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = datetime.now()
		print payee_name+" "+particulars
		cursor.execute('insert into project_ledgers(project_id, name, amount, particulars, mode_of_transaction, type_of_transaction, bill_no, tax_amount, remarks, created_by, created_at, bank, cheque_number, concern_person, date, path, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(proid, payee_name, amount, particulars, mode_of_transaction, type_of_transaction, bill_no, tax_amount, remarks, userid, submissionDateTime, bank, check_no, concern_person, date, path, file_type))
		
		db.commit()
		db.close()
		return 1 

################################# Installements Store ##################################################

 	def postStoreInstallements(self, userid, proid, amount, due, due_date, paid_date, mot, tax):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = datetime.now()
		cursor.execute('insert into project_payment(project_id, amount, tax_amount, due_date, paid_on, status, created_by, created_at, mode_of_transaction) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',(proid, amount, tax, due_date, paid_date, due, userid, submissionDateTime, mot))
		
		db.commit()
		db.close()
		return 1 


################################## public site ###############################################

	
################# Public Register ########################
	def PostPublicRegister(self, name, email, password):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		verified = 0;
		submissionDateTime = datetime.now()
		code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
		verified = 0

		sqlcmd = "select * from users where email = '%s'"%(email)
		cursor.execute(sqlcmd)
		dbDetails = []
		result = ""
		success = 0
		for row in cursor.fetchall():
			dbDetails.append(row)

		if dbDetails:
			success = 0
			result = "The email address you entered already exists. Please try with a different one."
		else:
			cursor.execute('insert into users(name, email, password, verified, verification_code, created_at, updated_at) values (%s, %s, %s, %s, %s, %s, %s)',(name, email, password, verified, code, submissionDateTime, submissionDateTime))
			result = 1
			success = 1
		# cursor.execute('insert into users(name, email, password) values(%s, %s, %s)'%(name, email, password))
		
		db.commit()
		db.close()
		
		# print 'dbDetails', user_login_id
		return result, success

################# Public Login ########################
	def getPublicLogin(self, username, password):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id ,email, password, name, verified from users where email='%s' and password='%s'"%(username, password)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		user_login_id = dbDetails[0][0]
		print 'dbDetails', user_login_id
		return dbDetails

	def getLoginCod(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select permissions.name from users join role_user on users.id = role_user.user_id join permission_role on role_user.role_id = permission_role.role_id join permissions on permission_role.permission_id = permissions.id where users.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getLoginPro_One(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from projects where client_user_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getLoginPro_Two(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from project_people where user_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getCart(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select items.id, items.name, items.brand, any_value(cart_item.count), any_value(cart_item.id), GROUP_CONCAT(distinct(item_mrp.value) order by item_mrp.created_at), GROUP_CONCAT(distinct(item_selling_price.value) order by item_selling_price.created_at), GROUP_CONCAT(distinct(images.file_name) order by images.id) from cart_item join items on items.id = cart_item.item_id join item_image on items.id = item_image.item_id join images on item_image.image_id = images.id join item_mrp on item_mrp.item_id = items.id join item_selling_price on item_selling_price.item_id = items.id join carts on carts.id = cart_item.cart_id where carts.user_id = '%s' group by (items.id)"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getpublicPackages(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.style, any_value(cart_package.count), packages.price, GROUP_CONCAT(distinct(images.file_name) order by images.id) from cart_package join packages on packages.id = cart_package.package_id join package_image on packages.id = package_image.package_id join images on package_image.image_id = images.id join carts on carts.id = cart_package.cart_id where carts.user_id = '%s' group by packages.id"(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getUserProject(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = "select timeline.project_id, timeline.message, timeline.id, timeline_attachment.id, timeline_attachment.path, timeline_attachment.type, Date(timeline.created_at), DayName(timeline.created_at), DayOfMonth(timeline.created_at), MonthName(timeline.created_at) from project_timeline as timeline left join timeline_attachment on timeline.id = timeline_attachment.timeline_id where timeline.project_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)

		sqlquery = "select comments.timeline_id, comments.comment, comments.commented_by, comments.created_at, users.name from timeline_comments as comments left join project_timeline on project_timeline.id = comments.timeline_id left join users on comments.commented_by = users.id left join project_people on project_people.project_id = project_timeline.project_id where project_timeline.project_id = '%s'"%(id)
		print sqlquery
		cursor.execute(sqlquery)
		dbDetails1 = []
		for row in cursor.fetchall():
			dbDetails1.append(row)

		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails, dbDetails1

	def  getAndroidProductbyStyle(self, style, section):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		dbDetails = []
		if style=='none' and section=='none':
			sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, package_category.category from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on packages.id = package_category.category group by packages.id"
			cursor.execute(sqlcmd)
		elif style=='none' and section:
			sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, package_category.category from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on packages.id = package_category.category where packages.section like '%s' group by packages.id"%(section)
			cursor.execute(sqlcmd)
		elif style and section=='none':
			sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, package_category.category from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on packages.id = package_category.category where packages.style like '%s' group by packages.id"%(style)
			cursor.execute(sqlcmd)
		else:
			sqlcmd = "select packages.id, packages.name, packages.url, packages.style, packages.price, packages.description, group_concat(distinct(images.file_name) order by images.id) as images, package_category.category from packages join package_image on packages.id = package_image.package_id left join images on package_image.image_id = images.id left join package_category on packages.id = package_category.category where packages.style like '%s' AND packages.section like '%s' group by packages.id"%(style,section)
			cursor.execute(sqlcmd)
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails

	def getAndroidStylelist(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(style) from packages"
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		return dbDetails

	def getAndroidSectionlist(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(section) from packages"
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		return dbDetails


	def postAndroidbookServices(self, servicename, name, contactnumber, address, city, state):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = datetime.now()
		cursor.execute('insert into bookservices(service_name, name, contact_number, address, city, state, created_at) values (%s, %s, %s, %s, %s, %s, %s)',(servicename, name, contactnumber, address, city, state, submissionDateTime))
		
		db.commit()
		db.close()
		return 1 

	def getpublicProjectData(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = "select timeline.project_id, projects.code, timeline.message, timeline.id, timeline_attachment.id, timeline_attachment.path, timeline_attachment.type, Date(timeline.created_at), Dayname(timeline.created_at) from project_timeline as timeline left join projects on projects.id = timeline.project_id left join timeline_attachment on timeline.id = timeline_attachment.timeline_id left join project_people on project_people.project_id = timeline.project_id where project_people.user_id = '%s' order by Date(timeline.created_at) desc"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)

		sqlquery = "select projects.code, projects.name, projects.id from projects left join project_people on project_people.project_id = projects.id where project_people.user_id = '%s'"%(id)
		
		cursor.execute(sqlquery)
		dbDetails1 = []
		for row in cursor.fetchall():
			dbDetails1.append(row)

		pro_id = dbDetails1[0][2]

		sqlquery2 = "select timeline.project_id, timeline.message, timeline.id, timeline_attachment.id, timeline_attachment.path, timeline_attachment.type, Date(timeline.created_at), DayName(timeline.created_at), DayOfMonth(timeline.created_at), MonthName(timeline.created_at) from project_timeline as timeline left join timeline_attachment on timeline.id = timeline_attachment.timeline_id where timeline.project_id = '%s'"%(pro_id)
		cursor.execute(sqlquery2)
		dbDetails2 = []
		for row in cursor.fetchall():
			dbDetails2.append(row)

		sqlquery3 = "select comments.timeline_id, comments.comment, comments.commented_by, comments.created_at, users.name from timeline_comments as comments left join project_timeline on project_timeline.id = comments.timeline_id left join users on comments.commented_by = users.id left join project_people on project_people.project_id = project_timeline.project_id where project_people.user_id = '%s' "%(id)
		cursor.execute(sqlquery3)
		dbDetails3 = []
		for row in cursor.fetchall():
			dbDetails3.append(row)

		sqlquery4 = "select project_status.project_id, project_status.status, projects.code from project_status left join project_people on project_people.project_id = project_status.project_id left join projects on projects.id = project_status.project_id where project_people.user_id = '%s'"%(id)
		cursor.execute(sqlquery4)
		dbDetails4 = []
		for row in cursor.fetchall():
			dbDetails4.append(row)


		db.commit()
		db.close()
		
		return dbDetails, dbDetails1, dbDetails2, dbDetails3, dbDetails4

	def getpublicProjectDataByprojectCode(self, projectcode):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		sqlcmd = "select distinct timeline.project_id, projects.code, timeline.message, timeline.id, timeline_attachment.id, timeline_attachment.path, timeline_attachment.type, Date(timeline.created_at), Dayname(timeline.created_at) from project_timeline as timeline left join projects on projects.id = timeline.project_id left join timeline_attachment on timeline.id = timeline_attachment.timeline_id left join project_people on project_people.project_id = timeline.project_id where projects.code = '%s' order by Date(timeline.created_at) desc"%(projectcode)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)

		db.commit()
		db.close()

		return dbDetails


	def getPublicUserComments(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlquery = "select DISTINCT comments.timeline_id, comments.comment, comments.commented_by, comments.created_at, users.name from timeline_comments as comments left join project_timeline on project_timeline.id = comments.timeline_id left join users on comments.commented_by = users.id left join project_people on project_people.project_id = project_timeline.project_id where comments.timeline_id = '%s' "%(id)
		cursor.execute(sqlquery)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getPublicUserProjectStatus(self, pro_code):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlquery = "select distinct project_status.project_id, project_status.status, projects.code from project_status left join project_people on project_people.project_id = project_status.project_id left join projects on projects.id = project_status.project_id where projects.code = '%s'"%(pro_code)
		cursor.execute(sqlquery)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getProjectLists(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlquery = "select * from projects where client_user_id = '%s'"%(id)
		cursor.execute(sqlquery)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails



###################################################################################################
################################### Cafe Indica Dash Board ######################################## 
###################################################################################################
##################################### Admin Site getting data #####################################

	def getAdminUser(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id ,email, password from users"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getLoginData(self, username, password):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id ,email, password, name from users where email='%s' and password='%s'"%(username, password)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAdminUserDetails(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.name, roles.display_name, permissions.name, users.id from users join role_user on role_user.user_id = users.id join roles on role_user.role_id = roles.id join permission_role on permission_role.role_id = roles.id join permissions on permissions.id = permission_role.permission_id where users.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

#####################################Bulk Orders#################################################
	def getBulkOrderDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select name, email, mobile, company, description, file, created_at from bulk_orders"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

###################################Callback Request################################################

	def getCallbackRequest(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select name, mobile, created_at from callback_requests"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

#################################Designer Request###################################################

	def getDesignerRequest(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select name, email, mobile, created_at, description from designer_requests order by created_at desc"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

###################################Item Request###################################################

	def getItemRequest(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name, mobile, email, created_at, description from item_requests order by created_at desc"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

#################################Package Request#################################################

	def getPackageRequest(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name, mobile, email, created_at, description from package_requests order by created_at desc"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

##################################Item Order#################################################

	def getItemOrderRequest(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select orders.id, orders.cart_id, orders.amount, orders.transaction_status, orders.bank_ref_no, orders.payment_mode, orders.status_message, orders.card_name, orders.created_at, items.id, items.name, items.brand, items.code, cart_item.price, packages.id, packages.name, packages.code, cart_package.price, billing.name, billing.mobile, billing.email, billing.address, billing.city, billing.state, billing.pin, shipping.name, shipping.mobile, shipping.email, shipping.address, shipping.city, shipping.state, shipping.pin from orders join addresses as shipping on orders.shipping_address_id = shipping.id join addresses as billing on orders.billing_address_id = billing.id left join cart_item on cart_item.cart_id = orders.cart_id left join items on items.id = cart_item.item_id left join cart_package on cart_package.cart_id = orders.cart_id left join packages on packages.id = cart_package.package_id where orders.transaction_status = 'success' order by orders.created_at desc"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

###############################Employee All##############################################

	def getEmployeeAllDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.name, employees.mobile, users.email, employees.dob, employees.alt_email, employees.address_line1, employees.address_line2, employees.id, employees.pin, employees.doj from users join employees on users.id = employees.user_id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getEmployeeAllmanageDetails(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.name, employees.mobile, users.email, employees.dob, employees.alt_email, employees.address_line1, employees.address_line2, employees.id, employees.pin, employees.doj from users join employees on users.id = employees.user_id where employees.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getEmployeeAllPermissionsroles(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(roles.display_name) from users join employees on users.id = employees.user_id join role_user on users.id = role_user.user_id join roles on role_user.role_id = roles.id  join permission_role on roles.id = permission_role.role_id join permissions on permission_role.permission_id = permissions.id where employees.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def postEmployeesPassword(self, password, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = str(datetime.now())
		sqlcmd = "update users join employees on users.id = employees.user_id set users.password = '%s', users.updated_at = '%s' where employees.id = '%s'"%(password, submissionDateTime, id)
		print sqlcmd
		cursor.execute(sqlcmd)
		db.commit()
		db.close()
		return 1

#################################       Packages      ##################################

	def getAdminPackageDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, type, name, style, section, code, price, availability, length, width, description, designers, added_by, created_at, updated_at, panorama_image_id, url from packages"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


############################# Package Ordering packagegold ######################################

	def getPackageGoldDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.style, packages.price, group_concat(distinct(images.file_name)order by images.id) as images from packages join package_image on packages.id = package_image.package_id join images on package_image.image_id = images.id left join package_ordering on package_ordering.package_id = packages.id where packages.type='Gold' group by packages.id order by any_value(package_ordering.order)"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

############################# Package Ordering packageplatinum ######################################

	def getPackagePlatinumDetails(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.style, packages.price, group_concat(distinct(images.file_name)order by images.id) as images from packages join package_image on packages.id = package_image.package_id join images on package_image.image_id = images.id left join package_ordering on package_ordering.package_id = packages.id where packages.type='Platinum' group by packages.id order by any_value(package_ordering.order);"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

############################# Package Ordering packageSilver ######################################

	def getPackageSilver(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select packages.id, packages.name, packages.style, packages.price, group_concat(distinct(images.file_name)order by images.id) as images from packages join package_image on packages.id = package_image.package_id join images on package_image.image_id = images.id left join package_ordering on package_ordering.package_id = packages.id where packages.type='Silver' group by packages.id order by any_value(package_ordering.order);"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


############################# Vendor selected vendors ######################################

	def getSelectedVendor(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name, address, city, pin, phone, website from vendors"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

#################################### All Projects ###############################################

	def CreateProject(self,client_email, society, name, contact_person, mobile, pin, address, city, state, user_id):
		db = connect_to_cloudsql()
		cursor = db.cursor()

		code_avail = False

		sqlcmd = "select id from users where email = '%s'"%(client_email)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		client_user_id = dbDetails[0][0]
		code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
		code = 'CI'+code
		submissionDateTime = str(datetime.now())

		sqlquery = "select code from projects"
		print sqlquery
		cursor.execute(sqlquery)
		dbDetails1 = []
		for row in cursor.fetchall():
			dbDetails1.append(row)

		if code not in dbDetails1:
			code_avail = True

		dbDetails2 = []
		if code_avail:
			cmdquery1 = "insert into projects(code, name, client_user_id, society, contact_person, mobile, address, pin, created_by, created_at, city, state) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(code, name, client_user_id, society, contact_person, mobile, address, pin, user_id, submissionDateTime, city, state)
			print cmdquery1
			cursor.execute(cmdquery1)
			
			projectid = cursor.lastrowid
			cursor.execute("insert into project_status(project_id, status, updated_by) values(%s, 'Negotiation', %s)"%(projectid, user_id))

		db.commit()
		db.close()
		print 'dbDetails', client_user_id, code, projectid
		return projectid


 	def getAllProjects(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(projects.id), projects.name, projects.society, projects.code, clients.name from projects join users as clients on clients.id = projects.client_user_id left join project_people on project_people.project_id = projects.id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

##################################### Post project team ###############################################

	def postProjectTeam(self, projectid, uid, proteamdata):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = datetime.now()

		for pteam in proteamdata['existingEmployee']:
			print pteam
			cursor.execute('insert into project_people(project_id, user_id, role, added_by, created_at) values (%s, %s, %s, %s, %s)',(projectid,pteam,proteamdata['existingRole'],uid,submissionDateTime))
		
		db.commit()
		db.close()
		return 1 

##################################### Post project team ###############################################

	def postClients(self, projectid, uid, proteamdata):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		submissionDateTime = datetime.now()
		role = "CLIENT"
		for pteam in proteamdata['existingclients']:
			cursor.execute('insert into project_people(project_id, user_id, role, added_by, created_at) values (%s, %s, %s, %s, %s)',(projectid,pteam,role,uid,submissionDateTime))
		
		db.commit()
		db.close()
		return 1 

##################################### remove Teams ###############################################

	def removeTeams(self, ppid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		
		cursor.execute('delete from project_people where id = "%s" '%(ppid))
		
		db.commit()
		db.close()
		return 1 


##################################### Get All Project Details  ##############################################

	def getAllProjectDetailsById(self, projectid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select projects.id, projects.name, projects.society, projects.code, projects.contact_person, projects.mobile, projects.pin, projects.address, users.name, users.email from projects join users on projects.client_user_id = users.id where projects.id = '%s'"%(projectid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectTeamsById(self, projectid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.id, users.name, users.email, project_people.role, project_people.id from project_people join users on users.id = project_people.user_id where project_people.project_id = '%s'"%(projectid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectTimelines(self, projectid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select timeline.project_id, timeline.message, timeline.id, timeline_attachment.id, timeline_attachment.path, timeline_attachment.type, timeline.created_at from project_timeline as timeline left join timeline_attachment on timeline.id = timeline_attachment.timeline_id where timeline.project_id = '%s' order by timeline.created_at desc"%(projectid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

################################ All Eployeees Team ################################################
	
	def getAllProjectEmployees(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select employees.user_id, users.name, users.email from employees join users on users.id = employees.user_id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

################################ All Project Clients ################################################
	
	def getAllProjectCleints(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.id, users.name, users.email from users left join employees on employees.user_id = users.id where employees.user_id is null"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectpidata(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from project_display_pic"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getAllProjectStatus(self, uid, pid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select project_status.status, project_status.project_id from project_status where project_status.project_id = '%s'"%(pid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)

		if(dbDetails is None):
			sqlquery = "insert into project_status(project_id, status, updated_by) values('%s', 'Negotiation', '%s') where project_status.project_id = '%s'"%(pid, uid, pid)
			cursor.execute(sqlquery)

		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getUpdateBasic(self, proid, society, projectname, contact_person, mobile, address):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "update projects set society = '%s', name = '%s', mobile = '%s', contact_person = '%s', address = '%s' where id = '%s'"%(society, projectname, mobile, contact_person, address, proid)
		print sqlcmd
		cursor.execute(sqlcmd)
		
		db.commit()
		db.close()
		return 1

	def getAllLedgerClients(self, proid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select users.id, users.name, projects.name from projects join users on projects.client_user_id = users.id where projects.id = '%s'"%(proid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectInstallement(self, proid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from project_payment where project_id = '%s'"%(proid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectPayments(self, proid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select payments.id, payments.transaction_status, payments.amount, payments.bank_ref_no, payments.payment_mode, payments.card_name, payments.created_at from project_payment join payments on project_payment.id = payments.project_payment_id where project_payment.project_id = '%s'"%(proid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllProjectExpenses(self, proid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from project_ledgers where project_id = '%s' order by date desc"%(proid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllTimelineComment(self, projectid):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select comments.timeline_id, comments.comment, comments.commented_by, comments.created_at, users.name from timeline_comments as comments left join project_timeline on project_timeline.id = comments.timeline_id left join users on comments.commented_by = users.id where project_timeline.project_id = '%s'"%(projectid)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails',dbDetails
		return dbDetails

	

#################################### All Items Search Module ###############################################

 	def getAllSearchingItems(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select id, name from items"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


###################################  Campaign Module  ####################################

	def getAllCampaign(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from campaign"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllMailinglist(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from mailing_list"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


################################### Panorama Module  ######################################

	def getAllPanorama(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select panorama_users.id, images.file_name from panorama_users join images on images.id = panorama_users.panorama_image_id"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


################################### Coupon ######################################

	def getCreateCoupan(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from coupons"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


################################### package url customization ######################################

	def getpackageUrlCustomization1(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(section) from packages"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getpackageUrlCustomization2(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from package_url_views"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getpackageUrlCustomization3(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select distinct(style) from packages"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getpackagedetailsby(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from packages where id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getpackagesdetailscivilworks(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from package_civil_works where package_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getpackagesfurnitures(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from package_fixed_furnitures where package_id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getpackageimagesByID(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select images.id, images.file_name from images join packages on images.id = packages.panorama_image_id where packages.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getpackageimagestgsByID(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select images.id, images.file_name from images join item_image on images.id = item_image.image_id join package_item on item_image.item_id = package_item.item_id join packages on package_item.package_id = packages.id where packages.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getAllpackagesimagesByID(self, id):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select images.id, images.file_name from images join package_image on images.id = package_image.image_id join packages on package_image.package_id = packages.id where packages.id = '%s'"%(id)
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


################################### Manage Roles and Permissions #################################

	def getallRoles(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from roles"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getallrolePermissions(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from permissions"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


###################################Cash On delivery module################################################

	def getCashonDeliveryUsers(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from users"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


	def getCashonDeliveryroles(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select user_id from role_user where role_id = 5"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails


##################################### Manage Categories Module #################################

	def getallCategories(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from categories order by name"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails

	def getallCoupons(self):
		db = connect_to_cloudsql()
		cursor = db.cursor()
		sqlcmd = "select * from coupons"
		print sqlcmd
		cursor.execute(sqlcmd)
		dbDetails = []
		for row in cursor.fetchall():
			dbDetails.append(row)
		db.commit()
		db.close()
		print 'dbDetails', dbDetails
		return dbDetails
