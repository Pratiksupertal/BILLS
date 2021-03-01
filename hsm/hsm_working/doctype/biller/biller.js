// Copyright (c) 2020, Pratik Mane and contributors
// For license information, please see license.txt

frappe.ui.form.on('Biller', {
	// refresh: function(frm) {
  po_number: function(frm){
    frappe.call({
			method: "hsm.hsm_working.doctype.biller.biller.make_biller",
      args:{
        po_number: frm.doc.po_number
      },
      callback:function(r){
        for (var row in r.message.po_structure){
        }
        frm.clear_table("billing_details")
				frm.refresh_fields('billing_details');
				$.each(r.message.po_structure, function(idx, item_row){
					var row = frm.add_child("billing_details");
					row.particulars = item_row['particulars']
					row.rate = item_row['rate']
					frm.refresh_fields('billing_details');
				});
      }
		})
  },
  validate:function(frm){
    frm.set_value("amount_in_words", "");
    frappe.call({
    	method: "hsm.hsm_working.doctype.biller.biller.number_to_word",
      args:{
        amount: frm.doc.total_amount
      },
      callback:function(r){
        frm.set_value("amount_in_words", (r.message));
        frm.set_df_property('cgst', 'read_only', 1);
      }
    })
  },
  billing_amount:function(frm){
    frm.set_value("cgst", (frm.doc.billing_amount*0.09));
    frm.set_value("sgst", (frm.doc.billing_amount*0.09));
    frm.set_df_property('cgst', 'read_only', 1);
    frm.set_df_property('sgst', 'read_only', 1);
    frm.set_value("total_amount", (frm.doc.billing_amount+frm.doc.cgst+frm.doc.sgst));
    frm.set_df_property('total_amount', 'read_only', 1);
  },
  reset_calculation:function(frm){
    frm.set_value("billing_amount", 0);

  }
	// }
});
frappe.ui.form.on("Billing Details", {
  qty:function(frm,cdt,cdn){
    var row = locals[cdt][cdn]
    frappe.model.set_value(cdt,cdn, 'amount',row.qty*row.rate);
    var bill_amount = row.amount + frm.doc.billing_amount
    frm.refresh_field("billing_amount");
    frm.set_value("billing_amount", bill_amount);

  }
});
cur_frm.fields_dict['po_number'].get_query = function(doc) {
  var filters = [['Purchase Order','is_active', '=', 1] ]
  if(doc.partner_company){
    filters.push(['Purchase Order','partner_company', '=', doc.partner_company])
  }
  return {
		filters:filters
	}
}
cur_frm.fields_dict['header'].get_query = function(doc) {
  if(doc.po_number){
    var filters = []
    filters.push(['Bill Header','po_number', '=', doc.po_number])
    return {
      filters:filters
    }
  }
}
