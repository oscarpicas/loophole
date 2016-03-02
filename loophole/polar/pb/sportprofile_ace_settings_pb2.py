# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sportprofile_ace_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sportprofile_ace_settings.proto',
  package='data',
  serialized_pb=_b('\n\x1fsportprofile_ace_settings.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"\xc5\x02\n\x19PbAceSportProfileSettings\x12\x41\n\x0bheart_touch\x18\x01 \x01(\x0e\x32,.data.PbAceSportProfileSettings.PbHeartTouch\x12\x12\n\nauto_start\x18\x04 \x01(\x08\x12\x42\n\x1cstride_sensor_calib_settings\x18\x06 \x01(\x0b\x32\x1c.PbStrideSensorCalibSettings\"\x8c\x01\n\x0cPbHeartTouch\x12\x13\n\x0fHEART_TOUCH_OFF\x10\x01\x12\"\n\x1eHEART_TOUCH_ACTIVATE_BACKLIGHT\x10\x02\x12!\n\x1dHEART_TOUCH_SHOW_PREVIOUS_LAP\x10\x03\x12 \n\x1cHEART_TOUCH_SHOW_TIME_OF_DAY\x10\x04')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PBACESPORTPROFILESETTINGS_PBHEARTTOUCH = _descriptor.EnumDescriptor(
  name='PbHeartTouch',
  full_name='data.PbAceSportProfileSettings.PbHeartTouch',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_OFF', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_ACTIVATE_BACKLIGHT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_SHOW_PREVIOUS_LAP', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEART_TOUCH_SHOW_TIME_OF_DAY', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=240,
  serialized_end=380,
)
_sym_db.RegisterEnumDescriptor(_PBACESPORTPROFILESETTINGS_PBHEARTTOUCH)


_PBACESPORTPROFILESETTINGS = _descriptor.Descriptor(
  name='PbAceSportProfileSettings',
  full_name='data.PbAceSportProfileSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_touch', full_name='data.PbAceSportProfileSettings.heart_touch', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auto_start', full_name='data.PbAceSportProfileSettings.auto_start', index=1,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stride_sensor_calib_settings', full_name='data.PbAceSportProfileSettings.stride_sensor_calib_settings', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBACESPORTPROFILESETTINGS_PBHEARTTOUCH,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=380,
)

_PBACESPORTPROFILESETTINGS.fields_by_name['heart_touch'].enum_type = _PBACESPORTPROFILESETTINGS_PBHEARTTOUCH
_PBACESPORTPROFILESETTINGS.fields_by_name['stride_sensor_calib_settings'].message_type = types_pb2._PBSTRIDESENSORCALIBSETTINGS
_PBACESPORTPROFILESETTINGS_PBHEARTTOUCH.containing_type = _PBACESPORTPROFILESETTINGS
DESCRIPTOR.message_types_by_name['PbAceSportProfileSettings'] = _PBACESPORTPROFILESETTINGS

PbAceSportProfileSettings = _reflection.GeneratedProtocolMessageType('PbAceSportProfileSettings', (_message.Message,), dict(
  DESCRIPTOR = _PBACESPORTPROFILESETTINGS,
  __module__ = 'sportprofile_ace_settings_pb2'
  # @@protoc_insertion_point(class_scope:data.PbAceSportProfileSettings)
  ))
_sym_db.RegisterMessage(PbAceSportProfileSettings)


# @@protoc_insertion_point(module_scope)