from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fullname = models.CharField(max_length=100)
    user_username = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_contact = models.CharField(max_length=15)
    user_city = models.CharField(max_length=100)
    user_state = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='images/user')
    user_bgimage = models.ImageField(default='images/user/bg.jpg')
    user_status = models.CharField(default='Pending', max_length=50)

    class Meta:
        db_table = 'User_Details'


class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    feed_desc = models.TextField()
    feed_rating = models.CharField(default='0', max_length=100)
    feedback_sentiment = models.CharField(max_length=50)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_feedbacks')

    class Meta:
        db_table = 'feedback_details'
