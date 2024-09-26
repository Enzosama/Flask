from _typeshed import Incomplete

class RemoteConnectionCreationRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        description: Incomplete | None = None,
        org_id: Incomplete | None = None,
        remote_url: Incomplete | None = None,
        remote_api_token: Incomplete | None = None,
        remote_org_id: Incomplete | None = None,
        allow_insecure_tls: bool = False,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def org_id(self): ...
    @org_id.setter
    def org_id(self, org_id) -> None: ...
    @property
    def remote_url(self): ...
    @remote_url.setter
    def remote_url(self, remote_url) -> None: ...
    @property
    def remote_api_token(self): ...
    @remote_api_token.setter
    def remote_api_token(self, remote_api_token) -> None: ...
    @property
    def remote_org_id(self): ...
    @remote_org_id.setter
    def remote_org_id(self, remote_org_id) -> None: ...
    @property
    def allow_insecure_tls(self): ...
    @allow_insecure_tls.setter
    def allow_insecure_tls(self, allow_insecure_tls) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
