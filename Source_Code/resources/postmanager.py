from flask import current_app, Flask, render_template, request
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from datetime import datetime
from models.models import db, PostModel, DonationPostModel,TripPostModel 
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel
import os

app = Flask(__name__)

#course material resource to post, edit and delete course material
course_material_post_post_args = reqparse.RequestParser()
course_material_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
course_material_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
course_material_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
course_material_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
course_material_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
course_material_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
course_material_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
course_material_post_post_args.add_argument('course', type=str, required=False, help='Course is required')

course_material_post_put_args = reqparse.RequestParser()
course_material_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
course_material_post_put_args.add_argument('title', type=str, required=False)
course_material_post_put_args.add_argument('description', type=str, required=False)
course_material_post_put_args.add_argument('post_type', type=str, required=False)
course_material_post_put_args.add_argument('is_archived', type=bool, required=False)
course_material_post_put_args.add_argument('share_date', type=str, required=False)
course_material_post_put_args.add_argument('criteria', type=str, required=False)
course_material_post_put_args.add_argument('owner', type=str, required=False)
course_material_post_put_args.add_argument('course', type=str, required=False)

course_material_post_delete_args = reqparse.RequestParser()
course_material_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

course_material_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'course': fields.String,
}

class CourseMaterialPostResource(Resource):

    @marshal_with(course_material_post_resource_fields)
    def post(self):
        args = course_material_post_post_args.parse_args()

        # Check if the post_type is CourseMaterialPost
        if args['post_type'].lower() != 'coursematerialpost':
            abort(400, message='Invalid post_type. Must be CourseMaterialPost.')

        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new course material post using the post_id from the new post
        new_course_material_post = CourseMaterialPostModel(
            post_id=new_post.post_id,
            course="CS IS BAD"
        )

        # Add and commit the new course material post to the database
        with current_app.app_context():
            db.session.add(new_course_material_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(course_material_post_resource_fields)
    def put(self):
        args = course_material_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the course material post exists
        course_material_post = CourseMaterialPostModel.query.get(post_id)
        if not course_material_post:
            abort(404, message='Course material post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['course'] is not None:
            course_material_post.course = args['course']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the course material post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = course_material_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the course material post exists
        course_material_post = CourseMaterialPostModel.query.get(post_id)
        if not course_material_post:
            abort(404, message='Course material post not found')

        # Delete the course material post from the database
        with current_app.app_context():
            db.session.delete(course_material_post)
            db.session.commit()

        return {'message': 'Course material post deleted successfully'}, 204







# donation post type to post, edit and delete
    
# Separate argument parsers for different methods
donation_post_post_args = reqparse.RequestParser()
donation_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
donation_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
donation_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
donation_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
donation_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
donation_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
donation_post_post_args.add_argument('image', type=str, required=True, help='Image URL is required')
donation_post_post_args.add_argument('isDonated', type=bool, default=False, help='Is donated (default: False)')
donation_post_post_args.add_argument('isNegotiated', type=bool, default=False, help='Is negotiated (default: False)')

donation_post_put_args = reqparse.RequestParser()
donation_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
donation_post_put_args.add_argument('title', type=str, required=False)
donation_post_put_args.add_argument('description', type=str, required=False)
donation_post_put_args.add_argument('post_type', type=str, required=False)
donation_post_put_args.add_argument('is_archived', type=bool, required=False)
donation_post_put_args.add_argument('owner', type=str, required=False)
donation_post_put_args.add_argument('criteria', type=str, required=False)
donation_post_put_args.add_argument('share_date', type=str, required=False)
donation_post_put_args.add_argument('image', type=str, required=False)
donation_post_put_args.add_argument('isDonated', type=bool)
donation_post_put_args.add_argument('isNegotiated', type=bool)

donation_post_delete_args = reqparse.RequestParser()
donation_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

donation_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'image': fields.String,
    'isDonated': fields.Boolean,
    'isNegotiated': fields.Boolean,
}

class DonationPostResource(Resource):

    @marshal_with(donation_post_resource_fields)
    def post(self):
        
        args = donation_post_post_args.parse_args()
        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            owner=args['owner'],
            criteria=args['criteria'],
            is_archived=False,
            share_date=share_date
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new donation post using the post_id from the new post
        new_donation_post = DonationPostModel(
            post_id=new_post.post_id,
            image=args['image'],
            isDonated=args['isDonated'],
            isNegotiated=args['isNegotiated']
        )
        
        # Add and commit the new donation post to the database
        with current_app.app_context():
            db.session.add(new_donation_post)
            db.session.commit()

        return new_post, 201
        
    @marshal_with(donation_post_resource_fields)
    def put(self):
        args = donation_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the donation post exists
        donation_post = DonationPostModel.query.get(post_id)
        if not donation_post:
            abort(404, message='Donation post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the donation post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['image'] is not None:
            donation_post.image = args['image']
        if args['isDonated'] is not None:
            donation_post.isDonated = args['isDonated']
        if args['isNegotiated'] is not None:
            donation_post.isNegotiated = args['isNegotiated']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the donation post and post details in the response

        return post_details, 200
    
    def delete(self):
        args = donation_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the donation post exists
        donation_post = DonationPostModel.query.get(post_id)
        if not donation_post:
            abort(404, message='Donation post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(donation_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204






#found item resource to post, edit and delete course material
    
found_item_post_post_args = reqparse.RequestParser()
found_item_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
found_item_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
found_item_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
found_item_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
found_item_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
found_item_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
found_item_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
found_item_post_post_args.add_argument('ownerFound', type=bool, default=False, help='Owner found (default: False)')
found_item_post_post_args.add_argument('image', type=str, required=True, help='Image URL is required')

found_item_post_put_args = reqparse.RequestParser()
found_item_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
found_item_post_put_args.add_argument('title', type=str, required=False)
found_item_post_put_args.add_argument('description', type=str, required=False)
found_item_post_put_args.add_argument('post_type', type=str, required=False)
found_item_post_put_args.add_argument('is_archived', type=bool, required=False)
found_item_post_put_args.add_argument('share_date', type=str, required=False)
found_item_post_put_args.add_argument('criteria', type=str, required=False)
found_item_post_put_args.add_argument('owner', type=str, required=False)
found_item_post_put_args.add_argument('ownerFound', type=bool, required=False)
found_item_post_put_args.add_argument('image', type=str, required=False)

found_item_post_delete_args = reqparse.RequestParser()
found_item_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

found_item_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'ownerFound': fields.Boolean,
    'image': fields.String,
}

class FoundItemPostResource(Resource):

    @marshal_with(found_item_post_resource_fields)
    def post(self):
        args = found_item_post_post_args.parse_args()

        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new found item post using the post_id from the new post
        new_found_item_post = FoundItemPostModel(
            post_id=new_post.post_id,
            ownerFound=args['ownerFound'],
            image=args['image']
        )

        # Add and commit the new found item post to the database
        with current_app.app_context():
            db.session.add(new_found_item_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(found_item_post_resource_fields)
    def put(self):
        args = found_item_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the found item post exists
        found_item_post = FoundItemPostModel.query.get(post_id)
        if not found_item_post:
            abort(404, message='Found item post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['ownerFound'] is not None:
            found_item_post.ownerFound = args['ownerFound']
        if args['image'] is not None:
            found_item_post.image = args['image']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the found item post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = found_item_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the found item post exists
        found_item_post = FoundItemPostModel.query.get(post_id)
        if not found_item_post:
            abort(404, message='Found item post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(found_item_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204






#gym buddy resource to post, edit and delete course material
    

gym_buddy_post_post_args = reqparse.RequestParser()
gym_buddy_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
gym_buddy_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
gym_buddy_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
gym_buddy_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
gym_buddy_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
gym_buddy_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
gym_buddy_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')

gym_buddy_post_put_args = reqparse.RequestParser()
gym_buddy_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
gym_buddy_post_put_args.add_argument('title', type=str, required=False)
gym_buddy_post_put_args.add_argument('description', type=str, required=False)
gym_buddy_post_put_args.add_argument('post_type', type=str, required=False)
gym_buddy_post_put_args.add_argument('is_archived', type=bool, required=False)
gym_buddy_post_put_args.add_argument('share_date', type=str, required=False)
gym_buddy_post_put_args.add_argument('criteria', type=str, required=False)
gym_buddy_post_put_args.add_argument('owner', type=str, required=False)

gym_buddy_post_delete_args = reqparse.RequestParser()
gym_buddy_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

gym_buddy_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
}

class GymBuddyPostResource(Resource):

    @marshal_with(gym_buddy_post_resource_fields)
    def post(self):
        args = gym_buddy_post_post_args.parse_args()

        # Check if the post_type is GymBuddyPost
        if args['post_type'].lower() != 'gymbuddypost':
            abort(400, message='Invalid post_type. Must be GymBuddyPost.')

        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new gym buddy post using the post_id from the new post
        new_gym_buddy_post = GymBuddySearchPostModel(
            post_id=new_post.post_id
        )

        # Add and commit the new gym buddy post to the database
        with current_app.app_context():
            db.session.add(new_gym_buddy_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(gym_buddy_post_resource_fields)
    def put(self):
        args = gym_buddy_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the gym buddy post exists
        gym_buddy_post = GymBuddySearchPostModel.query.get(post_id)
        if not gym_buddy_post:
            abort(404, message='Gym buddy post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the gym buddy post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = gym_buddy_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the gym buddy post exists
        gym_buddy_post = GymBuddySearchPostModel.query.get(post_id)
        if not gym_buddy_post:
            abort(404, message='Gym buddy post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(gym_buddy_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204







#lost item resource to post, edit and delete course material
    

lost_item_post_post_args = reqparse.RequestParser()
lost_item_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
lost_item_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
lost_item_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
lost_item_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
lost_item_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
lost_item_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
lost_item_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
lost_item_post_post_args.add_argument('image', type=str, required=True, help='Image URL is required')
lost_item_post_post_args.add_argument('isFound', type=bool, default=False, help='Is found (default: False)')

lost_item_post_put_args = reqparse.RequestParser()
lost_item_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
lost_item_post_put_args.add_argument('title', type=str, required=False)
lost_item_post_put_args.add_argument('description', type=str, required=False)
lost_item_post_put_args.add_argument('post_type', type=str, required=False)
lost_item_post_put_args.add_argument('is_archived', type=bool, required=False)
lost_item_post_put_args.add_argument('share_date', type=str, required=False)
lost_item_post_put_args.add_argument('criteria', type=str, required=False)
lost_item_post_put_args.add_argument('owner', type=str, required=False)
lost_item_post_put_args.add_argument('image', type=str, required=False)
lost_item_post_put_args.add_argument('isFound', type=bool, required=False)

lost_item_post_delete_args = reqparse.RequestParser()
lost_item_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

lost_item_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'image': fields.String,
    'isFound': fields.Boolean,
}

class LostItemPostResource(Resource):

    @marshal_with(lost_item_post_resource_fields)
    def post(self):
        args = lost_item_post_post_args.parse_args()

        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add the new post to the database
        db.session.add(new_post)

        # Commit the changes to the database
        db.session.commit()

        # Create a new lost item post using the post_id from the new post
        new_lost_item_post = LostItemPostModel(
            post_id=new_post.post_id,
            isFound=args['isFound'],
            image=args['image']
        )

        # Add the new lost item post to the database
        db.session.add(new_lost_item_post)

        # Commit the changes to the database
        db.session.commit()

        return new_post, 201
    
    @marshal_with(lost_item_post_resource_fields)
    def put(self):
        args = lost_item_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the lost item post exists
        lost_item_post = LostItemPostModel.query.get(post_id)
        if not lost_item_post:
            abort(404, message='Lost item post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['isFound'] is not None:
            lost_item_post.isFound = args['isFound']
        if args['image'] is not None:
            lost_item_post.image = args['image']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the lost item post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = lost_item_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the lost item post exists
        lost_item_post = LostItemPostModel.query.get(post_id)
        if not lost_item_post:
            abort(404, message='Lost item post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(lost_item_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204







#need to post, edit and delete course material
    

need_post_post_args = reqparse.RequestParser()
need_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
need_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
need_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
need_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
need_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
need_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
need_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
need_post_post_args.add_argument('foundNeed', type=bool, default=False, help='Found need (default: False)')
need_post_post_args.add_argument('isBorrowed', type=bool, default=False, help='Is borrowed (default: False)')

need_post_put_args = reqparse.RequestParser()
need_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
need_post_put_args.add_argument('title', type=str, required=False)
need_post_put_args.add_argument('description', type=str, required=False)
need_post_put_args.add_argument('post_type', type=str, required=False)
need_post_put_args.add_argument('is_archived', type=bool, required=False)
need_post_put_args.add_argument('share_date', type=str, required=False)
need_post_put_args.add_argument('criteria', type=str, required=False)
need_post_put_args.add_argument('owner', type=str, required=False)
need_post_put_args.add_argument('foundNeed', type=bool, required=False)
need_post_put_args.add_argument('isBorrowed', type=bool, required=False)

need_post_delete_args = reqparse.RequestParser()
need_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

need_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'foundNeed': fields.Boolean,
    'isBorrowed': fields.Boolean,
}

class NeedPostResource(Resource):

    @marshal_with(need_post_resource_fields)
    def post(self):
        args = need_post_post_args.parse_args()

        # Check if the post_type is NeedPost
        if args['post_type'].lower() != 'needpost':
            abort(400, message='Invalid post_type. Must be NeedPost.')

        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new need post using the post_id from the new post
        new_need_post = NeedPostModel(
            post_id=new_post.post_id,
            foundNeed=args['foundNeed'],
            isBorrowed=args['isBorrowed']
        )

        # Add and commit the new need post to the database
        with current_app.app_context():
            db.session.add(new_need_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(need_post_resource_fields)
    def put(self):
        args = need_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the need post exists
        need_post = NeedPostModel.query.get(post_id)
        if not need_post:
            abort(404, message='Need post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['foundNeed'] is not None:
            need_post.foundNeed = args['foundNeed']
        if args['isBorrowed'] is not None:
            need_post.isBorrowed = args['isBorrowed']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the need post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = need_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the need post exists
        need_post = NeedPostModel.query.get(post_id)
        if not need_post:
            abort(404, message='Need post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(need_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204






#roommate resource to post, edit and delete course material
    

roommate_post_post_args = reqparse.RequestParser()
roommate_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
roommate_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
roommate_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
roommate_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
roommate_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
roommate_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
roommate_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')

roommate_post_put_args = reqparse.RequestParser()
roommate_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
roommate_post_put_args.add_argument('title', type=str, required=False)
roommate_post_put_args.add_argument('description', type=str, required=False)
roommate_post_put_args.add_argument('post_type', type=str, required=False)
roommate_post_put_args.add_argument('is_archived', type=bool, required=False)
roommate_post_put_args.add_argument('share_date', type=str, required=False)
roommate_post_put_args.add_argument('criteria', type=str, required=False)
roommate_post_put_args.add_argument('owner', type=str, required=False)

roommate_post_delete_args = reqparse.RequestParser()
roommate_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

roommate_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
}

class RoommatePostResource(Resource):

    @marshal_with(roommate_post_resource_fields)
    def post(self):
        args = roommate_post_post_args.parse_args()

        # Check if the post_type is RoommatePost
        if args['post_type'].lower() != 'roommatepost':
            abort(400, message='Invalid post_type. Must be RoommatePost.')

        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new roommate post using the post_id from the new post
        new_roommate_post = RoommatePostModel(
            post_id=new_post.post_id
        )

        # Add and commit the new roommate post to the database
        with current_app.app_context():
            db.session.add(new_roommate_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(roommate_post_resource_fields)
    def put(self):
        args = roommate_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the roommate post exists
        roommate_post = RoommatePostModel.query.get(post_id)
        if not roommate_post:
            abort(404, message='Roommate post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the roommate post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = roommate_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the roommate post exists
        roommate_post = RoommatePostModel.query.get(post_id)
        if not roommate_post:
            abort(404, message='Roommate post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(roommate_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204







#second hand sale resource to post, edit and delete course material

second_hand_sale_post_post_args = reqparse.RequestParser()
second_hand_sale_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
second_hand_sale_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
second_hand_sale_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
second_hand_sale_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
second_hand_sale_post_post_args.add_argument('share_date', type=str, required=False, help='Share date is required')
second_hand_sale_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
second_hand_sale_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
second_hand_sale_post_post_args.add_argument('price', type=float, required=True, help='Price is required')
second_hand_sale_post_post_args.add_argument('image', type=str, required=True, help='Image URL is required')
second_hand_sale_post_post_args.add_argument('isNegotiated', type=bool, default=False, help='Is negotiated (default: False)')
second_hand_sale_post_post_args.add_argument('isSold', type=bool, default=False, help='Is sold (default: False)')

second_hand_sale_post_put_args = reqparse.RequestParser()
second_hand_sale_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
second_hand_sale_post_put_args.add_argument('title', type=str, required=False)
second_hand_sale_post_put_args.add_argument('description', type=str, required=False)
second_hand_sale_post_put_args.add_argument('post_type', type=str, required=False)
second_hand_sale_post_put_args.add_argument('is_archived', type=bool, required=False)
second_hand_sale_post_put_args.add_argument('share_date', type=str, required=False)
second_hand_sale_post_put_args.add_argument('criteria', type=str, required=False)
second_hand_sale_post_put_args.add_argument('owner', type=str, required=False)
second_hand_sale_post_put_args.add_argument('price', type=float, required=False)
second_hand_sale_post_put_args.add_argument('image', type=str, required=False)
second_hand_sale_post_put_args.add_argument('isNegotiated', type=bool, required=False)
second_hand_sale_post_put_args.add_argument('isSold', type=bool, required=False)

second_hand_sale_post_delete_args = reqparse.RequestParser()
second_hand_sale_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

second_hand_sale_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'price': fields.Float,
    'image': fields.String,
    'isNegotiated': fields.Boolean,
    'isSold': fields.Boolean,
}

class SecondHandSalePostResource(Resource):

    @marshal_with(second_hand_sale_post_resource_fields)
    def post(self):
        args = second_hand_sale_post_post_args.parse_args()

        # Check if the post_type is SecondHandSalePost
        if args['post_type'].lower() != 'secondhandsalepost':
            abort(400, message='Invalid post_type. Must be SecondHandSalePost.')

      
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new second hand sale post using the post_id from the new post
        new_second_hand_sale_post = SecondHandSalePostModel(
            post_id=new_post.post_id,
            price=args['price'],
            image=args['image'],
            isNegotiated=args['isNegotiated'],
            isSold=args['isSold']
        )

        # Add and commit the new second hand sale post to the database
        with current_app.app_context():
            db.session.add(new_second_hand_sale_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(second_hand_sale_post_resource_fields)
    def put(self):
        args = second_hand_sale_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the second hand sale post exists
        second_hand_sale_post = SecondHandSalePostModel.query.get(post_id)
        if not second_hand_sale_post:
            abort(404, message='Second hand sale post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['price'] is not None:
            second_hand_sale_post.price = args['price']
        if args['image'] is not None:
            second_hand_sale_post.image = args['image']
        if args['isNegotiated'] is not None:
            second_hand_sale_post.isNegotiated = args['isNegotiated']
        if args['isSold'] is not None:
            second_hand_sale_post.isSold = args['isSold']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the second hand sale post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = second_hand_sale_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the second hand sale post exists
        second_hand_sale_post = SecondHandSalePostModel.query.get(post_id)
        if not second_hand_sale_post:
            abort(404, message='Second hand sale post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(second_hand_sale_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204







#study buddy resource to post, edit and delete course material
    
study_buddy_post_post_args = reqparse.RequestParser()
study_buddy_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
study_buddy_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
study_buddy_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
study_buddy_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
study_buddy_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
study_buddy_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
study_buddy_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')

study_buddy_post_put_args = reqparse.RequestParser()
study_buddy_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
study_buddy_post_put_args.add_argument('title', type=str, required=False)
study_buddy_post_put_args.add_argument('description', type=str, required=False)
study_buddy_post_put_args.add_argument('post_type', type=str, required=False)
study_buddy_post_put_args.add_argument('is_archived', type=bool, required=False)
study_buddy_post_put_args.add_argument('share_date', type=str, required=False)
study_buddy_post_put_args.add_argument('criteria', type=str, required=False)
study_buddy_post_put_args.add_argument('owner', type=str, required=False)
study_buddy_post_put_args.add_argument('course', type=str, required=False)

study_buddy_post_delete_args = reqparse.RequestParser()
study_buddy_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

study_buddy_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
}

class StudyBuddyPostResource(Resource):

    @marshal_with(study_buddy_post_resource_fields)
    def post(self):
        args = study_buddy_post_post_args.parse_args()

        # Check if the post_type is StudyBuddyPost
        if args['post_type'].lower() != 'studybuddypost':
            abort(400, message='Invalid post_type. Must be StudyBuddyPost.')

        # Convert share_date string to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new study buddy post using the post_id from the new post
        new_study_buddy_post = StudyBuddyPostModel(
            post_id=new_post.post_id,
            course="null"
        )

        # Add and commit the new study buddy post to the database
        with current_app.app_context():
            db.session.add(new_study_buddy_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(study_buddy_post_resource_fields)
    def put(self):
        args = study_buddy_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the study buddy post exists
        study_buddy_post = StudyBuddyPostModel.query.get(post_id)
        if not study_buddy_post:
            abort(404, message='Study buddy post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['course'] is not None:
            study_buddy_post.course = args['course']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the study buddy post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = study_buddy_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the study buddy post exists
        study_buddy_post = StudyBuddyPostModel.query.get(post_id)
        if not study_buddy_post:
            abort(404, message='Study buddy post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(study_buddy_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204


#trip buddy resource to post, edit and delete course material
    
trip_buddy_post_post_args = reqparse.RequestParser()
trip_buddy_post_post_args.add_argument('title', type=str, required=True, help='Title is required')
trip_buddy_post_post_args.add_argument('description', type=str, required=True, help='Description is required')
trip_buddy_post_post_args.add_argument('post_type', type=str, required=True, help='Post type is required')
trip_buddy_post_post_args.add_argument('is_archived', type=bool, default=False, help='Is archived (default: False)')
trip_buddy_post_post_args.add_argument('share_date', type=str, required=True, help='Share date is required')
trip_buddy_post_post_args.add_argument('criteria', type=str, default='none', help='Criteria (default: none)')
trip_buddy_post_post_args.add_argument('owner', type=str, required=True, help='Owner is required')
trip_buddy_post_post_args.add_argument('tripDate', type=str, required=True, help='Trip date is required')
trip_buddy_post_post_args.add_argument('destination', type=str, required=True, help='Destination is required')
trip_buddy_post_post_args.add_argument('departure', type=str, required=True, help='Departure is required')

trip_buddy_post_put_args = reqparse.RequestParser()
trip_buddy_post_put_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
trip_buddy_post_put_args.add_argument('title', type=str, required=False)
trip_buddy_post_put_args.add_argument('description', type=str, required=False)
trip_buddy_post_put_args.add_argument('post_type', type=str, required=False)
trip_buddy_post_put_args.add_argument('is_archived', type=bool, required=False)
trip_buddy_post_put_args.add_argument('share_date', type=str, required=False)
trip_buddy_post_put_args.add_argument('criteria', type=str, required=False)
trip_buddy_post_put_args.add_argument('owner', type=str, required=False)
trip_buddy_post_put_args.add_argument('tripDate', type=str, required=False)
trip_buddy_post_put_args.add_argument('destination', type=str, required=False)
trip_buddy_post_put_args.add_argument('departure', type=str, required=False)

trip_buddy_post_delete_args = reqparse.RequestParser()
trip_buddy_post_delete_args.add_argument('post_id', type=int, required=True, help='Post ID is required')

trip_buddy_post_resource_fields = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'tripDate': fields.String,
    'destination': fields.String,
    'departure': fields.String,
}

class TripBuddyPostResource(Resource):

    @marshal_with(trip_buddy_post_resource_fields)
    def post(self):
        args = trip_buddy_post_post_args.parse_args()

        # Check if the post_type is TripBuddyPost
        if args['post_type'].lower() != 'tripbuddypost':
            abort(400, message='Invalid post_type. Must be TripBuddyPost.')

        # Convert share_date and tripDate strings to datetime
        share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')

        # Create a new post
        new_post = PostModel(
            title=args['title'],
            description=args['description'],
            post_type=args['post_type'],
            is_archived=args['is_archived'],
            share_date=share_date,
            criteria=args['criteria'],
            owner=args['owner']
        )

        # Add and commit the new post to the database
        with current_app.app_context():
            db.session.add(new_post)
            db.session.commit()

        # Create a new trip buddy post using the post_id from the new post
        new_trip_buddy_post = TripPostModel(
            post_id=new_post.post_id,
            tripDate=args['tripDate'],
            destination=args['destination'],
            departure=args['departure']
        )

        # Add and commit the new trip buddy post to the database
        with current_app.app_context():
            db.session.add(new_trip_buddy_post)
            db.session.commit()

        return new_post, 201
    
    @marshal_with(trip_buddy_post_resource_fields)
    def put(self):
        args = trip_buddy_post_put_args.parse_args()
        post_id = args['post_id']

        # Check if the trip buddy post exists
        trip_buddy_post = TripPostModel.query.get(post_id)
        if not trip_buddy_post:
            abort(404, message='Trip buddy post not found')

        # Get the parent post details
        post_details = PostModel.query.get(post_id)

        # Update the post attributes
        if args['title'] is not None:
            post_details.title = args['title']
        if args['description'] is not None:
            post_details.description = args['description']
        if args['post_type'] is not None:
            post_details.post_type = args['post_type']
        if args['is_archived'] is not None:
            post_details.is_archived = args['is_archived']
        if args['share_date'] is not None:
            post_details.share_date = datetime.strptime(args['share_date'], '%Y-%m-%dT%H:%M:%S')
        if args['criteria'] is not None:
            post_details.criteria = args['criteria']
        if args['owner'] is not None:
            post_details.owner = args['owner']
        if args['tripDate'] is not None:
            trip_buddy_post.tripDate = args['tripDate']
        if args['destination'] is not None:
            trip_buddy_post.destination = args['destination']
        if args['departure'] is not None:
            trip_buddy_post.departure = args['departure']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the trip buddy post and post details in the response
        return post_details, 200
    
    def delete(self):
        args = trip_buddy_post_delete_args.parse_args()
        post_id = args['post_id']

        # Check if the trip buddy post exists
        trip_buddy_post = TripPostModel.query.get(post_id)
        if not trip_buddy_post:
            abort(404, message='Trip buddy post not found')

        # Get the associated post
        post = PostModel.query.get(post_id)

        # Delete both the donation post and the associated post from the database
        with current_app.app_context():
            db.session.delete(trip_buddy_post)
            db.session.delete(post)  # This line deletes the associated post
            db.session.commit()

        return {'message': 'Donation post and associated post deleted successfully'}, 204

