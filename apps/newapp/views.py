from django.views.generic import base
from django.template.response import TemplateResponse


class IndexView(base.View):
	ALLOWED_METHODS = ('GET', )
	template = 'newapp/index.html'

	def get(self, request, *args, **kwargs):
		context = {}
		context.update({
			'some': 'value',
		})
		return TemplateResponse(
            request=self.request, template=self.template,
            context=context)


