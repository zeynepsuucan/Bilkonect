from flask import current_app
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models.models import db, Notification
from datetime import datetime

# Separate argument parsers for different methods
notification_args = reqparse.RequestParser()
notification_args.add_argument('ownerId', type=int, required=True, help='Owner ID is required')
notification_args.add_argument('message', type=str, required=True, help='Message is required')
notification_args.add_argument('date', type=str, required=True, help='Date is required')

notification_delete_args = reqparse.RequestParser()
notification_delete_args.add_argument('id', type=int, required=True, help='Notification ID is required')

report_resource_fields = {
    'ownerId': fields.Integer,
    'message': fields.String,
    'date': fields.String
}

class NotificationResource(Resource):

    @marshal_with(report_resource_fields)
    def post(self):
        args = notification_args.parse_args()

        # Convert share_date string to datetime
        date = datetime.strptime(args['date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new notification
        new_notification = Notification(
            ownerId=args['ownerId'],
            message=args['message'],
            date=date
        )

        # Add and commit the new notification to the database
        with current_app.app_context():
            db.session.add(new_notification)
            db.session.commit()

        return new_notification, 201
    
    def delete(self):
        args = notification_delete_args.parse_args()
        id = args['id']

        # Check if the donation notification exists
        notification = Notification.query.get(id)
        if not notification:
            abort(404, message='Report not found')

        # Get the associated notification
        notification = Notification.query.get(id)

        # Delete the notification
        with current_app.app_context():
            db.session.delete(notification)
            db.session.commit()

        return {'message': 'Notification deleted successfully'}, 204