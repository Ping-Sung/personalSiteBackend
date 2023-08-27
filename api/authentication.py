from rest_framework.authentication import TokenAuthentication as BaseTokenAuthentication

class TokenAuthentication(BaseTokenAuthentication):
    # this class overwrites the keyword attribute of the BaseTokenAuthentication class
    # can also change the model attribute as well (like JWTAuthentication)
    keyword = 'Bearer'