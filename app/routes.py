from flask import jsonify
from app import app, db
from app.models import User, Prompt
import logging
from api_for_sd import api
import config

@app.route('/<api_key>/post_prompt/<text>', methods=['POST'])
def post_prompt(api_key, text):
    user = User.query.get(api_key)
    sd = api.WebUIApi(config.BASE_URL)
    if user:
        user.num_prompts += 1
        pic = sd.prompt_to_image(text)
        prompt = Prompt(prompt_text=text, user=user, photo_path=pic) #TODO: do saving picture to db
        db.session.add(prompt)
        db.session.commit()
        logging.info(f"Prompt added to user {api_key} successfully")
        return jsonify({"message": "Prompt added successfully", "pic": pic}), 200
    else:
        logging.error("User not found")
        return jsonify({"error": "User not found"}), 404


@app.route('/<api_key>', methods=['GET'])
def get_user(api_key):
    user = User.query.get(api_key)
    if user:
        user_data = {
            "api_key": user.api_key,
            "num_prompts": user.num_prompts,
            "language": user.language
        }
        logging.info(f"User found: {user_data}")
        return jsonify(user_data), 200
    else:
        logging.error("User not found")
        return jsonify({"error": "User not found"}), 404


@app.route('/<api_key>/<prompt_id>', methods=['GET'])
def get_prompt(api_key, prompt_id):
    prompt = Prompt.query.get(prompt_id)
    if prompt and prompt.user.api_key == api_key:
        prompt_data = {
            "prompt_id": prompt.prompt_id,
            "prompt_text": prompt.prompt_text,
            "photo_path": prompt.photo_path,
            "coords": prompt.coords
        }
        logging.info("Prompt retrieved successfully")
        return jsonify(prompt_data), 200
    else:
        logging.error("Prompt not found")
        return jsonify({"error": "Prompt not found"}), 404


@app.route('/<api_key>/all', methods=['GET'])
def get_all_prompts(api_key):
    logging.info(f'Received GET request for all prompts from {api_key}')
    user = User.query.get(api_key)
    if user:
        prompts = Prompt.query.filter_by(user_api_key=api_key).all()
        prompts_data = [
            {
                "prompt_id": prompt.prompt_id,
                "prompt_text": prompt.prompt_text,
                "photo_path": prompt.photo_path,
                "coords": prompt.coords
            }
            for prompt in prompts
        ]
        logging.info('Returning prompts data')
        return jsonify(prompts_data), 200
    else:
        logging.error('User not found')
        return jsonify({"error": "User not found"}), 404