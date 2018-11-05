from django.db import models
import uuid

class Event(models.Model):
	identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	abstract = models.TextField(max_length=3000)
	place = models.CharField(max_length=100)
	time = models.DateTimeField()
	title = models.CharField(max_length=300)
	details = models.TextField()

	REQUEST = (
		('non', 'No Request'),
		('add', 'Addition'),
		('del', 'Deletion'),
		('mod', 'Modification'),
	)
	req = models.CharField(max_length=3, choices = REQUEST, default='non')
	abstractReq = models.TextField(max_length=3000, default=None, null=True)
	placeReq = models.CharField(max_length=100, default=None, null=True)
	timeReq = models.DateTimeField(default=None, null=True)
	titleReq = models.CharField(max_length=300, default=None, null=True)
	detailsReq = models.TextField(default=None, null=True)

	rankingVector = models.DecimalField(decimal_places=0, max_digits=5, null=True)

	#TODO poster_image

	def generateRankingVector():
		pass
	
	def __str__(self):
		return str(self.identifier)


class Tag(models.Model):
	name = models.CharField(max_length=30)
	rankingScore = models.DecimalField(decimal_places=0, max_digits=5)

	def calculateRankingScore():
		pass



