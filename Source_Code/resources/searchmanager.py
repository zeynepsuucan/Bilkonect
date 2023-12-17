from flask import current_app,jsonify
from flask_restful import Resource, fields, marshal_with
from models.models import db, UserModel, PostModel, DonationPostModel,TripPostModel 
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel
 

user_resource_fields = {
    'bilkent_id': fields.Integer,
    'username': fields.String,
    'usertype': fields.String,
    'email': fields.String,
    'score': fields.Integer,
    'pp': fields.String,
}

search_by_name_resource_fields = {
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
    'tripDate': fields.DateTime,
    'destination': fields.String,
    'departure': fields.String,
    'image': fields.String,
    'ownerFound': fields.Boolean,
    'isFound': fields.Boolean,
    'isNegotiated': fields.Boolean,
    'isSold': fields.Boolean,
    'foundNeed': fields.Boolean,
    'isBorrowed': fields.Boolean,
    'course': fields.String,
}

class Search_by_Name_Resource(Resource):
    @marshal_with(search_by_name_resource_fields)
    def get(self, search_string):
        # Retrieve all posts from both tables
        donation_posts = db.session.query(PostModel, DonationPostModel).outerjoin(DonationPostModel, PostModel.post_id == DonationPostModel.post_id).all()
        trip_posts = db.session.query(PostModel, TripPostModel).outerjoin(TripPostModel, PostModel.post_id == TripPostModel.post_id).all()
        found_posts = db.session.query(PostModel, FoundItemPostModel).outerjoin(FoundItemPostModel, PostModel.post_id == FoundItemPostModel.post_id).all()
        lost_posts = db.session.query(PostModel, LostItemPostModel).outerjoin(LostItemPostModel, PostModel.post_id == LostItemPostModel.post_id).all()
        second_posts = db.session.query(PostModel, SecondHandSalePostModel).outerjoin(SecondHandSalePostModel, PostModel.post_id == SecondHandSalePostModel.post_id).all()
        need_posts = db.session.query(PostModel, NeedPostModel).outerjoin(NeedPostModel, PostModel.post_id == NeedPostModel.post_id).all()
        gym_posts = db.session.query(PostModel, GymBuddySearchPostModel).outerjoin(GymBuddySearchPostModel, PostModel.post_id == GymBuddySearchPostModel.post_id).all()
        study_posts = db.session.query(PostModel, StudyBuddyPostModel).outerjoin(StudyBuddyPostModel, PostModel.post_id == StudyBuddyPostModel.post_id).all()
        room_posts = db.session.query(PostModel, RoommatePostModel).outerjoin(RoommatePostModel, PostModel.post_id == RoommatePostModel.post_id).all()
        course_posts = db.session.query(PostModel, CourseMaterialPostModel).outerjoin(CourseMaterialPostModel, PostModel.post_id == CourseMaterialPostModel.post_id).all()
        
        # Combine the data from both tables
        combined_data = []
        for post, donation_post in donation_posts:
            print(post.post_type)
            if post.post_type == 'DonationPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'image': donation_post.image if donation_post else None,
                    'isDonated': donation_post.isDonated if donation_post else None,
                    'isNegotiated': donation_post.isNegotiated if donation_post else None,
                }
                combined_data.append(combined_post)

        for post, trip_post in trip_posts:
            if post.post_type == 'TripBuddyPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'tripDate': trip_post.tripDate if trip_post else None,
                    'destination': trip_post.destination if trip_post else None,
                    'departure': trip_post.departure if trip_post else None,
                }
                combined_data.append(combined_post)
    
        for post, second_post in second_posts:
            if post.post_type == 'SecondHandSalePost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'price': second_post.price if second_post else None,
                    'image': second_post.image if second_post else None,
                    'isNegotiated': second_post.isNegotiated if second_post else None,
                    'isSold': second_post.isSold if second_post else None
                }
                combined_data.append(combined_post)
        
        for post, found_post in found_posts:
            if post.post_type == 'FoundPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'image': found_post.image if found_post else None,
                    'ownerFound': found_post.ownerFound if found_post else None
                }
                combined_data.append(combined_post)

        for post, lost_post in lost_posts:
            if post.post_type == 'LostPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'image': lost_post.image if lost_post else None,
                    'isFound': lost_post.isFound if lost_post else None
                }
                combined_data.append(combined_post)

        for post, need_post in need_posts:
            if post.post_type == 'NeedPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'foundNeed': need_post.foundNeed if need_post else None,
                    'isBorrowed': need_post.isBorrowed if need_post else None
                }
                combined_data.append(combined_post)

        for post, gym_posts in gym_posts:
            if post.post_type == 'GymBuddyPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner
                }
                combined_data.append(combined_post)

        for post, study_post in study_posts:
            if post.post_type == 'StudyBuddyPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'course': study_post.course if study_post else None
                }
                combined_data.append(combined_post)

        for post, room_post in room_posts:
            if post.post_type == 'RoommatePost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner
                }
                combined_data.append(combined_post)

        for post, course_post in course_posts:
            if post.post_type == 'CourseMaterialPost' and post.is_archived==False and (search_string.lower() in post.title.lower()):
                combined_post = {
                    'post_id': post.post_id,
                    'title': post.title,
                    'description': post.description,
                    'post_type': post.post_type,
                    'is_archived': post.is_archived,
                    'share_date': post.share_date,
                    'criteria': post.criteria,
                    'owner': post.owner,
                    'course': course_post.course if course_post else None
                }
                combined_data.append(combined_post)

        print(combined_data)
        combined_data = sorted(combined_data, key=lambda x: x['post_id'], reverse=True)
        return combined_data, 200
   
class Check_User_By_Name(Resource):
    @marshal_with(user_resource_fields)
    def get(self, search_string):
        filtered_data = []
        users=UserModel.query.all()
        for user in users:
            if search_string.lower() in user.username.lower():
                filtered_user = {
                    'bilkent_id': user.bilkent_id,
                    'username': user.username,
                    'usertype': user.usertype,
                    'email': user.email,
                    'score': user.score,
                    'pp': user.pp,
                }
                filtered_data.append(filtered_user)
        return filtered_data, 200