
from app import db

class User(db.Model):
    api_key = db.Column(db.String(50), primary_key=True)
    num_prompts = db.Column(db.Integer, default=0)
    language = db.Column(db.String(10), default='ru')
    prompts = db.relationship('Prompt', backref='user', lazy=True)


class Prompt(db.Model):
    promt_id = db.Column(db.Integer, primary_key=True)
    promt_text = db.Column(db.Text)
    photo_path = db.Column(db.String(255))
    coords = db.Column(db.String(255))
    user_api_key = db.Column(db.String(50), db.ForeignKey('user.api_key'), nullable=False)
