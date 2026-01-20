import time
from pymodbus.client import ModbusTcpClient, ModbusSerialClient
from .globals import CURRENT_CONFIG

def trigger_plc(cam_id):
    if not CURRENT_CONFIG.get('modbus_enabled'): return

    try:
        conf = CURRENT_CONFIG
        # Ambil coil sesuai mapping kamera
        coil = int(conf['plc_coils'].get(str(cam_id), 0))
        slave = int(conf.get('modbus_slave', 1))
        
        client = None
        if conf.get('modbus_type') == 'tcp':
            client = ModbusTcpClient(conf.get('modbus_ip'), port=int(conf.get('modbus_port', 502)))
        else:
            client = ModbusSerialClient(port=conf.get('modbus_com'), baudrate=int(conf.get('modbus_baud', 9600)), method='rtu')

        if client.connect():
            # Logic: ON -> Sleep 1s -> OFF
            client.write_coil(coil, True, slave=slave)
            time.sleep(1)
            client.write_coil(coil, False, slave=slave)
            client.close()
            print(f"✅ PLC Triggered: Cam {cam_id} -> Coil {coil}")
        else:
            print("❌ PLC Connection Failed")
    except Exception as e:
        print(f"⚠️ PLC Error: {e}")