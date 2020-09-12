from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def userprofile(request, username):
    user = get_object_or_404(User, username=username)

    number_of_votes = 0

    for story in user.stories.all():
        number_of_votes = number_of_votes + (story.number_of_votes - 1)
    
    return render(request, 'userprofile/userprofile.html', {'user': user, 'number_of_votes': number_of_votes})

def votes(request, username):
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()

    stories = []

    for vote in votes:
        stories.append(vote.story)
    
    return render(request, 'userprofile/votes.html', {'user': user, 'stories': stories})

def submissions(request, username):
    user = get_object_or_404(User, username=username)

    stories = user.stories.all()

    return render(request, 'userprofile/submissions.html', {'user': user, 'stories': stories})