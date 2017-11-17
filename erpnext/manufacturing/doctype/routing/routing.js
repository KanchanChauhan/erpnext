// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Routing', {
	currency: function(frm) {
		var company_currency = erpnext.get_currency(frm.doc.company)
		if(frm.doc.currency === company_currency) {
			frm.set_value("conversion_rate", 1.0);
		};
		if(frm.doc.currency && frm.doc.currency !== company_currency) {
			return frappe.call({
				method: "erpnext.setup.utils.get_exchange_rate",
				args: {
					from_currency: frm.doc.currency,
					to_currency: company_currency
				},
				callback: function(r) {
					frm.set_value("conversion_rate", flt(r.message));
					frm.set_df_property("conversion_rate", "description", "1 " + frm.doc.currency
					+ " = [?] " + company_currency);
				}
			});
		};
	}
});