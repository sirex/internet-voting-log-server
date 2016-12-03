from django.db import models


class Vote(models.Model):
    # Voter ballot id (base32 uuid4) will be published, should not be associated with voter id.
    ballot_id = models.CharField(max_length=36)
    timestamp = models.DateTimeField()
    encrypted_vote = models.TextField()
    vote_hash = models.CharField(max_length=255)
