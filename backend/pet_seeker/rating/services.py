from django.contrib.auth.models import User

def update_user_rating(user: User):
    user_info = user.user_info
    feedbacks = user.feedbacks.all()
    user_info.rating = sum([feedback.mark for feedback in feedbacks]) / len(feedbacks)
    user_info.save()
