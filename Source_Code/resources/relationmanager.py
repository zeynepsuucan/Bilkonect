from flask import current_app
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models.models import db, UserModel, BlockedUserModel, Report, FollowedUserModel, Notification, FavouritePostModel
from datetime import datetime

block_args = reqparse.RequestParser()
block_args.add_argument('blocker_username', type=str, required=True, help='blocker id is required')
block_args.add_argument('blocked_username', type=str, required=True, help='blocked is required')

follow_args = reqparse.RequestParser()
follow_args.add_argument('follower_name', type=str, required=True, help='follower name is required')
follow_args.add_argument('followed_name', type=str, required=True, help='followed name required')

user_resource_fields = {
    'blocker_username': fields.String, 
    'blocked_username': fields.String,
}

follow_user_resource_fields = {
    'follower_name': fields.String, 
    'followed_name': fields.String,
}

check_resource_fields = {
    'follows': fields.String
}

report_post_args = reqparse.RequestParser()
report_post_args.add_argument('reporterId', type=int, required=True, help='Reporter ID is required')
report_post_args.add_argument('reporteeId', type=int, required=True, help='Reportee ID is required')
report_post_args.add_argument('reason', type=str, required=True, help='Reason is required')

report_delete_args = reqparse.RequestParser()
report_delete_args.add_argument('id', type=int, required=True, help='Post ID is required')

report_resource_fields = {
    'reporterId': fields.Integer,
    'reporteeId': fields.Integer,
    'reason': fields.String,
    'date': fields.String
}

check_post_args = reqparse.RequestParser()
check_post_args.add_argument('followerName', type=str, required=True, help='Followed ID is required')
check_post_args.add_argument('followedName', type=str, required=True, help='Follower ID is required')

fav_resource_fields = {
    'fav_username': fields.String,
    'fav_post_id': fields.Integer,
}

fav_args = reqparse.RequestParser()
fav_args.add_argument('fav_username', type=str, required=True, help='fav username is required')
fav_args.add_argument('fav_post_id', type=int, required=True, help='fav post id is required')

class CheckFollowRelation(Resource):
    @marshal_with(check_resource_fields)
    def post(self):
        args = check_post_args.parse_args()
        our_user = UserModel.query.filter_by(username=args['followerName']).first()
        all_follows = FollowedUserModel.query.filter_by(followed_name=args['followedName']).all()

        follows = False  # Default value

        if all_follows:
            for follow in all_follows:
                if follow.followed_name == args['followedName']:
                    follows = True
                    break  # No need to continue checking if found

        return {'follows': str(follows)}  # Convert to string as specified in your resource fields

class FollowResource(Resource):
    @marshal_with(follow_user_resource_fields)
    def post(self):
        args = follow_args.parse_args()

        follower_user = UserModel.query.filter_by(username=args['follower_name']).first()
        followed_user = UserModel.query.filter_by(username=args['followed_name']).first()

        if follower_user and followed_user:
            # Update counts
            follower_user.following += 1
            followed_user.followers += 1

            # Create a new follow entry
            new_follow = FollowedUserModel(
                follower_name=args['follower_name'],
                followed_name=args['followed_name'],
            )

            # Create a new notification
            new_notification = Notification(
                ownerName=followed_user.username,  # Assuming ownerName is a foreign key
                message=f"{follower_user.username} has followed you."
            )

            # Commit changes to the database
            with current_app.app_context():
                db.session.add(new_notification)
                db.session.add(new_follow)
                db.session.commit()

            return new_follow, 201
        else:
            # Handle case where user not found
            return {'message': 'User not found'}, 404

    @marshal_with(user_resource_fields)
    def delete(self):
        args = follow_args.parse_args()
        follower_name = args['follower_name']
        followed_name = args['followed_name']

        # Find the follow relation
        follow = FollowedUserModel.query.filter_by(follower_name=follower_name, followed_name=followed_name).first()
        
        if not follow:
            # Handle case where follow relation not found
            return {'message': 'Follow relation does not exist'}, 404

        with current_app.app_context():
            # Delete the follow relation
            db.session.delete(follow)
            db.session.commit()

            follower_user = UserModel.query.filter_by(username=follower_name).first()
            followed_user = UserModel.query.filter_by(username=followed_name).first()

            if follower_user and followed_user:
                # Update counts
                follower_user.following -= 1
                followed_user.followers -= 1

                # Commit changes to the database
                db.session.commit()

        return {'message': 'Follow relation deleted successfully'}, 204

class BlockResource(Resource):
    @marshal_with(user_resource_fields)
    def post(self):
        args = block_args.parse_args()
        
        new_block = BlockedUserModel(
            blocker_username=args['blocker_username'],
            blocked_username=args['blocked_username'],
        )
        # blocking_user = UserModel.query.filter_by(username=new_block.blocker_username).first()
        
        # blocked_user = UserModel.query.filter_by(username=new_block.blocked_username).first()
        
        # if blocking_user:
        #     follow = FollowedUserModel.query.filter_by(follower_name=new_block.blocker_username,followed_name=new_block.blocked_username).first()
        #    # print("3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #     print(follow)
        #     if follow:
        #         print("4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                
        #         db.session.delete(follow)
        #         db.session.commit()
        #     print("5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        db.session.add(new_block)
        db.session.commit()

        return new_block, 201
    
    @marshal_with(user_resource_fields)
    def delete(self):
        args = block_args.parse_args()
        blocker_username = args['blocker_username']
        blocked_username = args['blocked_username']

        block = BlockedUserModel.query.filter_by(blocker_username=blocker_username, blocked_username=blocked_username).first()
        if not block:
            abort(404, message='block does not exist')
        
        with current_app.app_context():
            db.session.delete(block)
            db.session.commit()

        return{'message': 'Block deleted successfully'}, 204

class ReportResource(Resource):

    @marshal_with(report_resource_fields)
    def post(self):
        args = report_post_args.parse_args()


        # Create a new post
        new_report = Report(
            reporterId=args['reporterId'],
            reporteeId=args['reporteeId'],
            reason=args['reason']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_report)
            db.session.commit()

        return new_report, 201
    
    def delete(self):
        args = report_delete_args.parse_args()
        id = args['id']

        # Check if the donation post exists
        report = Report.query.get(id)
        if not report:
            abort(404, message='Report not found')

        # Get the associated post
        report = Report.query.get(id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(report)
            db.session.commit()

        return {'message': 'Report deleted successfully'}, 204

class FavouriteResource(Resource):
    @marshal_with(fav_resource_fields)
    def post(self):
        args = fav_args.parse_args()
        new_fav = FavouritePostModel(
            fav_username = args['fav_username'],
            fav_post_id = args['fav_post_id'],
        )
        db.session.add(new_fav)
        db.session.commit()

        return new_fav, 201
    
    @marshal_with(fav_resource_fields)
    def delete(self):
        args = fav_args.parse_args()
        fav_username = args['fav_username']
        fav_post_id = args['fav_post_id']
        fav = FavouritePostModel.query.filter_by(fav_username=fav_username,fav_post_id=fav_post_id)
        if not fav:
            abort(404, message='fav does not exist')
        
        with current_app.app_context():
            db.session.delete(fav)
            db.session.commit()

        return{'message': 'Fav deleted successfully'}, 204