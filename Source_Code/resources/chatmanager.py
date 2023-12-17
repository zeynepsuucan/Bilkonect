from flask import jsonify
from models.models import Chat, PostModel, UserModel, Message
from flask_restful import Resource, reqparse, fields, marshal_with, abort


class ChatListResource(Resource):
    def get(self, post_id):
        user_chats = Chat.query.filter_by(post_id=post_id).all()

        chats_data = [{'id': chat.id, 'sender_username': chat.sender_username,'receiver_username':chat.receiver_username, 'post_id': chat.post_id} for chat in user_chats]
        return jsonify({'chats': chats_data})

class ChatMessagesResource(Resource):
    def get(self, chat_id):
        chat = Chat.query.get_or_404(chat_id)
        messages = [{'sender_name': message.sender_name, 'content': message.content} for message in chat.messages]
        return jsonify({'messages': messages})
  
class GetAllChatsOfUser(Resource):
    def get(self, username):
        sender_user_chats = Chat.query.filter((Chat.sender_username == username)).all()
        rec_user_chats = Chat.query.filter((Chat.receiver_username == username)).all()

        if not (sender_user_chats or rec_user_chats):
            return jsonify({'message': 'No chats found for the user'}), 404

        return_chats = []
        for chat in sender_user_chats:
            last_message = chat.messages[-1] if chat.messages else None
            return_chats.append({
                'id': chat.id,
                'username': chat.receiver_username,
                'post_id': chat.post_id,
                'sender_name': last_message.sender_name if last_message else None,
                'content': last_message.content if last_message else None
            })
        for chat in rec_user_chats:
            last_message = chat.messages[-1] if chat.messages else None
            return_chats.append({
                'id': chat.id,
                'username': chat.sender_username,
                'post_id': chat.post_id,
                'sender_name': last_message.sender_name  if last_message else None,
                'content': last_message.content if last_message else None
            })

        return return_chats

check_chat_args = reqparse.RequestParser()
check_chat_args.add_argument('username', type=str, required=True, help='Username is required')
check_chat_args.add_argument('post_id', type=int, required=True, help='Post ID is required')
       
class GetIfChatExists(Resource):
    def post(self):
        args = check_chat_args.parse_args()
        chats = Chat.query.filter_by(post_id=args['post_id']).all()

        check = any(chat.sender_username == args['username'] for chat in chats)

        if check:
            for chat in chats:
                if chat.sender_username == args['username']:
                    return_chat_id = chat.id
                    break
            else:
                # This block is executed if the loop completes without break
                return_chat_id = "none"
        else:
            return_chat_id = "none"

        response_data = {
            'result': str(check),
            'return_chat_id': return_chat_id
        }

        response = jsonify(response_data)
        return response

       
user_info_fields = {
    'other_username': fields.String,
    'post_id': fields.Integer,
}

class GetOtherUser(Resource):
    @marshal_with(user_info_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('chat_id', type=int, required=True, help='Chat ID is required')
        parser.add_argument('username', type=str, required=True, help='Username is required')
        args = parser.parse_args()

        chat = Chat.query.get_or_404(args['chat_id'])

        if args['username'] == chat.sender_username:
            other_username = chat.receiver_username
        elif args['username'] == chat.receiver_username:
            other_username = chat.sender_username
        else:
            return {'error': 'Provided username is not part of the chat'}, 400

        return {'other_username': other_username, 'post_id': chat.post_id}