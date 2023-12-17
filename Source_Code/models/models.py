from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

#This is the User Model, it holds the data of the user and the posts list of users
class UserModel(db.Model):
    __tablename__ = 'user_model'
    bilkent_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    usertype = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    following = db.Column(db.Integer, nullable=False)
    pp = db.Column(db.String(200), nullable=True)
    # Back reference to the posts
    posts = relationship('PostModel', back_populates='owner_user')
    
    def __repr__(self):
        return f"User(bilkent_id={self.bilkent_id}, username={self.username}, usertype={self.usertype}, email={self.email}, score={self.score})"

class PostModel(db.Model):
    __tablename__ = 'post_model'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    post_type = db.Column(db.String(50), nullable=False)
    is_archived = db.Column(db.Boolean, default=False)
    share_date = db.Column(db.DateTime, default=db.func.now())
    criteria = db.Column(db.String(255))

    owner = db.Column(db.String(255), db.ForeignKey('user_model.username'))
    owner_user = relationship('UserModel', back_populates='posts')

    donation_post = db.relationship('DonationPostModel', back_populates='post', lazy=False, uselist=False)
    found_item_post = db.relationship('FoundItemPostModel', back_populates='post', lazy=True, uselist=False)
    lost_item_post = db.relationship('LostItemPostModel', back_populates='post', lazy=True, uselist=False)
    course_material_post = db.relationship('CourseMaterialPostModel', back_populates='post', lazy=True, uselist=False)
    gym_buddy_search_post = db.relationship('GymBuddySearchPostModel', back_populates='post', lazy=True, uselist=False)
    need_post = db.relationship('NeedPostModel', back_populates='post', lazy=True, uselist=False)
    roommate_post = db.relationship('RoommatePostModel', back_populates='post', lazy=True, uselist=False)
    second_hand_sale_post = db.relationship('SecondHandSalePostModel', back_populates='post', lazy=True, uselist=False)
    study_buddy_post = db.relationship('StudyBuddyPostModel', back_populates='post', lazy=True, uselist=False)
    trip_post = db.relationship('TripPostModel', back_populates='post', lazy=True, uselist=False)

    def __repr__(self):
        return f"Post(post_id={self.post_id}, title={self.title}, description={self.description}, " \
               f"post_type={self.post_type}, is_archived={self.is_archived}, " \
               f"share_date={self.share_date}, criteria={self.criteria}, owner_bilkent_id={self.owner_bilkent_id})"

# Donation Post Model
class DonationPostModel(db.Model):
    __tablename__ = 'donation_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    image = db.Column(db.String(255))
    isDonated = db.Column(db.Boolean, default=False)
    isNegotiated = db.Column(db.Boolean, default=False)

    # Define backref to access the post from DonationPostModel
    post = db.relationship('PostModel', back_populates='donation_post', uselist=False)

    def __repr__(self):
        return f"DonationPost(post_id={self.post_id}, image={self.image}, " \
               f"isDonated={self.isDonated}, isNegotiated={self.isNegotiated})"

# Found Item Post Model
class FoundItemPostModel(db.Model):
    __tablename__ = 'found_item_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    ownerFound = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255))

    # Define backref to access the post from FoundItemPostModel
    post = db.relationship('PostModel', back_populates='found_item_post', uselist=False)

    def __repr__(self):
        return f"FoundItemPost(post_id={self.post_id}, ownerFound={self.ownerFound}, " 

# Lost Item Post Model
class LostItemPostModel(db.Model):
    __tablename__ = 'lost_item_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    image = db.Column(db.String(255))
    isFound = db.Column(db.Boolean, default=False)

    # Define backref to access the post from LostItemPostModel
    post = db.relationship('PostModel', back_populates='lost_item_post', uselist=False)

    def __repr__(self):
        return f"LostItemPost(post_id={self.post_id}, image={self.image}, " 

# Course Material Post Model
class CourseMaterialPostModel(db.Model):
    __tablename__ = 'course_material_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    course = db.Column(db.String(100), nullable=False)

    # Define backref to access the post from CourseMaterialPostModel
    post = db.relationship('PostModel', back_populates='course_material_post', uselist=False)

    def __repr__(self):
        return f"CourseMaterialPost(post_id={self.post_id}, course={self.course})"

# Gym Buddy Search Post Model
class GymBuddySearchPostModel(db.Model):
    __tablename__ = 'gym_buddy_search_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)

    # Define backref to access the post from GymBuddySearchPostModel
    post = db.relationship('PostModel', back_populates='gym_buddy_search_post', uselist=False)

    def __repr__(self):
        return f"GymBuddySearchPost(post_id={self.post_id})"

# Need Post Model
class NeedPostModel(db.Model):
    __tablename__ = 'need_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    foundNeed = db.Column(db.Boolean, default=False)
    isBorrowed = db.Column(db.Boolean, default=False)

    # Define backref to access the post from NeedPostModel
    post = db.relationship('PostModel', back_populates='need_post', uselist=False)

    def __repr__(self):
        return f"NeedPost(post_id={self.post_id}, foundNeed={self.foundNeed}, isBorrowed={self.isBorrowed})"

# Roommate Post Model
class RoommatePostModel(db.Model):
    __tablename__ = 'roommate_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)

    # Define backref to access the post from RoommatePostModel
    post = db.relationship('PostModel', back_populates='roommate_post', uselist=False)

    def __repr__(self):
        return f"RoommatePost(post_id={self.post_id})"

# Second Hand Sale Post Model
class SecondHandSalePostModel(db.Model):
    __tablename__ = 'second_hand_sale_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(255))
    isNegotiated = db.Column(db.Boolean, default=False)
    isSold = db.Column(db.Boolean, default=False)

    # Define backref to access the post from SecondHandSalePostModel
    post = db.relationship('PostModel', back_populates='second_hand_sale_post', uselist=False)

    def __repr__(self):
        return f"SecondHandSalePost(post_id={self.post_id}, price={self.price}, " \
               f"image={self.image}, isNegotiated={self.isNegotiated}, isSold={self.isSold})"

# Study Buddy Post Model
class StudyBuddyPostModel(db.Model):
    __tablename__ = 'study_buddy_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    course = db.Column(db.String(100), nullable=True)

    # Define backref to access the post from StudyBuddyPostModel
    post = db.relationship('PostModel', back_populates='study_buddy_post', uselist=False)

    def __repr__(self):
        return f"StudyBuddyPost(post_id={self.post_id}, course={self.course})"

# Trip Post Model
class TripPostModel(db.Model):
    __tablename__ = 'trip_post_model'

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'), primary_key=True)
    tripDate = db.Column(db.String(255))
    destination = db.Column(db.String(100))
    departure = db.Column(db.String(100))

    # Define backref to access the post from TripPostModel
    post = db.relationship('PostModel', back_populates='trip_post', uselist=False)

    def __repr__(self):
        return f"TripPost(post_id={self.post_id}, tripDate={self.tripDate}, " \
               f"destination={self.destination}, departure={self.departure})"

#Chat Model
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, nullable=False)
    sender_username = db.Column(db.String(50), nullable=False)
    receiver_username = db.Column(db.String(50), nullable=False)
    messages = db.relationship('Message', backref='chat', lazy=True)

#Message Model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_name = db.Column(db.String(50))
    content = db.Column(db.String(500))
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False, autoincrement=False, default=1)

#Request Model
class Request(db.Model):
    __tablename__ = 'request_model'
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    senderId = db.Column(db.Integer,db.ForeignKey('user_model.bilkent_id'), nullable=False)
    receiverId = db.Column(db.Integer, db.ForeignKey('user_model.bilkent_id'), nullable=False)
    isApproved = db.Column(db.Boolean, nullable=False, default=False)
    isRejected = db.Column(db.Boolean, nullable=False, default=False)
    requestType = db.Column(db.String(50), nullable=False)

class FollowRequest(db.Model):
    __tablename__ = 'follow_request_model'

    request_id = db.Column(db.Integer, db.ForeignKey('request_model.id'), primary_key=True)
    pending = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Follow Request: (request_id={self.request_id}," \
               f"pending={self.pending})"
    
class ChatRequest(Request):
    __tablename__ = 'chat_request_model'

    id = db.Column(db.Integer, db.ForeignKey('request_model.id'), primary_key=True)
    message = db.Column(db.String(255))  # Adjust the length as needed
    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'))
    post = relationship('PostModel', foreign_keys=[post_id])

    def __repr__(self):
        return f"ChatRequest(id={self.id}, senderId={self.senderId}, " \
               f"receiverId={self.receiverId}, isApproved={self.isApproved}, " \
               f"isRejected={self.isRejected}, requestType={self.requestType}, " \
               f"message={self.message}, post_id={self.post_id})"
    
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reporterId=db.Column(db.Integer, db.ForeignKey('user_model.bilkent_id'),nullable=False)
    reporteeId=db.Column(db.Integer, db.ForeignKey('user_model.bilkent_id'), nullable=False)
    reason=db.Column(db.String, nullable=False)

#Notification Model 
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ownerName=db.Column(db.String(255), nullable=False)
    message=db.Column(db.String(500), nullable =False)

#Mark Found Item Relation
class MarkFoundItemPostModel(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return f"MarkedPost(post_id={self.post_id}, user_id={self.user_id}, ...)"

#Mark Lost Item Relation
class MarkFoundItemPostModel(db.Model):
    __tablename__ = 'marked_post_model'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return f"MarkedPost(post_id={self.post_id}, user_id={self.user_id}, ...)"

#Blocked User Relation
class BlockedUserModel(db.Model):
    blocker_username = db.Column(db.String, primary_key=True)
    blocked_username = db.Column(db.String, primary_key=True)
    def repr(self):
        return f"Blocked user (blocker_username={self.blocker_username}, blocked_username={self.blocked_username}, ...)"
#Followed User Relation

class FollowedUserModel(db.Model):
    follower_name = db.Column(db.String, primary_key=True)
    followed_name = db.Column(db.String, primary_key=True)
    def _repr_(self):
        return f"Following relation (follower_name={self.follower_name}, followed_name={self.followed_name}, ...)"
    
#Favourite Post Relation
class FavouritePostModel(db.Model):
    fav_username = db.Column(db.String, primary_key = True)
    fav_post_id = db.Column(db.Integer, primary_key = True)
    def repr(self):
        return f"Favourite user (fav_username={self.fav_username}, fav_post_id={self.fav_post_id}, ...)"