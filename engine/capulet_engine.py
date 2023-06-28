from abc import ABC


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        raise NotImplementedError("needs_service() method must be implemented in subclass")


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 3
        if (today - last_service_date).days >= battery_service_interval:
            return True
        return False

    def engine_should_be_serviced(self):
        mileage_threshold = 30000
        if self.current_mileage - self.last_service_mileage >= mileage_threshold:
            return True
        return False


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 3
        if (today - last_service_date).days >= battery_service_interval:
            return True
        return False

    def engine_should_be_serviced(self):
        mileage_threshold = 60000
        if self.current_mileage - self.last_service_mileage >= mileage_threshold:
            return True
        return False


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 5
        if (today - last_service_date).days >= battery_service_interval:
            return True
        return False

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        return False


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 5
        if (today - last_service_date).days >= battery_service_interval:
            return True
        return False

    def engine_should_be_serviced(self):
        mileage_threshold = 60000
        if self.current_mileage - self.last_service_mileage >= mileage_threshold:
            return True
        return False


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        return False

    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = self.last_service_date
        battery_service_interval = 5
        if (today - last_service_date).days >= battery_service_interval:
            return True
        return False

    def engine_should_be_serviced(self):
        mileage_threshold = 30000
        if self.current_mileage - self.last_service_mileage >= mileage_threshold:
            return True
        return False
