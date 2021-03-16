# Rest api urls file.
from rest_framework.routers import SimpleRouter
from .import api
# from .api_collection import virtual_operations


urlpatterns = [
]

router = SimpleRouter(trailing_slash=False)
router.register(r'get_ticket_details', api.GetTicketDetails, "GetTicketDetails"),
router.register(r'get_os_ticket_status',api.GetOsTicketStatus,"GetOsTicketStatus")
router.register(r'get_status_of_list_of_ticket_id',api.GetStatusOfListOfTicketId,"GetStatusOfListOfTicketId")
router.register(r'get_help_topic',api.GetHelpTopic,"GetHelpTopic")
router.register(r'update_ticket',api.UpdateTicket,"UpdateTicket")
router.register(r'get_ticket_history',api.GetTicketHistory,"GetTicketHistory")
router.register(r'get_ticket_status',api.GetTicketStatus,"GetTicketStatus")

urlpatterns += router.urls
