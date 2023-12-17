from flask import current_app,jsonify
from flask_restful import Resource, fields, marshal_with
from models.models import db, UserModel, PostModel, DonationPostModel,TripPostModel 
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel, BlockedUserModel

student_page_resource_fields={
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
    'ownerFound': fields.Boolean,
    'foundDate': fields.DateTime,
    'isFound': fields.Boolean,
    'lostDate': fields.DateTime,
    'isSold': fields.Boolean,
    'foundNeed': fields.Boolean,
    'isBorrowed': fields.Boolean,
    'course': fields.String,
}

class StudentPageResource(Resource):
    
    @marshal_with(student_page_resource_fields)
    def get(self, username):
        posts=PostModel.query.all()
        combined_data = []

        
            
            
        study_posts = db.session.query(PostModel, StudyBuddyPostModel).outerjoin(StudyBuddyPostModel, PostModel.post_id == StudyBuddyPostModel.post_id).all()
        course_posts = db.session.query(PostModel, CourseMaterialPostModel).outerjoin(CourseMaterialPostModel, PostModel.post_id == CourseMaterialPostModel.post_id).all()
        
        # Combine the data from both tables

        for post, study_post in study_posts:
            if post.post_type == 'StudyBuddyPost' and post.is_archived==False and post.owner!=username:
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

        

        for post, course_post in course_posts:
            if post.post_type == 'CourseMaterialPost' and post.is_archived==False and post.owner!=username:
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

        
        combined_data = sorted(combined_data, key=lambda x: x['post_id'], reverse=True)
        return combined_data, 200