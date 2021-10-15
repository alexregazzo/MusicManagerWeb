import os

from dotenv import load_dotenv

load_dotenv()

PSQL_DSN = F"postgresql://{os.environ['PSQL_USERNAME']}:{os.environ['PSQL_PASSWORD']}@" \
           F"{os.environ['PSQL_HOST']}:{os.environ['PSQL_PORT']}/{os.environ['PSQL_DATABASE']}"

ROOT_PATH = os.path.dirname(__file__)
PRODUCTION = os.environ.get('IS_HEROKU', 'false') == 'true'
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

SCOPES = ["playlist-modify-private",
          "playlist-read-private",
          "playlist-modify-public",
          "playlist-read-collaborative",
          "user-read-private",
          "user-read-email",
          "user-read-playback-state",
          "user-modify-playback-state",
          "user-read-currently-playing",
          "user-library-modify",
          "user-library-read",
          "user-read-playback-position",
          "user-read-recently-played",
          "user-top-read",
          "app-remote-control",
          "streaming"]
