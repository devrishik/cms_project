from tastypie.resources import ModelResource
from core.models import User

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		allowed_methods = ['get']