from customer.models import WishItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_wish(request, pk):
    WishItem.objects.create(customer=request.user.customer, product_id=pk)
    return Response({'result': 'added'}, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def remove_wish(request, pk):
    WishItem.objects.filter(customer=request.user.customer, product_id=pk).delete()
    return Response({'result': 'removed'}, status=status.HTTP_202_ACCEPTED)