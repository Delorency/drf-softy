from django.db import models
from django.contrib.auth import get_user_model



class Member(models.Model):
	COLUMNS = [
		("Backend", "Backend"),
		("Frontend", "Frontend"),
		("Design", "Design"),
		("Stakeholder", "Stakeholder"),
		("UX", "UX"),
		("Product owner", "Product owner")
	]
	role = models.CharField(
		max_length=20,
		choices=COLUMNS,
	)

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
		related_name='user_member', verbose_name='User')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')


	def __str__(self):
		return f'id: {self.id} | name: {self.user.username} | role: {self.role}'

	class Meta:
		verbose_name_plural = 'Members'
		verbose_name = 'Member'
		ordering = ('-created_at',)