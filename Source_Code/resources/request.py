from flask import current_app
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models.models import db, FollowRequest, ChatRequest

follow_request_post_args = reqparse.RequestParser()
follow_request_post_args.add_argument('request_id', type=int, required=True, help='Request ID is required')
follow_request_post_args.add_argument('pending', type=bool, required=True, help='Pending status is required')

chat_request_post_args = reqparse.RequestParser()
chat_request_post_args.add_argument('id', type=int, required=True, help='ID is required')
chat_request_post_args.add_argument('message', type=str, required=True, help='Message is required')
chat_request_post_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

follow_request_resource_fields = {
    'request_id': fields.Integer,
    'pending': fields.Boolean,
}

chat_request_resource_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'post_id': fields.Integer,
}

class FollowRequestResource(Resource):

    @marshal_with(follow_request_resource_fields)
    def post(self):
        args = follow_request_post_args.parse_args()

        new_follow_request = FollowRequest(
            request_id=args['request_id'],
            pending=args['pending']
        )

        with current_app.app_context():
            db.session.add(new_follow_request)
            db.session.commit()

        return new_follow_request, 201

    def delete(self):
        args = follow_request_post_args.parse_args()
        request_id = args['request_id']

        follow_request = FollowRequest.query.get(request_id)
        if not follow_request:
            abort(404, message='Follow request not found')

        with current_app.app_context():
            db.session.delete(follow_request)
            db.session.commit()

        return {'message': 'Follow request deleted successfully'}, 204


class ChatRequestResource(Resource):

    @marshal_with(chat_request_resource_fields)
    def post(self):
        args = chat_request_post_args.parse_args()

        new_chat_request = ChatRequest(
            id=args['id'],
            message=args['message'],
            post_id=args['post_id']
        )

        with current_app.app_context():
            db.session.add(new_chat_request)
            db.session.commit()

        return new_chat_request, 201

    def delete(self):
        args = chat_request_post_args.parse_args()
        id = args['id']

        chat_request = ChatRequest.query.get(id)
        if not chat_request:
            abort(404, message='Chat request not found')

        with current_app.app_context():
            db.session.delete(chat_request)
            db.session.commit()

        return {'message': 'Chat request deleted successfully'}, 204
