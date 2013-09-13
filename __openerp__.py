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
{
    'name': 'Risk Management',
    'version': '2.0',
    'author': 'Tactix4 Ltd',
    'website': 'http://www.tactix4.com',
    'category': 'Project Management',
    'description': """
       This module allows to manage risk in at least two different contexts
       Project Management
       Business Continuity Planning
       
       A risk is always associated with a project and has an impact and probability assessment pre- and post-response with resulting expected values (scores).
       Actions on risk are tasks, which can be identified easily in the extended task view via the 'Action on Risk' button and associated risk id.
       
       Risk categories, response categories and proximity are set-up according to the PRINCE2 project methodology.
       They are easily changed via the 'Configuration' menu to get them in accordance with Business Continuity Planning, PIP, SCRUM or DSDM.
       
       Besides the above mentioned information the following information can and ought to be documented as well:
       Risk description, author, date registered, date modified, event, effect, cause and risk owner.
       
       A graphical view to get an overview of the risks based on the expected values (scores) is included as well.
        
       More information can be found on our website: http://valuedecision.com
       
    """,
    'depends': ['project'],
    'update_xml':['risk_management_data.xml',
                  'risk_management_sequence.xml',
                  'view/risk_management_view.xml',
                  'view/risk_management_category_view.xml',
                  'view/risk_management_category_response_view.xml',
                  'view/risk_management_proximity_view.xml',
                  'view/risk_management_menus.xml',
                  'view/project_task_view.xml',
                  'security/risk_management_security.xml',
                  'security/ir.model.access.csv'], 
    'demo': ['risk_management_demo.xml'],
    'test': ['test/test_risk_management.yml'],
    'installable': True,
    'application': True,
    'images': ['images/Risk_Action.jpg','images/Risk_Score.jpg','Task_Action_on_Risk.jpg'],
    'active': False,
}

