from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
from .models import Comment
from .serializer import CommentSerializer
from utils import customResponse

@api_view(['GET'])
def blog_comments(request , id) : 
    comments = CommentSerializer(Comment.objects.filter(blogId = id) , many = True)        
    return Response(customResponse(status= "success" , data = comments.data,message = None)
                   , status= status.HTTP_200_OK)


@api_view(['POST'])
def blog_add_comments(request) : 
        comment_details = request.data
        serializer = CommentSerializer(data=comment_details)

        if serializer.is_valid() : 
            # check with BlogService that blogId exists
            blogId = request.data['blogId']
            checkBlogResponse = requests.get(f'http://127.0.0.1:8000/api/blogs/{blogId}')
            if str(checkBlogResponse.status_code) == '404' : 
                return Response(customResponse(status="fail" , message= "blogId does not exist") ,
                         status= status.HTTP_400_BAD_REQUEST)
            
            serializer.save()   
            return Response(customResponse(status="success" , message= "added succesfully") 
                           , status= status.HTTP_201_CREATED)
        
        return Response(customResponse(status="fail" , message=  serializer.errors) ,
                         status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'  , 'PUT'])
def comments_get_put(request , id) : 
    comment_id = int(id) 
    try :                   
        curr_comment = Comment.objects.get(id = comment_id)     
        if request.method == 'GET' : 
            serializer = CommentSerializer(curr_comment)  
            return Response(customResponse(status="success" ,data= serializer.data ) ,  
                            status= status.HTTP_200_OK)
    
        if request.method == 'PUT' : 
            serializer = CommentSerializer(curr_comment, data = request.data)  
            if serializer.is_valid() : 
                serializer.save()  
                return Response(customResponse(status="success" , message= "updated succesfully")
                                , status= status.HTTP_200_OK)
        
            return Response(customResponse(status="fail" , message=  serializer.errors) 
                            , status= status.HTTP_400_BAD_REQUEST)
    
    except Comment.DoesNotExist: 
        return Response(customResponse(status="fail" , message= "comment not found") 
                        , status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def blog_delete_comments(request , id) : 
    try : 
        comments = Comment.objects.filter(blogId = id)  
        for comment in comments: 
            # delete any reaction for this comment and delete current comment
            data = {"targetType" : "comment"}
            try : 
                currResp = requests.delete(f'http://127.0.0.1:8002/api/reactions/delete/{id}', data=data)
                if str(currResp.status_code) == '500' :
                    # add to log for deleting undeleted reactions 
                    print('reactions not deleted') 

            except Exception as e : 
                print(e)
                return Response(customResponse(status="fail" , message= "internal server error"),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR )
            
            comment.delete()     

        return Response(customResponse(status="success" , message= "deleted successfully") 
                         , status= status.HTTP_200_OK)
    except Exception as e:
        print('exception occured while deleting', e) # log
        return Response(customResponse(status="fail" , message= "internal server error"),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR )


