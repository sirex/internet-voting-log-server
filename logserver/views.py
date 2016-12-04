import json
import datetime

from django.http import JsonResponse

from logserver.forms import VoteForm
from logserver.models import Vote
from logserver.services import get_log_id


def add_vote(request):
    if request.method == "POST":
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            return JsonResponse({'errors': 'Only application/json requests are accepted.'})
        form = VoteForm(data)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.timestamp = datetime.datetime.now()
            vote.log_id = get_log_id()
            vote.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'errors': form.errors})
    else:
        return JsonResponse({'errors': 'Only POST method allowed.'})


def all_votes(request):
    return JsonResponse({'votes': [{
        'ballot_id': x.ballot_id,
        'timestamp': x.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'encrypted_vote': x.encrypted_vote,
        'vote_hash': x.vote_hash,
    } for x in Vote.objects.order_by('timestamp')]})
