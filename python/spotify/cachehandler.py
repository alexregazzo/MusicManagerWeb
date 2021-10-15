from datetime import datetime, timezone

from spotipy import CacheHandler

import python.database.fastcode as fdb


class StorageTokenHandler(CacheHandler):
    def __init__(self, use_id):
        self.use_id = use_id

    def get_cached_token(self):
        tok = fdb.selectToken(self.use_id)
        if tok is None:
            return None
        return {
            'user_id': self.use_id,
            'access_token': tok['tok_token'],
            'token_type': tok['tok_token_type'],
            'scope': tok['tok_token_scope'],
            'expires_in': tok['tok_token_expires_in'],
            'refresh_token': tok['tok_token_refresh'],
            'expires_at': tok['tok_token_expires_at'],
            'tok_last_updated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }

    def save_token_to_cache(self, token_info):
        dic = {
            'user_id': self.use_id,
            'tok_token': token_info['access_token'],
            'tok_token_type': token_info['token_type'],
            'tok_token_scope': token_info['scope'],
            'tok_token_expires_in': token_info['expires_in'],
            'tok_token_refresh': token_info['refresh_token'],
            'tok_token_expires_at': token_info['expires_at'],
            'tok_last_updated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f%z')
        }
        fdb.createUpdateToken(**dic)
