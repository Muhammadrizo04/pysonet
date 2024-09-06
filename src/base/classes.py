from rest_framework import generics, permissions, mixins, decorators, viewsets


class MixedPermission:
    """ mixin permissions for action """

    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]


class MixedPermissionViewSer(MixedPermission, viewsets.ViewSet):
    pass


class MixedPermissionGenericViewSet(MixedPermission, viewsets.ViewSet):
    pass


class CreateUpdateDestroy(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          MixedPermission,
                          viewsets.GenericViewSet):
    """
    """
    pass


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  MixedPermission,
                                  viewsets.GenericViewSet):
    """
    """
    pass
