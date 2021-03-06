from utilities.epoch_date_converter import EpochDateConverter


class SnapshotHistory:
    def __init__(self):
        self.snapshots = []

    def import_snapshot(self, snapshot):
        self.snapshots.append(snapshot)
        self.snapshots.sort(key=lambda x: x.timestamp)

    def all(self):
        return self.snapshots

    def value(self, query_time=None):
        if not self.snapshots:
            return 0
        if query_time is None:
            return self.__find_value(EpochDateConverter().date_to_epoch())
        return self.__find_value(query_time)

    def last_updated(self):
        timestamp = self.snapshots[-1].timestamp
        return EpochDateConverter().epoch_to_date(timestamp)

    def __find_value(self, query_time):
        value = 0
        for snapshot in self.snapshots:
            if query_time >= snapshot.timestamp:
                value = snapshot.value
        return value
