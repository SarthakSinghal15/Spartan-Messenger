# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chat_pb2 as chat__pb2


class SpartanChatServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ChatStream = channel.unary_stream(
        '/grpc.SpartanChatServer/ChatStream',
        request_serializer=chat__pb2.Ugroupid.SerializeToString,
        response_deserializer=chat__pb2.Note.FromString,
        )
    self.SendNote = channel.unary_unary(
        '/grpc.SpartanChatServer/SendNote',
        request_serializer=chat__pb2.Note.SerializeToString,
        response_deserializer=chat__pb2.Empty.FromString,
        )
    self.UserLogin = channel.unary_unary(
        '/grpc.SpartanChatServer/UserLogin',
        request_serializer=chat__pb2.User.SerializeToString,
        response_deserializer=chat__pb2.Ugroupid.FromString,
        )


class SpartanChatServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ChatStream(self, request, context):
    """This bi-directional stream makes it possible to send and receive Notes between 2 persons
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendNote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UserLogin(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpartanChatServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ChatStream': grpc.unary_stream_rpc_method_handler(
          servicer.ChatStream,
          request_deserializer=chat__pb2.Ugroupid.FromString,
          response_serializer=chat__pb2.Note.SerializeToString,
      ),
      'SendNote': grpc.unary_unary_rpc_method_handler(
          servicer.SendNote,
          request_deserializer=chat__pb2.Note.FromString,
          response_serializer=chat__pb2.Empty.SerializeToString,
      ),
      'UserLogin': grpc.unary_unary_rpc_method_handler(
          servicer.UserLogin,
          request_deserializer=chat__pb2.User.FromString,
          response_serializer=chat__pb2.Ugroupid.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.SpartanChatServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
