from resources.auth import RegisterResource, LoginResource

routes = (
    (RegisterResource, '/register/'),
    (LoginResource, '/login/'),

)