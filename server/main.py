from flask import Flask
from data_base.main import create_user_in_db, check_api_key, add_promt_to_user, create_user_in_db

app = Flask(__name__)


@app.route("/<api_key>/<prompt>")
def main(api_key, prompt):
    return preprop(api_key, prompt)


def preprop(api_key, prompt):
    if check_api_key(api_key):
        add_promt_to_user(api_key, prompt)
        return '200 OK'
    else:
        create_user_in_db(api_key)
        add_promt_to_user(api_key, prompt)
        return '200 OK'


if __name__ == "__main__":
    app.run(debug=True)
