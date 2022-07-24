from django.http import JsonResponse
from rest_framework.decorators import api_view

from .util import image_upload_s3


@api_view(['GET', 'POST', 'PATCH'])
def images(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        return image_upload(request)


def image_upload(request):
    uploaded_image = request.FILES
    # url = image_upload_s3(uploaded_image, "hello")
    return JsonResponse({"message": uploaded_image}, status=401)
