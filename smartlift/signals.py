from dmqtt.signals import connect, regex, topic,message

from django.db.models.signals import post_save

from django.dispatch import receiver
from smartlift.models import LiftEnvironmentLog
from smartlift.models import LiftControlLog
from smartlift.models import LiftDoorEventLog
from smartlift.models import LiftOccupancyLog
from smartlift.models import EnergyMeterLog
from smartlift.models import LiftFloorEventLog
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



@receiver(connect)
def on_connect(sender, **kwargs):
    sender.subscribe("#")

@topic("lift1\\join")
def simple_topic(sender, topic, data, **kwargs):
    print(data, "------------------------------------------joined the network")

# Mapping text values to door events
DOOR_TEXT_CODES = {
    "767724a46c6b": "open",   # Example: door open
    "76772ce9506b": "close",  # Example: door close
}



Kp = 1       # Power scaling
Ki = 1       # Current scaling
Kvp = 0.1    # Voltage scaling (e.g., 2245 = 224.5V)

@receiver(post_save, sender=LiftEnvironmentLog)
def send_lift_env_log_ws(sender, instance, created, **kwargs):
    print("sad  ------------------------------------------")
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "lift_logs",
            {
                "type": "send_lift_log",
                "data": {
                    "device": instance.device_name,
                    "temperature": str(instance.temperature),
                    "humidity": str(instance.humidity),
                    "time": str(instance.gateway_time),
                },
            },
        )

@topic("lift1\\uplink")
def simple_topic(sender, topic, data, **kwargs):
    
    if data.get("deviceName") == "TEK102":
        try:
            log = LiftEnvironmentLog.objects.create(
                topic=topic.replace("\\", "/"),
                application_id=data.get("applicationID"),
                battery=data.get("battery"),
                cellular_ip=data.get("cellularIP", "0.0.0.0"),
                dev_eui=data.get("devEUI"),
                device_name=data.get("deviceName"),
                gateway_time=data.get("gatewayTime"),
                humidity=data.get("humidity"),
                temperature=data.get("temperature"),
                raw_payload=data
            )
            
            print(f"✅ {log.gateway_time} | {log.device_name} | Temp: {log.temperature}°C | Hum: {log.humidity}%")
        except Exception as e:
            print(f"❌ Error saving data: {e}")
    
    if data.get("deviceName") == "TEK300" and "text" not in data:
        try:
            log = LiftControlLog.objects.create(
                topic=topic.replace("\\", "/"),
                application_id=data.get("applicationID"),
                cellular_ip=data.get("cellularIP"),
                dev_eui=data.get("devEUI"),
                device_name=data.get("deviceName"),
                gateway_time=data.get("gatewayTime"),

                gpio_input_1=data.get("gpio_input_1"),
                gpio_input_2=data.get("gpio_input_2"),
                gpio_input_4=data.get("gpio_input_4"),
                gpio_output_1=data.get("gpio_output_1"),
                gpio_output_2=data.get("gpio_output_2"),
                gpio_counter_3=data.get("gpio_counter_3"),

                adv_1=data.get("adv_1"),
                adv_1_avg=data.get("adv_1_avg"),
                adv_1_max=data.get("adv_1_max"),
                adv_1_min=data.get("adv_1_min"),
                adv_2=data.get("adv_2"),
                adv_2_avg=data.get("adv_2_avg"),
                adv_2_max=data.get("adv_2_max"),
                adv_2_min=data.get("adv_2_min"),

                raw_payload=data
            )
            print(f"✅ {log.gateway_time} | {log.device_name} | DIN1: {log.gpio_input_1} | DIN2: {log.gpio_input_2} | DIN3: {log.gpio_counter_3} | DIN3: {log.gpio_input_4} ")
        except Exception as e:
            print(f"❌ Failed to save TEK300 control log: {e}")

    if data.get("deviceName") == "TEK300" and "text" in data:
        text = data.get("text", "").strip()

        if text.startswith("QR"):
            try:
                log = LiftFloorEventLog.objects.create(
                    topic=topic.replace("\\", "/"),
                    application_id=data.get("applicationID"),
                    cellular_ip=data.get("cellularIP"),
                    dev_eui=data.get("devEUI"),
                    device_name=data.get("deviceName"),
                    gateway_time=data.get("gatewayTime"),
                    qr_code=text,
                    floor_number= text.split("Floor")[-1],
                    raw_payload=data
                )
                print(f"✅ {log.gateway_time} | {log.device_name} | QR: {log.qr_code} | Floor : {log.floor_number}")
            
            except Exception as e:
                print(f"❌ Failed to save floor QR log: {e}")
        else:
            try:
                # Clean and normalize text (remove \r\n)
                raw_text = text
                event_type = DOOR_TEXT_CODES.get(raw_text)

                if event_type is None:
                    print(f"⚠️ Unknown door event text: {raw_text} — Skipping")
                    return

                log = LiftDoorEventLog.objects.create(
                    topic=topic.replace("\\", "/"),
                    application_id=data.get("applicationID"),
                    cellular_ip=data.get("cellularIP"),
                    dev_eui=data.get("devEUI"),
                    device_name=data.get("deviceName"),
                    gateway_time=data.get("gatewayTime"),
                    text=raw_text,
                    event_type=event_type,
                    raw_payload=data
                )
                print(f"✅ {log.gateway_time} | {log.device_name} | Event: {log.event_type} | Text: {log.text}")

            except Exception as e:
                print(f"❌ Error saving door event: {e}")

    if data.get("deviceName") == "TEK121":
        try:
            log = LiftOccupancyLog.objects.create(
                topic=topic.replace("\\", "/"),
                application_id=data.get("applicationID"),
                cellular_ip=data.get("cellularIP"),
                dev_eui=data.get("devEUI"),
                device_name=data.get("deviceName"),
                gateway_time=data.get("gatewayTime"),
                people_count_all=data.get("people_count_all", 0),
                region_1=data.get("region_1"),
                region_count=data.get("region_count"),
                raw_payload=data
            )
            print(f"✅ {log.gateway_time} | {log.device_name} | Count: {log.people_count_all} | Entry: {log.region_count}")

        except Exception as e:
            print(f"❌ Error saving occupancy log: {e}")

    if data.get("deviceName") == "TEK100":
        try:
            modbus = data

            # Handle signed conversion (e.g., for kvar)
            def to_signed(val):
                return val - 65536 if val > 32767 else val
            
            modbus_chn_18 = modbus.get("modbus_chn_18", 0)
            modbus_chn_19 = modbus.get("modbus_chn_19", 0)
            modbus_chn_20 = modbus.get("modbus_chn_20", 0)
            modbus_chn_21 = modbus.get("modbus_chn_21", 0)

            e_scale = (modbus_chn_18 << 16) | modbus_chn_19
            kwh_raw = (modbus_chn_20 << 16) | modbus_chn_21
            kwh_value = kwh_raw * (10 ** -e_scale) * 10000

            log = EnergyMeterLog.objects.create(
                topic=topic.replace("\\", "/"),
                device_name=modbus.get("deviceName"),
                dev_eui=modbus.get("devEUI"),
                gateway_time=modbus.get("gatewayTime"),
                system_kw=modbus.get("modbus_chn_1", 0) * Kp,
                system_kva=modbus.get("modbus_chn_2", 0) * Kp,
                system_kvar=to_signed(modbus.get("modbus_chn_3", 0)) * Kp,
                system_pf=modbus.get("modbus_chn_4", 0) / 1000,
                frequency=modbus.get("modbus_chn_5", 0) / 10,

                phase1_volts=modbus.get("modbus_chn_6", 0) * Kvp,
                phase1_amps=modbus.get("modbus_chn_7", 0) * Ki,
                phase1_kw=modbus.get("modbus_chn_8", 0) * Kp,
                phase2_volts=modbus.get("modbus_chn_9", 0) * Kvp,
                phase2_amps=modbus.get("modbus_chn_10", 0) * Ki,
                phase2_kw=modbus.get("modbus_chn_11", 0) * Kp,
                phase3_volts=modbus.get("modbus_chn_12", 0) * Kvp,
                phase3_amps=modbus.get("modbus_chn_13", 0) * Ki,
                phase3_kw=modbus.get("modbus_chn_14", 0) * Kp,

                phase1_pf=modbus.get("modbus_chn_15", 0) / 1000,
                phase2_pf=modbus.get("modbus_chn_16", 0) / 1000,
                phase3_pf=modbus.get("modbus_chn_17", 0) / 1000,

                escale_high = modbus_chn_18,
                escale_low = modbus_chn_19,
                kwh_high = modbus_chn_20,
                kwh_low = modbus_chn_21,

                kwh_raw=kwh_raw,
                e_scale=e_scale,
                kwh_value=kwh_value,

                raw_payload=data
            )

            print(f"✅ Energy log saved: {log.gateway_time} | {log.device_name} | {log.system_kw} kW")

        except Exception as e:
            print(f"❌ Error saving energy meter data: {e}")

# @receiver(message)
# def handle_mqtt_message(sender, **kwargs):
#     msg = kwargs.get("msg")
#     if msg is not None:
#         topic = msg.topic
#         payload = msg.payload.decode() if isinstance(msg.payload, bytes) else msg.payload
#         print(f"[MQTT RECEIVED] Topic: {topic} | Payload: {payload}")
#     else:
#         print("[MQTT RECEIVED] Empty message or invalid format.")