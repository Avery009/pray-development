from django.db import models
from django.forms import ModelForm

# Create your models here.
prayerCategories = [
		('thanks','Thanksgiving'),
		('healing','Healing'),
		('trauma','Trauma'),
		('conversion','Conversion'),
		('belief','Belief'),
		('strength','Strength'),
		('leaders','Leaders'),
		('needs','Needs'),
		('forgiveness','Forgiveness'),
	]
class Prayer(models.Model):
	prayerCategoriesDefault = [('thanks'),('Thanksgiving')]
	prayer_id = models.BigAutoField(primary_key=True,unique=True)
	prayer_title = models.CharField(max_length=100, blank=False, null=False)
	prayer_request_date = models.DateField('prayer request date')
	prayer_answer_date = models.DateField('prayer answer date',blank=True,null=True)
	prayer_description = models.CharField(max_length=1000)
	prayer_recipients = models.CharField(max_length=100,blank=True,null=True)
	prayer_recipients_email = models.EmailField(max_length=100,blank=True,null=True)
	#prayer_categories = models.ManyToManyField(choices=prayerCategories,max_length=100,blank=False,default=prayerCategoriesDefault)
	prayer_answered = models.BooleanField(editable=True)
	prayer_updates = models.CharField(max_length=1400,blank=True,null=True)
	prayer_updates_user = models.CharField(max_length=30,blank=True,null=True)
	#prayer_image = models.ImageField(upload_to='prayer_images/%Y/%m/%d',blank=True,null=True)
	#prayer_answered_image = models.ImageField(upload_to='answered_prayer_images/%Y/%m/%d',blank=True,null=True)
	prayer_count = models.IntegerField(editable=True,null=False)
	def __str__(self):
		return self.prayer_id

class PrayerUpdates(models.Model):
	prayers = models.ManyToManyField(Prayer)

class PrayerForm(ModelForm):
	class Meta:
		model = Prayer
		fields = '__all__'

class PrayerUpdatesForm(ModelForm):
        class Meta:
				model = PrayerUpdates
				fields = ['prayer_id','prayer_title','prayer_description','prayer_count','prayer_updates','prayer_updates_user']
