from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .serializers import ServerSerializer, ChannelSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(name="category", type=OpenApiTypes.STR, description="Category of servers to retrieve.", location=OpenApiParameter.QUERY),
        OpenApiParameter(name="qty", type=OpenApiTypes.INT, description="Number of Serverts to retrieve", location=OpenApiParameter.QUERY),
        OpenApiParameter(name="by_user", type=OpenApiTypes.BOOL, description="Servers related to the current user.", location=OpenApiParameter.QUERY),
        OpenApiParameter(name="by_serverid", type=OpenApiTypes.STR, description="Retrive server by server ID.", location=OpenApiParameter.QUERY),
        OpenApiParameter(name="with_num_members", type=OpenApiTypes.BOOL, description="Contain the number of memberes", location=OpenApiParameter.QUERY),
        
        
        
    ]
)