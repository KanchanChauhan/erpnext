# Copyright (c) 2017, Frappe and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.reload_doctype('Training Event')

	training_events = frappe.get_all("Training Event", fields = ["*"])
	for training_event in training_events:
		if not frappe.db.get_value("Training Program", training_event.name):
			training_doc = frappe.new_doc("Training Program")
			training_doc.training_name = training_event.event_name
			training_doc.trainer_name = training_event.trainer_name
			training_doc.trainer_email = training_event.trainer_email
			training_doc.supplier = training_event.supplier
			training_doc.contact_number = training_event.contact_number
			training_doc.save(ignore_permissions=True)
			training_doc.submit()
		
		if not training_event.training:
			frappe.db.set_value("Training Event", training_event.name,
				"training", training_event.event_name, update_modified=False)