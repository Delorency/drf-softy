from rest_framework.permissions import BasePermission



class TaskChangePermission(BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method == 'GET':
			return obj.task_backlogs.first().scrum_project.team.filter(
				user=request.user).exists()
		return obj.task_backlogs.first().scrum_project.team.filter(
			user=request.user, role='Project owner').exists()


class TaskChangeColumnPermission(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.workers.filter(user = request.user) and obj.close == False


class TaskItemChangePermission(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.taskitem_tasks.first().task_backlogs.first().scrum_project.team.filter(
			user=request.user, role='Project owner').exists()


class TaskItemChangeClosePermission(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.worker.user == request.user