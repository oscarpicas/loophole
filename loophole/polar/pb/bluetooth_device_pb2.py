# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bluetooth_device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2 as structures__pb2
import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bluetooth_device.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x62luetooth_device.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"K\n\tPbBleUser\x12\x12\n\nuser_index\x18\x01 \x02(\r\x12\x19\n\x11\x64\x65vice_user_index\x18\x02 \x02(\r\x12\x0f\n\x07\x63onsent\x18\x03 \x01(\r\"\x99\x18\n\x0bPbBleDevice\x12!\n\x06paired\x18\x01 \x02(\x0b\x32\x11.PbSystemDateTime\x12(\n\rlast_modified\x18\x02 \x02(\x0b\x32\x11.PbSystemDateTime\x12\x34\n\x0cmanufacturer\x18\x03 \x02(\x0e\x32\x1e.data.PbDeviceManufacturerType\x12-\n\x12\x64\x65leted_time_stamp\x18\x05 \x01(\x0b\x32\x11.PbSystemDateTime\x12\x16\n\x03mac\x18\x06 \x01(\x0b\x32\t.PbBleMac\x12\x11\n\tdevice_id\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x15\n\rbattery_level\x18\t \x01(\r\x12\x19\n\x11manufacturer_name\x18\n \x01(\t\x12\x12\n\nmodel_name\x18\x0b \x01(\t\x12\x10\n\x08peer_ltk\x18\x0c \x01(\x0c\x12\x10\n\x08peer_irk\x18\r \x01(\x0c\x12\x11\n\tpeer_csrk\x18\x0e \x01(\x0c\x12*\n\x12\x61vailable_features\x18\x0f \x03(\x0e\x32\x0e.PbFeatureType\x12\x1f\n\x08services\x18\x10 \x03(\x0b\x32\r.PbBleService\x12\x11\n\tpeer_rand\x18\x11 \x01(\x0c\x12\x11\n\tpeer_ediv\x18\x12 \x01(\r\x12\x15\n\rencr_key_size\x18\x13 \x01(\r\x12\x18\n\x10\x64istributed_keys\x18\x14 \x01(\r\x12\x15\n\rauthenticated\x18\x15 \x01(\x08\x12;\n\x0fsensor_location\x18\x16 \x01(\x0e\x32\".data.PbBleDevice.PbSensorLocation\x12\x1f\n\x17OBSOLETE_device_version\x18\x17 \x01(\t\x12\"\n\x1asecondary_software_version\x18\x18 \x01(\t\x12\x15\n\rserial_number\x18\x19 \x01(\t\x12\x11\n\tlocal_ltk\x18\x1a \x01(\x0c\x12\x12\n\nlocal_rand\x18\x1b \x01(\x0c\x12\x12\n\nlocal_ediv\x18\x1c \x01(\r\x12\"\n\tuser_data\x18\x1d \x03(\x0b\x32\x0f.data.PbBleUser\x12?\n\x11\x64\x65vice_appearance\x18\x1e \x01(\x0e\x32$.data.PbBleDevice.PbDeviceAppearance\x12(\n part_of_distributed_power_system\x18\x1f \x01(\x08\x12\x15\n\rhardware_code\x18  \x01(\t\x12/\n\x12sub_component_info\x18! \x03(\x0b\x32\x13.PbSubcomponentInfo\x12\"\n\x0e\x64\x65vice_version\x18\" \x01(\x0b\x32\n.PbVersion\"\xc1\x01\n\x0cPbBleKeyType\x12\x1b\n\x17\x42LE_PEER_ENCRYPTION_KEY\x10\x01\x12\x1f\n\x1b\x42LE_PEER_IDENTIFICATION_KEY\x10\x02\x12\x18\n\x14\x42LE_PEER_SIGNING_KEY\x10\x04\x12\x1c\n\x18\x42LE_LOCAL_ENCRYPTION_KEY\x10\x08\x12 \n\x1c\x42LE_LOCAL_IDENTIFICATION_KEY\x10\x10\x12\x19\n\x15\x42LE_LOCAL_SIGNING_KEY\x10 \"\xe0\x03\n\x10PbSensorLocation\x12\x19\n\x15SENSOR_LOCATION_OTHER\x10\x00\x12\x1f\n\x1bSENSOR_LOCATION_TOP_OF_SHOE\x10\x01\x12\x1b\n\x17SENSOR_LOCATION_IN_SHOE\x10\x02\x12\x17\n\x13SENSOR_LOCATION_HIP\x10\x03\x12\x1f\n\x1bSENSOR_LOCATION_FRONT_WHEEL\x10\x04\x12\x1e\n\x1aSENSOR_LOCATION_LEFT_CRANK\x10\x05\x12\x1f\n\x1bSENSOR_LOCATION_RIGHT_CRANK\x10\x06\x12\x1e\n\x1aSENSOR_LOCATION_LEFT_PEDAL\x10\x07\x12\x1f\n\x1bSENSOR_LOCATION_RIGHT_PEDAL\x10\x08\x12\x1d\n\x19SENSOR_LOCATION_FRONT_HUB\x10\t\x12 \n\x1cSENSOR_LOCATION_REAR_DROPOUT\x10\n\x12\x1d\n\x19SENSOR_LOCATION_CHAINSTAY\x10\x0b\x12\x1e\n\x1aSENSOR_LOCATION_REAR_WHEEL\x10\x0c\x12\x1c\n\x18SENSOR_LOCATION_REAR_HUB\x10\r\x12\x19\n\x15SENSOR_LOCATION_CHEST\x10\x0e\"\xf0\n\n\x12PbDeviceAppearance\x12!\n\x1d\x42LE_DEVICE_APPEARENCE_UNKNOWN\x10\x00\x12\'\n#BLE_DEVICE_APPEARENCE_GENERIC_PHONE\x10@\x12+\n&BLE_DEVICE_APPEARENCE_GENERIC_COMPUTER\x10\x80\x01\x12(\n#BLE_DEVICE_APPEARENCE_GENERIC_WATCH\x10\xc0\x01\x12\'\n\"BLE_DEVICE_APPEARENCE_SPORTS_WATCH\x10\xc1\x01\x12(\n#BLE_DEVICE_APPEARENCE_GENERIC_CLOCK\x10\x80\x02\x12*\n%BLE_DEVICE_APPEARENCE_GENERIC_DISPLAY\x10\xc0\x02\x12\x39\n4BLE_DEVICE_APPEARENCE_GENERIC_GENERIC_REMOTE_CONTROL\x10\x80\x03\x12.\n)BLE_DEVICE_APPEARENCE_GENERIC_EYE_GLASSES\x10\xc0\x03\x12&\n!BLE_DEVICE_APPEARENCE_GENERIC_TAG\x10\x80\x04\x12*\n%BLE_DEVICE_APPEARENCE_GENERIC_KEYRING\x10\xc0\x04\x12/\n*BLE_DEVICE_APPEARENCE_GENERIC_MEDIA_PLAYER\x10\x80\x05\x12\x32\n-BLE_DEVICE_APPEARENCE_GENERIC_BARCODE_SCANNER\x10\xc0\x05\x12.\n)BLE_DEVICE_APPEARENCE_GENERIC_THERMOMETER\x10\x80\x06\x12*\n%BLE_DEVICE_APPEARENCE_THERMOMETER_EAR\x10\x81\x06\x12\x34\n/BLE_DEVICE_APPEARENCE_GENERIC_HEART_RATE_SENSOR\x10\xc0\x06\x12\x31\n,BLE_DEVICE_APPEARENCE_BELT_HEART_RATE_SENSOR\x10\xc1\x06\x12\x31\n,BLE_DEVICE_APPEARENCE_GENERIC_BLOOD_PRESSURE\x10\x80\x07\x12-\n(BLE_DEVICE_APPEARENCE_BLOOD_PRESSURE_ARM\x10\x81\x07\x12/\n*BLE_DEVICE_APPEARENCE_BLOOD_PRESSURE_WRIST\x10\x82\x07\x12\x31\n,BLE_DEVICE_APPEARENCE_HUMAN_INTERFACE_DEVICE\x10\xc0\x07\x12\'\n\"BLE_DEVICE_APPEARENCE_HID_KEYBOARD\x10\xc1\x07\x12$\n\x1f\x42LE_DEVICE_APPEARENCE_HID_MOUSE\x10\xc2\x07\x12\'\n\"BLE_DEVICE_APPEARENCE_HID_JOYSTICK\x10\xc3\x07\x12&\n!BLE_DEVICE_APPEARENCE_HID_GAMEPAD\x10\xc4\x07\x12/\n*BLE_DEVICE_APPEARENCE_HID_DIGITIZER_TABLET\x10\xc5\x07\x12*\n%BLE_DEVICE_APPEARENCE_HID_CARD_READER\x10\xc6\x07\x12*\n%BLE_DEVICE_APPEARENCE_HID_DIGITAL_PEN\x10\xc7\x07\x12.\n)BLE_DEVICE_APPEARENCE_HID_BARCODE_SCANNER\x10\xc8\x07\x12\x30\n+BLE_DEVICE_APPEARENCE_GENERIC_GLUCOSE_METER\x10\x80\x08*J\n\x18PbDeviceManufacturerType\x12\x16\n\x12MANUFACTURER_POLAR\x10\x01\x12\x16\n\x12MANUFACTURER_OTHER\x10\x02')
  ,
  dependencies=[structures__pb2.DESCRIPTOR,types__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PBDEVICEMANUFACTURERTYPE = _descriptor.EnumDescriptor(
  name='PbDeviceManufacturerType',
  full_name='data.PbDeviceManufacturerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUFACTURER_POLAR', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANUFACTURER_OTHER', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=3240,
  serialized_end=3314,
)
_sym_db.RegisterEnumDescriptor(_PBDEVICEMANUFACTURERTYPE)

PbDeviceManufacturerType = enum_type_wrapper.EnumTypeWrapper(_PBDEVICEMANUFACTURERTYPE)
MANUFACTURER_POLAR = 1
MANUFACTURER_OTHER = 2


_PBBLEDEVICE_PBBLEKEYTYPE = _descriptor.EnumDescriptor(
  name='PbBleKeyType',
  full_name='data.PbBleDevice.PbBleKeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLE_PEER_ENCRYPTION_KEY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_PEER_IDENTIFICATION_KEY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_PEER_SIGNING_KEY', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_LOCAL_ENCRYPTION_KEY', index=3, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_LOCAL_IDENTIFICATION_KEY', index=4, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_LOCAL_SIGNING_KEY', index=5, number=32,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1167,
  serialized_end=1360,
)
_sym_db.RegisterEnumDescriptor(_PBBLEDEVICE_PBBLEKEYTYPE)

_PBBLEDEVICE_PBSENSORLOCATION = _descriptor.EnumDescriptor(
  name='PbSensorLocation',
  full_name='data.PbBleDevice.PbSensorLocation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_TOP_OF_SHOE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_IN_SHOE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_HIP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_FRONT_WHEEL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_LEFT_CRANK', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_RIGHT_CRANK', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_LEFT_PEDAL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_RIGHT_PEDAL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_FRONT_HUB', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_REAR_DROPOUT', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_CHAINSTAY', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_REAR_WHEEL', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_REAR_HUB', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_LOCATION_CHEST', index=14, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1363,
  serialized_end=1843,
)
_sym_db.RegisterEnumDescriptor(_PBBLEDEVICE_PBSENSORLOCATION)

_PBBLEDEVICE_PBDEVICEAPPEARANCE = _descriptor.EnumDescriptor(
  name='PbDeviceAppearance',
  full_name='data.PbBleDevice.PbDeviceAppearance',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_PHONE', index=1, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_COMPUTER', index=2, number=128,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_WATCH', index=3, number=192,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_SPORTS_WATCH', index=4, number=193,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_CLOCK', index=5, number=256,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_DISPLAY', index=6, number=320,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_GENERIC_REMOTE_CONTROL', index=7, number=384,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_EYE_GLASSES', index=8, number=448,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_TAG', index=9, number=512,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_KEYRING', index=10, number=576,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_MEDIA_PLAYER', index=11, number=640,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_BARCODE_SCANNER', index=12, number=704,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_THERMOMETER', index=13, number=768,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_THERMOMETER_EAR', index=14, number=769,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_HEART_RATE_SENSOR', index=15, number=832,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_BELT_HEART_RATE_SENSOR', index=16, number=833,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_BLOOD_PRESSURE', index=17, number=896,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_BLOOD_PRESSURE_ARM', index=18, number=897,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_BLOOD_PRESSURE_WRIST', index=19, number=898,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HUMAN_INTERFACE_DEVICE', index=20, number=960,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_KEYBOARD', index=21, number=961,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_MOUSE', index=22, number=962,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_JOYSTICK', index=23, number=963,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_GAMEPAD', index=24, number=964,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_DIGITIZER_TABLET', index=25, number=965,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_CARD_READER', index=26, number=966,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_DIGITAL_PEN', index=27, number=967,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_HID_BARCODE_SCANNER', index=28, number=968,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLE_DEVICE_APPEARENCE_GENERIC_GLUCOSE_METER', index=29, number=1024,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1846,
  serialized_end=3238,
)
_sym_db.RegisterEnumDescriptor(_PBBLEDEVICE_PBDEVICEAPPEARANCE)


_PBBLEUSER = _descriptor.Descriptor(
  name='PbBleUser',
  full_name='data.PbBleUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_index', full_name='data.PbBleUser.user_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_user_index', full_name='data.PbBleUser.device_user_index', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consent', full_name='data.PbBleUser.consent', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=138,
)


_PBBLEDEVICE = _descriptor.Descriptor(
  name='PbBleDevice',
  full_name='data.PbBleDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paired', full_name='data.PbBleDevice.paired', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='data.PbBleDevice.last_modified', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='data.PbBleDevice.manufacturer', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_time_stamp', full_name='data.PbBleDevice.deleted_time_stamp', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac', full_name='data.PbBleDevice.mac', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='data.PbBleDevice.device_id', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='data.PbBleDevice.name', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_level', full_name='data.PbBleDevice.battery_level', index=7,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer_name', full_name='data.PbBleDevice.manufacturer_name', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='data.PbBleDevice.model_name', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_ltk', full_name='data.PbBleDevice.peer_ltk', index=10,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_irk', full_name='data.PbBleDevice.peer_irk', index=11,
      number=13, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_csrk', full_name='data.PbBleDevice.peer_csrk', index=12,
      number=14, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available_features', full_name='data.PbBleDevice.available_features', index=13,
      number=15, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='services', full_name='data.PbBleDevice.services', index=14,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_rand', full_name='data.PbBleDevice.peer_rand', index=15,
      number=17, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer_ediv', full_name='data.PbBleDevice.peer_ediv', index=16,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encr_key_size', full_name='data.PbBleDevice.encr_key_size', index=17,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distributed_keys', full_name='data.PbBleDevice.distributed_keys', index=18,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authenticated', full_name='data.PbBleDevice.authenticated', index=19,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensor_location', full_name='data.PbBleDevice.sensor_location', index=20,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_device_version', full_name='data.PbBleDevice.OBSOLETE_device_version', index=21,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondary_software_version', full_name='data.PbBleDevice.secondary_software_version', index=22,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='data.PbBleDevice.serial_number', index=23,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_ltk', full_name='data.PbBleDevice.local_ltk', index=24,
      number=26, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_rand', full_name='data.PbBleDevice.local_rand', index=25,
      number=27, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_ediv', full_name='data.PbBleDevice.local_ediv', index=26,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_data', full_name='data.PbBleDevice.user_data', index=27,
      number=29, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_appearance', full_name='data.PbBleDevice.device_appearance', index=28,
      number=30, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='part_of_distributed_power_system', full_name='data.PbBleDevice.part_of_distributed_power_system', index=29,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware_code', full_name='data.PbBleDevice.hardware_code', index=30,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_component_info', full_name='data.PbBleDevice.sub_component_info', index=31,
      number=33, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_version', full_name='data.PbBleDevice.device_version', index=32,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBBLEDEVICE_PBBLEKEYTYPE,
    _PBBLEDEVICE_PBSENSORLOCATION,
    _PBBLEDEVICE_PBDEVICEAPPEARANCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=3238,
)

_PBBLEDEVICE.fields_by_name['paired'].message_type = types__pb2._PBSYSTEMDATETIME
_PBBLEDEVICE.fields_by_name['last_modified'].message_type = types__pb2._PBSYSTEMDATETIME
_PBBLEDEVICE.fields_by_name['manufacturer'].enum_type = _PBDEVICEMANUFACTURERTYPE
_PBBLEDEVICE.fields_by_name['deleted_time_stamp'].message_type = types__pb2._PBSYSTEMDATETIME
_PBBLEDEVICE.fields_by_name['mac'].message_type = structures__pb2._PBBLEMAC
_PBBLEDEVICE.fields_by_name['available_features'].enum_type = types__pb2._PBFEATURETYPE
_PBBLEDEVICE.fields_by_name['services'].message_type = structures__pb2._PBBLESERVICE
_PBBLEDEVICE.fields_by_name['sensor_location'].enum_type = _PBBLEDEVICE_PBSENSORLOCATION
_PBBLEDEVICE.fields_by_name['user_data'].message_type = _PBBLEUSER
_PBBLEDEVICE.fields_by_name['device_appearance'].enum_type = _PBBLEDEVICE_PBDEVICEAPPEARANCE
_PBBLEDEVICE.fields_by_name['sub_component_info'].message_type = structures__pb2._PBSUBCOMPONENTINFO
_PBBLEDEVICE.fields_by_name['device_version'].message_type = structures__pb2._PBVERSION
_PBBLEDEVICE_PBBLEKEYTYPE.containing_type = _PBBLEDEVICE
_PBBLEDEVICE_PBSENSORLOCATION.containing_type = _PBBLEDEVICE
_PBBLEDEVICE_PBDEVICEAPPEARANCE.containing_type = _PBBLEDEVICE
DESCRIPTOR.message_types_by_name['PbBleUser'] = _PBBLEUSER
DESCRIPTOR.message_types_by_name['PbBleDevice'] = _PBBLEDEVICE
DESCRIPTOR.enum_types_by_name['PbDeviceManufacturerType'] = _PBDEVICEMANUFACTURERTYPE

PbBleUser = _reflection.GeneratedProtocolMessageType('PbBleUser', (_message.Message,), dict(
  DESCRIPTOR = _PBBLEUSER,
  __module__ = 'bluetooth_device_pb2'
  # @@protoc_insertion_point(class_scope:data.PbBleUser)
  ))
_sym_db.RegisterMessage(PbBleUser)

PbBleDevice = _reflection.GeneratedProtocolMessageType('PbBleDevice', (_message.Message,), dict(
  DESCRIPTOR = _PBBLEDEVICE,
  __module__ = 'bluetooth_device_pb2'
  # @@protoc_insertion_point(class_scope:data.PbBleDevice)
  ))
_sym_db.RegisterMessage(PbBleDevice)


# @@protoc_insertion_point(module_scope)
