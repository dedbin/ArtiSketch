import logging
from flask import Flask
from data_base.main import *

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/<api_key>/<prompt>")
def main(api_key, prompt):
    logging.info(f"Received request with api_key='{api_key}' and prompt='{prompt}'")
    return preprop(api_key, prompt)

def preprop(api_key, prompt):
    if isinstance(prompt, int):
        logging.info("Prompt is about number of generations")
        return num_gens(api_key)
    
    if check_api_key(api_key):
        logging.debug("API key is valid")
        add_promt_to_user(api_key, prompt)
        logging.info("Added prompt to user")
        return '200 OK'
    
    else:
        logging.debug("API key is invalid")
        create_user_in_db(api_key)
        logging.info("Created user in db")
        add_promt_to_user(api_key, prompt)
        logging.info("Added prompt to user")
        return '200 OK'


if __name__ == "__main__":
    app.run(debug=True)