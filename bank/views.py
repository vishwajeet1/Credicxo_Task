from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Branches, Banks
from .serializers import BranchSerializer, BankSerializer
from django.core import serializers

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def branchDetail(request):
    '''
           {
               "ifsc":"ABHY0065001"
                }
    '''
    try:
        ifsc_code = request.data['ifsc']
        branch = Branches.objects.get(ifsc=ifsc_code)
        return JsonResponse(
            {
                "status": True,
                "data": {
                    "user_data": {
                        "ifsc": branch.ifsc,
                        "bank_name": branch.bank.name,
                        "branch": branch.branch,
                        "address": branch.address,
                        "city": branch.city,
                        "district": branch.district,
                        "state": branch.state
                    }
                }
            }, status=status.HTTP_200_OK)

        # ['ifsc','bank','branch','address','city','district','state']
    except Exception as e:
        s = "Error {0}".format(str(e))  # string
        msg = s.encode("utf-8")
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": msg})


@api_view(['POST'])
@csrf_exempt
def allBranch(request):
    '''
        {
            "bankName":"BANK OF BARODA",
            "city":"GAMBHIRA"
            }
    '''
    try:
        bankName = request.data['bankName']
        city = request.data['city']
        bank = Banks.objects.get(name=bankName)
        bankId = bank.id
        branchList = Branches.objects.filter(bank=bankId, city=city)
        print(branchList)
        i = 0
        data = {}
        for e in branchList:
            data[i] = {
                "ifsc": e.ifsc,
                "bank_name": e.bank.name,
                "branch": e.branch,
                "address": e.address,
                "city": e.city,
                "district": e.district,
                "state": e.state
            }
            i += 1
        return JsonResponse(
            {
                "status": True,
                "data": data
            }, status=status.HTTP_200_OK)

        # ['ifsc','bank','branch','address','city','district','state']
    except Exception as e:
        s = "Error {0}".format(str(e))  # string
        msg = s.encode("utf-8")
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": msg})
