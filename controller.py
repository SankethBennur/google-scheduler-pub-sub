from daily_reports import *
from instagram_ad_insights import *


def perform_task(message):
    """
    """
    data = message.data.decode('utf-8')
    attributes = dict(message.attributes)
    T = None

    msg_dict = {
        "data": data,
        "attributes": attributes
    }

    if("daily report" in data.lower()):
        T = daily_reports(msg_dict)
    elif("instagram ad" in data.lower()):
        T = instagram_ad_insights(msg_dict)

    try:
        T.print_message()

    except Exception as e:
        print(e)


