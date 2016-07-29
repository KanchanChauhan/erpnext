# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Salary Structure')

class TestSalaryStructure(unittest.TestCase):
	def setUp(self):
	self.make_employee("test_employee@salarystructure.com")
	self.make_salary_component()
	
	def make_employee(self, user):
		if not frappe.db.get_value("User", user):
			frappe.get_doc({
				"doctype": "User",
				"email": user,
				"first_name": user,
				"new_password": "password",
				"user_roles": [{"doctype": "UserRole", "role": "Employee"}]
			}).insert()

		if not frappe.db.get_value("Employee", {"user_id": user}):
			frappe.get_doc({
				"doctype": "Employee",
				"naming_series": "T-Employee-",
				"employee_name": user,
				"company": frappe.db.get_value("Company", {"user_id": user}),
				"user_id": user,
				"date_of_birth": "1990-05-08",
				"date_of_joining": "2013-01-01",
				"department": "Test Department 1",
				"gender": "Female",
				"company_email": user,
				"status": "Active"
			}).insert()
	
	def make_salary_component(self):
		salary_components = ["Basic Salary", "Allowance", "HRA", "Professional Tax", "TDS"]
		for salary_component in salary_components:
			if not frappe.db.exists('Salary Component', salary_component):
				sal_comp = frappe.get_doc({
					"doctype": "Salary Component",
					"salary_component": salary_component
				})
				sal_comp.insert()
				
				