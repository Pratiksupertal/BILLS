# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pratik Mane and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import hsm.utils
from frappe.utils import cint, flt
from hsm.hsm_working.doctype.biller.digit import Digit
# from hsm_working.doctype.biller.digit import digit

class Biller(Document):
	def po_number(doc,method):
		pass


@frappe.whitelist()
def make_biller(po_number=None):
	return frappe.get_doc("Purchase Order", po_number)

@frappe.whitelist()
def number_to_word(amount):
	num = Digit()
	integer = int(amount)
	num_to_word = num.guess(round(integer))
	return num_to_word
	pass
