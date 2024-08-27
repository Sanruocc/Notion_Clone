from utils.data_handler import DataHandler

class EventManager:
    def __init__(self):
        self.data_handler = DataHandler("data/events.json")

    def add_event(self, name, start_time, end_time):
        event = {
            "name": name,
            "start_time": start_time,
            "end_time": end_time
        }
        self.data_handler.create(name, event)

    def get_events(self):
        events = self.data_handler.read_data()
        return list(events.values()) if events else []