# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document
from frappe.utils import flt

class Routing(Document):
	def validate(self):
		self.validate_base_hour_rate()

	def validate_base_hour_rate(self):
		for r in self.routing_details:
			r.base_hour_rate = flt(r.hour_rate) * flt(self.conversion_rate)