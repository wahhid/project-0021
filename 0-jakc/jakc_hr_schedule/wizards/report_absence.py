import time
from openerp.osv import osv, fields


class AbsenceDetails(osv.osv_memory):
    _name = 'absence.details'
    _description = 'Absence Details'

    _columns = {
        'date_start': fields.date('Date Start', required=True),
        'date_end': fields.date('Date End', required=True),
        'employee_ids': fields.many2many('hr.employee', 'absence_details_report_employee_rel', 'employee_id', 'wizard_id', 'Employees'),
    }

    def print_report(self, cr, uid, ids, context=None):
        print "Print Absence Detail"
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, ['date_start', 'date_end', 'employee_ids'], context=context)
        res = res and res[0] or {}
        datas['form'] = res
        if res.get('id', False):
            datas['ids'] = [res['id']]

        return self.pool['report'].get_action(cr, uid, [], 'jakc_hr_schedule.report_absencedetails', data=datas, context=context)