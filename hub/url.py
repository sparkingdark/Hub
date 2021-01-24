# NOT IMPLEMENTED COMPLETELY YET!

from typing import Union
from enum import Enum

from hub.defaults import AZURE_HOST_SUFFIX


class UrlProtocol(Enum):
    UNKNOWN = "unknown"
    S3 = "s3"
    GCS = "gcs"
    AZURE = "azure"
    FILESYSTEM = "filesystem"


class UrlType(Enum):
    HUB = "hub"
    LOCAL = "local"
    CLOUD = "cloud"


class Url:
    @classmethod
    def parse(cls, url: str) -> "Url":
        assert isinstance(url, str)

        pass

    def __init__(
        self,
        url_type: UrlType,
        protocol: UrlProtocol,
        path: str,  # for get_mapper(path)
        bucket: Union[str, None] = None,
        user: Union[str, None] = None,
        dataset: Union[str, None] = None,
        endpoint_url: Union[str, None] = None,
    ):
        assert isinstance(url_type, UrlType)
        assert isinstance(protocol, UrlProtocol)
        assert isinstance(path, str)
        assert isinstance(bucket, str) or bucket is None
        assert isinstance(user, str) or user is None
        assert isinstance(dataset, str) or dataset is None
        assert isinstance(endpoint_url, str) or endpoint_url is None

        self.url_type = url_type
        self.protocol = protocol
        self.path = path
        self.bucket = bucket
        self.user = user
        self.dataset = dataset
        self.endpoint_url = endpoint_url

    @property
    def url(self) -> str:
        pass
