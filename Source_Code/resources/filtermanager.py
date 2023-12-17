from flask import current_app,jsonify
from flask_restful import Resource, fields, marshal_with
from models.models import db, UserModel, PostModel, DonationPostModel,TripPostModel 
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel

full_post_resource_fields_donation = {
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

full_post_resource_fields_trip={
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

full_post_resource_fields_found = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'image': fields.String,
    'ownerFound': fields.Boolean
}

full_post_resource_fields_lost = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
    'image': fields.String,
    'isFound': fields.Boolean
}

full_post_resource_fields_second = {
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

full_post_resource_fields_need = {
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

full_post_resource_fields_gym = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
}

full_post_resource_fields_study = {
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

full_post_resource_fields_room = {
    'post_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'post_type': fields.String,
    'is_archived': fields.Boolean,
    'share_date': fields.String,
    'criteria': fields.String,
    'owner': fields.String,
}

full_post_resource_fields_course = {
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

class ShowDonationPostResource(Resource):

    @marshal_with(full_post_resource_fields_donation)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, DonationPostModel).outerjoin(DonationPostModel, PostModel.post_id == DonationPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, donation_post in posts:
            if post.post_type == 'DonationPost':
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

        return combined_data, 200

class ShowTripPostResource(Resource):
    @marshal_with(full_post_resource_fields_trip)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, TripPostModel).outerjoin(TripPostModel, PostModel.post_id == TripPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, trip_post in posts:
            if post.post_type == 'TripBuddyPost':
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

        return combined_data, 200
    
class ShowFoundPostResource(Resource):
     
    @marshal_with(full_post_resource_fields_found)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, FoundItemPostModel).outerjoin(FoundItemPostModel, PostModel.post_id == FoundItemPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, found_post in posts:
            if post.post_type == 'FoundPost':
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

        return combined_data, 200

class ShowLostPostResource(Resource):
    @marshal_with(full_post_resource_fields_lost)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, LostItemPostModel).outerjoin(LostItemPostModel, PostModel.post_id == LostItemPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, lost_post in posts:
            if post.post_type == 'LostPost':
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

        return combined_data, 200

class ShowNeedPostResource(Resource):
    @marshal_with(full_post_resource_fields_need)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, NeedPostModel).outerjoin(NeedPostModel, PostModel.post_id == NeedPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, need_post in posts:
            if post.post_type == 'NeedPost':
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

        return combined_data, 200

class ShowGymPostResource(Resource):
    @marshal_with(full_post_resource_fields_gym)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, GymBuddySearchPostModel).outerjoin(GymBuddySearchPostModel, PostModel.post_id == GymBuddySearchPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, gym_post in posts:
            if post.post_type == 'GymBuddyPost':
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

        return combined_data, 200

class ShowStudyPostResource(Resource):
    @marshal_with(full_post_resource_fields_study)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, StudyBuddyPostModel).outerjoin(StudyBuddyPostModel, PostModel.post_id == StudyBuddyPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, study_post in posts:
            if post.post_type == 'StudyBuddyPost':
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

        return combined_data, 200

class ShowRoomPostResource(Resource):
    @marshal_with(full_post_resource_fields_room)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, RoommatePostModel).outerjoin(RoommatePostModel, PostModel.post_id == RoommatePostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, room_post in posts:
            if post.post_type == 'RoomMatePost':
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

        return combined_data, 200

class ShowCoursePostResource(Resource):
    @marshal_with(full_post_resource_fields_course)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, CourseMaterialPostModel).outerjoin(CourseMaterialPostModel, PostModel.post_id == CourseMaterialPostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, course_post in posts:
            if post.post_type == 'CourseMaterialPost':
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

        return combined_data, 200

class ShowSecondPostResource(Resource):
    @marshal_with(full_post_resource_fields_second)
    def get(self):
        # Retrieve all posts from both tables
        posts = db.session.query(PostModel, SecondHandSalePostModel).outerjoin(SecondHandSalePostModel, PostModel.post_id == SecondHandSalePostModel.post_id).all()

        # Combine the data from both tables
        combined_data = []
        for post, second_post in posts:
            if post.post_type == 'SecondHandSalePost':
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

        return combined_data, 200

