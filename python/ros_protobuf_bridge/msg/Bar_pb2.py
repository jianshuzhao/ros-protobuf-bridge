# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Bar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Bar.proto',
  package='ros_protobuf_bridge',
  syntax='proto3',
  serialized_pb=_b('\n\tBar.proto\x12\x13ros_protobuf_bridge\"0\n\x03\x42\x61r\x12\x13\n\x0bpage_number\x18\x01 \x01(\x05\x12\x14\n\x0csome_strings\x18\x02 \x03(\tb\x06proto3')
)




_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='ros_protobuf_bridge.Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_number', full_name='ros_protobuf_bridge.Bar.page_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='some_strings', full_name='ros_protobuf_bridge.Bar.some_strings', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['Bar'] = _BAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), dict(
  DESCRIPTOR = _BAR,
  __module__ = 'Bar_pb2'
  # @@protoc_insertion_point(class_scope:ros_protobuf_bridge.Bar)
  ))
_sym_db.RegisterMessage(Bar)


# @@protoc_insertion_point(module_scope)
