from django.db import models
from django.contrib.auth import get_user_model

from utils.mixins import ObjMixin



# class CheckList_item(ObjMixin):
# 	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')

# 	done = models.BooleanField(default=False, verbose_name='Done')

# 	taskcard = models.OneToOneField('TaskCard', on_delete=models.CASCADE,
# 		related_name='taskcard_checklistitems', verbose_name='TaskCard')

# 	def __str__(self):
# 		return f'id: {self.id}'


# 	class Meta:
# 		verbose_name_plural = 'CheckList_items'
# 		verbose_name = 'CheckList_item'
# 		ordering = ('updated_at',)

		

class TaskCard(ObjMixin):

	COLUMNS = [
		("ToDO", "To do"),
		("InProgress", "In progress"),
		("ToReview", "To review"),
		("Done", "Done")
	]

	column = models.CharField(
		max_length=10,
		choices=COLUMNS,
		default='To do',
	)

	description = models.CharField(max_length=1000, null=True, blank=True,
		verbose_name='Description')
	worker = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
		related_name='user_taskcard_workers', null=True, blank=True,
		verbose_name='Worker')
	creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
		related_name='user_taskcard_creators', verbose_name='Creator')

	date = models.DateTimeField(null=True, blank=True, verbose_name='Date')


	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		verbose_name_plural = 'TaskCards'
		verbose_name = 'TaskCard'
		ordering = ('created_at',)