# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import communication_pb2 as communication__pb2


class CommunicationStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SyncState = channel.unary_unary(
            "/Communication/SyncState",
            request_serializer=communication__pb2.State.SerializeToString,
            response_deserializer=communication__pb2.State.FromString,
        )
        self.GetFrameBackTrace = channel.unary_unary(
            "/Communication/GetFrameBackTrace",
            request_serializer=communication__pb2.Location.SerializeToString,
            response_deserializer=communication__pb2.FrameBackTrace.FromString,
        )


class CommunicationServicer(object):
    """Interface exported by the server.
    """

    def SyncState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetFrameBackTrace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_CommunicationServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SyncState": grpc.unary_unary_rpc_method_handler(
            servicer.SyncState,
            request_deserializer=communication__pb2.State.FromString,
            response_serializer=communication__pb2.State.SerializeToString,
        ),
        "GetFrameBackTrace": grpc.unary_unary_rpc_method_handler(
            servicer.GetFrameBackTrace,
            request_deserializer=communication__pb2.Location.FromString,
            response_serializer=communication__pb2.FrameBackTrace.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "Communication", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Communication(object):
    """Interface exported by the server.
    """

    @staticmethod
    def SyncState(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Communication/SyncState",
            communication__pb2.State.SerializeToString,
            communication__pb2.State.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetFrameBackTrace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/Communication/GetFrameBackTrace",
            communication__pb2.Location.SerializeToString,
            communication__pb2.FrameBackTrace.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )