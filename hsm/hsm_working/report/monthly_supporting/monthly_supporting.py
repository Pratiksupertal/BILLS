# Copyright (c) 2013, Govt and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import datetime
def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_data(filters):
	query_data = frappe.db.sql("""
		select working_date,sum(qty) AS qty from `tabMonthly Working` {} group by working_date;
			""".format(validate_filters(filters)))
	return query_data

def validate_filters(filters):
	conditions = ' where 1 = 1'
	# if filters.get('BDC'):
	# 	conditions += " and SI.supplier_bdc = '{0}'".format(filters.get('BDC'))
	if filters.get("from_date"):
		date = datetime.datetime.strptime(filters.get("from_date"), "%Y-%m-%d")
		month =date.strftime("%b %Y")
		filters["month"]=month
		print('-----------------------------------------------')
		print(month)
		print('-----------------------------------------------')
		conditions += " and working_date >= '{0}'".format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions += " and working_date <= '{0}'".format(filters.get("to_date"))

	return conditions

def get_columns():

	return [
		{
			"fieldname": "working_date",
			"label": _("Working Date"),
			"fieldtype": "Date",
			"options": "",
			"width": 100
		},
		{
			"fieldname": "qty",
			"label": _("Quontity"),
			"fieldtype": "Int",
			"options": "",
			"width": 80
		}

	]
