# -*- coding: utf-8 -*-
from flectra import api, fields, models
from flectra.addons.studentmanagementsystem.models import student_course
from flectra.addons.studentmanagementsystem.models.student_course import StudentCourse


class StudPartner(models.Model):
    _inherit = 'studentcourse.details'

    student_id = fields.Many2one("student.details", string="Student", required=True)
    total_course1 = fields.Integer(string="Total Course11", readonly=True)
    graduation = fields.Selection([('ssc', 'ssc'),
                                   ('hsc', 'hsc')], string="Enter your graduation ")

    @api.multi
    def count_total_course(self):
        super(StudPartner, self).count_total_course()
        print("total students-------", len(self))
        self.total_course1 = len(self.course_ids)*2


    @api.onchange('student_id')
    def onchage_student_id(self):
        print("------student gradution", self.student_id)
        self.graduation = self.student_id.graduation
        self.description = False



#    website = fields.Char(string="website",required=True)
#    passed_override_write_function = fields.Boolean(string='Has passed our super method')
#    sale_order_count = fields.Integer(compute='_compute_sale_order_count', string='# of Sales Order')
#    course_name = fields.Char(string="Enter course Name")

#    passed_override_write_function = fields.Boolean(string='Has passed our super method')
"""
    @api.model
    def create(self, values):
        if 'is_student' in values:
            values['is_student']=values['is_student'].upper()
            new_value = super(ResPartner, self).create(values)
        return new_value
"""
"""
    @api.model
    def _compute_sale_order_count(self, values):
        res = super(ResPartner, self)._compute_sale_order_count(values)
        res['passed_override_write_function'] = True
        print
        'Passed this function. passed_override_write_function value: ' + str(res['passed_override_write_function'])
        return res

"""
