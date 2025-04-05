from app.controllers.user_controller import UserResource, UserListResource

def register_routes(api):
    """
    Register all API routes
    """
    # User routes
    api.add_resource(UserListResource, '/api/users')
    api.add_resource(UserResource, '/api/users/<string:user_id>')