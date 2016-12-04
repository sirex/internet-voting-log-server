from django import forms


from logserver.models import Vote


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['ballot_id', 'encrypted_vote', 'vote_hash']
