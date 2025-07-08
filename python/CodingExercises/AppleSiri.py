"""
Assume we have real-time stream of user interaction events from a website. We want to build a system that can maintain the state of all active user sessions. Your task is to write a function that processes a batch of these events. return a dictionary of the final, active sessions, keyed by user_id. The session info for each user should contain:

* session_id
* start_ts (the timestamp of the SESSION_START event)
* last_seen_ts (the timestamp of the user's most recent event)
* pages_viewed (unique page paths visited per session)
* cart_items (a dictionary of item_id to quantity)
* cart_total_value (a float, calculated using the price_catalog)
# When you encounter event type as SESSION_END then remove all the items for that given user id.
"""

def solution(events_log, price_catalog):
    result_dict = {}

    for element in events_log:

        if element['user_id'] in result_dict.keys():
            if element['event_type'] == 'PAGE_VIEW':
                if 'pages_viewed' not in result_dict[element['user_id']].keys():
                    result_dict[element['user_id']]['pages_viewed'] = []
                result_dict[element['user_id']]['pages_viewed'].append(element['data']['path'])

                result_dict[element['user_id']]['last_seen_ts'] = element["timestamp"]

            elif element['event_type'] == 'ADD_TO_CART':
                if 'cart_items' not in result_dict[element['user_id']].keys():
                    result_dict[element['user_id']]['cart_items'] = {}

                if element['data']['item_id'] not in result_dict[element['user_id']]['cart_items'].keys():
                    result_dict[element['user_id']]['cart_items'][element['data']['item_id']] = element['data']['quantity']

                else:
                    result_dict[element['user_id']]['cart_items'][element['data']['item_id']] = \
                    result_dict[element['user_id']]['cart_items'][element['data']['item_id']] + element['data'][
                        'quantity']

                if 'cart_total_value' not in result_dict[element['user_id']].keys():
                    result_dict[element['user_id']]['cart_total_value'] = price_catalog[element['data']['item_id']] * element['data']['quantity']
                else:
                    result_dict[element['user_id']]['cart_total_value'] = result_dict[element['user_id']]['cart_total_value'] +  (price_catalog[element['data']['item_id']] * element['data']['quantity'])

                result_dict[element['user_id']]['last_seen_ts'] = element["timestamp"]

            elif element['event_type'] == 'REMOVE_FROM_CART':

                if element['data']['item_id'] not in result_dict[element['user_id']]['cart_items'].keys():
                    pass
                else:
                    result_dict[element['user_id']]['cart_items'][element['data']['item_id']] = \
                    result_dict[element['user_id']]['cart_items'][element['data']['item_id']] - element['data'][
                        'quantity']
                    result_dict[element['user_id']]['cart_total_value'] = result_dict[element['user_id']]['cart_total_value'] - (price_catalog[element['data']['item_id']] * element['data']['quantity'])
                    if result_dict[element['user_id']]['cart_items'][element['data']['item_id']] == 0:
                        del result_dict[element['user_id']]['cart_items'][element['data']['item_id']]

                result_dict[element['user_id']]['last_seen_ts'] = element["timestamp"]

            elif element['event_type'] == 'SESSION_END':
                result_dict[element['user_id']] = {}

        else:
            if element['event_type'] == "SESSION_START":
                result_dict[element['user_id']] = {}
                result_dict[element['user_id']]["session_id"] = element["session_id"]
                result_dict[element['user_id']]['start_ts'] = element["timestamp"]
                result_dict[element['user_id']]['last_seen_ts'] = element["timestamp"]

    return result_dict

def main():

    events_log = [
        {"event_type": "SESSION_START", "user_id": 101, "session_id": "sess_abc_123", "timestamp": 1672531200},
        {"event_type": "PAGE_VIEW", "user_id": 101, "timestamp": 1672531215, "data": {"path": "/"}},
        {"event_type": "SESSION_START", "user_id": 202, "session_id": "sess_def_456", "timestamp": 1672531220},
        {"event_type": "ADD_TO_CART", "user_id": 101, "timestamp": 1672531230,
         "data": {"item_id": "item_abc", "quantity": 1}},
        {"event_type": "PAGE_VIEW", "user_id": 101, "timestamp": 1672531260, "data": {"path": "/products/item_abc"}},
        {"event_type": "ADD_TO_CART", "user_id": 202, "timestamp": 1672531275,
         "data": {"item_id": "item_xyz", "quantity": 1}},
        {"event_type": "ADD_TO_CART", "user_id": 101, "timestamp": 1672531280,
         "data": {"item_id": "item_abc", "quantity": 1}},
        {"event_type": "SESSION_END", "user_id": 202, "timestamp": 1672531285},
        {"event_type": "ADD_TO_CART", "user_id": 101, "timestamp": 1672531290,
         "data": {"item_id": "item_xyz", "quantity": 1}},
        {"event_type": "REMOVE_FROM_CART", "user_id": 101, "timestamp": 1672531295,
         "data": {"item_id": "item_abc", "quantity": 1}}
    ]

    # Price Catalog
    price_catalog = {
        "item_abc": 10.50,
        "item_xyz": 5.00,
        "item_pqr": 99.99,
    }

    result_dict = {}
    result_dict[101] = {
        "session_id": "sess_abc_123",
        "start_ts": 1672531200,
        "last_seen_ts": 1672531295,
        "pages_viewed": ["/", "/products/item_abc"],
        "cart_items": {"item_abc": 1, "item_xyz": 1 },
        "cart_total_value": 15.50
    }

    result_dict[202] = {}

    assert result_dict == solution(events_log, price_catalog)

if __name__=='__main__':
    main()