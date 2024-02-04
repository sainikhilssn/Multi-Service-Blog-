# To run the application
1. In Multi Service Blog Folder , create a virtual environment 
```
python -m venv venv
```
2. Activate virtual environment by running Activate.ps1 in the venv/Scripts/ folder. Ex:

- Windows:
```Windows
& venv/Scripts/activate
```
- Linux:
```Linux
source venv/bin/activate
```

3. Install all required libraries listed in the requirements.txt
```
pip install -r requirements.txt
```
4. to start services
   Go to each service directory and run 
```
python manage.py runserver <PORT> 
```
```
BlogService port 8000
CommentService port 8001
ReactionService port 8002
```
5. By Default all services connect to a single sqlite3 db (we can also go for individual db for each service as services inter communicate for existance checking not foreignKey) .
6. Runs on localhost (127.0.0.1) . 
# About Application

## Database Model Parameters
## Blog
- id: Long
- title: String
- content: String

## Comment
- id: Long
- text: String

## Reaction
- id: Long
- type: ReactionType
- targetType: TargetType
- targetId: Long

## Port
- Blog-service: 8000
- Comment-service: 8001
- Reaction-service: 8002

## Tasks

### Blog Service
- Fetch a single blog using GET mapping with API endpoint `/api/blogs/{id}`. 
- Fetch all blogs using GET mapping with API endpoint `/api/blogs/`.
- Create a single blog using POST mapping with API endpoint `/api/blogs/`.
- Update a single blog using PUT mapping with API endpoint `/api/blogs/{id}`.
- Delete a single blog using DELETE mapping with API endpoint `/api/blogs/{id}`.
- Search for blogs using GET mapping with API endpoint `/api/blogs/search`.

### Comment Service
- Fetch comments for a specific blog using GET mapping with API endpoint `/api/comments/blog/{id}`.
- Add a comment for a blog using POST mapping with API endpoint `/api/comments`.
- Fetch a single comment using GET mapping with API endpoint `/api/comments/{id}`.
- Update a single comment using PUT mapping with API endpoint `/api/comments/{id}`.
- Delete all comments for a specific blog using DELETE mapping with API endpoint `/api/comments/blog/{id}/comments`.

### Reaction Service
- Add a reaction to a specific blog or comment using POST mapping with API endpoint `/api/reactions/add`.
- Delete a specific reaction for the blog or comment using DELETE mapping with API endpoint `/api/reactions/delete/{id}`.
