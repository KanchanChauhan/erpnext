// Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Training Program', {
	refresh: function(frm) {
		if(frm.doc.status == 'Scheduled') {
			frm.add_custom_button(__("Training Event"), function () {
				frm.trigger('make_training_event');
			});
		}
	},
	make_training_event: function() {
		frappe.model.open_mapped_doc({
			method: "erpnext.hr.doctype.training_program.training_program.make_training_event",
			frm: cur_frm
		});
	},
});
