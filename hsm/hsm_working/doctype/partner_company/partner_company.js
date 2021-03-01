// Copyright (c) 2020, Pratik Mane and contributors
// For license information, please see license.txt

frappe.ui.form.on('Partner Company', {
	// refresh: function(frm) {

	// }
  validate: function(frm){
    frm.refresh();
  }
});
