	frappe.pages['monthly_work'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Monthly Work',
		single_column: true
	});
	controller = new frappe.monthly_work(wrapper);
}
frappe.monthly_work = Class.extend({
	init : function(wrapper){
		var me = this;
    me.wrapper_page = wrapper.page
		// '.layout-main-section-wrapper' class for blank dashboard page
		// this.page = $(wrapper).find('.layout-main-section-wrapper');
		this.page = $(wrapper).find('.layout-main-section-wrapper');
		$(frappe.render_template('monthly_work')).appendTo(this.page);
	},
});
