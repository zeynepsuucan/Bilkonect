from flask import current_app,jsonify
from flask_restful import Resource, fields, marshal_with
from models.models import db, UserModel, PostModel, DonationPostModel,TripPostModel 
from models.models import SecondHandSalePostModel,CourseMaterialPostModel, RoommatePostModel, LostItemPostModel
from models.models import StudyBuddyPostModel, GymBuddySearchPostModel, NeedPostModel, FoundItemPostModel
from models.models import FollowedUserModel, BlockedUserModel, FavouritePostModel, Notification

feed_resource_fields = {
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
    'price': fields.Float,
    'isNegotiated': fields.Boolean,
    'tripDate': fields.String,
    'destination': fields.String,
    'departure': fields.String,
    'ownerFound': fields.Boolean,
    'isFound': fields.Boolean,
    'isSold': fields.Boolean,
    'foundNeed': fields.Boolean,
    'isBorrowed': fields.Boolean,
    'course': fields.String,
}

user_info_fields = {
    'bilkent_id': fields.Integer,
    'followers': fields.Integer,
    'following': fields.Integer,
    'score': fields.Integer,
    'pp': fields.String,
}


follow_resource_fields = {
    'follower_name': fields.String,
    'followed_name': fields.String,
}

blocked_info_field = {
    'username': fields.String
}

not_info_field = {
    'message': fields.String
}

class GetOwnPosts(Resource):
    @marshal_with(feed_resource_fields)
    def get(self,username):

        user = db.query.filter_by(username=username).first()
        posts = user.posts
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
        for post, donation_post in posts:
            if post.post_type == 'DonationPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'TripBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'SecondHandSalePost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'FoundPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'LostPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'NeedPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'GymBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'StudyBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'RoomMatePost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'CourseMaterialPost' and post.is_archived==False and post.owner==username:
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

class FeedResource(Resource):
    @marshal_with(feed_resource_fields)
    def get(self,username):
        # Retrieve all posts from both tables
        donation_posts = db.session.query(PostModel, DonationPostModel).outerjoin(DonationPostModel, PostModel.post_id == DonationPostModel.post_id).all()
        trip_posts = db.session.query(PostModel, TripPostModel).outerjoin(TripPostModel, PostModel.post_id == TripPostModel.post_id).all()
        found_posts = db.session.query(PostModel, FoundItemPostModel).outerjoin(FoundItemPostModel, PostModel.post_id == FoundItemPostModel.post_id).all()
        lost_posts = db.session.query(PostModel, LostItemPostModel).outerjoin(LostItemPostModel, PostModel.post_id == LostItemPostModel.post_id).all()
        second_posts = db.session.query(PostModel, SecondHandSalePostModel).outerjoin(SecondHandSalePostModel, PostModel.post_id == SecondHandSalePostModel.post_id).all()
        need_posts = db.session.query(PostModel, NeedPostModel).outerjoin(NeedPostModel, PostModel.post_id == NeedPostModel.post_id).all()
        gym_posts = db.session.query(PostModel, GymBuddySearchPostModel).outerjoin(GymBuddySearchPostModel, PostModel.post_id == GymBuddySearchPostModel.post_id).all()
        room_posts = db.session.query(PostModel, RoommatePostModel).outerjoin(RoommatePostModel, PostModel.post_id == RoommatePostModel.post_id).all()
        
        # Combine the data from both tables
        combined_data = []
        for post, donation_post in donation_posts:
            if post.post_type == 'DonationPost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'TripBuddyPost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'SecondHandSalePost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'FoundPost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'LostPost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'NeedPost' and post.is_archived==False and post.owner != username:
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
            if post.post_type == 'GymBuddyPost' and post.is_archived==False and post.owner != username:
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

        for post, room_post in room_posts:
            if post.post_type == 'RoomMatePost' and post.is_archived==False and post.owner != username:
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

        combined_data = sorted(combined_data, key=lambda x: x['post_id'], reverse=True)
        return combined_data, 200

class GetPostFromId(Resource):

    def get(self, id):
        with current_app.app_context():
            # Retrieve the post from the database based on the provided post_id
            post = PostModel.query.get(id)

            if post:
                if post.post_type == 'DonationPost':
                    donation_post = DonationPostModel.query.get(id)
                    return self.get_donation_post_info(post, donation_post)
                elif post.post_type == 'TripBuddyPost':
                    trip_post = TripPostModel.query.get(id)
                    return self.get_trip_post_info(post, trip_post)
                elif post.post_type == 'FoundPost':
                    found_post = FoundItemPostModel.query.get(id)
                    return self.get_found_post_info(post, found_post)
                elif post.post_type == 'LostPost':
                    lost_post = LostItemPostModel.query.get(id)
                    return self.get_lost_post_info(post, lost_post)
                elif post.post_type == 'SecondHandSalePost':
                    second_post = SecondHandSalePostModel.query.get(id)
                    return self.get_second_post_info(post, second_post)
                elif post.post_type == 'NeedPost':
                    need_post = NeedPostModel.query.get(id)
                    return self.get_need_post_info(post, need_post)
                elif post.post_type == 'GymBuddyPost':
                    gym_post = GymBuddySearchPostModel.query.get(id)
                    return self.get_gym_post_info(post, gym_post)
                elif post.post_type == 'StudyBuddyPost':
                    study_post = StudyBuddyPostModel.query.get(id)
                    return self.get_study_post_info(post, study_post)
                elif post.post_type == 'RoomMatePost':
                    room_post = RoommatePostModel.query.get(id)
                    return self.get_room_post_info(post, room_post)
                elif post.post_type == 'CourseMaterialPost':
                    course_post = CourseMaterialPostModel.query.get(id)
                    return self.get_course_post_info(post, course_post)
                else:
                    return {'message': 'Unsupported post type'}, 404
            else:
                return {'message': 'Post not found'}, 404

    def get_donation_post_info(self, post, donation_post):
        if donation_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'image': donation_post.image,
                'isDonated': donation_post.isDonated,
                'isNegotiated': donation_post.isNegotiated,
            }
        else:
            return {'message': 'Donation post not found'}, 404
            
    def get_trip_post_info(self, post, trip_post):
        if trip_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'tripDate': trip_post.tripDate,
                'destination': trip_post.destination,
                'departure': trip_post.departure,
            }
        else:
            return {'message': 'Trip post not found'}, 404

    def get_found_post_info(self, post, found_post):
        if found_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'image': found_post.image,
                'ownerFound': found_post.ownerFound
            }
        else:
            return {'message': 'Found post not found'}, 404

    def get_lost_post_info(self, post, lost_post):
        if lost_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'image': lost_post.image,
                'isFound': lost_post.isFound,
            }
        else:
            return {'message': 'Lost post not found'}, 404

    def get_second_post_info(self, post, second_post):
        if second_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'price': second_post.price,
                'image': second_post.image,
                'isNegotiated': second_post.isNegotiated,
                'isSold': second_post.isSold,
            }
        else:
            return {'message': 'Second-hand post not found'}, 404

    def get_need_post_info(self, post, need_post):
        if need_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'foundNeed': need_post.foundNeed,
                'isBorrowed': need_post.isBorrowed,
            }
        else:
            return {'message': 'Need post not found'}, 404

    def get_gym_post_info(self, post, gym_post):
        if gym_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
            }
        else:
            return {'message': 'Gym post not found'}, 404

    def get_study_post_info(self, post, study_post):
        if study_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'course': study_post.course,
            }
        else:
            return {'message': 'Study post not found'}, 404

    def get_room_post_info(self, post, room_post):
        if room_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
            }
        else:
            return {'message': 'Room post not found'}, 404

    def get_course_post_info(self, post, course_post):
        if course_post:
            return {
                'post_id': post.post_id,
                'title': post.title,
                'description': post.description,
                'post_type': post.post_type,
                'is_archived': post.is_archived,
                'share_date': post.share_date.strftime('%Y-%m-%dT%H:%M:%S'),
                'criteria': post.criteria,
                'owner': post.owner,
                'course': course_post.course,
            }
        else:
            return {'message': 'Course post not found'}, 404
           
class GetPostsfromUsername(Resource):
    @marshal_with(feed_resource_fields)
    def get(self,username):
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
            if post.post_type == 'DonationPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'TripBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'SecondHandSalePost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'FoundPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'LostPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'NeedPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'GymBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'StudyBuddyPost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'RoomMatePost' and post.is_archived==False and post.owner==username:
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
            if post.post_type == 'CourseMaterialPost' and post.is_archived==False and post.owner==username:
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
    
class GetProfileInfoFromUsername(Resource):

    @marshal_with(user_info_fields)
    def get(self, username):
        with current_app.app_context():
            # Fetch the user from the database based on the provided username
            user = UserModel.query.filter_by(username=username).first()

            # Check if the user exists
            if user:
                # Extract the required information
                user_info = {
                    'bilkent_id': user.bilkent_id,
                    'followers': user.followers,
                    'following': user.following,
                    'score': user.score,
                    'pp': user.pp # Assuming there is an 'image' column in your UserModel
                }

                return user_info
            else:
                # You may want to return a default value or raise an exception based on your requirements
                return {'followers': 0, 'following': 0, 'score': 0, 'image': ''}

class GetFollowedUsers(Resource):
    @marshal_with(follow_resource_fields)
    def get(self, username):
          with current_app.app_context():
            # Fetch the user from the database based on the provided username
            follows = FollowedUserModel.query.filter_by(follower_name=username).all()

            return_follows = []
            # Check if the user exists
            if follows:
                for follow in follows:
                # Extract the required information
                    follow_info = {
                        'follower_name': follow.follower_name,
                        'followed_name': follow.followed_name }
                    
                    return_follows.append(follow_info)
                return return_follows
            else:
               return {'followers': 0, 'following': 0, 'score': 0, 'image': ''}

class GetFollowedPosts(Resource):

    @marshal_with(feed_resource_fields)
    def get(self, username):
          with current_app.app_context():
            # Fetch the user from the database based on the provided username
            follows = FollowedUserModel.query.filter_by(follower_name=username).all()

            combined_data = []
            # Check if the user exists
            if follows:
                for follow in follows:
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
                    
                    for post, donation_post in donation_posts:
                        if post.post_type == 'DonationPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'TripBuddyPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'SecondHandSalePost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'FoundPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'LostPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'NeedPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'GymBuddyPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'StudyBuddyPost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'RoomMatePost' and post.is_archived==False and post.owner==follow.followed_name:
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
                        if post.post_type == 'CourseMaterialPost' and post.is_archived==False and post.owner==follow.followed_name:
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
            else:
               return {'followers': 0, 'following': 0, 'score': 0, 'image': ''}

class GetBlockedUsersOfResource(Resource):
    @marshal_with(blocked_info_field)
    def get(self, username):
        block_relation = BlockedUserModel.query.all()
        combined_data = []
        for block in block_relation:
            if(block.blocker_username==username):
                foundUsername = block.blocked_username
                user = UserModel.query.all()
                for user in user:
                    if(user.username == foundUsername):
                        blocked_info = {
                            'username' : user.username
                        }
                        combined_data.append(blocked_info)
        print(combined_data)
        return combined_data, 200

class GetNotifications(Resource):
    @marshal_with(not_info_field)
    def get(self, username):
        with current_app.app_context():
            nots = Notification.query.filter_by(ownerName=username).all()

            return_nots = []

            # Check if there are any notifications
            if nots:
                for not1 in nots:
                    # Extract the required information
                    message = not1.message

                    return_nots.append({'message': message})

                return return_nots
            else:
                return {'notifications': 'no notifications'}
            


class GetFavouritedPostsOfUserResource(Resource):
    @marshal_with(feed_resource_fields)
    def get(self, username):
        fav_relation = FavouritePostModel.query.all()
        combined_data = []
        for fav in fav_relation:
            
            if username == fav.fav_username:
                #posts = PostModel.query.filter_by(post_id=fav.fav_post_id).all()
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
                    if post.post_type == 'DonationPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
                        print("yes")
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
                    if post.post_type == 'TripBuddyPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'SecondHandSalePost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'FoundPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                            'ownerFound': found_post.ownerFound if found_post else None,
                            'foundDate': found_post.foundDate if found_post else None
                        }
                        combined_data.append(combined_post)

                for post, lost_post in lost_posts:
                    if post.post_type == 'LostPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                            'isFound': lost_post.isFound if lost_post else None,
                            'lostDate': lost_post.lostDate if lost_post else None
                        }
                        combined_data.append(combined_post)

                for post, need_post in need_posts:
                    if post.post_type == 'NeedPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'GymBuddyPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'StudyBuddyPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'RoomMatePost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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
                    if post.post_type == 'CourseMaterialPost' and post.is_archived==False and post.post_id==fav.fav_post_id:
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