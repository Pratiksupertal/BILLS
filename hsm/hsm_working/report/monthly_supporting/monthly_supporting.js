// Copyright (c) 2016, Pratik Mane and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Monthly Supporting"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"options": '',
			"default": ""
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"options": '',
			"default": ""
		},
		{
			"fieldname":"month",
			"label": __("Month"),
			"fieldtype": "Data",
			"options": '',
			// "hidden": 1
		}
	]
};
