from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q
from .models import Reaction
from .serializer import ReactionSerializer
from utils import customResponse


@api_view(['POST'])
def reactions_post(request) : 
        reaction_details = request.data
        serializer = ReactionSerializer(data= reaction_details)
        if serializer.is_valid() : 
            serializer.save()   
            return Response(customResponse(status="success" , message= "added succesfully") 
                           , status= status.HTTP_201_CREATED)
        
        return Response(customResponse(status="fail" , message=  serializer.errors) ,
                         status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def reaction_delete(request , id) : 
    try : 
        # get the reaction based on type and typeId 
        reaction = Reaction.objects.get(Q(typeId = id) & Q(targetType = request.data['targetType'])) 
        reaction.delete()     
        return Response(customResponse(status="success" , message= "deleted successfully") 
                         , status= status.HTTP_200_OK)
    except Reaction.DoesNotExist:
        return Response(customResponse(status="fail" , message= "reaction does not exist"),
                        status=status.HTTP_404_NOT_FOUND )
    except Exception as e:
        print('exception deleting reaction ' + id  , e)  # log
        return Response(customResponse(status="fail" , message= "internal server error"),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR )


