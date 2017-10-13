# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class TrainingProgram(Document):
	pass

def set_missing_values(source, target):
	target.run_method("set_missing_values")

@frappe.whitelist()
def make_training_event(source_name, target_doc=None):
	#Returns a Training Event based on parent Training Program Fields
	doc = get_mapped_doc("Training Program", source_name, {
		"Training Program": {
			"doctype": "Training Event",
			"field_map": {
				"training_program": "training_program"
			},
			"validation": {
				"docstatus": ["!=", 2],
			}
		},
	}, target_doc, set_missing_values)

	return doc
