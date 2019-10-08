from odoo import http
from odoo.http import request
import plotly as py
import plotly.graph_objs as go

class send_view(http.Controller):

    @http.route("/issues/analysis", auth='user')
    def send_view(self,**kwargs):
        Issue = request.env['issue_new.model']
        new_stat = len(Issue.search([('stage_id', '=', 'New')]))
        pending_stat = len(Issue.search([('stage_id', '=', 'Pending')]))
        solved_stat = len(Issue.search([('stage_id', '=', 'Solved')]))

        data = [go.Bar(x=["New", "Pending", "Solved"], y=[new_stat, pending_stat, solved_stat])]
        result1 = py.offline.plot(data, include_plotlyjs=False, output_type='div')

        lis = [person.salesperson.name for person in Issue.search([])]
        listy = {pers: lis.count(pers) for pers in lis}

        res = [go.Bar(x=[person for person in listy.keys()], y=[value for value in listy.values()])]
        result2 = py.offline.plot(res, include_plotlyjs=False, output_type='div')

        return request.render('issue.show',{'result1':'result1','result2':'result2'})
