# resources/markfounditempostresource.py
from flask import current_app
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.models import db, MarkFoundItemPostModel, FoundItemPostModel, UserModel

mark_found_item_post_args = reqparse.RequestParser()
mark_found_item_post_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
mark_found_item_post_args.add_argument('user_id', type=int, required=True, help='User ID is required')

mark_found_item_post_resource_fields = {
    'post_id': fields.Integer,
    'user_id': fields.Integer,
}

class MarkFoundItemPostResource(Resource):

    @marshal_with(mark_found_item_post_resource_fields)
    def post(self):
        args = mark_found_item_post_args.parse_args()
        post_id = args['post_id']
        user_id = args['user_id']

        # Check if post_id exists in FoundItemPostModel
        found_item_post = FoundItemPostModel.query.get(post_id)
        if not found_item_post:
            abort(404, message='Found Item Post not found')

        # Check if user_id exists in UserModel
        user = UserModel.query.get(user_id)
        if not user:
            abort(404, message='User not found')

        # Create a new marked found item post
        marked_found_item_post = MarkFoundItemPostModel(
            post_id=post_id,
            user_id=user_id
        )

        # Add and commit the new marked found item post to the database
        with current_app.app_context():
            db.session.add(marked_found_item_post)
            db.session.commit()

        return marked_found_item_post, 201
