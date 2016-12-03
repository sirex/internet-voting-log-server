import datetime

from logserver.models import Vote


def test_add_vote_error(app):
    resp = app.get('/add-vote/')
    assert resp.json == {'errors': 'Only POST method allowed.'}

    resp = app.post('/add-vote/', {})
    assert resp.json == {'errors': 'Only application/json requests are accepted.'}

    resp = app.post_json('/add-vote/', {})
    assert resp.json == {'errors': {
        'ballot_id': ['This field is required.'],
        'encrypted_vote': ['This field is required.'],
        'timestamp': ['This field is required.'],
        'vote_hash': ['This field is required.'],
    }}


def test_add_vote(app):
    resp = app.post_json('/add-vote/', {
        'ballot_id': '123',
        'encrypted_vote': 'enc',
        'timestamp': '2016-01-01 00:00:00',
        'vote_hash': 'hash',
    })
    assert resp.json == {'status': 'ok'}
    assert Vote.objects.filter(ballot_id='123').exists()


def test_all_votes(app):
    Vote.objects.create(
        ballot_id='123',
        timestamp=datetime.datetime(2016, 1, 1),
        encrypted_vote='enc',
        vote_hash='hash',
    )
    assert app.get('/').json == {
        'votes': [{
            'ballot_id': '123',
            'encrypted_vote': 'enc',
            'timestamp': '2016-01-01 00:00:00',
            'vote_hash': 'hash',
        }],
    }
