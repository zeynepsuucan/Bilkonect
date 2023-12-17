from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.models import db, UserModel
import re

login_args = reqparse.RequestParser()
login_args.add_argument('username', type=str, required=True, help='Username is required')
login_args.add_argument('password', type=str, required=True, help='Password is required')

# Assuming you have a marshal definition for the user resource fields
user_resource_fields = {
    'bilkent_id': fields.Integer,
    'username': fields.String,
    'usertype': fields.String,
    'email': fields.String,
    'score': fields.Integer,
}

class LoginResource(Resource):

    @marshal_with(user_resource_fields)
    def post(self):
        args = login_args.parse_args()
        username = args['username']
        password = args['password']

        user = UserModel.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            return user, 200
        else:
            abort(401, message='Invalid credentials')


# Define the parser for registration arguments
register_args = reqparse.RequestParser()
register_args.add_argument('bilkent_id', type=int, required=True, help='Bilkent ID is required')
register_args.add_argument('username', type=str, required=True, help='Username is required')
register_args.add_argument('password', type=str, required=True, help='Password is required')
register_args.add_argument('usertype', type=str, required=True, help='User type is required')
register_args.add_argument('email', type=str, required=True, help='Email is required')
register_args.add_argument('pp', type=str)

edit_args = reqparse.RequestParser()
edit_args.add_argument('bilkent_id', type=str, required = True)
edit_args.add_argument('username', type=str)
edit_args.add_argument('pp', type=str)

user_resource_fields = {
    'bilkent_id': fields.Integer,
    'username': fields.String,
    'usertype': fields.String,
    'email': fields.String,
    'score': fields.Integer,
    'pp': fields.String,
}

class RegisterResource(Resource):
    
    @marshal_with(user_resource_fields)
    def post(self):
        def validate_username(username):
            return not re.search(r'\s', username)
        
        args = register_args.parse_args()

        username = args['username']

        if not validate_username(username):
            abort(400, message="Username cannot contain spaces")

        existing_user = UserModel.query.filter_by(username=username).first()
        if existing_user:
            abort(409, message="Username is already taken")

        existing_email = UserModel.query.filter_by(email=args['email']).first()
        if existing_email:
            abort(409, message="Email address is already registered")

        existing_bilkent_id = UserModel.query.filter_by(bilkent_id=args['bilkent_id']).first()
        if existing_bilkent_id:
            abort(409, message="Bilkent ID already exists")

        # Hash the password before storing it
        hashed_password = generate_password_hash(args['password'], method='sha256')

        new_user = UserModel(
            bilkent_id=args['bilkent_id'],
            username=args['username'],
            password=hashed_password,
            usertype=args['usertype'],
            email=args['email'],
            pp =args['pp'],
            score=0,
            followers=0,
            following=0
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user, 201
    
    @marshal_with(user_resource_fields)
    def put(self):
        args = edit_args.parse_args()
        bilkent_id = args['bilkent_id']

        # Check if the course material post exists
        user = UserModel.query.get(bilkent_id)
        if not user:
            abort(404, message='User not found')

        # Update the post attributes
        if args['username'] is not None:
            user.username = args['username']
        if args['pp'] is not None:
            user.pp = args['pp']

        # Commit the changes to the database
        with current_app.app_context():
            db.session.commit()

        # Combine the course material post and post details in the response
        return user, 200

    
    