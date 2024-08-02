def update_user_rating(user):
    user_info = user.user_info
    feedbacks = user.feedbacks.all()
    user_info.rating = sum([feedback.mark for feedback in feedbacks]) / len(feedbacks)
    user_info.save()
