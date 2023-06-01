# Create your views here.


from django.shortcuts import render
import cv2
import numpy as np
from django.http import HttpResponse


def grayscale_view(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        nparr = np.fromstring(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        retval, buffer = cv2.imencode('.jpg', gray)
        image = buffer.tobytes()
        return HttpResponse(image, content_type="image/jpeg")

    return render(request, 'grayscale.html')
