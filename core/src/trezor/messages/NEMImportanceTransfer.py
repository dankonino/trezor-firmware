# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEMImportanceTransferMode = Literal[1, 2]
    except ImportError:
        pass


class NEMImportanceTransfer(p.MessageType):

    def __init__(
        self,
        *,
        mode: Optional[EnumTypeNEMImportanceTransferMode] = None,
        public_key: Optional[bytes] = None,
    ) -> None:
        self.mode = mode
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mode', p.EnumType("NEMImportanceTransferMode", (1, 2,)), None),
            2: ('public_key', p.BytesType, None),
        }
