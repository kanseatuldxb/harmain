from django.db import models

# Create your models here.
class LiftEnvironmentLog(models.Model):
    topic = models.CharField(max_length=255)
    application_id = models.IntegerField()
    battery = models.IntegerField(null=True, blank=True)
    cellular_ip = models.GenericIPAddressField(null=True, blank=True)
    dev_eui = models.CharField(max_length=32)
    device_name = models.CharField(max_length=100)
    gateway_time = models.DateTimeField()
    humidity = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)
    raw_payload = models.JSONField()

    def __str__(self):
        return f"{self.device_name} Temp: {self.temperature}°C | Hum: {self.humidity}% at {self.gateway_time}"

class LiftControlLog(models.Model):
    topic = models.CharField(max_length=255)
    application_id = models.IntegerField()
    cellular_ip = models.GenericIPAddressField(null=True, blank=True)
    dev_eui = models.CharField(max_length=32)
    device_name = models.CharField(max_length=100)
    gateway_time = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)

    # GPIO inputs/outputs
    gpio_input_1 = models.IntegerField(null=True, blank=True)
    gpio_input_2 = models.IntegerField(null=True, blank=True)
    gpio_input_4 = models.IntegerField(null=True, blank=True)
    gpio_output_1 = models.IntegerField(null=True, blank=True)
    gpio_output_2 = models.IntegerField(null=True, blank=True)
    gpio_counter_3 = models.IntegerField(null=True, blank=True)

    # ADC (analog) values
    adv_1 = models.FloatField(null=True, blank=True)
    adv_1_avg = models.FloatField(null=True, blank=True)
    adv_1_max = models.FloatField(null=True, blank=True)
    adv_1_min = models.FloatField(null=True, blank=True)
    adv_2 = models.FloatField(null=True, blank=True)
    adv_2_avg = models.FloatField(null=True, blank=True)
    adv_2_max = models.FloatField(null=True, blank=True)
    adv_2_min = models.FloatField(null=True, blank=True)

    raw_payload = models.JSONField()

    def __str__(self):
        return f"{self.device_name} control log @ {self.gateway_time}"
    

class LiftDoorEventLog(models.Model):
    topic = models.CharField(max_length=255)
    application_id = models.IntegerField()
    cellular_ip = models.GenericIPAddressField(null=True, blank=True)
    dev_eui = models.CharField(max_length=32)
    device_name = models.CharField(max_length=100)
    gateway_time = models.DateTimeField()
    text = models.TextField()
    event_type = models.CharField(max_length=10, choices=[("open", "Open"), ("close", "Close")])
    received_at = models.DateTimeField(auto_now_add=True)
    raw_payload = models.JSONField()

    def __str__(self):
        return f"{self.device_name} {self.event_type.upper()} @ {self.gateway_time}"

class LiftFloorEventLog(models.Model):
    topic = models.CharField(max_length=255)
    application_id = models.IntegerField()
    cellular_ip = models.GenericIPAddressField(null=True, blank=True)
    dev_eui = models.CharField(max_length=32)
    device_name = models.CharField(max_length=100)
    gateway_time = models.DateTimeField()

    qr_code = models.CharField(max_length=50)
    floor_number = models.CharField(max_length=10)

    received_at = models.DateTimeField(auto_now_add=True)
    raw_payload = models.JSONField()

    def __str__(self):
        return f"{self.device_name} → Floor {self.floor_number} @ {self.gateway_time}"
    
class LiftOccupancyLog(models.Model):
    topic = models.CharField(max_length=255)
    application_id = models.IntegerField()
    cellular_ip = models.GenericIPAddressField(null=True, blank=True)
    dev_eui = models.CharField(max_length=32)
    device_name = models.CharField(max_length=100)
    gateway_time = models.DateTimeField()
    people_count_all = models.IntegerField()
    region_1 = models.IntegerField(null=True, blank=True)
    region_count = models.IntegerField(null=True, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)
    raw_payload = models.JSONField()

    def __str__(self):
        return f"{self.device_name} - {self.people_count_all} people @ {self.gateway_time}"
    
class EnergyMeterLog(models.Model):
    topic = models.CharField(max_length=255)
    device_name = models.CharField(max_length=100)
    dev_eui = models.CharField(max_length=32)
    gateway_time = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)

    # Raw readings after scaling
    system_kw = models.FloatField(null=True, blank=True)
    system_kva = models.FloatField(null=True, blank=True)
    system_kvar = models.FloatField(null=True, blank=True)
    system_pf = models.FloatField(null=True, blank=True)
    frequency = models.FloatField(null=True, blank=True)

    phase1_volts = models.FloatField(null=True, blank=True)
    phase1_amps = models.FloatField(null=True, blank=True)
    phase1_kw = models.FloatField(null=True, blank=True)
    phase2_volts = models.FloatField(null=True, blank=True)
    phase2_amps = models.FloatField(null=True, blank=True)
    phase2_kw = models.FloatField(null=True, blank=True)
    phase3_volts = models.FloatField(null=True, blank=True)
    phase3_amps = models.FloatField(null=True, blank=True)
    phase3_kw = models.FloatField(null=True, blank=True)

    phase1_pf = models.FloatField(null=True, blank=True)
    phase2_pf = models.FloatField(null=True, blank=True)
    phase3_pf = models.FloatField(null=True, blank=True)

    escale_high = models.IntegerField(null=True, blank=True)           # modbus_chn_18 (Reg: 512)
    escale_low = models.IntegerField(null=True, blank=True)            # modbus_chn_19 (Reg: 513)

    kwh_high = models.IntegerField(null=True, blank=True)              # modbus_chn_20 (Reg: 514)
    kwh_low = models.IntegerField(null=True, blank=True)               # modbus_chn_21 (Reg: 515)

    kwh_raw = models.BigIntegerField(null=True, blank=True)
    e_scale = models.IntegerField(null=True, blank=True)
    kwh_value = models.FloatField(null=True, blank=True)


    raw_payload = models.JSONField()

    

    def __str__(self):
        return f"{self.device_name} | {self.gateway_time} | {self.system_kw} kW"

