from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Blog
from .serializer import BlogSerializer
from utils import customResponse 
import requests
from django.db.models import Q

@api_view(['GET' , 'POST'])
def blogs_get_post(request ) : 
    if request.method == 'GET' : 
        blogs = BlogSerializer(Blog.objects.all() , many = True)        
        return Response(customResponse(status = "success" , data = blogs.data) ,
                        status= status.HTTP_200_OK)

    if request.method == 'POST' : 
        blog_details = request.data
        # validate request data 
        serializer = BlogSerializer(data = blog_details)
        if serializer.is_valid() : 
            # add to the database
            serializer.save()   
            return Response(customResponse(status = "success",  message = "added successfully")
                            ,status= status.HTTP_201_CREATED)

        return Response(customResponse(status = "fail", message = serializer.errors)
                        ,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'  , 'PUT' , 'DELETE'])
def blogs_put_delete(request , id) : 
    blog_id = int(id) 
    try :                   
        curr_blog = Blog.objects.get(id = blog_id)          # will raise exception if not found 

        if request.method == 'GET' : 
            serializer = BlogSerializer(curr_blog)  
            return Response(customResponse(status  = "success", data = serializer.data)
                            ,status= status.HTTP_200_OK)
    
        if request.method == 'PUT' : 
            # passing (blog in db , blog in request) for updation 
            serializer = BlogSerializer(curr_blog , data = request.data)  
            if serializer.is_valid() : 
                # updating current blog entity in database
                serializer.save()  
                return Response(customResponse(status = "success", message = "updated succesfully")
                                , status= status.HTTP_200_OK)
            return Response(customResponse(status = "fail", message = serializer.errors)
                            , status= status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE' : 
            curr_blog.delete()
            # delete all of its comments and reactions 
            data = {"targetType" : "blog"}
            try : 
                delComment  = requests.delete(f'http://127.0.0.1:8001/api/comments/blog/{id}/comments')
                delReaction = requests.delete(f'http://127.0.0.1:8002/api/reactions/delete/{id}', data=data)

                if str(delComment.status_code) == '500' : 
                    print('comments not deleted for blog' ,  id)   # log , comment del failure case
                
                if str(delReaction.status_code) == '500' : 
                    print('reactions not deleted for blog ' , id)  # log  , reaction del failure case

            except Exception as e : 
                print(e)
                return Response(customResponse(status="fail" , message= "internal server error"),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR )
            
            return Response(customResponse(status = "success", message = "deleted successfully"), 
                            status= status.HTTP_200_OK)
        
    except Blog.DoesNotExist: 
        return Response(customResponse(status = "fail" , message = "blog does not exists")
                        , status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def blogs_search(request) : 
     query = request.GET.get('query')
     # basic search on query 
     results = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) ) 
     serializer = BlogSerializer(results , many  = True)
     return Response(customResponse(status = "success", message = serializer.data ), 
                            status= status.HTTP_200_OK)