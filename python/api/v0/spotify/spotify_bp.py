import json

import spotipy
from flask import Blueprint, request, Response, url_for, redirect

import settings
from python.api.utils import ensure_response
from python.spotify.cachehandler import StorageTokenHandler

spotify_blueprint = Blueprint('spotify', __name__, url_prefix='/spotify')


def get_auth_manager(use_id):
    cache_handler = StorageTokenHandler(use_id=use_id)
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        client_id=settings.CLIENT_ID,
        client_secret=settings.CLIENT_SECRET,
        redirect_uri=url_for('api.v0.spotify.connect_to_spotify', _external=True),
        scope=settings.SCOPES,
        cache_handler=cache_handler,
        state=F'#{use_id}',
        show_dialog=True)
    return cache_handler, auth_manager


@spotify_blueprint.route("/connect")
@ensure_response
def connect_to_spotify():
    use_id = int(request.args['state'][1:])
    cache_handler, auth_manager = get_auth_manager(use_id)
    code = request.args["code"]
    auth_manager.get_access_token(code)
    if settings.PRODUCTION:
        return redirect(url_for('/'))
    return redirect("http://localhost:3000/")


@spotify_blueprint.route("/isconnected")
@ensure_response
def is_connected():
    use_id = request.args['id']
    cache_handler, auth_manager = get_auth_manager(use_id)
    isvalid = auth_manager.validate_token(cache_handler.get_cached_token())
    auth_url = auth_manager.get_authorize_url()

    return Response(json.dumps({
        'is_connected': isvalid is not None,
        'connect_link': auth_url
    }, indent=4, ensure_ascii=False),
        status=200,
        content_type='application/json')
