import json
import hashlib
import collections

from logserver.models import Vote


def get_log_id():
    try:
        vote = Vote.objects.latest('id')
    except Vote.DoesNotExist:
        data = ''
    else:
        data = json.dumps(collections.OrderedDict([
            ('ballot_id', vote.ballot_id),
            ('timestamp', vote.timestamp.strftime('%Y-%m-%d %H:%M:%S')),
            ('encrypted_vote', vote.encrypted_vote),
            ('vote_hash', vote.vote_hash),
        ]))
    return hashlib.sha1(data.encode('utf-8')).hexdigest()
