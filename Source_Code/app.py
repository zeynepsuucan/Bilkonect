from flask import Flask, render_template, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO
from flask import Flask, render_template, request

from resources.usermanager import RegisterResource, LoginResource

from resources.filtermanager import ShowDonationPostResource, ShowTripPostResource, ShowFoundPostResource
from resources.filtermanager import ShowLostPostResource, ShowNeedPostResource, ShowGymPostResource, ShowStudyPostResource 
from resources.filtermanager import ShowRoomPostResource, ShowCoursePostResource, ShowSecondPostResource

from resources.postmanager import DonationPostResource, FoundItemPostResource, LostItemPostResource
from resources.postmanager import SecondHandSalePostResource, NeedPostResource, CourseMaterialPostResource
from resources.postmanager import StudyBuddyPostResource, GymBuddyPostResource, TripBuddyPostResource, RoommatePostResource
from resources.displaymanager import GetProfileInfoFromUsername, GetPostFromId, FeedResource, GetPostsfromUsername, GetFollowedPosts, GetFollowedUsers

from resources.searchmanager import Check_User_By_Name, Search_by_Name_Resource

from resources.chatmanager import ChatListResource, ChatMessagesResource, GetAllChatsOfUser, GetIfChatExists, GetOtherUser

from resources.studentmanager import StudentPageResource

from resources.adminmanager import getReportsResource

from resources.relationmanager import ReportResource, BlockResource, FollowResource, CheckFollowRelation
from resources.displaymanager import GetFavouritedPostsOfUserResource, GetBlockedUsersOfResource, GetNotifications

from resources.request import ChatRequestResource, FollowRequestResource

from resources.notification import NotificationResource

from models.models import db, Chat, Message

from resources.mark import MarkFoundItemPostResource

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
socketio = SocketIO(app)
CORS(app)

# Import and register resources
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')


#bunlar her post tipi için var her birinde post atma post editleme ve silme işlemleri var
api.add_resource(DonationPostResource, '/DonationPost')
api.add_resource(FoundItemPostResource, '/FoundPost')
api.add_resource(LostItemPostResource, '/LostPost')
api.add_resource(SecondHandSalePostResource, '/SecondHandSalePost')
api.add_resource(NeedPostResource, '/NeedPost')
api.add_resource(GymBuddyPostResource, '/GymBuddyPost')
api.add_resource(StudyBuddyPostResource, '/StudyBuddyPost')
api.add_resource(TripBuddyPostResource, '/TripBuddyPost')
api.add_resource(RoommatePostResource, '/RoomMatePost')
api.add_resource(CourseMaterialPostResource, '/CourseMaterialPost')
api.add_resource(BlockResource, '/block')
api.add_resource(FollowResource, '/follow')
api.add_resource(CheckFollowRelation, '/checkfollows')
#unblock için delete kullanılmalı

#bunlar nerede kullanılacak bilmiyorum daha requestler ne durumda ????
api.add_resource(ReportResource, '/report')
api.add_resource(ChatRequestResource, '/chatrequest')
api.add_resource(FollowRequestResource, '/followrequest')
api.add_resource(NotificationResource, '/notification')

#ayrı ayrı hepsini görmek için filter da bunlar olsunnnnnnnnnnn
api.add_resource(ShowDonationPostResource, '/getdonation')
api.add_resource(ShowTripPostResource,'/gettrip')
api.add_resource(ShowFoundPostResource,'/getfound')
api.add_resource(ShowLostPostResource, '/getlost')
api.add_resource(ShowNeedPostResource, '/getneed')
api.add_resource(ShowGymPostResource, '/getgym')
api.add_resource(ShowStudyPostResource, '/getstudy')
api.add_resource(ShowRoomPostResource, '/getroom')
api.add_resource(ShowCoursePostResource, '/getcourse')
api.add_resource(ShowSecondPostResource, '/getsecond')

api.add_resource(GetOtherUser, '/get_other_user')

#birer birer username falan denemesiiiiiiiiiii
api.add_resource(ChatListResource, '/get_chats/<string:post_id>', '/create_chat')
api.add_resource(ChatMessagesResource, '/get_messages/<int:chat_id>')
api.add_resource(GetProfileInfoFromUsername, '/getProfile/<string:username>')
api.add_resource(GetPostsfromUsername, '/getPosts/<string:username>')
api.add_resource(Search_by_Name_Resource, '/searchByTitle/<string:search_string>')
api.add_resource(GetPostFromId, '/getPostFromID/<int:id>')
api.add_resource(Check_User_By_Name, '/getuserbyname/<string:search_string>')
api.add_resource(GetFollowedPosts, '/getfollow/<string:username>')
api.add_resource(GetFollowedUsers, '/getfollowed/<string:username>')
api.add_resource(FeedResource, '/feed/<string:username>')
api.add_resource(StudentPageResource, '/studentpage/<string:username>')
api.add_resource(GetBlockedUsersOfResource, '/getblockedusers/<string:username>')
api.add_resource(GetFavouritedPostsOfUserResource, '/getfavoriteposts/<string:username>')
api.add_resource(GetAllChatsOfUser,'/getallchats/<string:username>')
api.add_resource(getReportsResource,'/reports')
api.add_resource(GetIfChatExists,'/checkexistance')
api.add_resource(GetNotifications, '/getnot/<string:username>')

api.add_resource(MarkFoundItemPostResource, '/marked')

@app.route('/create_chat', methods=['POST'])
def create_chat():
    data = request.get_json()

    if not data or 'receiver_username' not in data or 'post_id' not in data or 'sender_username' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    receiver_username = data['receiver_username']
    sender_username = data['sender_username']
    post_id = data['post_id']

    new_chat = Chat(sender_username=sender_username, post_id=post_id, receiver_username = receiver_username)
    db.session.add(new_chat)
    db.session.commit()

    return jsonify({'message': new_chat.id}), 201

@app.route('/send_message/<int:chat_id>', methods=['POST'])
def send_message(chat_id):
    data = request.get_json()

    if not data or 'sender_name' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    sender_name = data['sender_name']
    content = data['content']

    chat = Chat.query.get_or_404(chat_id)
    new_message = Message(sender_name=sender_name, content=content, chat=chat)
    db.session.add(new_message)
    db.session.commit()

    # Broadcast the message to all clients in the same chat
    socketio.emit('my_response', {'sender_name': sender_name, 'content': content}, room=str(chat_id))

    return jsonify({'message': 'Message sent successfully'}), 201

@socketio.on('my_custom_event')
def handle_my_custom_event(json):
    sender_name = json['sender_name']
    content = json['content']
    chat_id = json['chat_id']

    chat = Chat.query.get_or_404(chat_id)
    new_message = Message(sender_name=sender_name, content=content, chat=chat)
    db.session.add(new_message)
    db.session.commit()

    # Broadcast the message to all clients in the same chat
    socketio.emit('my_response', json, room=str(chat_id))

from models.models import db
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)