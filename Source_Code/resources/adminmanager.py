from flask import current_app, Flask, render_template, request
from flask.json import jsonify
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from datetime import datetime
from models.models import db, PostModel, DonationPostModel,TripPostModel 
from models.models import Report
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel

import os

getReportResource={
    "reporterId":fields.Integer,
    "reporteeId":fields.Integer,
    "reason":fields.Integer
}

# this method gets all of the reports so that admins can see them in their 
# homepage and resolve them

class getReportsResource(Resource):
    #@marshal_with()
    def get(self):
        reports = Report.query.all()
    
    # Convert reports to JSON
        combined_data=[]
        for report in reports:
            jsonn={
                "reporterId":report.reporterId,
                "reporteeId":report.reporteeId,
                "reason":report.reason
                }
            combined_data.append(jsonn)
    
        return combined_data