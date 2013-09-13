# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Enterprise Management Solution
#    risk_management Module
#    Copyright (C) 2011 ValueDecision Ltd (<http://www.valuedecision.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################
from openerp.osv import osv, fields
from datetime import date

class risk_management_risk_category (osv.osv):
    _name = 'risk.management.category'
    _description = 'Risk log category table'
    
    _columns= {
        'name': fields.char('Risk Category',64, required=True)
    }
risk_management_risk_category()

class risk_management_risk_response_category (osv.osv):
    _name = 'risk.management.response.category'
    _description = 'Risk log response category table'
    
    _columns= {
        'type': fields.selection([('threat','Threat'),('opportunity','Opportunity')],'Type'),       
        'name': fields.char('Response Category',64, required=True)
    }
risk_management_risk_response_category()

class risk_management_proximity (osv.osv):
    _name = 'risk.management.proximity'
    _description = 'Risk log proximity table'
    
    _columns= {
        'name': fields.char('Proximity',64, required=True)
    }
risk_management_proximity()

class risk_management_risk (osv.osv):
    _name = 'risk.management.risk'
    _description = 'Risk log table'
    
    def _calculate_expected_inherent_value(self, cr, uid, ids, field_name, arg, context={}):
        ret = {}
        for risk in self.browse(cr, uid, ids):
            ret[risk.id] = risk.impact_inherent * risk.probability_inherent  
        return ret
    
    def _calculate_expected_residual_value(self, cr, uid, ids, field_name, arg, context={}):
        ret = {}
        for risk in self.browse(cr, uid, ids, context=context):
            ret[risk.id] = risk.impact_residual * risk.probability_residual  
        return ret
    
    def set_state_draft(self,cr, uid, id, context=None):
        return self.write(cr,uid,id, {'state' : 'draft'})

    def set_state_active(self,cr, uid, id, context=None):
        return self.write(cr,uid,id, {'state' : 'active'})
    
    def set_state_closed(self,cr, uid, id, context=None):
        return self.write(cr,uid,id, {'state' : 'closed'})
    
    _columns = {
        'name': fields.char('Risk Id', size=64, required=True,
            readonly=True, states={'draft': [('readonly', False)]}, select=True, help="Risk label. Can be changed as long as risk is in state 'draft'."),
        'description': fields.char('Risk Description',64, help="Short description of the Risk."),
        'project_id': fields.many2one('project.project', 'Project', required=True),
        'author_id': fields.many2one('res.users','Author', required=True),
        'date_registered': fields.date('Date Registered', required=True, help="Date of the Risk registered. Auto populated."),
        'date_modified': fields.date('Date Modified', help="Date of last update."),
        'risk_category_id': fields.many2one('risk.management.category','Risk Category', required=True, help="Risk Category: The type of risk in terms of the project's or business' chosen categories (e.g. Schedule, quality, legal etc.)"),
        'description_cause': fields.text('Cause'),
        'description_event': fields.text('Event'),
        'description_effect': fields.text('Effect'),
        'impact_inherent': fields.integer('Inherent Impact', required=True, help="Impact: The result of a particular threat or opportunity actually occurring, or the anticipation of such a result. This is the pre-response value, common used scales are 1 to 10 or 1 to 100."),
        'impact_residual': fields.integer('Residual Impact', required=True, help="Impact: The result of a particular threat or opportunity actually occurring, or the anticipation of such a result. This is the post-response value, common used scales are 1 to 10 or 1 to 100."),
        'probability_inherent': fields.integer('Inherent Probability', required=True, help="Probability: The evaluated likelihood of a particular threat or opportunity actually happening, including a consideration of the frequency with which this may arise. This is the pre-response value, common used scales are 1 to 10 or 1 to 100."),
        'probability_residual': fields.integer('Residual Probability', required=True, help="Probability: The evaluated likelihood of a particular threat or opportunity actually happening, including a consideration of the frequency with which this may arise. This is the post-response value, common used scales are 1 to 10 or 1 to 100."),
        'expected_value_inherent': fields.function(_calculate_expected_inherent_value, method=True, string='Expected Inherent Value', store=True, help="Expected Value. Cost of inherent impact * inherent probability. This is the pre-response value."),
        'expected_value_residual': fields.function(_calculate_expected_residual_value, method=True, string='Expected Residual Value', store=True, help="Expected Value. Cost of residual impact * residual probability. This is the post-response value."),
        'proximity_id': fields.many2one('risk.management.proximity','Proximity', help="Proximity: This would typically state how close to the present time the risk event is anticipated to happen (e.g. for project risks Imminent, within stage, within project, beyond project).  Proximity should be recorded in accordance with the project's chosen scales or business continuity time scales."),
        'risk_response_category_id': fields.many2one('risk.management.response.category','Response Category', help="Risk Response Categories: How the project will treat the risk in terms of the project's (or business continuity planning) chosen categories."),
        'risk_response_ids': fields.one2many('project.task','risk_id','Response Ids'),
        'state': fields.selection([('draft','Draft'),('active','Active'),('closed','Closed')],'State', readonly=True, help="A risk can have one of these three states: draft, active, closed."),
        'risk_owner_id': fields.many2one('res.users','Owner', help="Risk Owner: The person responsible for managing the risk (there can be only one risk owner per risk), risk ownership is assigned to a managerial level, in case of business continuity to a C-level manager."),
    }
    _defaults = {
        'author_id': lambda obj,cr,uid,context: uid,                 
        'date_registered': lambda *a: date.today().strftime('%Y-%m-%d'),
        'state': 'draft',
        'name': lambda obj,cr,uid,context: obj.pool.get('ir.sequence').get(cr, uid, 'risk.management.risk')
}
risk_management_risk()