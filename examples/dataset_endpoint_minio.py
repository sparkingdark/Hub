import numpy as np
from hub.schema.features import Tensor
import hub

# fill in the below fields
token = {
    "aws_access_key_id": "",
    "aws_secret_access_key": "",
    "endpoint_url": "",
    "region": "",
}

schema = {"abc": Tensor((100, 100, 3))}
ds = hub.Dataset(
    "s3://mybucket/random_dataset", token=token, shape=(10,), schema=schema, mode="w"
)

for i in range(10):
    ds["abc", i] = np.ones((100, 100, 3))
ds.flush()
